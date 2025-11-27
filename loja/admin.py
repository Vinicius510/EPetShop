from django.contrib import admin
from .models import Pagina, Produto, Contato, Pedido


class PaginaAdmin(admin.ModelAdmin):
    list_display = ('nome_do_site', 'email', 'atualizado_em')
    readonly_fields = ('criado_em', 'atualizado_em')


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'estoque', 'preco', 'atualizado_em')
    list_filter = ('criado_em',)
    search_fields = ('nome', 'descricao')
    readonly_fields = ('criado_em', 'atualizado_em')


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'criado_em')
    list_filter = ('criado_em',)
    search_fields = ('nome', 'email')
    readonly_fields = ('criado_em', 'nome', 'email', 'mensagem')


class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'produto', 'quantidade', 'total', 'data')
    list_filter = ('data', 'usuario')
    search_fields = ('usuario__username', 'produto__nome')
    readonly_fields = ('data',)


admin.site.register(Pagina, PaginaAdmin)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Contato, ContatoAdmin)
admin.site.register(Pedido, PedidoAdmin)
