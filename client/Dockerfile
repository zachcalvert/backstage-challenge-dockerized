# syntax=docker/dockerfile:1.4
FROM node:lts AS development

RUN npm install -g react-scripts

WORKDIR /code

COPY package.json /code/package.json
COPY package-lock.json /code/package-lock.json
RUN npm ci
COPY . /code

CMD [ "npm", "start" ]
