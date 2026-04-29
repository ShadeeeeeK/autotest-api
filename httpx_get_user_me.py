import httpx

BASE_URL = "http://127.0.0.1:8000"
login_payload = {
    "email": "user@example.com",
    "password": "string"
}

login_response= httpx.post(f'{BASE_URL}/api/v1/authentication/login', json=login_payload)
login_response_data = login_response.json()

headers = {
    "Authorization": f"Bearer {login_response_data['token']['accessToken']}"
}

get_me_response = httpx.get(f'{BASE_URL}/api/v1/users/me', headers=headers)
get_me_response_data = get_me_response.json()
print(get_me_response.status_code)
print(get_me_response_data)