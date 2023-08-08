FROM python:slim-bullseye

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["python3", "show_wordcloud.py"]