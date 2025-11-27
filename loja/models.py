from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Pagina(models.Model):
    """Modelo para armazenar dados institucionais e informações da página inicial."""
    nome_do_site = models.CharField(max_length=200)
    logo_do_site = models.ImageField(upload_to='logos/', null=True, blank=True)
    texto_chamada = models.TextField()
    texto_sobre = models.TextField()
    imagem_sobre = models.ImageField(upload_to='sobre/')
    endereco = models.CharField(max_length=300)
    email = models.EmailField()
    whatsapp = models.CharField(max_length=20)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Páginas"

    def __str__(self):
        return self.nome_do_site


class Produto(models.Model):
    """Modelo para armazenar os produtos disponíveis para compra."""
    nome = models.CharField(max_length=200)
    estoque = models.IntegerField(default=0)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField()
    foto = models.ImageField(upload_to='produtos/')
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome


class Contato(models.Model):
    """Modelo para armazenar as mensagens enviadas pelo formulário de contato."""
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    mensagem = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Contatos"

    def __str__(self):
        return f"{self.nome} - {self.criado_em.strftime('%d/%m/%Y')}"


class Pedido(models.Model):
    """Modelo para registrar os pedidos realizados pelos usuários."""
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pedidos')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=1)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pedido #{self.id} - {self.usuario.username} - {self.produto.nome}"

    class Meta:
        verbose_name_plural = "Pedidos"
        ordering = ['-data']
