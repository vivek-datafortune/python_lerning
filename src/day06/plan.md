# Plan: Day 6 Learning Files in src/day06/

Create step-by-step learning files following the Days 1–5 pattern (demo → exercises → mini-project), adapted for Day 6's Django Setup content. Since Django is command-line/setup heavy, the .py files **simulate Django concepts in pure Python** so they're runnable without installing Django, with a companion command reference for the real setup.

---

## Steps

### Phase 1: Core learning files (all parallel — no interdependencies)

1. **Create `src/day06/demo.py`** — Django overview walkthrough
   - Print-based numbered sections (same style as `day04/demo.py`)
   - Django vs Express.js comparison, component tree, project structure diagram
   - `uv` vs `pip` cheatsheet, key `settings.py` concepts inline
   - Ends with "now try the exercises" pointers

2. **Create `src/day06/exercise1.py`** — Project structure & settings exercises
   - TODO-style with commented-out tests (same as `day04/exercise1.py`):
     - TODO 1: Build a dictionary representing Django project structure, print as tree
     - TODO 2: `DjangoSettings` class simulating `settings.py` (toggle DEBUG, add apps, validate)
     - TODO 3: Function to validate a settings dictionary has all required keys
     - CHALLENGE: `ManagementCommand` class simulating `manage.py` commands

3. **Create `src/day06/exercise2.py`** — Models & admin simulation
   - Multi-part exercise (same as `day04/exercise2.py`):
     - TODO 1: `Model` base class mimicking `models.Model` (with `save()`, class-level `objects` list)
     - TODO 2: `Post` and `Comment` classes inheriting Model (matching the guide's blog models)
     - TODO 3: `ModelAdmin` class displaying instances in a formatted table (simulating admin `list_display`)
     - CHALLENGE: Add filtering & search to ModelAdmin

4. **Create `src/day06/blog_setup.py`** — Mini-project: Blog system
   - Interactive CLI (same pattern as `bank_system.py` / `library_system.py`)
   - `DjangoProject`, `BlogApp`, `AdminPanel` classes
   - Menu: list posts, add post, add comment, search, filter by status, admin view, exit
   - Seeded with initial data

### Phase 2: Companion reference

5. **Create `src/day06/SETUP_COMMANDS.md`** — Terminal command quick-reference
   - Step-by-step commands for actual Django setup (install uv → create project → migrations → superuser → runserver → shell)
   - Checklist the learner follows alongside the .py exercises

---

## Relevant reference files

- `src/day04/demo.py` — print-walkthrough pattern
- `src/day04/exercise1.py` — TODO + commented-test pattern
- `src/day04/exercise2.py` — multi-part exercise pattern
- `src/day04/bank_system.py` — interactive CLI menu pattern
- `chapters/day06_django_setup/DAY6_GUIDE.md` — source content

## Verification

1. `python src/day06/demo.py` — prints full walkthrough, no errors
2. `python src/day06/exercise1.py` — prints headers; tests work when TODOs are completed
3. `python src/day06/exercise2.py` — same
4. `python src/day06/blog_setup.py` — shows seeded data and interactive menu
5. `ls src/day06/` — confirms all 5 files present

## Key decisions

- Exercises simulate Django in pure Python (no Django install needed) — keeps the learning progression consistent with Days 1–5
- Blog mini-project mirrors the guide's exact models (`Post` with status/slug/author, `Comment`) so concepts map directly to real Django
- `SETUP_COMMANDS.md` covers the hands-on terminal work that .py files can't replicate
