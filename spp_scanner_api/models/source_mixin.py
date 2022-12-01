import logging

from odoo import models

_logger = logging.getLogger(__name__)


class ChangeRequestSourceMixinCustom(models.AbstractModel):
    _inherit = "spp.change.request.source.mixin"

    def set_scanner_upload(self):
        for rec in self:
            self.env.user.current_dms_directory_id.id = rec.dms_directory_ids[0].id
