## 🚀 Features

- 📄 Movie list and detail pages  
- 🔍 Search and filtering  
- 👤 User registration & login  
- ❤️ Add to favourites  
- 🧪 Automated tests  
- 🗄️ Relational database (Movie ↔ Genre)

---

## 🧱 Tech Stack

- Python  
- Django  
- SQLite (default)  

---

## 📁 Project Structure

```
movie_explorer/
├── movies/
├── users/
├── templates/
├── manage.py
└── movie_explorer/
```

---

## ⚙️ Setup (Local Development)

### 1. Clone or Extract
```bash
unzip movie_explorer.zip
cd movie_explorer
```

### 2. Create Virtual Environment
```bash
python -m venv venv
```

Activate:
- Windows: `venv\Scripts\activate`
- Mac/Linux: `source venv/bin/activate`

### 3. Install Dependencies
```bash
pip install django
```

### 4. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser
```bash
python manage.py createsuperuser
```

### 6. Run Server
```bash
python manage.py runserver
```

Open:
- App → http://127.0.0.1:8000/
- Admin → http://127.0.0.1:8000/admin/

---

## ☁️ Deployment (Render)

### 1. Prepare Project
```bash
pip freeze > requirements.txt
pip install gunicorn
pip freeze > requirements.txt
```

Create `Procfile`:
```
web: gunicorn movie_explorer.wsgi
```

Update `settings.py`:
```python
ALLOWED_HOSTS = ['*']
STATIC_ROOT = 'staticfiles'
```

---

### 2. Deploy Steps

1. Push to GitHub  
2. Create account on Render  
3. New Web Service → connect repo  

**Build Command**
```bash
pip install -r requirements.txt
```

**Start Command**
```bash
gunicorn movie_explorer.wsgi
```

---

## 🧪 Tests

Run tests:
```bash
python manage.py test
```

Includes:
- Model test  
- View test  
- Detail page test  

---

## 📸 Screenshots

> Add screenshots here before submission for higher marks

```
/screenshots/home.png
/screenshots/detail.png
/screenshots/login.png
```

---

## 📄 Documentation

- README (this file)  
- 1-page report (PDF)  

---

## ✅ Assignment Criteria Covered

✔ Database models (2+ related tables)  
✔ Open dataset ready  
✔ List + detail pages  
✔ Authentication + interaction  
✔ Search/filter  
✔ Validation & structure  
✔ Tests  
✔ Documentation  

---

## 👨‍💻 Author

Student Project – Enterprise Software Development  
Generated: 2026-04-07

---

## 📜 License

This project is for academic use.
