# Day 9: Authentication & Permissions

**Duration**: 3 hours  
**Goal**: Implement authentication and authorization for your APIs

---

## 📋 Learning Objectives

By the end of Day 9, you will:
- ✅ Implement token-based authentication
- ✅ Create user registration and login endpoints
- ✅ Use DRF permissions
- ✅ Secure API endpoints
- ✅ Handle user-specific data
- ✅ Implement custom permissions

---

## ⏱️ Time Breakdown

| Activity | Duration | Type |
|----------|----------|------|
| Theory: Authentication Methods | 30 min | Reading |
| Exercise: Token Authentication | 30 min | Coding |
| Theory: Permissions | 30 min | Reading |
| Exercise: Implement Permissions | 30 min | Coding |
| Theory: User Registration | 20 min | Reading |
| Mini-Project: Secure Blog API | 40 min | Project |

---

## 🎯 Hour 1: Authentication (60 min)

### Authentication Methods (30 min)

#### 1. Token Authentication (Recommended for APIs)

Install package:
```bash
pip install djangorestframework-simplejwt
pip freeze > requirements.txt
```

Configure `settings.py`:
```python
INSTALLED_APPS = [
    # ...
    'rest_framework',
    'rest_framework.authtoken',  # For token auth
    # ...
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
}

# JWT Settings
from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
}
```

#### 2. JWT Authentication URLs

Create `users/urls.py`:
```python
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
```

Add to main `urls.py`:
```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/auth/', include('users.urls')),
]
```

#### 3. Testing Authentication

```bash
# Get token
POST /api/auth/token/
{
    "username": "admin",
    "password": "password123"
}

# Response:
{
    "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}

# Use token in requests:
# Header: Authorization: Bearer <access_token>

# Refresh token
POST /api/auth/token/refresh/
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

### User Registration (30 min)

Create `users/serializers.py`:
```python
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, 
        required=True, 
        validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2', 'first_name', 'last_name')
    
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')
        read_only_fields = ('id',)
```

Create `users/views.py`:
```python
from rest_framework import generics, permissions
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import RegisterSerializer, UserSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer

class UserDetailView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserSerializer
    
    def get_object(self):
        return self.request.user
```

Update `users/urls.py`:
```python
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView, UserDetailView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('me/', UserDetailView.as_view(), name='user-detail'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
```

---

## 🎯 Hour 2: Permissions (60 min)

### Built-in Permissions (30 min)

```python
from rest_framework import permissions

# 1. AllowAny - No authentication required
class PublicViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]

# 2. IsAuthenticated - Must be logged in
class PrivateViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

# 3. IsAuthenticatedOrReadOnly - Read for all, write for authenticated
class ArticleViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# 4. IsAdminUser - Only admin users
class AdminOnlyViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser]
```

### Custom Permissions (30 min)

Create `api/permissions.py`:
```python
from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners to edit objects.
    """
    
    def has_object_permission(self, request, view, obj):
        # Read permissions for any request (GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Write permissions only for owner
        return obj.user == request.user

class IsOwner(permissions.BasePermission):
    """
    Only allow owners to view or edit objects.
    """
    
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user

class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Authors can edit, others can only read.
    """
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
```

Using custom permissions:
```python
from rest_framework import viewsets
from .permissions import IsOwnerOrReadOnly
from .models import Post
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    
    def perform_create(self, serializer):
        # Automatically set user to current user
        serializer.save(user=self.request.user)
```

### Filtering by User

```python
class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        # Only return user's own todos
        return Todo.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        # Automatically set user
        serializer.save(user=self.request.user)
```

---

## 🎯 Hour 3: Mini-Project - Secure Blog API (60 min)

Create complete authenticated blog:

### Models (`blog/models.py`)

```python
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]
    
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['created_at']
    
    def __str__(self):
        return f'Comment by {self.author.username} on {self.post.title}'
```

### Serializers (`blog/serializers.py`)

```python
from rest_framework import serializers
from .models import Post, Comment
from django.contrib.auth.models import User

class CommentSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.username', read_only=True)
    
    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'author_name', 'content', 'created_at']
        read_only_fields = ['id', 'author', 'created_at']

class PostSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.username', read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comments.count', read_only=True)
    
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'author_name', 
                  'status', 'created_at', 'updated_at', 'comments', 'comment_count']
        read_only_fields = ['id', 'author', 'created_at', 'updated_at']
```

### Permissions (`blog/permissions.py`)

```python
from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
```

### Views (`blog/views.py`)

```python
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsAuthorOrReadOnly

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.filter(status='published')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    
    def get_queryset(self):
        if self.request.user.is_authenticated:
            # Show all posts to authenticated users (including drafts if author)
            return Post.objects.filter(
                models.Q(status='published') | 
                models.Q(author=self.request.user)
            )
        # Only published for anonymous
        return Post.objects.filter(status='published')
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    
    @action(detail=False, methods=['get'])
    def my_posts(self, request):
        """Get current user's posts"""
        posts = Post.objects.filter(author=request.user)
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
```

### URLs (`blog/urls.py`)

```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
```

### Testing the API

```bash
# 1. Register a new user
POST /api/auth/register/
{
    "username": "john",
    "email": "john@example.com",
    "password": "SecurePass123!",
    "password2": "SecurePass123!"
}

# 2. Login and get token
POST /api/auth/token/
{
    "username": "john",
    "password": "SecurePass123!"
}

# 3. Create a post (with token)
POST /api/posts/
Authorization: Bearer <access_token>
{
    "title": "My First Post",
    "content": "Hello World!",
    "status": "published"
}

# 4. Get user's posts
GET /api/posts/my_posts/
Authorization: Bearer <access_token>

# 5. Add a comment
POST /api/comments/
Authorization: Bearer <access_token>
{
    "post": 1,
    "content": "Great post!"
}
```

---

## 🔍 Key Takeaways

### Authentication Flow

```
1. User registers → /api/auth/register/
2. User logs in → /api/auth/token/ → Receives JWT
3. User makes request with token in header
4. DRF validates token
5. Request.user is populated
6. Permissions are checked
7. View executes
```

### Permission Classes

| Permission | Description |
|-----------|-------------|
| `AllowAny` | No auth required |
| `IsAuthenticated` | Must be logged in |
| `IsAuthenticatedOrReadOnly` | Read for all, write for authenticated |
| `IsAdminUser` | Only admins |
| Custom | Your own logic |

---

## 📚 Resources

- [DRF Authentication](https://www.django-rest-framework.org/api-guide/authentication/)
- [DRF Permissions](https://www.django-rest-framework.org/api-guide/permissions/)
- [JWT Documentation](https://django-rest-framework-simplejwt.readthedocs.io/)

---

## ✅ Day 9 Checklist

- [ ] Implement JWT authentication
- [ ] Create registration endpoint
- [ ] Use built-in permissions
- [ ] Create custom permissions
- [ ] Filter data by user
- [ ] Complete secure blog API

---

## 🎯 Homework

1. Add password reset functionality
2. Implement user profiles
3. Add user following system
4. **Challenge**: Add email verification

---

**Tomorrow**: Day 10 - Advanced API Features

**Your APIs are now secure! 🔒**
