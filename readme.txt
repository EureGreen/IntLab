# Backend AI Contact API

REST API для обработки формы обратной связи с AI-анализом сообщений, отправкой email, логированием и защитой от спама.

## 1. Запуск проекта

### Требования

- Python 3.12+
- pip

### Установка

Клонировать репозиторий:

```bash
git clone <repository_url>
cd backend-ai-contact-api
```

Создать виртуальное окружение:

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

Установить зависимости:

```bash
pip install -r requirements.txt
```

### Настройка переменных окружения

Создать файл `.env`:

```env
APP_NAME=Backend AI Contact

OPENROUTER_API_KEY=YOUR_API_KEY
OPENROUTER_BASE_URL=https://openrouter.ai/api/v1
OPENROUTER_MODEL=poolside/laguna-s-2.1:free

SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=your_email@gmail.com
SMTP_PASSWORD=your_app_password
OWNER_EMAIL=your_email@gmail.com
```

### Запуск приложения

```bash
python -m uvicorn app.main:app --reload
```

Swagger-документация будет доступна по адресу:

```
http://127.0.0.1:8000/docs
```

## 2. Стек технологий

### Backend

- Python 3.12
- FastAPI
- Pydantic
- Uvicorn

### AI

- OpenRouter API
- OpenAI Python SDK

### Email

- smtplib
- email.message

### Хранение данных

Для хранения используется файловая система (JSON).

## 3. Архитектура

Проект построен по слоистой архитектуре.

Структура проекта:

```text
app/
├── api/
├── controllers/
├── middleware/
├── models/
├── repositories/
├── services/
├── utils/
├── config.py
└── main.py

data/
```

### Используемые слои

- Router — обработка HTTP-запросов.
- Controller — получение данных от API.
- Service — бизнес-логика приложения.
- Repository — работа с файловым хранилищем.

FastAPI выбран благодаря высокой производительности, встроенной Swagger-документации и удобной интеграции с Pydantic.

## 4. Реализация API

### POST /api/contact

Создает новое обращение.

Пример запроса:

```json
{
  "name": "Erik",
  "email": "test@example.com",
  "phone": "+79999999999",
  "comment": "Хочу заказать разработку сайта"
}
```

Пример ответа:

```json
{
  "message": "Contact request created successfully"
}
```

### GET /api/health

Возвращает состояние сервиса.

### GET /api/metrics

Возвращает статистику обработанных обращений.

### Валидация

Проверяется:

- имя;
- email;
- телефон;
- комментарий.

Валидация реализована средствами Pydantic.

### Обработка ошибок

Используются стандартные HTTP-коды:

- 201 — обращение успешно создано;
- 422 — ошибка валидации;
- 429 — превышен лимит запросов;
- 500 — внутренняя ошибка сервера.

Все ошибки записываются в лог.

## 5. AI-интеграция

Для анализа обращений используется OpenRouter API.

После получения комментария AI определяет:

- тональность сообщения;
- категорию обращения;
- краткое описание.

Используемый промпт:

```text
Ты анализируешь обращения клиентов.

Верни только JSON следующего формата:

{
  "sentiment": "",
  "category": "",
  "summary": ""
}
```

### Fallback

Если AI недоступен, сервис продолжает работу без прерывания обработки запроса.

В этом случае сохраняется:

```json
{
  "sentiment": "unknown",
  "category": "unknown",
  "summary": "AI unavailable"
}
```

## 6. Что сделано с помощью AI

AI использовался для:

- генерации отдельных шаблонов классов;
- помощи при интеграции OpenRouter API;
- подготовки структуры документации.

Вручную были реализованы:

- архитектура проекта;
- бизнес-логика;
- обработка ошибок;
- логирование;
- SMTP-интеграция;
- собственный Rate Limiter;
- файловая блокировка;
- взаимодействие между компонентами приложения;
- тестирование и исправление ошибок.

## 7. Хранение данных

Все данные сохраняются в папке `data`.

```text
data/
├── contacts.json
├── metrics.json
├── rate_limit.json
└── logs/
    └── app.log
```

### Логирование

Все HTTP-запросы и ошибки записываются в файл `data/logs/app.log`.

### Rate Limiting

Ограничение количества запросов реализовано с помощью JSON-файла. Для безопасной записи используется файловая блокировка.

### Статистика

Статистика успешных и неуспешных запросов хранится в `metrics.json` и доступна через эндпоинт `/api/metrics`.