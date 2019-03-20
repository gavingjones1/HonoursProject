import json

password = ''

with open('Auth.json') as json_file:
    data = json.load(json_file)
    password = (data['Crypt'][0]['password'])
    print (password)
