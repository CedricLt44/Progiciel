
from django.shortcuts import render
import os
from mistralai import Mistral
import json
import requests
from django.conf import settings  # Importez les paramètres

# Initialisation
api_key = os.environ.get("MISTRAL_API_KEY")
model = "mistral-small-latest"

client = Mistral(api_key=api_key)

def chatbot_page(request):
    bot_response = None
    user_input = None
    
    api_key = "7QFI2xd83dVeel1zgiOYNklwhtnjDing"
    if not api_key:
        return render(request, 'chatbot/chatbot.html', {
            "user_input": None,
            "bot_response": "Erreur: Clé API Mistral non configurée"
        })
    if request.method == 'POST':
        user_input = request.POST.get('user_input', '').strip()
        
        if user_input:
            try:
                api_url = "https://api.mistral.ai/v1/chat/completions"
                headers = {
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                    "Authorization": f"Bearer {api_key}"
                }
                payload = {
                    "model": model,
                    "messages": [
                        {"role": "system", "content": "Réponds toujours en français."},
                        {"role": "user", "content": user_input}]
                }
                
                response = requests.post(
                    api_url,
                    headers=headers,
                    data=json.dumps(payload, ensure_ascii=False).encode('utf-8')
                )
                
                if response.status_code == 200:
                    result = response.json()
                    bot_response = result["choices"][0]["message"]["content"]
                else:
                    bot_response = f"Erreur API: {response.status_code} - {response.text}"
                    
            except Exception as e:
                bot_response = f"Erreur : {str(e)}"
    
    return render(request, 'chatbot/chatbot.html', {
        "user_input": user_input,
        "bot_response": bot_response
    })