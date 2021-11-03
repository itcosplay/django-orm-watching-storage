# django-orm-watching-storage
Репозиторий с сайтом для урока «Пишем пульт охранника банка» курса dvmn.org

### Требования к окружению:
Python 3.0 (или выше) должен быть уже установлен.  
  
Переменная окружения для БД:  
```
DATABASE_URL = postgres://USER:PASSWORD@HOST:PORT/NAME`
```
Также необходимы переменные 
```
SECRET_KEY = 'somesecretword'
ALLOWED_HOSTS = .localhost,127.0.0.1
```

### Как установить
* Клонируем репозиторий
* Создаем виртуальное окружение:
* Устанавливаем зависимости
* В корень проекта добавляем .env c требуемыми переменными
```
pip install -r requirements.txt
```
* Запускаем отладочный сервер
```
python manage.py runserver
```
