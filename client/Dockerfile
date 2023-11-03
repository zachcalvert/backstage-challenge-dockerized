# syntax=docker/dockerfile:1.4
FROM node:lts AS development

ENV CI=true
ENV PORT=3000

WORKDIR /code
ARG REACT_APP_DJANGO_URL
ENV REACT_APP_DJANGO_URL http://localhost:8000/
COPY package.json /code/package.json
COPY package-lock.json /code/package-lock.json
RUN npm ci
COPY . /code

CMD [ "npm", "start" ]
