# 🍽️ Ateliê da Cris - Site de Receitas

Aplicação web completa desenvolvida com **Django 5**, **HTML5**, **CSS3** e banco de dados **SQLite**.
O projeto é um site de receitas com listagem, detalhes e sistema de categorias — desenvolvido como projeto prático de aprendizagem de desenvolvimento web com Python.

---

## 🖥️ Telas do Projeto

> Página inicial com listagem de receitas por categoria e pesquisa.

---

## 🚀 Tecnologias Utilizadas

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)

---

## ⚙️ Funcionalidades

- ✅ Listagem de receitas na página inicial
- ✅ Página de detalhes de cada receita
- ✅ Sistema de categorias (FK entre `Recipe` e `Category`)
- ✅ Upload de imagem de capa para cada receita
- ✅ Painel administrativo Django (`/admin`) para cadastro de receitas
- ✅ Templates dinâmicos com herança (`{% extends %}`, `{% block %}`, `{% include %}`)
- ✅ Arquivos estáticos organizados (`base_static/`)

---

## 📁 Estrutura do Projeto

```
projeto-site-atelie-da-cris/
│
├── base_static/            # Arquivos CSS e estáticos globais
│   └── global/css/
│
├── base_template/          # Template base HTML (base.html)
│   └── global/
│
├── projeto/                # Configurações do projeto Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── recipes/                # App principal
│   ├── models.py           # Modelos: Recipe e Category
│   ├── views.py            # Views: home, recipeviews
│   ├── urls.py             # Rotas do app
│   ├── admin.py            # Registro no painel admin
│   ├── templates/
│   │   └── recipes/
│   │       ├── page/       # Páginas completas (home, detalhe)
│   │       └── partials/   # Componentes reutilizáveis (header, footer, recipe card)
│   └── migrations/
│
├── utils/                  # Utilitários auxiliares
│   └── recipes/factory.py
│
├── manage.py
├── requirements.txt
└── .gitignore
```

---

## 🔧 Como Executar Localmente

### Pré-requisitos
- Python 3.10+
- pip

### Passo a passo

```bash
# 1. Clone o repositório
git clone https://github.com/Edmundocabocolino/projeto-site-atelie-da-cris.git
cd projeto-site-atelie-da-cris

# 2. Crie e ative o ambiente virtual
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Aplique as migrações do banco de dados
python manage.py migrate

# 5. Crie um superusuário para acessar o admin
python manage.py createsuperuser

# 6. Inicie o servidor de desenvolvimento
python manage.py runserver
```

### 🌐 Acesse no navegador:
- **Site:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Painel Admin:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 📐 Modelos de Dados

```python
class Category(models.Model):
    name = models.CharField(max_length=65)

class Recipe(models.Model):
    title       = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    slug        = models.SlugField(unique=True)
    preparation_step = models.TextField()
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover       = models.ImageField(upload_to='recipes/covers/%Y/%m/%d/')
    category    = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    author      = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
```

---

## 👨‍💻 Autor

**Edmundo Cabocolino**
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/edmundo-do-carmo-cabocolino-06a2a087/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/Edmundocabocolino)
