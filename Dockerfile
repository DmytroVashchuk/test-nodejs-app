# Вибір базового образу Node.js з офіційного Docker Hub
FROM node:14

# Встановлення робочої директорії в контейнері
WORKDIR /usr/src/app

# Копіювання package.json та package-lock.json у контейнер
COPY package*.json ./

# Встановлення залежностей Node.js
RUN npm install

# Копіювання всіх файлів додатку в контейнер
COPY . .

# Виставлення порту, який буде використовувати контейнер
EXPOSE 3000

# Запуск додатку через npm
CMD ["npm", "start"]
