from httplib2 import Http
from json import dumps

#
# Hangouts Chat incoming webhook quickstart
#
def main():
    url = '<https://chat.googleapis.com/v1/spaces/AAAA1mevZW8/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=Goov7pLsYVmgwyvfkoCuak7PEV7862R6JTgyvWhEYa4%3D>'
    bot_message = {
        'text' : 'Hello from Python script!'}

    message_headers = { 'Content-Type': 'application/json; charset=UTF-8'}

    http_obj = Http()

    response = http_obj.request(
        uri=url,
        method='POST',
        headers=message_headers,
        body=dumps(bot_message),
    )

    print(response)

if __name__ == '__main__':
    main()
