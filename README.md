Perfect — here's your updated `README.md` with the **correct GitHub repo URL**:

---

```markdown
# 📧 Email API

A FastAPI backend for sending emails, built with async support using `aiosmtplib`. Managed with Poetry.

---

## 🚀 Features

- Async email sending via SMTP
- FastAPI with CORS support
- Poetry-based dependency and environment management
- Built for easy integration with a frontend

---

## 🛠 Requirements

- Python 3.9+
- [Poetry](https://python-poetry.org/docs/#installation)

---

## 📦 Install Dependencies

Clone the project and install dependencies:

```bash
git clone git@github.com:brandon95547/synexisai-api-python.git
cd synexisai-api-python
poetry install
```

---

## ▶️ Run the Server

```bash
poetry run uvicorn main:app --reload
```

Visit:
- Root: [http://127.0.0.1:8000](http://127.0.0.1:8000)
- Docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🛑 Stop the Server

- Press `Ctrl + C` in the terminal running the server

---

## ✨ Best Practices

- Set `allow_origins` in CORS middleware to your actual frontend domain before deploying
- Store SMTP credentials in a `.env` file using `python-dotenv`
- Expand your app modularly (`routers/`, `services/`, `schemas/`) as it grows
- Use `gunicorn` with `uvicorn` workers for production deployment:
  ```bash
  poetry add gunicorn
  poetry run gunicorn main:app -k uvicorn.workers.UvicornWorker
  ```
- Lock exact dependency versions in `pyproject.toml` for production

---

## 🧪 Example Request

### POST `/send-email`

```json
{
  "to": "recipient@example.com",
  "subject": "Hello",
  "message": "This is a test email!"
}
```

---

## 📁 Project Structure

```
synexisai-api-python/
├── main.py
├── email_utils.py
├── pyproject.toml
├── README.md
```

---

## 📄 License

MIT License © 2025 Brandon Sanders
```

---