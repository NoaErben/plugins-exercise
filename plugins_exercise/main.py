from dummy_api_plugin import DummyApiPlugin


def main():
    base_url = 'https://dummyjson.com'

    username = input("Enter your username: ")
    password = input("Enter your password: ")
    credentials = {'username': username, 'password': password}

    plugin = DummyApiPlugin(base_url, credentials)
    plugin.run()


if __name__ == '__main__':
    main()
