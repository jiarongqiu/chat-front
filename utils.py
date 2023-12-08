import requests

def get_chat_routes():
    data = requests.get(url="http://localhost:8080/openapi.json").json().get('paths')
    chat_routes = [k.split('/')[-1] for k in data if 'chat' in k]
    print(f"chat_routes {chat_routes}")
    return chat_routes

def answer(question,version='v1',history=[]):
    url = f"http://localhost:8080/chat/{version}"
    params = {
        "question": question,
        "chat_history": []
    }
    response = requests.post(url=url,json=params)
    print(response,response.status_code)
    if response.status_code == 200:
        response = response.json()['answer']
    else:
        response = f"Error calling backend with status_code {response.status_code}"
    return response


