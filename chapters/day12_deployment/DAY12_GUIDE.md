# Day 12: Deployment & Final Project

**Duration**: 3 hours  
**Goal**: Deploy your Django API to production and complete a final project

---

## 📋 Learning Objectives

By the end of Day 12, you will:
- ✅ Prepare Django for production
- ✅ Deploy to a hosting platform
- ✅ Configure environment variables
- ✅ Set up database in production
- ✅ Complete a final project
- ✅ Plan your next steps

---

## ⏱️ Time Breakdown

| Activity | Duration | Type |
|----------|----------|------|
| Theory: Production Setup | 40 min | Reading |
| Exercise: Deploy to Railway | 40 min | Hands-on |
| Theory: Post-Deployment | 20 min | Reading |
| Final Project: Build Complete API | 80 min | Project |

---

## 🎯 Hour 1: Production Setup (60 min)

### Preparing for Production (40 min)

#### 1. Security Settings

Create `settings/production.py`:
```python
from .base import *

DEBUG = False
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',')

# Security settings
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Database - Use PostgreSQL in production
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT', '5432'),
    }
}

# Static and Media files
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_ROOT = os.path.join(BASE_DIR, 'mediafiles')

# WhiteNoise for static files
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

#### 2. Install Production Dependencies

```bash
pip install gunicorn whitenoise psycopg2-binary python-dotenv
pip freeze > requirements.txt
```

#### 3. Create Procfile (for deployment)

```
web: gunicorn myproject.wsgi --log-file -
```

#### 4. Configure WhiteNoise

`settings.py`:
```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Add this
    # ... other middleware
]
```

#### 5. Runtime.txt (specify Python version)

```
python-3.11.0
```

#### 6. requirements.txt

```
Django>=5.0,<6.0
djangorestframework>=3.14
djangorestframework-simplejwt>=5.3
django-cors-headers>=4.3
django-filter>=24.1
python-dotenv>=1.0
gunicorn>=21.2
whitenoise>=6.6
psycopg2-binary>=2.9
Pillow>=10.1  # For ImageField
```

### Environment Variables (20 min)

`.env.production`:
```env
# Security
SECRET_KEY=your-super-secret-key-here-use-generate-secret-key
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com,yourapp.railway.app

# Database (provided by Railway)
DATABASE_URL=postgresql://user:password@host:port/database

# Or individual settings:
DB_ENGINE=django.db.backends.postgresql
DB_NAME=railway
DB_USER=postgres
DB_PASSWORD=your-db-password
DB_HOST=containers-us-west-1.railway.app
DB_PORT=5432

# AWS S3 (optional, for media files)
AWS_ACCESS_KEY_ID=your-key
AWS_SECRET_ACCESS_KEY=your-secret
AWS_STORAGE_BUCKET_NAME=your-bucket
AWS_S3_REGION_NAME=us-east-1
```

**Generate Secret Key:**
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

---

## 🎯 Hour 2: Deployment to Railway (60 min)

### Deploy to Railway (40 min)

#### Step 1: Prepare Project

```bash
# Initialize git (if not already)
git init
git add .
git commit -m "Initial commit"

# Create .gitignore
cat > .gitignore << EOL
*.pyc
__pycache__/
db.sqlite3
.env
venv/
.DS_Store
media/
staticfiles/
EOL

git add .gitignore
git commit -m "Add gitignore"
```

#### Step 2: Railway Setup

1. Go to [railway.app](https://railway.app)
2. Sign up with GitHub
3. Click "New Project"
4. Select "Deploy from GitHub repo"
5. Choose your repository
6. Railway will detect Django and provision PostgreSQL

#### Step 3: Configure Environment Variables

In Railway dashboard, add:
```
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=yourapp.railway.app
DISABLE_COLLECTSTATIC=0
```

#### Step 4: Add Database

Railway automatically adds PostgreSQL. Get the connection string:
- Click on PostgreSQL service
- Copy `DATABASE_URL`

#### Step 5: Deploy

```bash
# Push to GitHub
git push origin main

# Railway automatically deploys!
```

#### Step 6: Run Migrations

In Railway CLI or dashboard:
```bash
railway run python manage.py migrate
railway run python manage.py createsuperuser
```

### Alternative: Deploy to Heroku

```bash
# Install Heroku CLI
# https://devcenter.heroku.com/articles/heroku-cli

# Login
heroku login

# Create app
heroku create your-app-name

# Add PostgreSQL
heroku addons:create heroku-postgresql:mini

# Set environment variables
heroku config:set SECRET_KEY=your-secret-key
heroku config:set DEBUG=False

# Deploy
git push heroku main

# Run migrations
heroku run python manage.py migrate
heroku run python manage.py createsuperuser

# Open app
heroku open
```

### Alternative: Deploy to PythonAnywhere

1. Create account at [pythonanywhere.com](https://www.pythonanywhere.com)
2. Upload your code or clone from GitHub
3. Create virtual environment
4. Configure WSGI file
5. Set up static files
6. Reload web app

### Post-Deployment Checklist (20 min)

- [ ] Environment variables configured
- [ ] Database connected
- [ ] Migrations run
- [ ] Superuser created
- [ ] Static files collected
- [ ] CORS configured for frontend
- [ ] SSL enabled (HTTPS)
- [ ] API endpoints working
- [ ] Admin panel accessible

---

## 🎯 Hour 3: Final Project (80 min)

### Build Complete Task Management API

Create a production-ready task management API with:

#### Features Checklist

**User Management**
- [ ] User registration
- [ ] Login with JWT
- [ ] User profile

**Task Management**
- [ ] Create tasks
- [ ] List tasks (with pagination)
- [ ] Update tasks
- [ ] Delete tasks
- [ ] Filter by status, priority, due date
- [ ] Search tasks

**Categories**
- [ ] Create categories
- [ ] Assign tasks to categories
- [ ] List tasks by category

**Advanced Features**
- [ ] Task comments
- [ ] File attachments
- [ ] Task assignments (multi-user)
- [ ] Due date reminders
- [ ] Task statistics

#### Project Structure

```
taskmanager/
├── taskmanager/
│   ├── settings/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── development.py
│   │   └── production.py
│   ├── urls.py
│   └── wsgi.py
├── apps/
│   ├── users/
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── tests/
│   ├── tasks/
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── filters.py
│   │   ├── permissions.py
│   │   └── tests/
│   └── categories/
├── requirements/
│   ├── base.txt
│   ├── development.txt
│   └── production.txt
├── .env.example
├── .gitignore
├── Procfile
├── runtime.txt
├── README.md
└── manage.py
```

#### Quick Start Code

`tasks/models.py`:
```python
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    color = models.CharField(max_length=7, default='#3B82F6')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='categories')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['name']
    
    def __str__(self):
        return self.name

class Task(models.Model):
    STATUS_CHOICES = [
        ('todo', 'To Do'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    ]
    
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo')
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='medium')
    due_date = models.DateTimeField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='tasks')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    assigned_to = models.ManyToManyField(User, related_name='assigned_tasks', blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['created_at']
    
    def __str__(self):
        return f'Comment by {self.user.username} on {self.task.title}'

class Attachment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='attachments')
    file = models.FileField(upload_to='attachments/')
    filename = models.CharField(max_length=255)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.filename
```

#### API Documentation (README.md)

```markdown
# Task Manager API

RESTful API for task management built with Django REST Framework.

## Features

- User authentication (JWT)
- CRUD operations for tasks
- Categories and tags
- Task filtering and search
- File attachments
- Task comments
- Multi-user assignment

## API Endpoints

### Authentication
- POST /api/auth/register/ - Register new user
- POST /api/auth/token/ - Login (get JWT)
- POST /api/auth/token/refresh/ - Refresh token
- GET /api/auth/me/ - Get current user

### Tasks
- GET /api/tasks/ - List all tasks
- POST /api/tasks/ - Create task
- GET /api/tasks/{id}/ - Get task detail
- PUT /api/tasks/{id}/ - Update task
- PATCH /api/tasks/{id}/ - Partial update
- DELETE /api/tasks/{id}/ - Delete task
- GET /api/tasks/my_tasks/ - Get user's tasks
- GET /api/tasks/assigned/ - Get assigned tasks

### Categories
- GET /api/categories/ - List categories
- POST /api/categories/ - Create category
- GET /api/categories/{id}/ - Get category
- PUT /api/categories/{id}/ - Update category
- DELETE /api/categories/{id}/ - Delete category

### Comments
- GET /api/comments/ - List comments
- POST /api/comments/ - Create comment
- DELETE /api/comments/{id}/ - Delete comment

## Query Parameters

### Filtering
- ?status=todo
- ?priority=high
- ?category=1

### Search
- ?search=keyword

### Ordering
- ?ordering=due_date
- ?ordering=-created_at

### Pagination
- ?page=2
- ?page_size=20

## Setup

\`\`\`bash
# Clone repository
git clone https://github.com/yourusername/taskmanager.git
cd taskmanager

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate

# Install dependencies
pip install -r requirements/development.txt

# Copy environment variables
cp .env.example .env

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run server
python manage.py runserver
\`\`\`

## Testing

\`\`\`bash
python manage.py test
coverage run --source='.' manage.py test
coverage report
\`\`\`

## Deployment

See [DEPLOYMENT.md](DEPLOYMENT.md) for deployment instructions.

## License

MIT
```

---

## 🔍 Key Takeaways

### Production Checklist

- ✅ Set `DEBUG = False`
- ✅ Configure `ALLOWED_HOSTS`
- ✅ Use environment variables
- ✅ Use production database (PostgreSQL)
- ✅ Configure static files
- ✅ Enable HTTPS
- ✅ Set security headers
- ✅ Use gunicorn
- ✅ Run migrations
- ✅ Collect static files

### Deployment Platforms

| Platform | Pros | Cons |
|----------|------|------|
| **Railway** | Easy, free tier, PostgreSQL included | Limited free resources |
| **Heroku** | Mature, lots of addons | Paid only |
| **PythonAnywhere** | Python-focused, easy | Limited on free tier |
| **AWS/GCP** | Full control, scalable | Complex setup |
| **DigitalOcean** | Good balance | Requires server management |

---

## 📚 Resources

- [Django Deployment Checklist](https://docs.djangoproject.com/en/stable/howto/deployment/checklist/)
- [Railway Documentation](https://docs.railway.app/)
- [Heroku Django Tutorial](https://devcenter.heroku.com/articles/django-app-configuration)
- [WhiteNoise](http://whitenoise.evans.io/)

---

## ✅ Day 12 Checklist

- [ ] Configure production settings
- [ ] Deploy to hosting platform
- [ ] Set up production database
- [ ] Configure environment variables
- [ ] Run migrations in production
- [ ] Test deployed API
- [ ] Complete final project

---

## 🎯 What's Next?

### Continue Learning

1. **Advanced Django**
   - Custom user models
   - Celery for background tasks
   - Redis for caching
   - WebSockets with Channels

2. **Frontend Integration**
   - Build React frontend
   - Connect to your API
   - Handle authentication
   - Deploy full-stack app

3. **DevOps**
   - Docker containerization
   - CI/CD with GitHub Actions
   - Monitoring and logging
   - Load balancing

4. **Advanced Features**
   - Real-time notifications
   - File processing
   - Payment integration
   - Email services

### Project Ideas

- Social media platform
- E-commerce marketplace
- Content management system
- Project management tool
- Learning management system
- Real estate listings
- Job board
- Event management system

---

## 🎉 Congratulations!

You've completed the 12-day Python & Django learning journey!

You now know:
- ✅ Python fundamentals
- ✅ Object-oriented programming
- ✅ Django framework
- ✅ Django REST Framework
- ✅ Authentication & permissions
- ✅ Testing
- ✅ Deployment

**You're ready to build professional APIs!**

Keep coding, keep learning, and build amazing things! 🚀

---

## 📝 Feedback & Next Steps

1. **Review your progress**: Go through all 12 days
2. **Build a portfolio project**: Use what you learned
3. **Contribute to open source**: Find Django projects on GitHub
4. **Join communities**: Django Discord, Reddit, Stack Overflow
5. **Keep learning**: Follow Django blogs and tutorials

**Happy coding! 🐍 🎊**
