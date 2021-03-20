import requests as req
import random

usr_inp = input('enter term:')

url = "https://icanhazdadjoke.com/search"
res = req.get(url,
	headers={"Accept":"application/json"},
	params={"term":usr_inp}
)
r = res.json()['results']
n = len(r)
if(n == 0):
	print('no jokes available')
elif (n == 1):
	print(r[0]['joke'])
else:
	r1 = random.choice(r)
	print(r1['joke'])