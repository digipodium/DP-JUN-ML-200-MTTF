from flask import Flask, render_template, request
from joblib import load

def load_model():
    return load('static/salary_reg.joblib')

def predict_salary(exp):
    if isinstance(exp, str):
        exp = float(exp)
    model = load_model()
    out = model.predict([[exp]])
    return f'Rs. {int(out[0])}'

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        exp = request.form.get('exp')
        salary = predict_salary(exp)
        return render_template('index.html', salary=salary)
    return render_template('index.html')

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 