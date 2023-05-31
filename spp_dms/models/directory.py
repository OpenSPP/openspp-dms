import logging

from odoo import _, api, models
from odoo.exceptions import ValidationError

# from ..tools.file import check_name
from odoo.addons.dms.tools.file import check_name

_logger = logging.getLogger(__name__)


class DmsDirectory(models.Model):
    _inherit = "dms.directory"

    @api.constrains("name")
    def _check_name(self):
        for record in self:
            if self.env.context.get("check_name", True) and not check_name(record.name):
                raise ValidationError(_("The directory name is invalid."))

            if record.is_root_directory:
                storage_id = record.sudo().storage_id.id
                childs = (
                    self.env["dms.directory"]
                    .sudo()
                    .search(
                        [
                            ("storage_id", "=", storage_id),
                            ("id", "!=", record.id),
                            ("complete_name", "=", record.name),
                        ]
                    )
                )
            else:
                parent_id = record.sudo().parent_id.id
                childs = (
                    self.env["dms.directory"]
                    .sudo()
                    .search(
                        [
                            ("parent_id", "=", parent_id),
                            ("id", "!=", record.id),
                            ("complete_name", "=", record.name),
                        ]
                    )
                )

            _logger.debug("DEBUG: _check_name childs: %s" % childs.sudo().name_get())
            if childs:
                raise ValidationError(
                    _("A directory with the same name already exists.")
                )
