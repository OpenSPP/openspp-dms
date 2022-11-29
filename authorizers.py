from pyftpdlib.authorizers import DummyAuthorizer


class OpenSPPAuthorizer(DummyAuthorizer):
    def authorize_from_openspp(self, username, password):
        # TODO: Call OpenSPP auth here
        return True

    def add_user(
        self,
        username,
        password,
        homedir,
        perm="elr",
        msg_login="Login successful.",
        msg_quit="Goodbye.",
        **kwargs,
    ):
        self.authorize_from_openspp(username, password)
        super().add_user(
            username=username,
            password=password,
            homedir=homedir,
            perm=perm,
            msg_login=msg_login,
            msg_quit=msg_quit,
        )

    def add_anonymous(self, homedir, **kwargs):
        raise Exception("Action not allowed.")
