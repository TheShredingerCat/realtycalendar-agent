import os
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials
from typing import List, Dict, Optional


SPREADSHEET_ID = "1FTuOZNxg3G0mckYJ8RRdOdaHCNsJI2pWDyKWhVk3WHE"
RANGE_NAME = "Лист1!A:B"

SERVICE_ACCOUNT_FILE = os.getenv("GOOGLE_APPLICATION_CREDENTIALS", "credentials.json")
SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

def _sheet_service():
    creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    return build("sheets", "v4", credentials=creds).spreadsheets()

def get_all_rows() -> List[Dict[str, str]] | Dict[str, str]:
    """Вернём [{tool, url}, ...] или {error:...}"""
    try:
        sheet = _sheet_service()
        result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
        values = result.get("values", [])
        if not values:
            return {"error": "Пустая таблица"}
        rows = []
        for row in values:
            if len(row) >= 2:
                rows.append({"tool": row[0].strip(), "url": row[1].strip()})
        return rows
    except Exception as e:
        return {"error": str(e)}

def get_tool_by_index(index_1based: int) -> Optional[Dict[str, str]]:
    data = get_all_rows()
    if isinstance(data, dict) and data.get("error"):
        return None
    idx = index_1based - 1
    if 0 <= idx < len(data):
        return data[idx]
    return None

def find_tool_by_name(query: str) -> Optional[Dict[str, str]]:
    data = get_all_rows()
    if isinstance(data, dict) and data.get("error"):
        return None
    q = query.lower()

    for row in data:
        if q in row["tool"].lower():
            return row
    return None
