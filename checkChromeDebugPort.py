import requests


def checkChromeDebugPort(port):
    devtools_url = f"http://localhost:{port}/json/version"
    try:
        response = requests.get(devtools_url)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.ConnectionError:
        return False
