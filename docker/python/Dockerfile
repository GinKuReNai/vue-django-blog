FROM python:3.8
ENV PYTHONUNBUFFERD 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . /code/

COPY docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]
