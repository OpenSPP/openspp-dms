from pyftpdlib.authorizers import DummyAuthorizer


class OpenSPPAuthorizer(DummyAuthorizer):
    def authorize_from_openspp(self, username, password):
        # TODO: Call OpenSPP auth here
        return True

    def validate_authentication(self, username, password, handler):
        """Authenticate using OpenSPP auth
        AuthenticationFailed in case of failed authentication.
        """
        self.authorize_from_openspp(username, password)

    def get_home_dir(self, username):
        """Return the user's in-memory directory.
        Since this is called during authentication (PASS),
        AuthenticationFailed can be freely raised by subclasses in case
        the provided username no longer exists.
        """
        return ""

    def has_perm(self, username, perm, path=None):
        return True

    def get_msg_login(self, username):
        """Return the user's login message."""
        return "Welcome"

    def add_user(
        self,
        **kwargs,
    ):
        raise Exception("Action not allowed.")

    def add_anonymous(self, homedir, **kwargs):
        raise Exception("Action not allowed.")
