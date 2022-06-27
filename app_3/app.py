from flask import Flask, render_template
app = Flask(__name__)
from joblib import load

def load_model():
    path = 'app_3/static/house_pricing_model.pk'
    model_dict = load(path)
    return model_dict

@app.route('/')
def index():
    md = load_model()
    return render_template('index.html')

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 