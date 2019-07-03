#!/usr/bin/env python
# coding: utf-8




import requests
# Use scratch api
# in request api search user and projects user
res = requests.get("https://api.scratch.mit.edu/users/masg92")
resP = requests.get(f"https://api.scratch.mit.edu/users/masg92/projects")





# store responses on variable as json type
user = res.json()['username']
project = resP.json()





print(f'Projects on SCRATCH from {user}')
# print each project with it's id
for item in project:
    print(f"ID {item['id']} Project Name {item['title']}")







