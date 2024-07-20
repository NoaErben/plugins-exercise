from plugin import Plugin
import json
from api_operations import ApiOperations

class DummyApiPlugin(Plugin):
    """
    DummyApiPlugin is a plugin designed to interact with the dummyjson.com API.
    It authenticates the user, collects user details, posts, and their comments.
    """
    _LOGIN_ENDPOINT = 'auth/login'
    _POST_ENDPOINT = 'posts'
    _AUTH_ENDPOINT = 'auth/me'

    def __init__(self, base_url, credentials):
        self.base_url = base_url
        self.credentials = credentials
        self.token = None  # Token is initialized as None and set after successful authentication.

    def _authenticate(self):
        response = ApiOperations.post_request(self.base_url, self._LOGIN_ENDPOINT, json=self.credentials)
        self.token = response.get('token')

    def _make_authenticated_get_request(self):
        return ApiOperations.get_request(self.base_url, self._AUTH_ENDPOINT, headers={'Authorization': f'Bearer {self.token}'})

    def _get_user_details(self):
        return self._make_authenticated_get_request()

    def _get_posts(self, limit=0):
        # Retrieve a list of posts, with an optional limit on the number of posts.
        return ApiOperations.get_request(self.base_url, self._POST_ENDPOINT, params={'limit': limit})

    def _get_posts_with_comments(self):
        # Get posts and add their comments.
        posts = self._get_posts(limit=60)
        posts_lists = posts["posts"]
        for post in posts_lists:
            comments_endpoint = f'{self._POST_ENDPOINT}/{post["id"]}/comments'
            comments_response = ApiOperations.get_request(self.base_url ,comments_endpoint, params={'limit': 60})
            comments = comments_response["comments"]
            post["comments"] = comments

        return posts_lists

    def connectivity_test(self):
        self._authenticate()

        return True

    def collect(self):
        # Collect and print user details and posts with their comments.
        self._print_title("Current authenticated user details")
        user_details = self._get_user_details()
        print(json.dumps(user_details, indent=4))

        self._print_title("Posts")
        posts = self._get_posts(limit=60)
        print(json.dumps(posts['posts'], indent=4))

        self._print_title("Posts with comments")
        posts_with_comments = self._get_posts_with_comments()
        print(json.dumps(posts_with_comments, indent=4))

    def _print_title(self, title):
        print(f"---------------------- {title} ----------------------")