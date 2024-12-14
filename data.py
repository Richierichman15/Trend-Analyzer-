# from curl_cffi import requests
# from selectolax.parser import HTMLParser
# import orjson
# from rich import print

# url = 'https://netaura.store/products/pre-lit-mixed-flocked-artificial-christmas-tree-5-6-and-7-feet-with-250-warm-white-led-lights-and-stand'
# resp= requests.get(url, impersonate='chrome120')
# html = HTMLParser(resp.text)
# sripts = html.css("script[type='application/ld+json']")

# for script in sripts:
#     if "offeres" in script.text():
#         data = orjson.loads(script.text())
#         print(data.get("offers"))

# for script in sripts:
#     print(script.text())
