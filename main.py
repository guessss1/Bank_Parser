import openai
import sys
import os
from config.settings import API_KEY, MODEL, GENERATION_PARAMS
from pathlib import Path

# Добавляем корневую папку проекта в sys.path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# Устанавливаем API-ключ
openai.api_key = API_KEY

# Загружаем промпт из файла
def load_prompt(file_path):
    return Path(file_path).read_text(encoding="utf-8")

# Путь к файлу с промптом
prompt_file = "prompts/accounting_prompt.txt"
prompt = load_prompt(prompt_file)
print(f"Prompt content: {prompt}")  # Отладочный вывод промпта

# Вызов модели с дополнительными параметрами генерации
response = openai.ChatCompletion.create(
    model=MODEL,
    messages=[
        {"role": "system", "content": "Ты — интеллектуальный парсер данных для банковского приложения."},
        {"role": "user", "content": prompt}
    ],
    **GENERATION_PARAMS
)

print(response)  # Полный ответ от API
print(response.choices[0].message["content"])  # Вывод содержимого ответа



