<<<<<<< HEAD
# Парковочный сервис

Тестовый проект для практики 29.5
=======
# 🅿️ Parking Service — сервис управления парковкой

## Описание
Сервис для учёта клиентов, парковок и времени пребывания. Реализован на Flask с использованием SQLAlchemy, покрыт тестами (pytest) и фабриками данных (Factory Boy).

## Стек
- Python 3.11+
- Flask (Application Factory)
- SQLAlchemy (ORM)
- PostgreSQL / SQLite
- Pytest, Factory Boy, Faker

## Как запустить
```bash
python -m venv venv
source venv/bin/activate  # или .\venv\Scripts\activate
pip install -r requirements.txt
python run.py
Тесты
bash
pytest -v
API
Метод	Эндпоинт	Описание
GET	/clients	Список клиентов
GET	/clients/<id>	Клиент по ID
POST	/clients	Создать клиента
POST	/parkings	Создать парковку
POST	/client_parkings	Заезд
DELETE	/client_parkings	Выезд
Автор
Денис Науменко (SokolykOFF)
>>>>>>> f917de328d936a0315226a823320b78209ef9040
