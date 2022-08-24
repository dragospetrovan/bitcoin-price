FROM python:3.9

RUN mkdir /app
WORKDIR /app
ADD ./rest_api.py ./rest_api.py
ADD requirements.txt requirements.txt

RUN pip install -r requirements.txt

EXPOSE 80
CMD [ "python", "./rest_api.py"]
