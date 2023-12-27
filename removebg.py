# Requires "requests" to be installed (see python-requests.org)
import requests

response = requests.post(
    'https://api.remove.bg/v1.0/removebg',
    files={'image_file': open('c:\Users\IVAN\Downloads\493shots_so.png', 'rb')},
    data={'size': 'auto'},
    headers={'X-Api-Key': 'BBb69YqYKEgX7w2BXRY2Bgc9'},
)
if response.status_code == requests.codes.ok:
    with open('no-bg.png', 'wb') as out:
        out.write(response.content)
else:
    print("Error:", response.status_code, response.text)