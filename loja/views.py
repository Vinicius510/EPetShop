from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from django.db.models import Q
from .models import Pagina, Produto, Contato, Pedido
from .forms import CadastroForm, LoginForm, ContatoForm, PedidoForm


def index(request):
    """Página inicial com informações da loja e produtos."""
    try:
        pagina = Pagina.objects.first()
    except Pagina.DoesNotExist:
        pagina = None
    
    produtos = Produto.objects.all()
    context = {
        'pagina': pagina,
        'produtos': produtos,
    }
    return render(request, 'loja/index.html', context)


@require_http_methods(["GET", "POST"])
def cadastro(request):
    """Página de cadastro de usuário."""
    if request.user.is_authenticated:
        return redirect('loja:index')
    
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('loja:index')
    else:
        form = CadastroForm()
    
    return render(request, 'loja/cadastro.html', {'form': form})


@require_http_methods(["GET", "POST"])
def login_view(request):
    """Página de login."""
    if request.user.is_authenticated:
        return redirect('loja:index')
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Bem-vindo, {user.username}!')
                return redirect('loja:index')
            else:
                messages.error(request, 'Usuário ou senha inválidos.')
    else:
        form = LoginForm()
    
    return render(request, 'loja/login.html', {'form': form})


@login_required(login_url='loja:login')
def logout_view(request):
    """Logout do usuário."""
    logout(request)
    messages.success(request, 'Você foi desconectado.')
    return redirect('loja:index')


@login_required(login_url='loja:login')
def perfil(request):
    """Página de perfil do usuário com histórico de pedidos."""
    pedidos = Pedido.objects.filter(usuario=request.user)
    context = {
        'pedidos': pedidos,
    }
    return render(request, 'loja/perfil.html', context)


@require_http_methods(["GET", "POST"])
def comprar(request, produto_id):
    """Página de compra de um produto."""
    if not request.user.is_authenticated:
        return redirect('loja:login')
    
    produto = get_object_or_404(Produto, id=produto_id)
    
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            quantidade = form.cleaned_data['quantidade']
            if quantidade > produto.estoque:
                messages.error(request, 'Quantidade solicitada maior que o estoque disponível.')
            else:
                total = produto.preco * quantidade
                pedido = Pedido.objects.create(
                    usuario=request.user,
                    produto=produto,
                    quantidade=quantidade,
                    total=total
                )
                produto.estoque -= quantidade
                produto.save()
                messages.success(request, 'Pedido realizado com sucesso!')
                return redirect('loja:perfil')
    else:
        form = PedidoForm()
    
    context = {
        'produto': produto,
        'form': form,
    }
    return render(request, 'loja/comprar.html', context)


@require_http_methods(["POST"])
def processar_pedido(request):
    """Processa um pedido (método alternativo)."""
    if not request.user.is_authenticated:
        return redirect('loja:login')
    
    produto_id = request.POST.get('produto_id')
    quantidade = request.POST.get('quantidade')
    
    try:
        quantidade = int(quantidade)
        produto = get_object_or_404(Produto, id=produto_id)
        
        if quantidade > produto.estoque:
            messages.error(request, 'Quantidade solicitada maior que o estoque disponível.')
        else:
            total = produto.preco * quantidade
            pedido = Pedido.objects.create(
                usuario=request.user,
                produto=produto,
                quantidade=quantidade,
                total=total
            )
            produto.estoque -= quantidade
            produto.save()
            messages.success(request, 'Pedido realizado com sucesso!')
    except (ValueError, TypeError):
        messages.error(request, 'Quantidade inválida.')
    
    return redirect('loja:perfil')


@require_http_methods(["GET", "POST"])
def contato(request):
    """Página de contato."""
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mensagem enviada com sucesso!')
            return redirect('loja:index')
    else:
        form = ContatoForm()
    
    return render(request, 'loja/contato.html', {'form': form})
