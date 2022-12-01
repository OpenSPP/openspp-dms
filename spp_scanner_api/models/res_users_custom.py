import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class PDSSPPUser(models.Model):
    _inherit = "res.users"

    scanner_password = fields.Char()
    current_dms_directory_id = fields.Many2one(
        "dms.directory", string="Current DMS Directory"
    )
