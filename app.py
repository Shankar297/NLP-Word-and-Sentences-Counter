from flask import Flask, render_template, request, url_for
from textblob import TextBlob

app = Flask('__name__')

@app.route('/', methods = ['GET'])
def home():
    return render_template('index.html')

@app.route('/predict',methods = ['POST'])
def predict():
    if request.method == 'POST':
        received_text = request.form['rawtext']
        text = TextBlob(received_text)
        number_of_tokens = len(text.words)
        len_of_sentences = len(text.sentences)
    return render_template('index.html',received_text = received_text, number_of_tokens = number_of_tokens, len_of_sentences=len_of_sentences)
    

if __name__ =='__main__':
    app.run(debug=True)