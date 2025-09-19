import os
from openai import OpenAI
from app.services.gdrive_service import find_tool_by_name

# создаём клиент
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_agent(question: str) -> str:
    try:
        tool = find_tool_by_name(question)
        context = (
            f"Название инструмента: {tool['name']}, ссылка: {tool['link']}"
            if tool else "Инструмент не найден."
        )

        response = client.chat.completions.create(
            model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
            messages=[
                {"role": "system", "content": "Ты AI-ассистент RealtyCalendar. Объясняй инструменты с сайта."},
                {"role": "user", "content": f"Вопрос: {question}. Данные: {context}"}
            ],
            max_tokens=400,
            temperature=0.3
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"Ошибка при работе с OpenAI: {e}"
