testcelery
==========

Dummy Django app which uses celery to send emails via GMail

# What ?
This is just to demonstrate how to do it, it is not an actual app. The
destination mail is fixed please make sure you edit it before firing
emails at people ;)

# Deploying
First edit the following files :
 * testcelery/settings.py : Change the email settings accordingly
 * mail/tasks.py : Change the destination email accrdingly

# Virtualenv
Then create some virtualenv and install the requirements via `pip install -r requirements.txt`

# Run the Django app
run `python manage.py runserver`

# Run Celery
run `python manage.py celery worker`

# Enjoy!
Just go to 0.0.0.0:8000 and you should see `woot :)` which will
indicate that the email had been sent to the specified adress :)

For further configuration refer to the Celery documentation !

