# 🚀 AI SaaS – Natural Language to SQL Platform

An AI-powered SaaS application that enables users to interact with a MySQL database using plain English. Instead of writing SQL queries manually, users simply ask questions in natural language, and the application automatically generates SQL using a locally hosted Large Language Model (LLM), validates the generated query, executes it safely, and returns the results.

This project demonstrates real-world Full Stack Development, AI Integration, Backend Development, Database Management, and Prompt Engineering using modern technologies.

---

# 📌 Features

- Convert Natural Language into SQL queries
- AI-powered SQL generation using Ollama + LLaMA 3
- FastAPI REST Backend
- React.js Frontend
- MySQL Database Integration
- SQL Validation Layer for Safe Execution
- Read-Only Query Execution
- Fully Offline AI (No Paid APIs)
- Easy to Configure with Any MySQL Database
- Sample Database Included for Quick Testing

---

# 🧠 System Architecture

```
                User
                  │
                  ▼
          React Frontend
                  │
                  ▼
          FastAPI Backend
                  │
                  ▼
          Prompt Builder
                  │
                  ▼
        Ollama (LLaMA 3)
                  │
                  ▼
      Generated SQL Query
                  │
                  ▼
      SQL Validation Layer
                  │
                  ▼
          MySQL Database
                  │
                  ▼
          Query Results
                  │
                  ▼
             React UI
```

---

# 🛠 Tech Stack

## Backend

- Python 3.10+
- FastAPI
- Pydantic

## AI

- Ollama
- LLaMA 3

## Frontend

- React.js
- Axios

## Database

- MySQL

## Development Tools

- Git
- GitHub
- Docker (Optional)

---

# 📂 Project Structure

```
AI-SaaS-Natural-Language-to-SQL/
│
├── backend/
│   ├── config.py
│   ├── db.py
│   ├── llm_client.py
│   ├── main.py
│   ├── prompt_builder.py
│   ├── schema_context.py
│   ├── sql_validator.py
│   ├── requirements.txt
│   └── seed.sql
│
├── frontend/
│   ├── public/
│   ├── src/
│   ├── package.json
│   └── ...
│
└── README.md
```

---

# ⚙️ Installation Guide

Follow the steps below to run the project on your own computer.

---

## Step 1 – Clone the Repository

```bash
git clone https://github.com/mamidi-joseph/AI-SaaS-Natural-Language-to-SQL-Platform.git

cd AI-SaaS-Natural-Language-to-SQL-Platform
```

Replace **YOUR_USERNAME** and **YOUR_REPOSITORY** with your GitHub repository details.

---

## Step 2 – Install Ollama

### Linux

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Verify the installation.

```bash
ollama --version
```

Download the LLaMA 3 model.

```bash
ollama pull llama3
```

Start Ollama.

```bash
ollama serve
```

Keep this terminal running while using the application.

---

## Step 3 – Install MySQL

Ubuntu

```bash
sudo apt update

sudo apt install mysql-server
```

Start MySQL.

```bash
sudo systemctl start mysql

sudo systemctl enable mysql
```

---

# Step 4 – Choose Your Database

This project works with **any MySQL database**.

### Option 1 (Recommended)

If you already have an existing MySQL database, simply connect this project to it by updating your database credentials.

No additional setup is required.

---

### Option 2 (For Testing)

If you do not have an existing database, this repository includes a sample SQL file named:

```
seed.sql
```

The sample database contains example tables and records so you can quickly test the application.

Create a database.

```sql
CREATE DATABASE your_database_name;
```

Import the sample data.

```bash
mysql -u your_username -p your_database_name < seed.sql
```

**Note**

The sample database is provided only for demonstration purposes.

In real-world applications, organizations already have production databases containing their own business data. In those cases, simply connect the project to the existing database without using the sample SQL file.

---

# Step 5 – Configure Database Connection

Open

```
backend/config.py
```

Update the following values.

```python
DB_CONFIG = {

    "host": "localhost",

    "user": "your_username",

    "password": "your_password",

    "database": "your_database_name"

}
```

Also verify the Ollama configuration.

```python
OLLAMA_MODEL = "llama3"

OLLAMA_URL = "http://localhost:11434/api/generate"
```

---

# Step 6 – Backend Setup

Move to the backend folder.

```bash
cd backend
```

Create a virtual environment.

```bash
python3 -m venv venv
```

Activate it.

Linux / macOS

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

---

# Step 7 – Start the Backend

```bash
uvicorn main:app --reload
```

Backend

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

# Step 8 – Frontend Setup

Open another terminal.

Move to the frontend folder.

```bash
cd frontend
```

Install dependencies.

```bash
npm install
```

Run the application.

```bash
npm start
```

Frontend

```
http://localhost:3000
```

---

# 💬 Example Questions

You can ask questions like:

```
Show all customers
```

```
Customers from Chennai
```

```
Show products under ₹1000
```

```
Which customer placed the most orders?
```

```
Show total sales by month
```

```
List all products in the Electronics category
```

---

# 🔄 How It Works

1. The user enters a question in plain English.

2. The React frontend sends the request to the FastAPI backend.

3. The backend builds a prompt describing the database schema.

4. Ollama generates an SQL query.

5. The SQL validation layer checks whether the generated SQL is safe.

6. Only valid read-only SQL queries are executed.

7. The query results are retrieved from the MySQL database.

8. The generated SQL query and results are displayed in the frontend.

---

# 📌 Important Notes

- The application supports any MySQL database.
- Existing databases can be connected directly by updating the database credentials.
- The included `seed.sql` file is optional and intended only for quick testing.
- Ensure Ollama is running before starting the backend.
- Download the LLaMA 3 model before using the application.
- The application only allows safe read-only SQL queries.
- Update `schema_context.py` if your database schema is different from the sample schema.

---

# 🚀 Future Enhancements

- PostgreSQL Support
- SQLite Support
- User Authentication
- Role-Based Access Control (RBAC)
- Query History
- Saved Reports
- Dashboard and Analytics
- Docker Compose
- Cloud Deployment (AWS, Azure, GCP)

---

# 👨‍💻 Author

**Mamidi Joseph**

AI & Backend Developer

GitHub: https://github.com/mamidi-joseph

---

⭐ If you found this project useful, consider giving it a star on GitHub.
