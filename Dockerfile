FROM python:3.8.5
ADD . /raid_roster_planner
WORKDIR /raid_roster_planner
RUN pip install -r requirements.txt
CMD [ "python", "./manage.py collectstatic" ]
CMD [ "python", "./manage.py runserver 0.0.0.0:8000" ]
