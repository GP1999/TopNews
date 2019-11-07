from django import template

register = template.Library()

@register.filter(name='index')
def index(listvar,ind):
    if len(listvar) > ind:    
         return listvar[ind]
    else:
        return listvar[0]