import requests

class ApiOperations:
    """
    ApiOperations provides static methods for common HTTP operations,
    including GET and POST requests and response handling.
    """

    @staticmethod
    def get_request(base_url, endpoint, headers={}, params={}):
        url = f"{base_url}/{endpoint}"
        response = requests.get(url, headers=headers, params=params)

        return ApiOperations.handle_response(response)

    @staticmethod
    def post_request(base_url, endpoint, headers={}, params={}, json={}):
        url = f"{base_url}/{endpoint}"
        response = requests.post(url, headers=headers, params=params, json=json)

        return ApiOperations.handle_response(response)

    @staticmethod
    def handle_response(response):
        try:
            response.raise_for_status()

            return response.json()

        except requests.exceptions.HTTPError as http_err:
            print(http_err)
            raise

        except requests.exceptions.RequestException as req_err:
            print(f"Request error occurred: {req_err}")
            raise
