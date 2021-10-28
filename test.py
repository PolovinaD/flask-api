import requests

base_url = "http://127.0.0.1:5000/"

test_urls = {
    "google" : "google.com",
    "fb" : "facebook.com",
    "ebay" : "ebay.com"
}

res = requests.get(base_url + "status", {"url": test_urls['google']} )
print(res.json())

res = requests.get(base_url + "status", {"url": test_urls['fb']} )
print(res.json())

res = requests.get(base_url + "status", {"url": test_urls['ebay']} )
print(res.json())

res = requests.get(base_url + "me")
print(res.json())