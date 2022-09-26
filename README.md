![Build Status](https://github.com/Syzhet/cooking_vk_bot/actions/workflows/coockingvkbot.yml/badge.svg)


# coocking_vk_bot

## Телеграм-бот - витрина булочной/кондитерской.

Исходный функционал:
- Предоставление информации о категориях продуктов.
- Предоставление информации о продуктах.
- Детальное описание продуктов.
- Навигация по меню.
- Данные о категориях и продуктах хранятся в базе данных.
- Статические картинки подгружаются через отдельный web-сервер.


## Стек технологий 

<div>
  <a href="https://www.python.org/">
    <img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original-wordmark.svg" title="Python" alt="Python" width="40" height="40"/>&nbsp;
  </a>
  <a href ="https://www.docker.com/">
    <img src="https://github.com/devicons/devicon/blob/master/icons/docker/docker-original.svg" title="Docker" alt="Docker" width="40" height="40"/>&nbsp;
  </a>
  <a href="https://github.com/">
    <img src="https://github.com/devicons/devicon/blob/master/icons/github/github-original.svg" title="GitHub" alt="GitHub" width="40" height="40"/>&nbsp;
  </a>
  <a href="https://nginx.org/">
    <img src="https://github.com/devicons/devicon/blob/master/icons/nginx/nginx-original.svg" title="GitHub" alt="GitHub" width="40" height="40"/>&nbsp;
  </a>
  <a href="https://www.postgresql.org/">
    <img src="https://github.com/devicons/devicon/blob/master/icons/postgresql/postgresql-original.svg" title="GitHub" alt="GitHub" width="40" height="40"/>&nbsp;
  </a>  
</div>

Версии ПО:

- python: 3.10.4;
- vkvawe: 0.2.17;
- gino: 1.0.1;
- Docker: 20.10.18;
- docker-compose: 1.26.0;
- nginx: 1.19.3;
- PostgreSQL: 13.0.


# Установка проекта локально
Склонировать репозиторий на локальную машину:
```sh
git clone https://github.com/Syzhet/cooking_vk_bot.git
```
Cоздать и активировать виртуальное окружение:
```sh
python -m venv venv
source venv/bin/activate
```
Cоздайте файл .env в корневой директории проекта содержанием:
- BOT_TOKEN= токен бота;
- GROUP_ID= id сообщества где находится бот;
- HOST_ID= id хоста бота;
- DB_IP= ip адрес базы данных;
- POSTGRES_USER= роль для базы данных;
- POSTGRES_PASSWORD= пароль для пользователя базы данных;
- POSTGRES_DB= имя базы данных;
- DB_PORT= порт для подключения к базе данных;
- TAG= версия ообраза docker для базы данных;
- NGINX_ID= id вэб сервера nginx для раздачи статических файлов.

Установить зависимости из файла requirements.txt:
```sh
pip install -r requirements.txt
```


# Запуск проекта в Docker контейнере
Установите Docker и docker-compose
```sh
sudo apt install docker.io 
sudo curl -L "https://github.com/docker/compose/releases/download/1.26.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```
Параметры запуска описаны в файлах docker-compose.yml.

Запустите docker-compose:
```sh
sudo docker-compose up -d
```

После сборки появляется 3 контейнера:

| Контайнер | Описание |
| ------ | ------ |
| vkbot | контейнер с запущенным ботом |
| vknginx | контейнер с web-сервером |
| vkdb | контейнер с базой данных |


## Авторы проекта

- [Ионов А.В.](https://github.com/Syzhet) - Python разработчик.