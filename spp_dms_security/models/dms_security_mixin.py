from odoo import api, models
from odoo.osv.expression import TRUE_DOMAIN


class DmsSecurityMixin(models.AbstractModel):
    _inherit = "dms.security.mixin"

    @api.model
    def _get_permission_domain(self, operator, value, operation):
        return TRUE_DOMAIN
