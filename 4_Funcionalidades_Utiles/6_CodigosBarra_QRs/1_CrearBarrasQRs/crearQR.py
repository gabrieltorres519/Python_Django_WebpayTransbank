import qrcode 

img = qrcode.make("https://www.instagram.com/gabrielletorricelli/") # Ponemos la liga a la que redirigirá el QR

print(img)

f = open("qr.png", "wb")
img.save(f)
f.close
