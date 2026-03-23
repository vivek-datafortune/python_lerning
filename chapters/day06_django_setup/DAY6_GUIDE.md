# Day 6: Django Setup & First Project

**Duration**: 3 hours  
**Goal**: Install Django, create your first project, and understand Django's structure

---

## 📋 Learning Objectives

By the end of Day 6, you will:
- ✅ Install Django and create a project
- ✅ Understand Django project structure
- ✅ Run the development server
- ✅ Create your first Django app
- ✅ Use the Django admin panel
- ✅ Understand settings.py configuration

---

## 🔧 Before You Start: Switch from pip to uv

Now that you're starting Django (real project work), switch to `uv` — the modern Python package manager (like npm for Python).

### Install uv (one-time, global)
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
Restart terminal, then verify:
```powershell
uv --version
```

### uv vs pip cheatsheet
| pip (old) | uv (new) | npm equivalent |
|-----------|----------|----------------|
| `pip install django` | `uv add django` | `npm install express` |
| `pip uninstall django` | `uv remove django` | `npm uninstall express` |
| `pip install -r requirements.txt` | `uv sync` | `npm install` |
| `pip freeze > requirements.txt` | auto-handled | auto-handled |

From Day 6 onwards, use `uv add` instead of `pip install` — it auto-updates your dependencies file!

---

## ⏱️ Time Breakdown

| Activity | Duration | Type |
|----------|----------|------|
| Theory: Django Overview | 20 min | Reading |
| Setup: Install Django | 20 min | Hands-on |
| Theory: Project Structure | 20 min | Reading |
| Exercise: Create First App | 30 min | Coding |
| Theory: Admin Panel | 20 min | Reading |
| Mini-Project: Blog Setup | 50 min | Project |

---

## 🎯 Hour 1: Django Overview & Setup (60 min)

### What is Django? (20 min)

#### Django vs Express.js

| Feature | Express.js | Django |
|---------|-----------|--------|
| Philosophy | Minimalist | Batteries included |
| Routing | Manual | URLs config |
| ORM | Choose (Sequelize, Prisma) | Built-in ORM |
| Templates | Choose (EJS, Pug) | Built-in templates |
| Admin | Build yourself | Built-in admin panel |
| Auth | Passport.js | Built-in authentication |

#### Django Components

```
Django Framework
├── ORM (Database)
├── URL Routing
├── Views (Route handlers)
├── Templates (HTML)
├── Forms & Validation
├── Authentication
├── Admin Panel
└── Management Commands
```

### Installing Django (20 min)

```bash
# 1. Create project directory
mkdir django_api_project
cd django_api_project

# 2. Create virtual environment
python -m venv venv

# 3. Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# 4. Install Django and DRF
pip install django djangorestframework

# 5. Verify installation
python -m django --version

# 6. Create requirements.txt
pip freeze > requirements.txt
```

### Creating First Project (20 min)

```bash
# Create Django project
django-admin startproject myproject .

# The '.' creates it in current directory
# Without '.', it creates nested folder
```

#### Project Structure

```
django_api_project/
├── venv/                   # Virtual environment
├── myproject/              # Project configuration folder
│   ├── __init__.py        # Python package marker
│   ├── settings.py        # Project settings (like config.js)
│   ├── urls.py            # Root URL configuration
│   ├── asgi.py            # ASGI deployment
│   └── wsgi.py            # WSGI deployment
├── manage.py              # Django CLI tool
└── requirements.txt
```

#### Run Development Server

```bash
# Run server (like npm run dev)
python manage.py runserver

# Server runs at: http://127.0.0.1:8000/
# Visit it to see Django welcome page!

# Run on different port
python manage.py runserver 8080
```

---

## 🎯 Hour 2: Django Apps & Structure (60 min)

### Django Apps (30 min)

#### Creating an App

```bash
# Create an app (like a module in Node)
python manage.py startapp blog

# This creates:
blog/
├── __init__.py
├── admin.py       # Admin panel config
├── apps.py        # App configuration
├── models.py      # Database models
├── tests.py       # Tests
├── views.py       # Route handlers
└── migrations/    # Database migrations
    └── __init__.py
```

#### Register the App

Edit `myproject/settings.py`:
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Your apps
    'blog',
]
```

### Understanding settings.py (30 min)

```python
# myproject/settings.py

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'your-secret-key-here'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []  # Add your domain in production

# Application definition
INSTALLED_APPS = [
    # Django built-in apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Third-party apps
    'rest_framework',
    
    # Your apps
    'blog',
]

# Database configuration (default: SQLite)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'  # Change to your timezone, e.g., 'America/New_York'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
```

---

## 🎯 Hour 3: Admin Panel & Mini-Project (60 min)

### Django Admin Panel (20 min)

#### Create Superuser

```bash
# Create admin user
python manage.py createsuperuser

# Follow prompts:
# Username: admin
# Email: admin@example.com
# Password: (enter secure password)
```

#### Access Admin Panel

```bash
# Run server
python manage.py runserver

# Visit: http://127.0.0.1:8000/admin/
# Login with your superuser credentials
```

### Mini-Project: Blog Setup (40 min)

#### 1. Create Blog Model

Edit `blog/models.py`:
```python
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    """Blog post model"""
    
    # Status choices
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]
    
    # Fields
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    content = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    """Comment model"""
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['created_at']
    
    def __str__(self):
        return f'Comment by {self.name} on {self.post}'
```

#### 2. Create Migrations

```bash
# Create migration files
python manage.py makemigrations blog

# You'll see:
# Migrations for 'blog':
#   blog/migrations/0001_initial.py
#     - Create model Post
#     - Create model Comment

# Apply migrations
python manage.py migrate

# You'll see tables being created
```

#### 3. Register in Admin

Edit `blog/admin.py`:
```python
from django.contrib import admin
from .models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'status', 'created_at']
    list_filter = ['status', 'created_at', 'author']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'
    ordering = ['-created_at']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'post', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'email', 'content']
```

#### 4. Test in Admin Panel

```bash
# Run server
python manage.py runserver

# Visit: http://127.0.0.1:8000/admin/
# 1. Click "Posts" → "Add Post"
# 2. Fill in the form
# 3. Save and add more posts
# 4. Add some comments too
```

#### 5. Use Django Shell

```bash
# Open Django shell
python manage.py shell

# Try these commands:
>>> from blog.models import Post, Comment
>>> from django.contrib.auth.models import User

# Get all posts
>>> Post.objects.all()

# Get specific post
>>> post = Post.objects.get(id=1)
>>> print(post.title)

# Filter posts
>>> published = Post.objects.filter(status='published')
>>> print(published.count())

# Create a post
>>> user = User.objects.first()
>>> post = Post.objects.create(
    title="My First Post",
    slug="my-first-post",
    author=user,
    content="This is my first blog post!",
    status="published"
)

# Get comments for a post
>>> post.comments.all()

# Exit shell
>>> exit()
```

### Exercise: Enhance Blog Models

Add these features to `blog/models.py`:

```python
# TODO 1: Add 'tags' field to Post model
# Use: models.CharField(max_length=200, blank=True)

# TODO 2: Add 'view_count' field to Post model
# Use: models.IntegerField(default=0)

# TODO 3: Add 'is_featured' field to Post model
# Use: models.BooleanField(default=False)

# TODO 4: Add 'is_approved' field to Comment model
# Use: models.BooleanField(default=False)

# After making changes:
python manage.py makemigrations
python manage.py migrate
```

---

## 🔍 Key Takeaways

### Django Project Structure

```
Project (myproject)
├── Settings & Configurations
├── Root URLs
└── Contains multiple Apps

App (blog, api, users)
├── Models (Database)
├── Views (Logic)
├── URLs (Routing)
├── Templates (HTML)
└── Admin (Admin config)
```

### Important Commands

```bash
# Project
django-admin startproject name .

# App
python manage.py startapp name

# Database
python manage.py makemigrations
python manage.py migrate

# Admin
python manage.py createsuperuser

# Server
python manage.py runserver

# Shell
python manage.py shell
```

---

## 📚 Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Django Tutorial](https://docs.djangoproject.com/en/stable/intro/tutorial01/)
- [Django Admin Docs](https://docs.djangoproject.com/en/stable/ref/contrib/admin/)

---

## ✅ Day 6 Checklist

- [ ] Install Django successfully
- [ ] Create first Django project
- [ ] Create and register an app
- [ ] Create models and run migrations
- [ ] Access and use admin panel
- [ ] Create superuser
- [ ] Use Django shell

---

## 🎯 Homework

1. Explore the admin panel thoroughly
2. Create 5+ blog posts via admin
3. Add more fields to models and migrate
4. **Challenge**: Create a Category model and link it to Post

---

**Tomorrow**: Day 7 - Django Models & ORM Deep Dive

**Great start with Django! 🎉**
