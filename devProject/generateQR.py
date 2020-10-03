import qrcode
from pyzbar.pyzbar import decode

from PIL import Image




img = qrcode.make('Some data here')

img1 = Image.open(img)
print("hello")
print(img)

result = decode(img1)

print(result)
