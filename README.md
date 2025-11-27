# E-commerce Pet Shop em Django

Um projeto completo de e-commerce para uma pet shop, desenvolvido com Django, incluindo autenticação de usuários, gerenciamento de produtos, pedidos e painel administrativo.

## Características

### Modelos de Dados
- **Pagina:** Informações institucionais da loja (nome, logo, endereço, contato)
- **Produto:** Catálogo de produtos com estoque e preço
- **Contato:** Mensagens enviadas pelos visitantes
- **Pedido:** Registro de compras com atualização automática de estoque

### Funcionalidades

#### Para Usuários Comuns
- Cadastro e autenticação
- Visualização de produtos
- Realização de compras com especificação de quantidade
- Histórico de pedidos no perfil
- Envio de mensagens de contato

#### Para Administradores
- Acesso completo ao painel administrativo Django
- CRUD de páginas (informações institucionais)
- CRUD de produtos
- Visualização de mensagens de contato
- Visualização de pedidos

### Interface
- Design moderno e responsivo
- Cores personalizadas (vermelho e teal)
- Validação visual de formulários
- Sistema de mensagens (sucesso/erro)
- Ícones FontAwesome
- Compatível com mobile, tablet e desktop

## Requisitos

- Python 3.8+
- Django 5.2+
- Pillow (para processamento de imagens)

## Instalação

1. **Clone ou extraia o projeto:**
```bash
cd projeto-de-petshop-f5bd91c2
```

2. **Crie um ambiente virtual:**
```bash
python3 -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

3. **Instale as dependências:**
```bash
pip install django pillow
```

4. **Execute as migrações:**
```bash
python3 manage.py migrate
```

5. **Crie um superusuário (opcional):**
```bash
python3 manage.py createsuperuser
```

6. **Inicie o servidor:**
```bash
python3 manage.py runserver
```

7. **Acesse a aplicação:**
- Página inicial: http://localhost:8000/
- Painel administrativo: http://localhost:8000/admin/

## Estrutura do Projeto

```
projeto-de-petshop-f5bd91c2/
├── petshop/                    # Configurações do projeto
│   ├── settings.py            # Configurações Django
│   ├── urls.py                # URLs principais
│   ├── wsgi.py                # Configuração WSGI
│   └── asgi.py                # Configuração ASGI
├── loja/                       # App principal
│   ├── models.py              # Modelos de dados
│   ├── views.py               # Views/Controladores
│   ├── forms.py               # Formulários
│   ├── urls.py                # URLs da app
│   ├── admin.py               # Configuração do painel admin
│   └── migrations/            # Migrações do banco de dados
├── templates/                  # Templates HTML
│   ├── base.html              # Template base
│   └── loja/                   # Templates da app
│       ├── index.html
│       ├── cadastro.html
│       ├── login.html
│       ├── comprar.html
│       ├── perfil.html
│       └── contato.html
├── static/                     # Arquivos estáticos (CSS, JS, imagens)
├── media/                      # Arquivos enviados pelos usuários
├── db.sqlite3                  # Banco de dados SQLite
└── manage.py                   # Script de gerenciamento Django
```

## Credenciais de Teste

**Superusuário:**
- Usuário: `admin`
- Senha: `admin123`

**Produtos de Exemplo:**
- Ração Premium para Cães - R$ 89,90
- Brinquedo Interativo para Gatos - R$ 45,50
- Coleira com GPS - R$ 199,90
- Cama Confortável para Pets - R$ 129,90
- Shampoo Neutro para Pets - R$ 35,90
- Escova de Banho para Pets - R$ 29,90

## URLs Principais

| URL | Descrição |
|-----|-----------|
| `/` | Página inicial |
| `/cadastro/` | Formulário de cadastro |
| `/login/` | Formulário de login |
| `/logout/` | Logout do usuário |
| `/perfil/` | Perfil do usuário (requer autenticação) |
| `/comprar/<id>/` | Página de compra do produto (requer autenticação) |
| `/contato/` | Formulário de contato |
| `/admin/` | Painel administrativo |

## Funcionalidades Principais

### Página Inicial
- Exibe informações da loja (nome, logo, texto de chamada)
- Seção "Sobre Nós" com imagem
- Grid de produtos com imagem, preço e botão de compra
- Seção de contato com informações e formulário

### Cadastro e Login
- Validação de email duplicado
- Requisitos de senha
- Redirecionamento automático se já autenticado
- Mensagens de sucesso/erro

### Compra de Produtos
- Seleção de quantidade
- Cálculo dinâmico do total
- Validação de estoque
- Atualização automática do estoque após compra

### Perfil do Usuário
- Exibição de dados pessoais
- Histórico completo de pedidos
- Cálculo automático do total gasto

### Painel Administrativo
- Gerenciamento de informações da loja
- CRUD completo de produtos
- Visualização de mensagens de contato
- Visualização de pedidos

## Personalização

### Modificar Informações da Loja
Acesse `/admin/` e edite o modelo "Páginas" com:
- Nome do site
- Logo
- Textos de chamada e sobre
- Endereço, email e WhatsApp

### Adicionar Novos Produtos
No painel administrativo, clique em "Produtos" e adicione:
- Nome
- Descrição
- Preço
- Estoque
- Foto

### Customizar Cores
Edite as variáveis CSS em `templates/base.html`:
```css
:root {
    --primary-color: #FF6B6B;      /* Vermelho */
    --secondary-color: #4ECDC4;    /* Teal */
    --dark-color: #2C3E50;         /* Cinza escuro */
    --light-color: #ECF0F1;        /* Cinza claro */
}
```

## Segurança

- Proteção CSRF em todos os formulários
- Validação de entrada em formulários
- Autenticação obrigatória para compras
- Senhas criptografadas
- Proteção contra SQL injection (Django ORM)

## Próximas Melhorias

- [ ] Integração com Google Maps
- [ ] Sistema de pagamento (Stripe/PayPal)
- [ ] Envio de emails de confirmação
- [ ] Carrinho de compras persistente
- [ ] Avaliações e comentários de produtos
- [ ] Cupons de desconto
- [ ] Relatórios de vendas
- [ ] Notificações por email
