from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseBadRequest
from django.conf import settings
import json

from openai import OpenAI
client = OpenAI(api_key=settings.OPENAI_API_KEY)

@csrf_exempt
def chat_view(request):
    if request.method != 'POST':
        return HttpResponseBadRequest('POST only')

    try:
        body = json.loads(request.body.decode('utf-8'))
        user_message = (body.get('message') or "").strip()
        if not user_message:
            return HttpResponseBadRequest('Missing "message"')
    except Exception:
        return HttpResponseBadRequest('Bad JSON')

    resp = client.chat.completions.create(
        model="gpt-3.5-turbo",   
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_message},
        ],
        max_tokens=150
    )
    ai_message = resp.choices[0].message.content
    return JsonResponse({"message": ai_message})
