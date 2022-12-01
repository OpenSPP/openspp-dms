import logging

from odoo import http
from odoo.http import Response, request

_logger = logging.getLogger(__name__)


class SPPScannerController(http.Controller):
    @http.route("/auth", type="json", auth="public", methods=["POST"], website=False)
    def login(self, **post):
        username = post.get("username", False)
        password = post.get("password", False)
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
                request.env.ref("spp_change_request.group_spp_change_request_agent").id
                in user[0].groups_id.ids
            ):
                return user, 200  # OK
            else:
                return None, 403  # Forbidden
        else:
            return None, 401  # Unauthorized

    @http.route("/upload", type="json", auth="public", methods=["POST"], website=False)
    def upload(self, **post):
        username = post.get("username", False)
        password = post.get("password", False)
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
                code = 200
                return Response("Succeed", code)
        else:
            return Response("Error", code)
