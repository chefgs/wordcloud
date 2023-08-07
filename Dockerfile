FROM python:3.12-rc-alpine

WORKDIR /app

COPY requirements.txt /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /app

CMD ["python", "show_wordcloud.py"]