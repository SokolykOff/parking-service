# 🅿️ Parking Service — сервис управления парковкой

Тестовый проект для практики 29.5. Сервис для учёта клиентов, парковок и времени пребывания.

---

## 🔧 Стек технологий

- Python 3.11+
- Flask (Application Factory)
- SQLAlchemy (ORM)
- PostgreSQL / SQLite
- Pytest, Factory Boy, Faker

---

## 🚀 Как запустить

```bash
python -m venv venv
source venv/bin/activate  # или .\venv\Scripts\activate
pip install -r requirements.txt
python run.py
🧪 Тесты
pytest -v
📌 API
Метод	Эндпоинт	Описание
GET	/clients	Список клиентов
GET	/clients/<id>	Клиент по ID
POST	/clients	Создать клиента
POST	/parkings	Создать парковку
POST	/client_parkings	Заезд
DELETE	/client_parkings	Выезд


Денис Науменко (SokolykOFF)
Telegram: @sokolykoff
GitHub: SokolykOff

