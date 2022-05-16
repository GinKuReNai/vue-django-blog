FROM node:lts

WORKDIR /code
COPY ./package*.json ./

RUN npm ci && \
    npm install -g npm && \
    npm install -g @vue/cli @vue/cli-service-global

COPY . .
EXPOSE 3000

COPY docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]