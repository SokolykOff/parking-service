# 🅿️ Parking Service — сервис управления парковкой

Тестовый проект для практики 29.5. Сервис для учёта клиентов, парковок и времени пребывания.

---
📁 Структура проекта

parking-service/
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── extensions.py
│   ├── models.py
│   └── routes.py
├── tests/
│   ├── conftest.py
│   ├── factories.py
│   └── test_api.py
├── .flake8
├── .gitignore
├── .gitlab-ci.yml
├── .isort.cfg
├── .github/workflows/ci.yml
├── pyproject.toml
├── requirements-dev.txt
├── requirements.txt
├── init_db.py
├── run.py
└── README.md


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

