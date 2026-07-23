# Coverage Chatbot API

A FastAPI backend for the Coverage Chatbot project.

## Prerequisites

- Python 3.10+
- pip

## Installation

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate it.

macOS/Linux:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the application

```bash
uvicorn main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

Health endpoint:

```
http://127.0.0.1:8000/health
```

Expected response:

```json
{
  "status": "ok"
}
```

Swagger UI:

```
http://127.0.0.1:8000/docs
```

ReDoc:

```
http://127.0.0.1:8000/redoc
```