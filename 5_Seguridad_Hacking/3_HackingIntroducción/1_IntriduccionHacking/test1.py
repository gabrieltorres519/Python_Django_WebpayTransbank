import dns.resolver 

def test():
    try: # ns ara obtener los domain names que tiene el dueño del aplicativo que usa esa url
        objetivos = dns.resolver.query("cesarcancino.com", "ns") # En lugar de ns usar A, para obtener la ip del servidor
        print(objetivos)
        for objetivo in objetivos:
            print(objetivo) 
    except Exception as e:
        print("No se pudo")

test()

# Para evitar que alguien ataque de esta manera a tu sitio, existen plataformas que envuelven tu dns en una dirección ip de ellos 
# así el atacante verá la ip que ellos han designado para ocultarte y no la ip real de tu proveedor de hosting

