import requests as req


params = {
  "name": "taa",
  "price": 0,
  "is_offer":True
}
request = req.put("http://127.0.0.1:8000/items/1234" ,params=params)

print(request.text)