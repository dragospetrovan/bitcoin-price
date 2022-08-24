FROM python:3.9

RUN mkdir /app
WORKDIR /app
ADD bitcoin_price.py bitcoin_price.py
ADD requirements.txt requirements.txt
ADD templates/ templates/

RUN pip install -r requirements.txt

EXPOSE 80

CMD [ "python", "./bitcoin_price.py"]