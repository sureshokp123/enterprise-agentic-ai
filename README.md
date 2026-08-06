# 🤖 MCP AI Agent

An AI-powered Assistant built using **FastAPI**, **Azure OpenAI**, **Docker**, and **Azure App Service**.

This project demonstrates how to build a production-ready AI Agent capable of answering user questions, invoking tools, maintaining conversation memory, and deploying to Azure using Docker containers.

---

# 🚀 Features

- AI Chat Assistant
- Azure OpenAI Integration
- Tool Calling
- Calculator Tool
- File Reader Tool
- Employee Database Tool
- Conversation Memory
- FastAPI REST API
- Swagger UI
- Docker Support
- Azure Container Registry (ACR)
- Azure Web App Deployment
- GitHub Repository
- GitHub Actions CI/CD (In Progress)

---

# 🛠 Tech Stack

## Backend

- Python 3.11
- FastAPI
- Uvicorn

## AI

- Azure OpenAI
- GPT Models
- Prompt Engineering

## Database

- SQLite

## Container

- Docker

## Cloud

- Microsoft Azure
- Azure Container Registry
- Azure App Service

## API Testing

- Swagger UI

## Version Control

- Git
- GitHub

---

# 📂 Project Structure

```
mcp-ai-agent
│
├── api
│   └── app.py
│
├── agent
│   └── ai_agent.py
│
├── services
│   └── agent_service.py
│
├── tools
│   ├── calculator.py
│   ├── database.py
│   └── file_reader.py
│
├── data
│   ├── company.db
│   └── employee.txt
│
├── config.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

# ⚙️ Setup

## Clone Repository

```bash
git clone https://github.com/sureshokp123/mcp-ai-agent.git

cd mcp-ai-agent
```

---

# Create Virtual Environment

Windows

```bash
python -m venv venv311
```

Activate

```bash
venv311\Scripts\activate
```

---

# Install Packages

```bash
pip install -r requirements.txt
```

---

# Configure Environment Variables

Create a `.env` file.

Example

```env
AZURE_OPENAI_ENDPOINT=https://YOUR-RESOURCE.openai.azure.com/openai/v1/

AZURE_OPENAI_API_KEY=YOUR_API_KEY

AZURE_OPENAI_MODEL=gpt-4.1
```

---

# Run Application

```bash
uvicorn api.app:app --reload
```

Application

```
http://localhost:8000
```

Swagger

```
http://localhost:8000/docs
```

---

# Docker

## Build Image

```bash
docker build -t mcp-ai-agent .
```

## Run Container

```bash
docker run -p 8000:8000 mcp-ai-agent
```

Swagger

```
http://localhost:8000/docs
```

---

# Azure Container Registry

Login

```bash
az login
```

Login to Registry

```bash
az acr login --name sureshdocker
```

Tag Image

```bash
docker tag mcp-ai-agent:latest sureshdocker-hnbwfchra7gtezhj.azurecr.io/mcp-ai-agent:v1
```

Push Image

```bash
docker push sureshdocker-hnbwfchra7gtezhj.azurecr.io/mcp-ai-agent:v1
```

---

# Restart Azure Web App

```bash
az webapp restart --resource-group rg-genai-learning --name mcp-ai-agent-suresh
```

---

# API Endpoints

## Health

```
GET /
```

## Chat

```
POST /chat
```
# Example 1
Request

```json
{
  "message": "What is 120 + 350?"
}
```

Response

```json
{
  "response": "470"
}
```
# Example 2
Request

```json
{
  "message": "Show all employees?"
}
```

Response

```json
{
  "response": "employee details"
}
```

---

# Available Tools

### Calculator

```
add(a,b)
```

```
multiply(a,b)
```

---

### File Reader

```
read_file(filename)
```

---

### Employee Database

```
get_all_employees()
```

```
get_employee_by_id(id)
```

---

# AI Workflow

```
User
   │
   ▼
FastAPI
   │
   ▼
Azure OpenAI
   │
   ▼
Tool Selection
   │
   ├── Calculator
   ├── File Reader
   └── Employee Database
   │
   ▼
Response
```

---

# Deployment Architecture

```
GitHub
   │
   ▼
Docker Build
   │
   ▼
Azure Container Registry
   │
   ▼
Azure Web App
   │
   ▼
Internet
```

---

# Commands

## Install

```bash
pip install -r requirements.txt
```

## Run

```bash
uvicorn api.app:app --reload
```

## Docker Build

```bash
docker build -t mcp-ai-agent .
```

## Docker Run

```bash
docker run -p 8000:8000 mcp-ai-agent
```

## Azure Login

```bash
az login
```

## ACR Login

```bash
az acr login --name sureshdocker
```

## Docker Push

```bash
docker push sureshdocker-hnbwfchra7gtezhj.azurecr.io/mcp-ai-agent:v1
```

## Restart Azure Web App

```bash
az webapp restart --resource-group rg-genai-learning --name mcp-ai-agent-suresh
```

---

# Future Enhancements

- LangGraph Multi-Agent Architecture
- PostgreSQL Database
- JWT Authentication
- User Login & Registration
- Conversation History
- RAG (Retrieval-Augmented Generation)
- ChromaDB / FAISS
- PDF Chat
- Azure Blob Storage
- Streaming Responses
- React / Next.js Frontend
- GitHub Actions CI/CD
- Monitoring with Azure Application Insights

---

# Author

**Suresh Kumar**

GitHub

https://github.com/sureshokp123

---

# License

MIT License