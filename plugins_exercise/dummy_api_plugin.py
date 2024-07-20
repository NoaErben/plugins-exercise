from plugin import Plugin


class DummyApiPlugin(Plugin):
    def __init__(self, base_url, credentials):
        self.base_url = base_url
        self.credentials = credentials
        self.token = None

    # TODO
    def _get_user_details(self):
        pass

    # TODO
    def get_posts(self):
        pass

    # TODO
    def _get_posts_with_comments(self):
        pass

    # TODO
    def connectivity_test(self):
        pass

    # TODO
    def collect(self):
        pass






