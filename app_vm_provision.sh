#!/bin/bash
# Оновлення списку пакетів
apt-get update

# Встановлення nginx (веб сервер)
apt-get install -y nginx

# Встановлення ufw (універсальний фаєрвол Ubuntu)
#apt-get install -y ufw

# Встановлення netdata (інструмент для моніторингу системи)
#apt-get install -y netdata

# Налаштування ufw (розкоментуйте при потребі)
#ufw allow 22
#ufw allow 8080
#ufw allow 19999
#ufw --force enable

# Запуск служби netdata (розкоментуйте при потребі)
#systemctl start netdata




