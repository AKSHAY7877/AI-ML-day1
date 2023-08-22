from nltk.chat.util import Chat

q1 = r'(.*)your name (.*)company (.*)'.lower()
a1 = ['my name is chatchat', 'I am chatchat']
q2 = r'kya aaj kuch acha hoga'
a2 = ['haan', 'mujhe kya pta', 'mein kyo batau']
qa_pair = [
    [q1,a1],
    [q2,a2],
]
cb = Chat(qa_pair)

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    text = 'hi'
    global cb
    if request.args.get('q') != None:
        que = request.args.get('q')
        text = cb.respond(que)
        if text == None:
            text = 'unknown'
    return render_template('chatbot.html', resp=text)

@app.route('/new')
def new():
    return "<html><h1>Awesome</h1></html>"




app.run(debug = True)