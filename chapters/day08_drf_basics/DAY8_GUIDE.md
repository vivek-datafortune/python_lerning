# Day 8: Django REST Framework - Serializers & Views

**Duration**: 3 hours  
**Goal**: Learn DRF serializers, create your first API endpoints

---

## 📋 Learning Objectives

By the end of Day 8, you will:
- ✅ Install and configure Django REST Framework
- ✅ Create serializers for your models
- ✅ Implement API views and viewsets
- ✅ Configure URL routing for APIs
- ✅ Test APIs with browsable API interface
- ✅ Understand request/response cycle

---

## ⏱️ Time Breakdown

| Activity | Duration | Type |
|----------|----------|------|
| Theory: DRF Setup | 20 min | Reading |
| Exercise: Configure DRF | 20 min | Hands-on |
| Theory: Serializers | 40 min | Reading |
| Exercise: Create Serializers | 20 min | Coding |
| Theory: Views & ViewSets | 40 min | Reading |
| Mini-Project: TODO API | 40 min | Project |

---

## 🎯 Hour 1: DRF Setup & Serializers (60 min)

### Installing DRF (20 min)

```bash
# Install Django REST Framework
pip install djangorestframework

# Update requirements.txt
pip freeze > requirements.txt
```

Configure `settings.py`:
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Third party
    'rest_framework',
    
    # Your apps
    'api',
]

# DRF Settings
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}
```

### What are Serializers? (40 min)

#### Concept

Serializers convert complex data types (Django models) to Python native datatypes that can be rendered into JSON.

**Like in Express.js**:
```javascript
// JavaScript - manual conversion
app.get('/api/users', (req, res) => {
    const users = User.findAll();
    const json = users.map(u => ({
        id: u.id,
        name: u.name,
        email: u.email
    }));
    res.json(json);
});
```

**Django REST Framework**:
```python
# Serializer handles conversion automatically
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
```

#### Creating Serializers

Create `api/serializers.py`:
```python
from rest_framework import serializers
from .models import Product, Category

class CategorySerializer(serializers.ModelSerializer):
    """Serializer for Category model"""
    
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']
        # or use '__all__' for all fields

class ProductSerializer(serializers.ModelSerializer):
    """Serializer for Product model"""
    
    # Nested serializer (read-only)
    category = CategorySerializer(read_only=True)
    
    # Write-only field for creating
    category_id = serializers.IntegerField(write_only=True)
    
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'stock', 
                  'category', 'category_id', 'is_active', 'created_at']
        read_only_fields = ['id', 'created_at']
    
    def validate_price(self, value):
        """Custom validation for price"""
        if value < 0:
            raise serializers.ValidationError("Price cannot be negative")
        return value
    
    def validate(self, data):
        """Validate multiple fields"""
        if data.get('price', 0) > 10000 and data.get('stock', 0) == 0:
            raise serializers.ValidationError(
                "Expensive products must have stock"
            )
        return data
```

#### Serializer Types

```python
# 1. ModelSerializer (most common)
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

# 2. Serializer (manual fields)
class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    
    def create(self, validated_data):
        return User.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance

# 3. Nested Serializers
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'content', 'created_at']

class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    author_name = serializers.CharField(source='author.username', read_only=True)
    
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author_name', 'comments']
```

---

## 🎯 Hour 2: Views & ViewSets (60 min)

### API Views (40 min)

#### Function-Based Views

```python
# api/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer

@api_view(['GET', 'POST'])
def product_list(request):
    """
    List all products or create a new product
    """
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, pk):
    """
    Retrieve, update or delete a product
    """
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
```

#### Class-Based Views

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ProductList(APIView):
    """List products or create a new product"""
    
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDetail(APIView):
    """Retrieve, update or delete a product"""
    
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return None
    
    def get(self, request, pk):
        product = self.get_object(pk)
        if not product:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    def put(self, request, pk):
        product = self.get_object(pk)
        if not product:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        product = self.get_object(pk)
        if not product:
            return Response(status=status.HTTP_404_NOT_FOUND)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
```

### ViewSets (Best Practice) (20 min)

```python
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

class ProductViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Product model
    Provides: list, create, retrieve, update, destroy
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    # Custom action
    @action(detail=False, methods=['get'])
    def in_stock(self, request):
        """Get only products in stock"""
        products = self.queryset.filter(stock__gt=0)
        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'])
    def reduce_stock(self, request, pk=None):
        """Reduce product stock"""
        product = self.get_object()
        quantity = request.data.get('quantity', 1)
        
        if product.stock >= quantity:
            product.stock -= quantity
            product.save()
            serializer = self.get_serializer(product)
            return Response(serializer.data)
        
        return Response(
            {'error': 'Insufficient stock'},
            status=status.HTTP_400_BAD_REQUEST
        )
```

### URL Configuration (20 min)

Create `api/urls.py`:
```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Router automatically generates URLs for ViewSets
router = DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'categories', views.CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    
    # Or manual URL patterns:
    # path('products/', views.ProductList.as_view()),
    # path('products/<int:pk>/', views.ProductDetail.as_view()),
]
```

Update main `urls.py`:
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]
```

---

## 🎯 Hour 3: Mini-Project - TODO API (60 min)

### Complete TODO API

Create `todos/models.py`:
```python
from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    due_date = models.DateField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todos')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
```

Create `todos/serializers.py`:
```python
from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.username', read_only=True)
    
    class Meta:
        model = Todo
        fields = ['id', 'title', 'description', 'completed', 'priority',
                  'due_date', 'user', 'user_name', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def validate_title(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Title must be at least 3 characters")
        return value
```

Create `todos/views.py`:
```python
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    
    @action(detail=False, methods=['get'])
    def completed(self, request):
        """Get completed todos"""
        todos = self.queryset.filter(completed=True)
        serializer = self.get_serializer(todos, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def active(self, request):
        """Get active (not completed) todos"""
        todos = self.queryset.filter(completed=False)
        serializer = self.get_serializer(todos, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'])
    def toggle(self, request, pk=None):
        """Toggle todo completion status"""
        todo = self.get_object()
        todo.completed = not todo.completed
        todo.save()
        serializer = self.get_serializer(todo)
        return Response(serializer.data)
```

Create `todos/urls.py`:
```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TodoViewSet

router = DefaultRouter()
router.register(r'todos', TodoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
```

### Testing Your API

```bash
# Run server
python manage.py runserver

# Visit in browser:
http://127.0.0.1:8000/api/todos/

# Available endpoints:
GET    /api/todos/              # List all todos
POST   /api/todos/              # Create new todo
GET    /api/todos/{id}/         # Get specific todo
PUT    /api/todos/{id}/         # Update todo
DELETE /api/todos/{id}/         # Delete todo
GET    /api/todos/completed/    # Get completed todos
GET    /api/todos/active/       # Get active todos
POST   /api/todos/{id}/toggle/  # Toggle completion
```

---

## 🔍 Key Takeaways

### DRF Components

| Component | Purpose | Like Express.js |
|-----------|---------|----------------|
| Serializer | Data validation & conversion | DTO/validation schema |
| View | Handle HTTP requests | Route handler |
| ViewSet | CRUD operations | Resource controller |
| Router | Generate URLs | Router |

### ViewSet Methods

- `list()` → GET `/api/resource/`
- `create()` → POST `/api/resource/`
- `retrieve()` → GET `/api/resource/{id}/`
- `update()` → PUT `/api/resource/{id}/`
- `partial_update()` → PATCH `/api/resource/{id}/`
- `destroy()` → DELETE `/api/resource/{id}/`

---

## 📚 Resources

- [DRF Tutorial](https://www.django-rest-framework.org/tutorial/quickstart/)
- [Serializers](https://www.django-rest-framework.org/api-guide/serializers/)
- [ViewSets](https://www.django-rest-framework.org/api-guide/viewsets/)

---

## ✅ Day 8 Checklist

- [ ] Install and configure DRF
- [ ] Create ModelSerializers
- [ ] Implement ViewSets
- [ ] Configure URL routing
- [ ] Test API with browsable interface
- [ ] Complete TODO API

---

## 🎯 Homework

1. Enhance TODO API with more features
2. Create a Notes API with tags
3. Test all endpoints thoroughly
4. **Challenge**: Add filtering and search

---

**Tomorrow**: Day 9 - Authentication & Permissions

**You're building real APIs now! 🚀**
