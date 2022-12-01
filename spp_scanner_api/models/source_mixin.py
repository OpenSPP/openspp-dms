import logging

from odoo import models

_logger = logging.getLogger(__name__)


class FileuploadSourceMixinCustom(models.AbstractModel):
    _inherit = "spp.change.request.source.mixin"

    def set_folder_as_active_file_upload(self):
        for rec in self:
            self.env.user.current_dms_directory_id.id = rec.dms_directory_ids[0].id
