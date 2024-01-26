from stegano import lsb

# Ocultar mensaje en la imagen
secreto = lsb.hide("logo.jpg", "mensaje oculto")
secreto.save("logo_secreto.png")

# Revelar el mensaje oculto
mensaje_revelado = lsb.reveal("logo_secreto.png")
print(mensaje_revelado)
