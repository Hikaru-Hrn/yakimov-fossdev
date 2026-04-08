import sys

import requests


def main():
    print(f"--- Running app with Python {sys.version.split()[0]} ---")

    url = "https://api.github.com"

    try:
        print(f"Attempting to connect to {url}...")
        response = requests.get(url)

        if response.status_code == 200:
            print("Successfully connected! API is reachable.")
            print(f"Server response header: {response.headers.get('Server')}")
        else:
            print(f"Connected, but got status code: {response.status_code}")

    except ImportError:
        print("Error: 'requests' library not found! Please use virtual environment.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
