import logging

from odoo import http
from odoo.http import Response, request

_logger = logging.getLogger(__name__)


class SPPScannerController(http.Controller):
    @http.route(
        "/dms/auth", type="json", auth="public", methods=["POST"], website=False
    )
    def login(self, **post):
        username = post.get("username", False)
        password = post.get("password", False)
        if not username or not password:
            return Response("Succeed", 400)  # Bad Request
        user, code = self._authenticate_user(username, password)
        if user:
            return Response("Succeed", code)
        else:
            return Response("Error", code)

    def _authenticate_user(self, username, password):
        user = (
            request.env["res.users"]
            .sudo()
            .search([("login", "=", username), ("scanner_password", "=", password)])
        )
        if user:
            if (
                request.env.ref("spp_scanner_api.group_spp_scanner").id
                in user[0].groups_id.ids
            ):
                return user, 200  # OK
            else:
                return None, 403  # Forbidden
        else:
            return None, 401  # Unauthorized

    @http.route(
        "/dms/upload", type="json", auth="public", methods=["POST"], website=False
    )
    def upload(self, **post):
        username = post.get("username", False)
        password = post.get("password", False)
        if not username or not password:
            return Response("Error", 400)  # Bad Request
        file = post.get("file", False)
        filename = post.get("filename", False)
        if not file or not filename:
            return Response("Error", 406)  # Not Acceptable

        user, code = self._authenticate_user(username, password)
        if user:
            current_dms_directory_id = user.current_dms_directory_id
            if current_dms_directory_id:
                directory_id = current_dms_directory_id.id
                vals = {
                    "directory_id": directory_id,
                    "content": file,
                    "name": filename,
                }
                request.env["dms.file"].sudo(user.id).create(vals)
                code = 200  # OK
                return Response("Succeed", code)
            else:
                return Response("Error", 400)  # Bad Request
        else:
            return Response("Error", code)
