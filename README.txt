##MOVIE EXPLORER DJANGO PROJECT - SETUP GUIDE

---
## Project features

- Movie list and detail pages  
- Search and filtering  
- User registration & login  
- Add to favourites  
- Automated tests  
- Relational database (Movie ↔ Genre)

---

## Tech Stack

- Python  
- Django  
- SQLite (default)  

---

## Deploy locally
---

1. Install Python (3.10+) and pip

2. Extract project:
unzip movie_explorer.zip
cd movie_explorer

3. Create virtual environment:
python -m venv env

Activate:
Windows: venv\Scripts\activate
Mac/Linux: source env/bin/activate

4. Install Django:
pip install django

5. Run migrations:
python manage.py makemigrations
python manage.py makemigrations movies
python manage.py migrate

6. Create admin user:
python manage.py createsuperuser
superuser: simi
email: simiolu@gmail.com
password: simi

7. Run server:
python manage.py runserver

Open browser:
http://127.0.0.1:8000/

Admin:
http://127.0.0.1:8000/admin/

Add Genres and Movies.


Importing Movies from Dataset
MovieLense is has sample dataset for 
Download the least file that has a bout 500 records
====================================================
1. I had to use pandas to trip the csv file from MobieLense to 500 records only.
2. I install pandas using PIP INSTALL PANDAS 
3. Imported csv file into movies tables



## Deploy on Github
---

1. Push to GitHub:
2. git init
3. git add .
4. git commit -m "Initial commit"
5. git log --date=local --pretty=format:"%h%x09%an%x09%ad%x09%s" > commits.local.tsv.txt
6. git branch -M main
7. git remote add origin https://github.com/simisolaolu/simi-CS551Q.git
8. git push -u origin main



6. Deploy on Render:
- Create account
- New Web Service
- Connect repo

Build Command:
pip install -r requirements.txt

Start Command:
gunicorn movie_explorer.wsgi

7. Run:
python manage.py migrate
python manage.py createsuperuser


8. App is now live.


## Documentation

- README (this file)  
- 1-page report (PDF)  

---

## Author
Simisola
Student Project – Enterprise Software Development  
Generated: 2026-04-07

---

## License

This project is for academic use.
