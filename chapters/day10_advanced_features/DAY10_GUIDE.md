# Day 10: Advanced API Features - Filtering, Search, Pagination

**Duration**: 3 hours  
**Goal**: Add advanced features to make your APIs production-ready

---

## 📋 Learning Objectives

By the end of Day 10, you will:
- ✅ Implement filtering and sorting
- ✅ Add search functionality
- ✅ Configure pagination
- ✅ Handle file uploads
- ✅ Add CORS headers
- ✅ Implement API versioning

---

## ⏱️ Time Breakdown

| Activity | Duration | Type |
|----------|----------|------|
| Theory: Filtering & Search | 40 min | Reading |
| Exercise: Implement Filters | 30 min | Coding |
| Theory: Pagination | 20 min | Reading |
| Exercise: Configure Pagination | 20 min | Coding |
| Theory: File Uploads & CORS | 30 min | Reading |
| Mini-Project: Feature-Rich API | 40 min | Project |

---

## 🎯 Hour 1: Filtering & Search (60 min)

### Django Filter (40 min)

#### Installation

```bash
pip install django-filter
pip freeze > requirements.txt
```

Configure `settings.py`:
```python
INSTALLED_APPS = [
    # ...
    'django_filters',
]

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ],
}
```

#### Simple Filtering

```python
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'is_active', 'price']

# Usage:
# GET /api/products/?category=1
# GET /api/products/?is_active=true
# GET /api/products/?price=99.99
```

#### Advanced Filtering

Create `api/filters.py`:
```python
import django_filters
from .models import Product

class ProductFilter(django_filters.FilterSet):
    # Exact match
    category = django_filters.NumberFilter(field_name='category')
    
    # Range filters
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    
    # Date filters
    created_after = django_filters.DateFilter(field_name='created_at', lookup_expr='gte')
    created_before = django_filters.DateFilter(field_name='created_at', lookup_expr='lte')
    
    # Text filters
    name = django_filters.CharFilter(lookup_expr='icontains')
    
    # Boolean
    in_stock = django_filters.BooleanFilter(method='filter_in_stock')
    
    # Choice filter
    status = django_filters.ChoiceFilter(choices=[
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ])
    
    class Meta:
        model = Product
        fields = ['category', 'is_active']
    
    def filter_in_stock(self, queryset, name, value):
        if value:
            return queryset.filter(stock__gt=0)
        return queryset.filter(stock=0)

# Use in ViewSet
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter

# Usage:
# GET /api/products/?min_price=10&max_price=100
# GET /api/products/?name=phone
# GET /api/products/?in_stock=true
# GET /api/products/?created_after=2024-01-01
```

### Search Filter (20 min)

```python
from rest_framework import filters

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description', 'category__name']

# Usage:
# GET /api/products/?search=phone
# Searches in name, description, and category name

# Advanced search patterns:
# '^name'  - starts with
# '=name'  - exact match
# '@name'  - full-text search (PostgreSQL only)
# '$name'  - regex search
```

### Ordering Filter

```python
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['price', 'created_at', 'name']
    ordering = ['-created_at']  # Default ordering

# Usage:
# GET /api/products/?ordering=price
# GET /api/products/?ordering=-price  (descending)
# GET /api/products/?ordering=price,-created_at  (multiple)
```

---

## 🎯 Hour 2: Pagination (60 min)

### Pagination Styles (30 min)

#### 1. PageNumber Pagination (Default)

Configure `settings.py`:
```python
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}

# Response format:
{
    "count": 100,
    "next": "http://api.example.org/products/?page=2",
    "previous": null,
    "results": [...]
}

# Usage:
# GET /api/products/?page=1
# GET /api/products/?page=2&page_size=20
```

#### 2. Limit/Offset Pagination

```python
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10,
}

# Usage:
# GET /api/products/?limit=10&offset=20
```

#### 3. Cursor Pagination (for large datasets)

```python
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.CursorPagination',
    'PAGE_SIZE': 10,
}

# Usage:
# GET /api/products/?cursor=cD0yMDIz...
```

#### 4. Custom Pagination

Create `api/pagination.py`:
```python
from rest_framework.pagination import PageNumberPagination

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class LargeResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000

# Use in ViewSet
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = StandardResultsSetPagination
```

### Per-View Pagination (30 min)

```python
from .pagination import StandardResultsSetPagination, LargeResultsSetPagination

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def get_pagination_class(self):
        if self.action == 'list':
            return StandardResultsSetPagination
        return None  # No pagination for detail view
```

---

## 🎯 Hour 3: File Uploads & CORS (60 min)

### File Uploads (30 min)

#### Models with Files

```python
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    pdf_manual = models.FileField(upload_to='manuals/', null=True, blank=True)
    
    def __str__(self):
        return self.name
```

#### Configure Media Files

`settings.py`:
```python
import os

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

`urls.py`:
```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... your url patterns
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

#### Serializer with File Fields

```python
class ProductSerializer(serializers.ModelSerializer):
    # Will automatically handle file uploads
    image_url = serializers.SerializerMethodField()
    
    class Meta:
        model = Product
        fields = ['id', 'name', 'image', 'image_url', 'pdf_manual']
    
    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image and request:
            return request.build_absolute_uri(obj.image.url)
        return None
```

#### Upload Files via API

```bash
# Using multipart/form-data
POST /api/products/
Content-Type: multipart/form-data

name: "iPhone 15"
price: 999.99
image: [file]
```

### CORS Headers (30 min)

#### Install django-cors-headers

```bash
pip install django-cors-headers
pip freeze > requirements.txt
```

#### Configure CORS

`settings.py`:
```python
INSTALLED_APPS = [
    # ...
    'corsheaders',
    # ...
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # Should be at the top
    'django.middleware.security.SecurityMiddleware',
    # ...
]

# Development - Allow all origins
CORS_ALLOW_ALL_ORIGINS = True

# Production - Specific origins
CORS_ALLOWED_ORIGINS = [
    "https://example.com",
    "https://sub.example.com",
    "http://localhost:3000",
    "http://localhost:8080",
]

# Allow credentials
CORS_ALLOW_CREDENTIALS = True

# Allowed methods
CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]

# Allowed headers
CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]
```

### Mini-Project: Feature-Rich Product API

```python
# models.py
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    
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
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['slug']),
            models.Index(fields=['category', 'is_active']),
        ]
    
    def __str__(self):
        return self.name

# filters.py
import django_filters
from .models import Product

class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    category = django_filters.NumberFilter()
    in_stock = django_filters.BooleanFilter(method='filter_in_stock')
    
    class Meta:
        model = Product
        fields = ['category', 'is_active', 'is_featured']
    
    def filter_in_stock(self, queryset, name, value):
        if value:
            return queryset.filter(stock__gt=0)
        return queryset

# views.py
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from .filters import ProductFilter
from .pagination import StandardResultsSetPagination

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.select_related('category').all()
    serializer_class = ProductSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_class = ProductFilter
    search_fields = ['name', 'description', 'category__name']
    ordering_fields = ['price', 'created_at', 'name', 'stock']
    ordering = ['-created_at']

# Usage examples:
# GET /api/products/                                    # All products
# GET /api/products/?page=2                             # Page 2
# GET /api/products/?min_price=10&max_price=100        # Price range
# GET /api/products/?category=1                         # By category
# GET /api/products/?search=phone                       # Search
# GET /api/products/?ordering=-price                    # Sort by price desc
# GET /api/products/?in_stock=true&is_featured=true    # Multiple filters
# GET /api/products/?search=phone&min_price=500&ordering=price  # Combined
```

---

## 🔍 Key Takeaways

### API Features Checklist

- ✅ **Filtering**: Filter by specific field values
- ✅ **Search**: Full-text search across multiple fields
- ✅ **Sorting**: Order results by fields
- ✅ **Pagination**: Handle large datasets
- ✅ **File Uploads**: Handle images and documents
- ✅ **CORS**: Enable cross-origin requests

### Query Parameter Patterns

```
# Filtering
?category=1&is_active=true

# Search
?search=keyword

# Ordering
?ordering=-created_at

# Pagination
?page=2&page_size=20

# Combined
?search=phone&min_price=100&ordering=price&page=1
```

---

## 📚 Resources

- [Django Filter Documentation](https://django-filter.readthedocs.io/)
- [DRF Filtering](https://www.django-rest-framework.org/api-guide/filtering/)
- [DRF Pagination](https://www.django-rest-framework.org/api-guide/pagination/)
- [Django CORS Headers](https://github.com/adamchainz/django-cors-headers)

---

## ✅ Day 10 Checklist

- [ ] Implement django-filter
- [ ] Add search functionality
- [ ] Configure pagination
- [ ] Handle file uploads
- [ ] Enable CORS
- [ ] Combine all features in one API

---

## 🎯 Homework

1. Add more advanced filters to your API
2. Implement custom pagination styles
3. Create an image gallery API with uploads
4. **Challenge**: Add CSV/Excel export functionality

---

**Tomorrow**: Day 11 - Testing & Best Practices

**Your APIs are feature-complete! 🎨**
