from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from prompt_builder import build_prompt
from llm_client import generate_sql
from sql_validator import clean_sql, is_safe_select
from db import run_query

app = FastAPI(title="NL to SQL API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class QueryRequest(BaseModel):
    question: str


@app.post("/query")
def query(request: QueryRequest):
    prompt = build_prompt(request.question)

    raw_sql = generate_sql(prompt)
    sql = clean_sql(raw_sql)

    if not is_safe_select(sql):
        raise HTTPException(
            status_code=400,
            detail=f"Rejected unsafe or invalid query: {sql}"
        )

    try:
        rows = run_query(sql)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Database error: {str(e)}"
        )

    return {
        "question": request.question,
        "sql": sql,
        "results": rows
    }


@app.get("/health")
def health():
    return {"status": "ok"}
