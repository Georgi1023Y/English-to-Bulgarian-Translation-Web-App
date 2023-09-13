from flask import Flask, render_template, request
import requests


app = Flask(__name__)

# Google Translate Rapid API URL
url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

# Creating a function called index that renders index.html 
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

# Creating a function called translate that handeles translation
@app.route('/translation', methods=['POST'])
def translate():
    # Checks if the translation route is accessed
    print("Translation route accessed")
    if request.method == 'POST':
        # Gets the text user entered for translation
        text = request.form['entered_text']
        # All of the data I need to provie when making request to this translation API. Target is Bulgarian and q is variable text, which user entered and we get from the form.
        # Text that is entered should be in English.
        payload = {
        	"q":f"{text}",
        	"target": "bg",
        	"source": "en"
        }
        headers = {
        	"content-type": "application/x-www-form-urlencoded",
        	"Accept-Encoding": "application/gzip",
        	"X-RapidAPI-Key": "your api key",
        	"X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
        }

        # Checks if every parameter of the API request works properly
        print("URL:", url)
        print("Payload:", payload)
        print("Headers:", headers)

        # Makes request and adds variable response.
        response = requests.post(url, data=payload, headers=headers)
        # Prints response status code. 
        print(response.status_code)
        # Gets the traslated text from the API response
        translated_text = response.json().get('data', {}).get('translations', [{}])[0].get('translatedText', '')
        # Prints the translated text
        print(translated_text)

        # Adds translated text variable to index.html as translated_text. Text variable too.
        return render_template('index.html', text=text, translated_text=translated_text)
    
    # Sets the text and translated_text empty
    return render_template('index.html', text='', translated_text='')

        

if __name__ == '__main__':
    app.run(debug=True)
