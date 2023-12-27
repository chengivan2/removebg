import requests

response = requests.post(
    'https://api.remove.bg/v1.0/removebg',
    files={'image_file': open('IMAGE-PATH', 'rb')},
    data={'size': 'auto'},
    headers={'X-Api-Key': 'ENTER-YOUR-API-KEY'},
)
if response.status_code == requests.codes.ok:
    with open('no-bg.png', 'wb') as out: #Replace no-bg.png with the name you want to call your resultant image
        out.write(response.content) #Image will be saved,by default, in the same directory your code file is in
else:
    print("Error:", response.status_code, response.text) #Throw some error message when you fail to get an OK response