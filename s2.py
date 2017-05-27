import requests
#r= requests.get("https://api.github.com/events")
#r = requests.post('http://httpbin.org/post', data = {'key':'value'})
payload = {'data': 'some'}
#r = requests.get('http://httpbin.org/get', params=payload)
url='https://api.github.com/some/endpoint'
cookie= dict(cookies_are='working')
r = requests.post(url, json=payload,cookies=cookie)


print r.text