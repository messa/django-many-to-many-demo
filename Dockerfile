FROM python:3.5-alpine

RUN pip install django gunicorn whitenoise

ENV PYTHONUNBUFFERED=1 PRODUCTION=1

COPY app1 demo/app1/
COPY proj1 demo/proj1/
COPY manage.py createsuperuser.py demo/

RUN demo/manage.py migrate
RUN demo/createsuperuser.py
RUN demo/manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "--bind", "0:8000", "-w", "4", "--pythonpath", "demo", "proj1.wsgi:application"]
