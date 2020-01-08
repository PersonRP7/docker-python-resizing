FROM python:3.9.0a2-alpine3.10
WORKDIR /application
COPY . .
RUN pip install --upgrade pip
RUN apk add zlib-dev jpeg-dev gcc musl-dev
RUN pip install Pillow
