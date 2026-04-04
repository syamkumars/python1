import requests, os 
from dotenv import load_dotenv

def get_apikey():
    from dotenv import load_dotenv
    print("Loading .env file...")
    loaded = load_dotenv()
    api_key = os.getenv("OPERROUTER_APIKEY")
    return api_key


def ask_ai(prompt):
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {get_apikey()}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "qwen/qwen3.6-plus:free",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(url, headers=headers, json=data)
    print("Status Code:", response.status_code)
    print("Raw Response:", response.text)  # VERY IMPORTANT

    try:
        result = response.json()
        return result["choices"][0]["message"]["content"]
    except Exception as e:
        print("Error parsing response:", e)
        return None