# 🤖 Chatbot API

A simple yet scalable chatbot backend built with FastAPI. This project demonstrates how to design and implement a rule-based chatbot system with clean architecture and RESTful APIs.

---

## 🚀 Features

- Chat endpoint (`/chat`)
- Rule-based response system
- Keyword matching
- Text preprocessing
- Optional chat history storage
- RESTful API design
- Auto-generated API docs (Swagger)

---

## 🧠 Tech Stack

- Python 3
- FastAPI
- Uvicorn
- Pydantic
- (Optional) SQLite / PostgreSQL

---

## 📁 Project Structure

app/
├── api/ # Routes
├── core/ # Config & security
├── services/ # Chatbot logic
├── schemas/ # Request/Response models
├── models/ # Database models
├── db/ # Database setup
└── utils/ # Helper functions


---

## ⚙️ Installation

```bash
git clone https://github.com/your-username/chatbot-api.git
cd chatbot-api
pip install -r requirements.txt
