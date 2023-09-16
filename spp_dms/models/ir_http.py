import logging

from odoo import models

_logger = logging.getLogger(__name__)


class CustomIrHttp(models.AbstractModel):
    _inherit = "ir.http"

    def binary_content(
        self,
        xmlid=None,
        model="ir.attachment",
        id=None,  # pylint: disable=W0622
        field="datas",
        unique=False,
        filename=None,
        filename_field="name",
        download=False,
        mimetype=None,
        default_mimetype="application/octet-stream",
        access_token=None,
    ):
        _logger.debug("DEBUG: ir.http: model: %s" % model)
        if model == "dms.file":
            if not self.env.user.has_group("base.group_user"):
                _logger.debug("DEBUG: ir.http: NOT ALLOWED")
                return 404, [], None
        return super().binary_content(
            xmlid,
            model,
            id,
            field,
            unique,
            filename,
            filename_field,
            download,
            mimetype,
            default_mimetype,
            access_token,
        )
