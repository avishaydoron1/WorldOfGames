FROM python:alpine
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
COPY ./MainScores.py /app/MainScores.py
RUN pip install -r requirements.txt
CMD python /app/MainScores.py




