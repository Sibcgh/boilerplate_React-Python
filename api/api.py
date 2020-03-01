import time
from flask import Flask

app = Flask(__name__)

@app.route('/time')
def get_current_time():
        return {'time': time.time()}
    
@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for getting data about SciFi books.</p>'''
