# 🤖 WSC - AI RAG Chatbot

An AI-powered Retrieval-Augmented Generation (RAG) chatbot that answers questions from uploaded PDF documents and also provides general Computer Science and Engineering knowledge.

---

# 📌 Project Overview

WSC (Website Support Chatbot) is an intelligent chatbot built using modern AI technologies.

The chatbot has two major capabilities:

- 📄 Answer questions from uploaded PDF documents (RAG)
- 🧠 Answer general Computer Science & Engineering questions using Groq LLM

The system combines semantic search with Large Language Models to provide accurate and context-aware responses.

---

# 🚀 Features

## 📄 PDF-based Question Answering

- Upload multiple PDF files
- Extract text automatically
- Split documents into chunks
- Generate embeddings
- Store embeddings using FAISS
- Retrieve the most relevant context
- Generate accurate answers based only on uploaded documents

---

## 🧠 General AI Assistant

If the uploaded documents do not contain the answer, the chatbot automatically switches to General AI mode and can answer topics such as:

- C
- C++
- Java
- Python
- JavaScript
- HTML
- CSS
- React
- Node.js
- DBMS
- Operating System
- Computer Networks
- Data Structures
- Algorithms
- AI
- Machine Learning
- Deep Learning
- Data Science
- Software Engineering
- Cloud Computing
- Git & GitHub

---

## 💬 Modern Chat Interface

- ChatGPT-style UI
- User & Bot avatars
- Markdown support
- Syntax highlighted code blocks
- Automatic scrolling
- Responsive design

---

## 🔐 Authentication

- User Registration
- User Login
- JWT Authentication
- Password Hashing using bcrypt

---

# 🛠 Tech Stack

## Frontend

- React
- Vite
- CSS
- React Markdown
- Remark GFM

---

## Python Backend (RAG)

- Flask
- Flask-CORS
- Sentence Transformers
- FAISS
- Groq API

---

## Node.js Backend

- Node.js
- Express.js
- MongoDB
- Mongoose
- JWT
- bcryptjs

---

## AI Models

- Groq LLM
- all-MiniLM-L6-v2 Embedding Model

---

# 📂 Project Structure

```
WSC
│
├── frontend
│   ├── src
│   ├── assets
│   └── App.jsx
│
├── backend
│   ├── controllers
│   ├── routes
│   ├── models
│   ├── middleware
│   ├── config
│   └── server.js
│
├── python-rag
│   ├── app.py
│   ├── embed.py
│   ├── vector_store.py
│   ├── query.py
│   ├── groq_client.py
│   ├── uploads
│   └── faiss_index
│
└── README.md
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone https://github.com/yourusername/WSC.git
```

```bash
cd WSC
```

---

## 2. Frontend

```bash
cd frontend
```

```bash
npm install
```

```bash
npm run dev
```

---

## 3. Node Backend

```bash
cd backend
```

```bash
npm install
```

```bash
npm run dev
```

---

## 4. Python Backend

Create a virtual environment

```bash
python -m venv venv
```

Activate environment

Windows

```bash
venv\Scripts\activate
```

Install packages

```bash
pip install -r requirements.txt
```

Run Flask server

```bash
python app.py
```

---

# 🌐 API Endpoints

## Python API

### Upload PDF

```
POST /upload
```

### Ask Question

```
POST /ask
```

---

## Node API

### Register

```
POST /api/auth/register
```

### Login

```
POST /api/auth/login
```

---

# 📸 Screenshots

You can add screenshots of:

- Home Page
- PDF Upload
- Chat Interface
- Login Page
- Register Page

---

# 🔮 Future Improvements

- Admin Dashboard
- Chat History
- User Profile
- Dark Mode
- Multiple LLM Support
- PDF Management
- Conversation Memory
- Role-based Authentication
- Deployment on Vercel & Render

---

# 👨‍💻 Author

**Shushovan Chakraborty**

B.Tech Student

Artificial Intelligence & Full Stack Developer

---

# 📜 License

This project is developed for educational and learning purposes.