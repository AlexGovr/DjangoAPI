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
5. start the server by running python manage.py runserver

