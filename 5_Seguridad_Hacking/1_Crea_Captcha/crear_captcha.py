from captcha.image import ImageCaptcha

image = ImageCaptcha(width=200, height=90)

texto = "crhH54"

data = image.generate(texto)

image.write(texto, "captcha2.png")

