FROM python:alpine
WORKDIR /app
COPY ./requierements.txt /app/requierements.txt
COPY ./MainScores.py /app/MainScores.py
RUN pip install -r requierements.txt
CMD python /app/MainScores.py




