from schema_context import SCHEMA_DESCRIPTION


def build_prompt(user_question: str) -> str:
    return f"""You are a MySQL expert. Convert the natural language question into a single valid MySQL SELECT query.

Database schema:
{SCHEMA_DESCRIPTION}

Rules:
- Output ONLY the SQL query, no explanation, no markdown formatting, no backticks.
- Only generate SELECT statements. Never write INSERT, UPDATE, DELETE, DROP, or ALTER.
- Use table and column names exactly as given above.

Question:
{user_question}

SQL query:
"""
