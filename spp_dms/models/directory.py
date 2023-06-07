import logging

from odoo import _, api, models
from odoo.exceptions import ValidationError

from odoo.addons.dms.tools.file import check_name

_logger = logging.getLogger(__name__)


class DmsDirectory(models.Model):
    _inherit = "dms.directory"

    @api.constrains("name")
    def _check_name(self):
        for record in self:
            if self.env.context.get("check_name", True) and not check_name(record.name):
                raise ValidationError(_("The directory name is invalid."))

            domain = [
                ("id", "!=", record.id),
                ("complete_name", "=", record.name),
            ]

            if record.is_root_directory:
                storage_id = record.sudo().storage_id.id
                domain.append(("storage_id", "=", storage_id))
            else:
                parent_id = record.sudo().parent_id.id
                domain.append(("parent_id", "=", parent_id))

            childs = self.env["dms.directory"].sudo().search(domain)

            _logger.debug(
                "DEBUG: _check_name childs: %s, domain: %s"
                % (childs.sudo().name_get(), domain)
            )
            if childs:
                raise ValidationError(
                    _("A directory with the same name already exists.")
                )
