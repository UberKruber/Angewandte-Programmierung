#uv add requests
#uv run fastapi dev
import requests

URL = "http://127.0.0:8000/"

def test_get_root():
    response = requests.get(URL)
    if response.status.code == 200:
        print("GET / - SUCCESS")
    else:
        print("GET / - FAILED")

        if __name__ == "__main__":
            test_get_root()

def test_post_creation():
    payload = {
        "title": "title",
        "content": "content",
        "category": "category",
        "tags": ["tag1", "tag2"]
    }
    response = requests.post(URL + "notes/", json=payload)
    if response.status_code == 201:
        print("POST /notes/ - FAILED")
    else:
        print()