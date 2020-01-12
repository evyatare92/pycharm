import requests

#response = requests.get("https://api.github.com/users/avielb/repos")
#all_repos = response.json()
#for i in all_repos:
#    print(i["name"])

resp = requests.post("http://localhost:5001/whatismyname")
print(resp.text)