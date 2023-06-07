from flask import Flask, render_template, request
import requests
import json
import pyttsx3

app3 = Flask(__name__)
engine = pyttsx3.init()


@app3.route('/', methods=['GET', 'POST'])
def chatbot():
    if request.method == 'POST':
        condition = request.form['condition']
        severity = request.form['severity']
        query = request.form['query']
        # requesting to url
        api_url = 'https://api.openai.com/v1/chat/completions'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ************'
        }
        data = {
            "model": "gpt-3.5-turbo",
            'messages': [
                {'role': 'user',  'content': f'Condition: {condition}, Severity: {severity},query: {query}'}],

        }

        response = requests.post(
            api_url, headers=headers, data=json.dumps(data))
        response_json = response.json()
        chatbot_response = response_json['choices'][0]['message']['content']

        return render_template('index3.html', response=chatbot_response)

    else:
        return render_template('index3.html')


if __name__ == '__main__':
    app3.run(debug=True)
