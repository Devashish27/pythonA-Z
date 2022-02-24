import requests

r = requests.get("https://financialmodelingprep.com/api/v3/actives")
print(r.text)
print(r.status_code)

# url = "www.somebodywhatsyou.com"
# data = {
#     "p1": 5,
#     "p2": 12
# }
#
# r2 = requests.post(url=url, data=data)