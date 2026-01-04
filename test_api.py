import requests

BASE_URL = 'http://127.0.0.1:8000'

# Test registration
def test_register():
    data = {
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'testpass123',
        'first_name': 'Test',
        'last_name': 'User'
    }
    response = requests.post(f'{BASE_URL}/users/register/', json=data)
    print('Register:', response.status_code, response.json())
    return response.json() if response.status_code == 201 else None

# Test login
def test_login():
    data = {
        'username': 'testuser',
        'password': 'testpass123'
    }
    response = requests.post(f'{BASE_URL}/users/login/', json=data)
    print('Login:', response.status_code, response.json())
    return response.json() if response.status_code == 200 else None

# Test get user details
def test_get_user(access_token, user_id):
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(f'{BASE_URL}/users/{user_id}/', headers=headers)
    print('Get User:', response.status_code, response.json())

if __name__ == '__main__':
    user_data = test_register()
    if user_data:
        login_data = test_login()
        if login_data:
            access_token = login_data['access']
            user_id = user_data['id']
            test_get_user(access_token, user_id)
