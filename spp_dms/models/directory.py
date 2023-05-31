from odoo import _, api, models
from odoo.exceptions import ValidationError

from ..tools.file import check_name


class DmsDirectory(models.Model):
    _inherit = "dms.directory"

    @api.constrains("name")
    def _check_name(self):
        for record in self:
            if self.env.context.get("check_name", True) and not check_name(record.name):
                raise ValidationError(_("The directory name is invalid."))

            raise_error = False
            if record.is_root_directory:
                storage_id = record.sudo().storage_id.id
                childs = (
                    self.env["dms.directory"]
                    .sudo()
                    .search(
                        [
                            ("storage_id", "=", storage_id),
                            ("id", "=", record.id),
                            ("display_name", "=", record.name),
                        ]
                    )
                )
                if childs:
                    raise_error = True
            else:
                parent_id = record.sudo().parent_id.id
                childs = (
                    self.env["dms.directory"]
                    .sudo()
                    .search(
                        [
                            ("parent_id", "=", parent_id),
                            ("id", "=", record.id),
                            ("display_name", "=", record.name),
                        ]
                    )
                )
                if childs:
                    raise_error = True
            if raise_error:
                raise ValidationError(
                    _("A directory with the same name already exists.")
                )
