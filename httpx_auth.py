from pprint import pprint

import httpx

from pprint import pprint
BASE_URL = "http://127.0.0.1:8000"
login_payload = {
    "email": "user@example.com",
    "password": "string"
}

login_response = httpx.post(f'{BASE_URL}/api/v1/authentication/login', json=login_payload)
login_response_data = login_response.json()

print('Login response', login_response_data)
print('Login statuCode', login_response.status_code)

refresh_payload = {
    "refreshToken": login_response_data['token']['refreshToken']
}

refresh_response = httpx.post(f'{BASE_URL}/api/v1/authentication/refresh', json=refresh_payload)
refresh_response_data = refresh_response.json()

print('Refresh token=', refresh_response_data)