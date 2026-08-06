# 🛒 AI Shopping Assistant

An AI-powered Shopping Assistant built using **Google Gemini**, **Model Context Protocol (MCP)**, **FastAPI**, **PostgreSQL**, and **Streamlit**.

The assistant understands natural language, searches products, remembers conversation context, verifies users, and places orders using MCP tools.

---

# 🚀 Features

- 🤖 AI-powered shopping assistant using Google Gemini Flash Lite
- 🔍 Intelligent product search
- 🛍️ Product selection and ordering
- 👤 User verification using phone number
- 🧠 Conversation memory and state management
- 🔗 MCP (Model Context Protocol) integration
- ⚡ FastAPI REST backend
- 🗄️ PostgreSQL database
- 🖥️ Streamlit web interface

---

# 🏗️ System Architecture

```
                User
                  │
                  ▼
        Streamlit Frontend
                  │
                  ▼
          Chat Service
                  │
        ┌─────────┴─────────┐
        ▼                   ▼
   Gemini LLM      Conversation Memory
        │
        ▼
   MCP Tool Selection
        │
        ▼
     MCP Server
        │
        ▼
     FastAPI Backend
        │
        ▼
 PostgreSQL Database
```

---

# 🔄 Workflow

1. User enters a request.
2. Gemini understands the user's intent.
3. Gemini decides whether an MCP tool is required.
4. The selected MCP tool is executed.
5. FastAPI retrieves live data from PostgreSQL.
6. Results are returned through the MCP Server.
7. Conversation memory stores the current context.
8. The assistant responds naturally.

---

# 🛠️ Tech Stack

## Frontend

- Streamlit

## AI

- Google Gemini Flash Lite
- Prompt Engineering

## Protocol

- Model Context Protocol (MCP)

## Backend

- FastAPI
- SQLAlchemy

## Database

- PostgreSQL

## Language

- Python

---

# 📂 Project Structure

```
ai-shopping-assistant/
│
├── ai_assistant/
│   ├── app.py
│   ├── chat_service.py
│   ├── gemini_client.py
│   ├── conversation_memory.py
│   ├── mcp_client.py
│   └── tool_manager.py
│
├── app/
│   ├── database/
│   ├── models/
│   ├── repositories/
│   ├── routes/
│   ├── schemas/
│   └── services/
│
├── mcp_server/
│   ├── database/
│   ├── tools/
│   ├── utils/
│   └── server.py
│
├── images/
├── requirements.txt
└── README.md
```

---

# 🧠 Conversation Memory

The assistant maintains:

- Current User
- Selected Product
- Last Search Results
- Pending Order
- Conversation State

This enables natural follow-up conversations such as:

```
Show me headphones

↓

Studio Headphones

↓

Buy it

↓

Enter phone number

↓

Confirm

↓

Order Created
```

---

# 📦 MCP Tools

- Search Products
- Get Product Details
- List Categories
- Verify User
- Create User
- Create Order
- Inventory Lookup

---

# 💾 Database

The system stores:

- Products
- Categories
- Users
- Orders
- Inventory

---

# ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/kishor-prog/ai-shopping-assistant.git
```

### Move into the project

```bash
cd ai-shopping-assistant
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Start the FastAPI backend

```bash
python app/main.py
```

### Start the MCP Server

```bash
python mcp_server/server.py
```

### Launch the Streamlit application

```bash
streamlit run ai_assistant/app.py
```

---

# 📸 Screenshots

## 🏠 Home

![Home](images/home.png)

---

## 🔍 Product Search

![Product Search](images/product-selection.png)

---

## 👤 User Verification

![User Verification](images/user-verification.png)

---

## ✅ Order Confirmation

![Order Success](images/order-success.png)

---

# 🔮 Future Improvements

- Product recommendation engine
- Multi-product comparison
- Shopping cart
- Order history
- Payment gateway integration
- Voice assistant
- Image-based product search

---

# 👨‍💻 Author

**Kishor**

GitHub: https://github.com/kishor-prog

Repository: https://github.com/kishor-prog/ai-shopping-assistant