# DjangoAPI
API represents simple service for polls. This is test task from https://fabrique.studio/

API functionality:
Stuff users
- authenticating
- creating/editing/deleting polls
- creating/editing/deleting polls' questions
Commong users
- getting active polls
- completing polls
- getting info for personal completed polls

To start local server:
0. install python > 3.5
1. download or clone this repo
2. run pip install -r requirenemts.txt
3. run python manage.py migrate
4. copy files from /deploy/ dir to /config/
5. create admin user via python manage.py createsuperuser
6. start the server by running python manage.py runserver

API methods:
1. Get list of all polls: /poll/ method via GET request
2. Create a new poll: /poll/ method via authenticated POST request. Data fields: date_start (required), date_end (required), questions (list), name, description
3. Delete a poll: /poll/poll_id via authenticated POST request
4. Edit existing poll: /poll/poll_id via authenticated POST request and specifyed data
5. Manipulating questions data is all the same using /question/ path
6. Completing polls: /mypolls/ method via POST request, Data fiels: poll, user_id, answers (list)
7. List completed polls: /mypolls/show/ method via GET request, specify user id in data (id field)
