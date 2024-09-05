# external libs
import requests
import json

def generate_script(prompt) -> str:
    url = "http://localhost:11434/api/generate"
    payload = {"model": "llama3.1", "prompt": prompt}
    response = requests.post(url, json=payload, stream=True)
    script = ""
    for line in response.iter_lines():
        if line:
            data = line.decode('utf-8')
            try:
                json_data = json.loads(data)
                script += json_data.get("response", "")
            except json.JSONDecodeError:
                print("Skipping invalid JSON:", data)

    return script
