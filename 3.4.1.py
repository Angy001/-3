import json

def register(username, password, filename='credentials.json'):
    credentials = {
        'username': username,
        'password': password
    }
    
    try:
        with open(filename, 'w') as json_file:
            json.dump(credentials, json_file)
        print("Credentials saved successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")


register('my_user', 'my_password')
