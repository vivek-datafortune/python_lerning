# Day 7: Django Models & ORM Deep Dive

**Duration**: 3 hours  
**Goal**: Master Django's powerful ORM and database relationships

---

## 📋 Learning Objectives

By the end of Day 7, you will:
- ✅ Master Django field types
- ✅ Create relationships (One-to-Many, Many-to-Many)
- ✅ Write complex database queries
- ✅ Use QuerySets effectively
- ✅ Understand migrations in depth
- ✅ Implement model methods and properties

---

## ⏱️ Time Breakdown

| Activity | Duration | Type |
|----------|----------|------|
| Theory: Model Fields | 30 min | Reading |
| Exercise: Field Types | 30 min | Coding |
| Theory: Relationships | 30 min | Reading |
| Exercise: Related Models | 30 min | Coding |
| Theory: QuerySets & Queries | 30 min | Reading |
| Mini-Project: E-commerce Models | 30 min | Project |

---

## 🎯 Hour 1: Model Fields (60 min)

### Django Model Fields (30 min)

```python
from django.db import models

class Product(models.Model):
    # Text fields
    name = models.CharField(max_length=200)              # Short text
    description = models.TextField()                      # Long text
    slug = models.SlugField(unique=True)                 # URL-friendly text
    
    # Numeric fields
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    rating = models.FloatField(default=0.0)
    
    # Boolean
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    
    # Date/Time
    created_at = models.DateTimeField(auto_now_add=True)  # Set once on creation
    updated_at = models.DateTimeField(auto_now=True)      # Update on every save
    publish_date = models.DateField(null=True, blank=True)
    
    # Files
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    pdf = models.FileField(upload_to='documents/', null=True, blank=True)
    
    # Email & URL
    contact_email = models.EmailField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    
    # JSON (Django 3.1+)
    metadata = models.JSONField(default=dict, blank=True)
    
    # Choices
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('archived', 'Archived'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        indexes = [
            models.Index(fields=['slug']),
            models.Index(fields=['created_at']),
        ]
    
    def __str__(self):
        return self.name
```

### Field Options

```python
# Common field options
name = models.CharField(
    max_length=200,              # Maximum length
    null=True,                   # Allow NULL in database
    blank=True,                  # Allow empty in forms
    default='Default Value',     # Default value
    unique=True,                 # Must be unique
    db_index=True,              # Create database index
    verbose_name='Product Name', # Human-readable name
    help_text='Enter product name',
    editable=False,             # Hide from admin forms
)
```

### Practice Exercise (30 min)

Create `day07_models/app/models.py`:

```python
from django.db import models
from django.contrib.auth.models import User

# TODO 1: Create a Book model
class Book(models.Model):
    # Add fields:
    # - title (CharField, 200 chars)
    # - isbn (CharField, 13 chars, unique)
    # - author (CharField, 100 chars)
    # - publish_date (DateField)
    # - pages (IntegerField)
    # - price (DecimalField)
    # - is_available (BooleanField, default True)
    # - cover_image (ImageField, optional)
    # - created_at, updated_at
    pass

# TODO 2: Create a Movie model
class Movie(models.Model):
    GENRE_CHOICES = [
        ('action', 'Action'),
        ('comedy', 'Comedy'),
        ('drama', 'Drama'),
        ('horror', 'Horror'),
        ('scifi', 'Science Fiction'),
    ]
    
    # Add fields:
    # - title
    # - genre (choices from above)
    # - release_year
    # - duration (in minutes)
    # - rating (1.0 to 10.0)
    # - director
    # - is_available
    pass

# TODO 3: Run migrations
# python manage.py makemigrations
# python manage.py migrate
```

---

## 🎯 Hour 2: Relationships (60 min)

### One-to-Many (ForeignKey) (20 min)

```python
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    # Many books can have one author
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,      # Delete books when author is deleted
        related_name='books'           # Access: author.books.all()
    )
    
    def __str__(self):
        return self.title

# Usage:
# author = Author.objects.create(name="John Doe")
# book = Book.objects.create(title="Python 101", author=author)
# author.books.all()  # Get all books by this author
```

### on_delete Options

```python
# CASCADE - Delete objects when parent is deleted
author = models.ForeignKey(Author, on_delete=models.CASCADE)

# PROTECT - Prevent deletion if references exist
category = models.ForeignKey(Category, on_delete=models.PROTECT)

# SET_NULL - Set to NULL when parent is deleted
owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

# SET_DEFAULT - Set to default value
user = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=1)
```

### Many-to-Many (20 min)

```python
class Tag(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=200)
    # Many articles can have many tags
    tags = models.ManyToManyField(Tag, related_name='articles', blank=True)
    
    def __str__(self):
        return self.title

# Usage:
# article = Article.objects.create(title="Django Tutorial")
# tag1 = Tag.objects.create(name="Python")
# tag2 = Tag.objects.create(name="Django")
# article.tags.add(tag1, tag2)
# article.tags.all()  # Get all tags for article
# tag1.articles.all()  # Get all articles with this tag
```

### One-to-One (20 min)

```python
from django.contrib.auth.models import User

class UserProfile(models.Model):
    # One user has one profile
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    avatar = models.ImageField(upload_to='avatars/', null=True)
    website = models.URLField(blank=True)
    
    def __str__(self):
        return f"{self.user.username}'s profile"

# Usage:
# user = User.objects.get(username='john')
# profile = UserProfile.objects.create(user=user, bio="Hello!")
# user.userprofile  # Access profile from user
```

### Practice Exercise (30 min)

```python
# TODO 1: Create a blog with relationships
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # TODO: Add ForeignKey to Category
    # TODO: Add ManyToManyField for tags
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    # TODO: Add ForeignKey to Post
    # TODO: Add ForeignKey to User
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
```

---

## 🎯 Hour 3: QuerySets & Mini-Project (60 min)

### QuerySet Operations (30 min)

```python
from django.db.models import Q, F, Count, Avg, Sum

# Basic queries
Product.objects.all()                    # Get all
Product.objects.get(id=1)                # Get one (raises error if not found)
Product.objects.filter(is_active=True)   # Filter
Product.objects.exclude(price=0)         # Exclude
Product.objects.first()                  # First object
Product.objects.last()                   # Last object
Product.objects.count()                  # Count

# Filtering
Product.objects.filter(price__gt=10)           # Greater than
Product.objects.filter(price__gte=10)          # Greater than or equal
Product.objects.filter(price__lt=100)          # Less than
Product.objects.filter(price__lte=100)         # Less than or equal
Product.objects.filter(name__icontains='phone') # Case-insensitive contains
Product.objects.filter(name__istartswith='iPhone')
Product.objects.filter(created_at__year=2024)

# Complex queries (OR)
Product.objects.filter(Q(price__lt=10) | Q(is_featured=True))

# Complex queries (AND)
Product.objects.filter(Q(price__lt=100) & Q(stock__gt=0))

# Field lookups
Product.objects.filter(price__range=(10, 100))  # Between
Product.objects.filter(name__in=['iPhone', 'Samsung'])

# Ordering
Product.objects.order_by('price')         # Ascending
Product.objects.order_by('-price')        # Descending
Product.objects.order_by('category', '-price')

# Limiting
Product.objects.all()[:10]               # First 10
Product.objects.all()[10:20]             # Next 10

# Aggregations
from django.db.models import Avg, Sum, Count, Max, Min

Product.objects.aggregate(Avg('price'))
Product.objects.aggregate(Sum('stock'))
Product.objects.aggregate(Count('id'))
Product.objects.aggregate(Max('price'), Min('price'))

# Annotations
Product.objects.annotate(comment_count=Count('comments'))

# Select related (for ForeignKey - JOIN)
Book.objects.select_related('author').all()

# Prefetch related (for ManyToMany)
Article.objects.prefetch_related('tags').all()

# Exists
Product.objects.filter(price__gt=1000).exists()

# Update
Product.objects.filter(stock=0).update(is_active=False)

# Delete
Product.objects.filter(is_active=False).delete()

# F expressions (compare fields)
Product.objects.filter(price__gt=F('cost') * 1.5)
```

### Mini-Project: E-commerce Models (30 min)

Create `day07_ecommerce/shop/models.py`:

```python
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    
    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    @property
    def is_in_stock(self):
        return self.stock > 0

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.quantity}x {self.product.name}"
    
    @property
    def subtotal(self):
        return self.quantity * self.price

# Register in admin.py
# Then use Django shell to test queries:

"""
# Create categories and products
category = Category.objects.create(name="Electronics", slug="electronics")
product = Product.objects.create(
    name="iPhone 15",
    slug="iphone-15",
    description="Latest iPhone",
    price=999.99,
    stock=50,
    category=category
)

# Query exercises
# 1. Get all products in stock
Product.objects.filter(stock__gt=0)

# 2. Get products by category
category.products.all()

# 3. Get expensive products (> $500)
Product.objects.filter(price__gt=500)

# 4. Get user's orders
user = User.objects.first()
user.orders.all()

# 5. Get order items
order = Order.objects.first()
order.items.all()

# 6. Calculate order total
order.items.aggregate(Sum('price))
"""
```

---

## 🔍 Key Takeaways

### Model Relationships

| Type | Django Field | Example |
|------|-------------|---------|
| One-to-Many | `ForeignKey` | Author → Books |
| Many-to-Many | `ManyToManyField` | Articles ↔ Tags |
| One-to-One | `OneToOneField` | User → Profile |

### Important QuerySet Methods

- **Retrieving**: `all()`, `get()`, `filter()`, `exclude()`
- **Limiting**: `first()`, `last()`, `[:10]`
- **Aggregating**: `count()`, `sum()`, `avg()`, `max()`, `min()`
- **Ordering**: `order_by()`
- **Optimization**: `select_related()`, `prefetch_related()`

---

## 📚 Resources

- [Django Model Field Reference](https://docs.djangoproject.com/en/stable/ref/models/fields/)
- [QuerySet API](https://docs.djangoproject.com/en/stable/ref/models/querysets/)
- [Making Queries](https://docs.djangoproject.com/en/stable/topics/db/queries/)

---

## ✅ Day 7 Checklist

- [ ] Understand Django field types
- [ ] Create ForeignKey relationships
- [ ] Implement ManyToManyField
- [ ] Write complex queries with filters
- [ ] Use aggregations and annotations
- [ ] Complete e-commerce models

---

## 🎯 Homework

1. Practice all QuerySet operations in Django shell
2. Create complex queries for your models
3. Add more models to e-commerce project
4. **Challenge**: Implement a review system (User → Product reviews)

---

**Tomorrow**: Day 8 - Django REST Framework Basics

**You're mastering Django! 💪**
