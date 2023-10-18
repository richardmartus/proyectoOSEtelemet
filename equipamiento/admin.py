from django.contrib import admin
from .models import Gateway, MarcasMedidores, ModelosMedidores, Modulo, Modulos, Trasmisiones

admin.site.register(Gateway)
admin.site.register(MarcasMedidores)
admin.site.register(ModelosMedidores)
admin.site.register(Modulo)
admin.site.register(Modulos)
admin.site.register(Trasmisiones)
