from .models import *


class DAOsItem:
    def listaritem():
        item = Item.objects.all()
        return item 
    
    def salvaritem(name, description):
        i = Item(name=name, 
                 description=description)
        i.save()
    
    def deletaritem(id):
        i = Item.objects.get(pk=id)
        i.delete()
    
    def atualizaritem(name, description, id):
        i = Item.objects.get(pk=id)
        i.name = name
        i.description = description
        i.save()
