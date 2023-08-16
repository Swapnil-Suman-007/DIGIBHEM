# Django-School-Management-System

this is online learning management system.

It currently doesn't allow students/staff to login.
Solely, it's expected to be used on a single machine or online for managers only.


username: admin
password: admin123

pip install -r requirements.txt #install required packages
python manage.py migrate # run first migration
python manage.py runserver # run the server
```

To create superuser use command-
python manage.py createsuperuser

Then locate http://172.0.0.1:8000

## Admin Login
When you run migrate, a superuser is created.
```bash
username: admin
password: admin123
```

.




