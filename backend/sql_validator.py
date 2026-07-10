BLOCKED_KEYWORDS = [
    "insert",
    "update",
    "delete",
    "drop",
    "alter",
    "truncate",
    "create",
    "grant",
    "--",
    ";--"
]


def clean_sql(raw_sql: str) -> str:
    sql = raw_sql.replace("```sql", "").replace("```", "").strip()
    sql = sql.split(";")[0].strip() + ";"
    return sql


def is_safe_select(sql: str) -> bool:
    lowered = sql.lower()

    if not lowered.strip().startswith("select"):
        return False

    if any(keyword in lowered for keyword in BLOCKED_KEYWORDS):
        return False

    return True
