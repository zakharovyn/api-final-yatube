# Yatube API

**Документация к API проекта Yatube (v1)**

## Описание
Проект **Yatube** — это простая социальная сеть для публикации текстовых постов, комментариев и подписок на авторов. Пользователи могут создавать публикации, комментировать их, подписываться на других авторов и просматривать контент в различных сообществах.

## Установка
1. Клонируйте репозиторий:
   ```bash
   git clone git@github.com:zakharovyn/api-final-yatube.git
   ```
   ```
   cd api-final-yatube
   ```
2. Cоздайте виртуальное окружение и активируйте его:
   ```bash
   python3 -m venv venv
   ```
   ```
   source venv/bin/activate
   ```
3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
4. Выполните миграции и создайте суперпользователя:
   ```bash
   python manage.py migrate
   ```
   ```
   python manage.py createsuperuser
   ```
5. Запустите сервер разработки:
   ```bash
   python manage.py runserver
   ```
   
## Примеры запросов
### Получение списка постов с пагинацией
```bash
curl -X GET "http://localhost:8000/api/v1/posts/?limit=5&offset=10" \
     -H "Authorization: Bearer <your_access_token>"
```

### Создание нового поста
```bash
curl -X POST "http://localhost:8000/api/v1/posts/" \
     -H "Authorization: Bearer <your_access_token>" \
     -H "Content-Type: application/json" \
     -d '{ "text": "Hello, Yatube!", "group": 1 }'
```
