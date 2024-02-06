from django import template


register = template.Library()

@register.filter(name="ejemploFiltro")
def ejemploFiltro(parametro):
    return f"el valor del parámetro es {parametro}"

@register.filter(name='numberFormat')
def numberFormat(numero):
    if numero == None:
        return 0
    else:
        return "{:,}".format(numero).replace(",",".")
    
