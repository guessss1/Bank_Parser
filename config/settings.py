import os
from dotenv import load_dotenv

# Загружаем переменные окружения из файла .env
load_dotenv()

# API-ключ для доступа к OpenAI
API_KEY = os.getenv("OPENAI_API_KEY")

# Модель для вызова
MODEL = "gpt-4o"

# Параметры генерации
GENERATION_PARAMS = {
    "temperature": 0.7,
    "max_tokens": 150,
    "top_p": 0.9,
    "stop": ["\n\n"],
    "frequency_penalty": 0.2,
    "presence_penalty": 0.3
}



