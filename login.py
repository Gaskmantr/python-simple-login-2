import requests

s = requests.session()

login = {
    'username' : 'gaskman',
    'password' : 'berke123'

}
giris = s.post("https://www.kogama.com/auth/login/",json=login)


print(giris.status_code)