FROM node:lts

WORKDIR /code/

RUN apt-get update && \
    npm install -g npm && \
    npm install -g create-vite@latest
    
CMD ["npm", "run", "dev"]