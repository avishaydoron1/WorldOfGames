FROM python3.6-alpine3.7
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
CMD [ "app.py" ]




