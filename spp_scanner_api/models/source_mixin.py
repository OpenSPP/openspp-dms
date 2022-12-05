import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class FileuploadSourceMixinCustom(models.AbstractModel):
    _inherit = "spp.change.request.source.mixin"

    is_active_user_dms = fields.Boolean(compute="_compute_active_user_dms")

    def set_folder_as_active_file_upload(self):
        for rec in self:
            self.env.user.current_dms_directory_id = rec.dms_directory_ids[0].id

    def _compute_active_user_dms(self):
        for rec in self:
            rec.is_active_user_dms = False
            if self.env.user.current_dms_directory_id.id == rec.dms_directory_ids[0].id:
                rec.is_active_user_dms = True

    def refresh_data(self):
        return
