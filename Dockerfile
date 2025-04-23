FROM node:18-alpine
WORKDIR /app
COPY . .
RUN npm install
CMD ["npm", "start"]
EXPOSE 3000
# docker build -t my-node-app .