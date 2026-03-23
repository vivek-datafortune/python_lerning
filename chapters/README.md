# 12-Day Python & Django API Development Course

**Complete curriculum for JavaScript developers transitioning to Python and Django**

---

## 📚 Course Overview

This 12-day intensive course takes you from Python basics to building and deploying production-ready Django REST APIs. Each day includes 3 hours of structured learning with theory, exercises, and hands-on projects.

**Prerequisites**: JavaScript/Node.js experience  
**Total Time**: 36 hours (3 hours × 12 days)  
**Outcome**: Build and deploy professional REST APIs with Django

---

## 🗓️ Course Curriculum

### Week 1: Python Fundamentals (Days 1-5)

#### [Day 1: Python Basics - Variables, Data Types & Operations](day01_python_basics/DAY1_GUIDE.md)
**3 hours** | Setup, syntax, strings, basic operations
- Python installation and setup
- Variables and data types
- String manipulation and formatting
- Type conversion
- JavaScript to Python syntax comparison
- **Project**: Simple calculator

#### [Day 2: Control Flow & Functions](day02_control_flow/DAY2_GUIDE.md)
**3 hours** | Functions, conditionals, loops
- Function definition and parameters
- If/elif/else statements
- For and while loops
- List comprehensions introduction
- **Project**: Number guessing game

#### [Day 3: Data Structures](day03_data_structures/DAY3_GUIDE.md)
**3 hours** | Lists, dictionaries, comprehensions
- Lists (like JS arrays)
- Dictionaries (like JS objects)
- Tuples and sets
- List/dict comprehensions
- **Project**: Contact manager

#### [Day 4: Object-Oriented Python](day04_oop/DAY4_GUIDE.md)
**3 hours** | Classes, inheritance, magic methods
- Creating classes
- Inheritance and polymorphism
- Magic methods (`__str__`, `__init__`, etc.)
- Properties and class methods
- **Project**: Library management system

#### [Day 5: Modules & Packages](day05_modules/DAY5_GUIDE.md)
**3 hours** | Modules, virtual environments, pip
- Creating and importing modules
- Python packages
- Virtual environments (like node_modules)
- pip package management
- Standard library overview
- **Project**: File organizer tool

---

### Week 2: Django & REST APIs (Days 6-12)

#### [Day 6: Django Setup & First Project](day06_django_setup/DAY6_GUIDE.md)
**3 hours** | Django installation, project structure, admin
- Installing Django
- Project and app structure
- Django models
- Admin panel
- Database migrations
- **Project**: Blog setup with admin

#### [Day 7: Django Models & ORM](day07_django_models/DAY7_GUIDE.md)
**3 hours** | Database relationships, QuerySets
- Model field types
- Relationships (ForeignKey, ManyToMany)
- Complex database queries
- QuerySet operations
- Aggregations and annotations
- **Project**: E-commerce models

#### [Day 8: Django REST Framework Basics](day08_drf_basics/DAY8_GUIDE.md)
**3 hours** | Serializers, views, ViewSets
- Installing DRF
- Creating serializers
- API views and ViewSets
- URL routing for APIs
- Testing with browsable API
- **Project**: TODO API

#### [Day 9: Authentication & Permissions](day09_authentication/DAY9_GUIDE.md)
**3 hours** | JWT auth, user management, permissions
- Token-based authentication
- User registration and login
- Built-in and custom permissions
- Securing endpoints
- User-specific data filtering
- **Project**: Secure blog API

#### [Day 10: Advanced API Features](day10_advanced_features/DAY10_GUIDE.md)
**3 hours** | Filtering, search, pagination, uploads
- Django Filter implementation
- Search functionality
- Pagination strategies
- File uploads
- CORS configuration
- **Project**: Feature-rich product API

#### [Day 11: Testing & Best Practices](day11_testing/DAY11_GUIDE.md)
**3 hours** | Unit tests, API tests, code quality
- Writing model tests
- API endpoint testing
- Authentication tests
- Test coverage
- Django/DRF best practices
- **Project**: Complete test suite

#### [Day 12: Deployment & Final Project](day12_deployment/DAY12_GUIDE.md)
**3 hours** | Production setup, deployment, final project
- Production configuration
- Environment variables
- Deployment to Railway/Heroku
- Post-deployment checklist
- **Project**: Complete task management API

---

## 🎯 Learning Path

### Choose Your Path

**Path A: Structured Learning (Recommended)**
- Follow days 1-12 in order
- Complete all exercises
- Build each day's project
- Best for beginners to Python

**Path B: Fast Track (Experienced)**
- Days 1-2: Python basics (skim if you know basics)
- Day 3-4: Focus on Python-specific features
- Day 5: Quick review of modules
- Days 6-12: Deep dive into Django/DRF

**Path C: Django Only**
- Skip to Day 6 if you know Python
- Complete Days 6-12
- Reference Days 1-5 as needed

---

## 📊 Progress Tracking

### Week 1 Checklist
- [ ] Day 1: Python setup and basics ✓
- [ ] Day 2: Functions and control flow ✓
- [ ] Day 3: Data structures mastered ✓
- [ ] Day 4: OOP concepts understood ✓
- [ ] Day 5: Modules and packages ✓

### Week 2 Checklist
- [ ] Day 6: Django project created ✓
- [ ] Day 7: Database models built ✓
- [ ] Day 8: First API created ✓
- [ ] Day 9: Authentication implemented ✓
- [ ] Day 10: Advanced features added ✓
- [ ] Day 11: Tests written ✓
- [ ] Day 12: API deployed ✓

---

## 🛠️ Tools & Technologies

### Core Stack
- **Python 3.11+**: Programming language
- **Django 5.0+**: Web framework
- **Django REST Framework 3.14+**: API toolkit
- **PostgreSQL**: Production database
- **SQLite**: Development database

### Additional Libraries
- **djangorestframework-simplejwt**: JWT authentication
- **django-filter**: Advanced filtering
- **django-cors-headers**: CORS handling
- **gunicorn**: Production server
- **whitenoise**: Static file serving

### Development Tools
- **VS Code**: Code editor
- **Postman/Thunder Client**: API testing
- **Git**: Version control
- **Railway/Heroku**: Deployment platform

---

## 📁 Project Structure

By the end of the course, your projects will follow this structure:

```
myproject/
├── myproject/
│   ├── settings/
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
│   └── api/
│       ├── models.py
│       ├── serializers.py
│       ├── views.py
│       ├── urls.py
│       ├── filters.py
│       ├── permissions.py
│       └── tests/
├── requirements/
│   ├── base.txt
│   ├── development.txt
│   └── production.txt
├── .env.example
├── .gitignore
├── Procfile
├── runtime.txt
└── README.md
```

---

## 🎓 Learning Resources

### Official Documentation
- [Python Documentation](https://docs.python.org/3/)
- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)

### Community Resources
- [Real Python](https://realpython.com/)
- [Django Forum](https://forum.djangoproject.com/)
- [DRF Slack](https://www.django-rest-framework.org/community/)
- [r/django](https://www.reddit.com/r/django/)

### Video Courses
- [Python Crash Course](https://www.youtube.com/results?search_query=python+crash+course)
- [Django REST Framework Tutorial](https://www.youtube.com/results?search_query=django+rest+framework)

---

## 💡 Study Tips

### Daily Routine
1. **Read theory**: 30-40 minutes
2. **Code along**: 60-90 minutes
3. **Build project**: 30-60 minutes
4. **Review and practice**: 20-30 minutes

### Best Practices
- ✅ Code every day, even if just 30 minutes
- ✅ Type out examples (don't copy-paste)
- ✅ Experiment and break things
- ✅ Read error messages carefully
- ✅ Use Git to track your progress
- ✅ Ask questions in communities

### Common Pitfalls
- ❌ Skipping exercises
- ❌ Not practicing enough
- ❌ Copying code without understanding
- ❌ Rushing through topics
- ❌ Not reading documentation

---

## 🏆 Certification Projects

After completing the course, build these projects for your portfolio:

### Beginner Level
1. **Blog API**: Posts, comments, categories, tags
2. **TODO Manager**: Tasks with priorities and due dates
3. **Recipe API**: Recipes, ingredients, cooking instructions

### Intermediate Level
4. **E-commerce API**: Products, orders, payment integration
5. **Social Media API**: Posts, likes, comments, follows
6. **Job Board API**: Job listings, applications, companies

### Advanced Level
7. **Learning Platform API**: Courses, lessons, progress tracking
8. **Real Estate API**: Listings, agents, bookings
9. **Fitness Tracker API**: Workouts, exercises, goals

---

## 🤝 Getting Help

### When You're Stuck
1. **Read error messages**: They often tell you exactly what's wrong
2. **Check documentation**: Official docs are comprehensive
3. **Search Stack Overflow**: Your question was probably already asked
4. **Use AI assistants**: ChatGPT, GitHub Copilot for explanations
5. **Join communities**: Ask in Django forums or Reddit

### Debugging Tips
```python
# Use print() liberally
print(f"Variable value: {my_var}")

# Use Django shell for testing
python manage.py shell

# Check Django logs
# Look at terminal output when running server

# Use breakpoint()
def my_view(request):
    breakpoint()  # Code pauses here
    # Inspect variables in debugger
```

---

## 📈 After Course Completion

### What You'll Be Able To Build
- ✅ Complete REST APIs with CRUD operations
- ✅ User authentication and authorization
- ✅ Database-backed applications
- ✅ Production-ready deployments
- ✅ Tested and documented APIs

### Next Steps
1. **Build portfolio projects**: 3-5 complete APIs
2. **Contribute to open source**: Find Django projects on GitHub
3. **Learn advanced topics**: Celery, WebSockets, GraphQL
4. **Frontend integration**: Connect with React/Vue/Angular
5. **DevOps**: Docker, CI/CD, monitoring

### Career Opportunities
- Backend Developer
- Full-Stack Developer (with frontend skills)
- API Developer
- Django Developer
- Python Developer

---

## 📞 Support

- **Issues**: Found a bug or error? [Report it](../../issues)
- **Questions**: Use discussions or Stack Overflow
- **Updates**: Watch the repository for updates

---

## 📜 License

MIT License - Feel free to use this for learning!

---

## 🎉 Ready to Start?

Begin your journey with **[Day 1: Python Basics](day01_python_basics/DAY1_GUIDE.md)**

Or check the main **[README.md](../../README.md)** for quick setup instructions.

**Happy Learning! 🐍 🚀**
