import requests
from PIL import Image
from io import BytesIO

r = requests.get("https://t3.ftcdn.net/jpg/05/71/06/76/360_F_571067620_JS5T5TkDtu3gf8Wqm78KoJRF1vobPvo6.jpg")
i = Image.open(BytesIO(r.content))
fp = open("img.jpg","wb")
i.save(fp)
fp.close()
