# 🛒 AI Shopping Assistant

An AI-powered Shopping Assistant that combines **Google Gemini**, **Model Context Protocol (MCP)**, **FastAPI**, **PostgreSQL**, and **Streamlit** to provide an intelligent shopping experience.

The assistant understands natural language, searches products, remembers conversation context, verifies users, and places orders using MCP tools.

---

# 🚀 Features

- 🤖 AI-powered shopping assistant using Google Gemini
- 🔍 Intelligent product search
- 🛍 Product selection and ordering
- 👤 User verification using phone number
- 🧠 Conversation memory and state management
- 🔗 MCP (Model Context Protocol) tool integration
- ⚡ FastAPI backend
- 🗄 PostgreSQL database
- 🖥 Streamlit user interface

---

# 🏗 Architecture

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
   Gemini LLM          Conversation Memory
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
2. Gemini understands the intent.
3. Gemini decides whether an MCP tool is required.
4. The selected MCP tool is executed.
5. FastAPI retrieves live data from PostgreSQL.
6. Results are returned to the assistant.
7. Conversation memory stores the selected product, current user, and conversation state.
8. The assistant responds naturally.

---

# 🛠 Tech Stack

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

## Programming Language
- Python

---

# 📂 Project Structure

```
ai-shopping-assistant/
│
├── ai_assistant/        # AI Assistant
│   ├── app.py
│   ├── chat_service.py
│   ├── gemini_client.py
│   ├── conversation_memory.py
│   ├── mcp_client.py
│   └── tool_manager.py
│
├── app/                 # FastAPI Backend
│   ├── models/
│   ├── routes/
│   ├── repositories/
│   ├── services/
│   ├── schemas/
│   └── database/
│
├── mcp_server/          # MCP Server
│   ├── tools/
│   ├── database/
│   ├── utils/
│   └── server.py
│
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

This enables follow-up interactions such as:

```
Show me headphones

↓

Sony WH-1000XM6

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

The project uses PostgreSQL with the following entities:

- Products
- Categories
- Users
- Orders
- Inventory

---

# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/kishor-prog/ai-shopping-assistant.git
```

Move into the project

```bash
cd ai-shopping-assistant
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the FastAPI backend

```bash
python app/main.py
```

Run the MCP Server

```bash
python mcp_server/server.py
```

Run the Streamlit application

```bash
streamlit run ai_assistant/app.py
```

---

# 📸 Screenshots

Screenshots will be added in future updates.

---

# 🔮 Future Improvements

- Product recommendation engine
- Multi-product comparison
- Shopping cart
- Order history
- Payment integration
- Voice assistant support
- Image-based product search

---

# 👨‍💻 Author

**Kishor**

GitHub: https://github.com/kishor-prog