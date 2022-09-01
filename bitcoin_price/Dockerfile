FROM python:3.9

RUN useradd -ms /bin/bash bitcoin_price
USER bitcoin_price

RUN mkdir /app
WORKDIR /app

ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt

ADD bitcoin_price.py bitcoin_price.py
ADD templates/ templates/


EXPOSE 80

CMD [ "python", "./bitcoin_price.py"]
