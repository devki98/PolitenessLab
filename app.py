#app.py

from flask import Flask, request #import main Flask class and request object
app = Flask(__name__) #create the Flask app
from vaderSentiment import analyse_sentence

@app.route('/query-example')
def query_example():
    sentence = request.args.get('sentence') #if key doesn't exist, returns None
    #sentiment = request.args['sentiment'] #if key doesn't exist, returns a 400, bad request error
    #website = request.args.get('website')
    sent = analyse_sentence(sentence)

    return '''<h1>The sentence value is: {}</h1>

              <h1>The website value is: {}'''.format(sentence)

@app.route('/form-example', methods=['GET', 'POST']) #allow both GET and POST requests
def form_example():
    if request.method == 'POST':  #this block is only entered when the form is submitted
        sentence = request.form.get('sentence')
        #sentiment = request.form['sentiment']
        sent = analyse_sentence(sentence)
        return '''<h1>The sentence value is: {}</h1>
                  <h1>The sentiment value is: {}</h1>'''.format(sentence, sent )

    return '''<form method="POST">
                  Sentence: <input type="text" name="sentence"><br>
                  <input type="submit" value="Submit"><br>
              </form>'''


if __name__ == '__main__':
    app.run(debug=True, port=5000) #run app in debug mode on port 5000
