FROM python:3.8.5-slim-buster
WORKDIR /raid_roster_planner

ADD ./requirements.txt .
RUN pip install -r requirements.txt

ADD . /raid_roster_planner

RUN python ./manage.py collectstatic
RUN python ./manage.py migrate

CMD [ "python", "./manage.py", "runserver", "0.0.0.0:8000" ]
