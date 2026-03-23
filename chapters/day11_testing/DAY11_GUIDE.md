# Day 11: Testing & Best Practices

**Duration**: 3 hours  
**Goal**: Write tests for your APIs and learn Django/DRF best practices

---

## 📋 Learning Objectives

By the end of Day 11, you will:
- ✅ Write unit tests for models
- ✅ Test API endpoints
- ✅ Use DRF test utilities
- ✅ Understand test coverage
- ✅ Apply best practices
- ✅ Handle errors gracefully

---

## ⏱️ Time Breakdown

| Activity | Duration | Type |
|----------|----------|------|
| Theory: Testing Basics | 30 min | Reading |
| Exercise: Model Tests | 30 min | Coding |
| Theory: API Testing | 30 min | Reading |
| Exercise: API Tests | 40 min | Coding |
| Theory: Best Practices | 20 min | Reading |
| Mini-Project: Complete Test Suite | 30 min | Project |

---

## 🎯 Hour 1: Testing Basics (60 min)

### Django Testing Framework (30 min)

#### Test Structure

```python
from django.test import TestCase
from .models import Product, Category

class ProductModelTest(TestCase):
    """Test Product model"""
    
    @classmethod
    def setUpTestData(cls):
        """Set up non-modified data for all class methods"""
        cls.category = Category.objects.create(
            name='Electronics',
            slug='electronics'
        )
        cls.product = Product.objects.create(
            name='iPhone 15',
            slug='iphone-15',
            description='Latest iPhone',
            price=999.99,
            stock=50,
            category=cls.category
        )
    
    def setUp(self):
        """Set up before each test method"""
        pass
    
    def test_product_creation(self):
        """Test product was created correctly"""
        self.assertEqual(self.product.name, 'iPhone 15')
        self.assertEqual(self.product.price, 999.99)
        self.assertTrue(self.product.is_active)
    
    def test_product_str(self):
        """Test string representation"""
        self.assertEqual(str(self.product), 'iPhone 15')
    
    def test_product_in_stock(self):
        """Test is_in_stock property"""
        self.assertTrue(self.product.is_in_stock)
        
        self.product.stock = 0
        self.assertFalse(self.product.is_in_stock)
    
    def test_category_relationship(self):
        """Test product-category relationship"""
        self.assertEqual(self.product.category.name, 'Electronics')
        self.assertIn(self.product, self.category.products.all())
```

### Running Tests

```bash
# Run all tests
python manage.py test

# Run tests for specific app
python manage.py test api

# Run specific test case
python manage.py test api.tests.ProductModelTest

# Run specific test method
python manage.py test api.tests.ProductModelTest.test_product_creation

# Run with verbosity
python manage.py test --verbosity=2

# Keep test database
python manage.py test --keepdb
```

### Model Tests Exercise (30 min)

Create `api/tests/test_models.py`:
```python
from django.test import TestCase
from django.contrib.auth.models import User
from api.models import Todo

class TodoModelTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        cls.todo = Todo.objects.create(
            title='Test Todo',
            description='Test description',
            user=cls.user,
            priority='high'
        )
    
    def test_todo_creation(self):
        """Test TODO: Implement this test"""
        pass  # TODO
    
    def test_todo_str(self):
        """Test TODO: Implement this test"""
        pass  # TODO
    
    def test_default_values(self):
        """Test TODO: Check default completed=False"""
        pass  # TODO
    
    def test_user_relationship(self):
        """Test TODO: Verify user relationship"""
        pass  # TODO
```

---

## 🎯 Hour 2: API Testing (70 min)

### DRF Test Client (30 min)

```python
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Product, Category

class ProductAPITest(APITestCase):
    """Test Product API endpoints"""
    
    def setUp(self):
        """Set up test data"""
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.category = Category.objects.create(
            name='Electronics',
            slug='electronics'
        )
        self.product = Product.objects.create(
            name='iPhone 15',
            slug='iphone-15',
            description='Latest iPhone',
            price=999.99,
            stock=50,
            category=self.category
        )
    
    def test_get_all_products(self):
        """Test retrieving all products"""
        response = self.client.get('/api/products/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
    
    def test_get_single_product(self):
        """Test retrieving a single product"""
        response = self.client.get(f'/api/products/{self.product.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'iPhone 15')
    
    def test_create_product_unauthenticated(self):
        """Test creating product without authentication fails"""
        data = {
            'name': 'New Product',
            'slug': 'new-product',
            'description': 'Description',
            'price': 99.99,
            'stock': 10,
            'category': self.category.id
        }
        response = self.client.post('/api/products/', data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_create_product_authenticated(self):
        """Test creating product with authentication"""
        self.client.force_authenticate(user=self.user)
        data = {
            'name': 'New Product',
            'slug': 'new-product',
            'description': 'Description',
            'price': 99.99,
            'stock': 10,
            'category': self.category.id
        }
        response = self.client.post('/api/products/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 2)
        self.assertEqual(response.data['name'], 'New Product')
    
    def test_update_product(self):
        """Test updating a product"""
        self.client.force_authenticate(user=self.user)
        data = {
            'name': 'Updated iPhone',
            'slug': 'iphone-15',
            'description': 'Updated description',
            'price': 899.99,
            'stock': 40,
            'category': self.category.id
        }
        response = self.client.put(f'/api/products/{self.product.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.product.refresh_from_db()
        self.assertEqual(self.product.name, 'Updated iPhone')
        self.assertEqual(self.product.price, 899.99)
    
    def test_partial_update_product(self):
        """Test partially updating a product"""
        self.client.force_authenticate(user=self.user)
        data = {'price': 799.99}
        response = self.client.patch(f'/api/products/{self.product.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.product.refresh_from_db()
        self.assertEqual(self.product.price, 799.99)
        self.assertEqual(self.product.name, 'iPhone 15')  # Unchanged
    
    def test_delete_product(self):
        """Test deleting a product"""
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(f'/api/products/{self.product.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.count(), 0)
    
    def test_filter_products(self):
        """Test filtering products"""
        response = self.client.get('/api/products/?category=1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
    
    def test_search_products(self):
        """Test searching products"""
        response = self.client.get('/api/products/?search=iPhone')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
    
    def test_invalid_product_id(self):
        """Test retrieving non-existent product"""
        response = self.client.get('/api/products/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
```

### Testing Authentication (40 min)

```python
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User

class AuthenticationTest(APITestCase):
    """Test authentication endpoints"""
    
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
    
    def test_user_registration(self):
        """Test user registration"""
        data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'newpass123',
            'password2': 'newpass123'
        }
        response = self.client.post('/api/auth/register/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)
    
    def test_registration_password_mismatch(self):
        """Test registration with mismatched passwords"""
        data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'newpass123',
            'password2': 'different123'
        }
        response = self.client.post('/api/auth/register/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_login(self):
        """Test user login"""
        data = {
            'username': 'testuser',
            'password': 'testpass123'
        }
        response = self.client.post('/api/auth/token/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)
    
    def test_login_invalid_credentials(self):
        """Test login with invalid credentials"""
        data = {
            'username': 'testuser',
            'password': 'wrongpassword'
        }
        response = self.client.post('/api/auth/token/', data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_protected_endpoint_without_auth(self):
        """Test accessing protected endpoint without token"""
        response = self.client.get('/api/auth/me/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_protected_endpoint_with_auth(self):
        """Test accessing protected endpoint with token"""
        self.client.force_authenticate(user=self.user)
        response = self.client.get('/api/auth/me/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'testuser')
```

---

## 🎯 Hour 3: Best Practices & Complete Tests (60 min)

### Django/DRF Best Practices (20 min)

#### 1. Project Structure

```
myproject/
├── myproject/
│   ├── settings/
│   │   ├── base.py      # Common settings
│   │   ├── development.py
│   │   └── production.py
│   ├── urls.py
│   └── wsgi.py
├── apps/
│   ├── api/
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── filters.py
│   │   ├── permissions.py
│   │   ├── pagination.py
│   │   └── tests/
│   │       ├── test_models.py
│   │       ├── test_views.py
│   │       └── test_serializers.py
│   └── users/
├── requirements/
│   ├── base.txt
│   ├── development.txt
│   └── production.txt
└── manage.py
```

#### 2. Environment Variables

```python
# settings.py
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = os.getenv('DEBUG', 'False') == 'True'
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',')

DATABASES = {
    'default': {
        'ENGINE': os.getenv('DB_ENGINE', 'django.db.backends.sqlite3'),
        'NAME': os.getenv('DB_NAME', BASE_DIR / 'db.sqlite3'),
        'USER': os.getenv('DB_USER', ''),
        'PASSWORD': os.getenv('DB_PASSWORD', ''),
        'HOST': os.getenv('DB_HOST', ''),
        'PORT': os.getenv('DB_PORT', ''),
    }
}
```

`.env` file:
```
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DB_ENGINE=django.db.backends.postgresql
DB_NAME=dbname
DB_USER=dbuser
DB_PASSWORD=dbpass
DB_HOST=localhost
DB_PORT=5432
```

#### 3. Error Handling

```python
from rest_framework.views import exception_handler
from rest_framework.response import Response

def custom_exception_handler(exc, context):
    """Custom exception handler"""
    response = exception_handler(exc, context)
    
    if response is not None:
        custom_response = {
            'error': {
                'code': response.status_code,
                'message': response.data,
                'timestamp': datetime.now().isoformat()
            }
        }
        response.data = custom_response
    
    return response

# settings.py
REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'myproject.utils.custom_exception_handler'
}
```

#### 4. Serializer Best Practices

```python
# Good: Explicit fields
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'category', 'created_at']
        read_only_fields = ['id', 'created_at']

# Good: Validation
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
    
    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be positive")
        return value
    
    def validate(self, attrs):
        if attrs['stock'] < 0:
            raise serializers.ValidationError("Stock cannot be negative")
        return attrs
```

### Complete Test Suite Exercise (40 min)

Create `api/tests/test_complete.py`:
```python
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from api.models import Product, Category, Order, OrderItem

class CompleteAPITest(APITestCase):
    """Complete test suite for e-commerce API"""
    
    def setUp(self):
        # Create users
        self.admin_user = User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='admin123'
        )
        self.regular_user = User.objects.create_user(
            username='user',
            email='user@example.com',
            password='user123'
        )
        
        # Create test data
        self.category = Category.objects.create(
            name='Electronics',
            slug='electronics'
        )
        self.product = Product.objects.create(
            name='iPhone 15',
            slug='iphone-15',
            description='Latest iPhone',
            price=999.99,
            stock=50,
            category=self.category
        )
    
    def test_complete_order_flow(self):
        """Test complete order creation flow"""
        # 1. List products
        response = self.client.get('/api/products/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # 2. Login
        self.client.force_authenticate(user=self.regular_user)
        
        # 3. Create order
        order_data = {
            'items': [
                {'product': self.product.id, 'quantity': 2}
            ]
        }
        response = self.client.post('/api/orders/', order_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        # 4. Verify order
        order_id = response.data['id']
        response = self.client.get(f'/api/orders/{order_id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['items']), 1)
    
    def test_permissions(self):
        """Test various permission scenarios"""
        # Anonymous can read
        response = self.client.get('/api/products/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Anonymous cannot create
        response = self.client.post('/api/products/', {})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
        # Regular user can create
        self.client.force_authenticate(user=self.regular_user)
        product_data = {
            'name': 'New Product',
            'slug': 'new-product',
            'description': 'Description',
            'price': 99.99,
            'stock': 10,
            'category': self.category.id
        }
        response = self.client.post('/api/products/', product_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    # TODO: Add more test methods
    def test_stock_management(self):
        """Test TODO: Implement stock reduction after order"""
        pass
    
    def test_pagination(self):
        """Test TODO: Verify pagination works"""
        pass
    
    def test_filtering(self):
        """Test TODO: Test all filters"""
        pass
```

### Test Coverage

```bash
# Install coverage
pip install coverage

# Run tests with coverage
coverage run --source='.' manage.py test

# View coverage report
coverage report

# Generate HTML report
coverage html

# Open htmlcov/index.html in browser
```

---

## 🔍 Key Takeaways

### Testing Checklist

- ✅ Unit tests for models
- ✅ API endpoint tests (CRUD)
- ✅ Authentication tests
- ✅ Permission tests
- ✅ Validation tests
- ✅ Edge cases and error handling

### Best Practices

1. **Keep tests isolated** - Use setUp/tearDown
2. **Test one thing** - One assert per test is ideal
3. **Use descriptive names** - `test_user_cannot_delete_other_users_post`
4. **Mock external services** - Don't call real APIs in tests
5. **Aim for high coverage** - 80%+ is good

---

## 📚 Resources

- [Django Testing](https://docs.djangoproject.com/en/stable/topics/testing/)
- [DRF Testing](https://www.django-rest-framework.org/api-guide/testing/)
- [Coverage.py](https://coverage.readthedocs.io/)

---

## ✅ Day 11 Checklist

- [ ] Write model tests
- [ ] Write API endpoint tests
- [ ] Test authentication
- [ ] Test permissions
- [ ] Measure test coverage
- [ ] Apply best practices

---

## 🎯 Homework

1. Achieve 80%+ test coverage
2. Write tests for all your models
3. Test all error scenarios
4. **Challenge**: Implement CI/CD with GitHub Actions

---

**Tomorrow**: Day 12 - Deployment & Final Project

**Your code is now production-ready! ✅**
