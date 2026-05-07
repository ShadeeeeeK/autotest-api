import httpx

from httpx_get_user_me import login_payload
from tools.fakers import get_random_email

create_user_payload = {
    "email": get_random_email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}

create_user_response = httpx.post("http://127.0.0.1:8000/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()
create_user_response_data_user_id = create_user_response_data["user"]["id"]

login_payload = {
  "email": create_user_payload["email"],
  "password": create_user_payload["password"]
}

login_response = httpx.post("http://127.0.0.1:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

create_file_headers = {
    "Authorization": f"Bearer {login_response_data["token"]["accessToken"]}"
}

create_file_response = httpx.post("http://127.0.0.1:8000/api/v1/files",
                                  headers=create_file_headers,
                                  data={"filename": "images.png", "directory": "images"},
                                  files={"upload_file": open('./testdata/files/images.png', 'rb')}
)

create_file_response_data = create_file_response.json()

print('Create file success', create_file_response_data)