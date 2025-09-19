from app.services.gdrive_service import get_all_rows

def get_data():
    """
    Возвращает для Open-WebUI табличку:
      {
        "columns": ["Инструмент", "Ссылка"],
        "rows": [["Шахматка бронирования", "https://..."], ...]
      }
    """
    data = get_all_rows()
    if isinstance(data, dict) and data.get("error"):
        return {"error": data["error"]}
    return {
        "columns": ["Инструмент", "Ссылка"],
        "rows": [[r["tool"], r["url"]] for r in data]
    }
