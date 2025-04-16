# gunicorn 
1. Install gunicorn `pip install gunicorn`
2. Collet static file to staticfiles `python manage.py collectstatic`
3. Run the server `gunicorn mysite.wsgi:application`