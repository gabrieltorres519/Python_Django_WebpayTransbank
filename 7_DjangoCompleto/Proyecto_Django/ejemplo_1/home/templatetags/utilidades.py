from django import template


register = template.Library()

@register.filter(name="ejemploFiltro")
def ejemploFiltro(parametro):
    return f"el valor del parámetro es {parametro}"