import requests
url = input("Write the url of the picture")

with open("file.png", "wb") as f:
    f.write(requests.get(url).content)

    
