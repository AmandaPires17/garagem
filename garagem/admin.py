from django.contrib import admin

from garagem.models import Marca, Categoria, Acessorios, Cor 

admin.site.register(Marca)
admin.site.register(Categoria)
admin.site.register(Acessorios)
admin.site.register(Cor)