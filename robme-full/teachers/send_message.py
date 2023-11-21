import requests


api_token = '1ee7069fc8b34c0551d01831212527a1'
def send_message(phone,message):
    url = f'https://semysms.net/api/3/sms.php?token={api_token}&device=active&phone=%2B{phone}&msg={message}'
    response = requests.get(url)
    print(response.json())
    return url 