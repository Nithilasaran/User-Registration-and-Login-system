
import json
import urllib.request
import urllib.error

BASE_URL = "http://127.0.0.1:5000"


def send_request(path, method="GET", data=None):
    url = BASE_URL + path

    headers = {"Content-Type": "application/json"}
    body = json.dumps(data).encode("utf-8") if data else None

    request = urllib.request.Request(
        url,
        data=body,
        headers=headers,
        method=method
    )

    try:
        with urllib.request.urlopen(request) as response:
            print(f"\n{method} {path} - Status: {response.status}")
            print(response.read().decode("utf-8"))

    except urllib.error.HTTPError as error:
        print(f"\n{method} {path} - Status: {error.code}")
        print(error.read().decode("utf-8"))

    except urllib.error.URLError:
        print("Cannot connect. Make sure app.py is running.")


# 1. Check the API
send_request("/")

# 2. Register a test user
send_request("/register", "POST", {
    "name": "Nova",
    "email": "nova@example.com",
    "password": "NovaPass123"
})

# 3. Test login
send_request("/login", "POST", {
    "email": "nova@example.com",
    "password": "NovaPass123"
})

# 4. List registered users
send_request("/users")
