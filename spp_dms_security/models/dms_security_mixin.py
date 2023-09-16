from odoo import api, models
from odoo.osv.expression import TRUE_DOMAIN


class DmsSecurityMixin(models.AbstractModel):
    _inherit = "dms.security.mixin"

    @api.model
    def _get_permission_domain(self, operator, value, operation):
        if self.check_user_group(self.env.user):
            return TRUE_DOMAIN
        return super()._get_permission_domain(operator, value, operation)

    def check_user_group(self, user):
        # Access the 'ir.model.data' model for external IDs
        mdl = self.env["ir.model.data"]

        # List of group external IDs to check
        group_external_ids = [
            "g2p_registry_base.group_g2p_admin",
            "spp_change_request.group_spp_change_request_administrator",
            "spp_change_request.group_spp_change_request_validator",
            "spp_change_request.group_spp_change_request_agent",
            "spp_change_request.group_spp_change_request_hq_validator",
            "spp_change_request.group_spp_change_request_local_validator",
            "spp_change_request.group_spp_change_request_applicator",
        ]

        # Check if the user is in any of the groups
        is_in_group = any(
            mdl._xmlid_to_res_id(group_xmlid) in user.groups_id.ids
            for group_xmlid in group_external_ids
        )

        return is_in_group
