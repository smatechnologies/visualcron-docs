FROM node:18
ENV NODE_OPTIONS="--max-old-space-size=7168"
COPY . /app
WORKDIR /app
RUN npm install
RUN npm run build
EXPOSE 3000
CMD ["npm", "run", "serve"]
