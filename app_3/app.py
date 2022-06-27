from flask import Flask, render_template, request
app = Flask(__name__)
from joblib import load
import numpy as np

def load_model():
    path = 'app_3/static/house_pricing_model.pk'
    model_dict = load(path)
    return model_dict

@app.route('/',methods=['GET','POST'])
def index():
    md = load_model()

    cities = md['cities']
    restype = md['resident_types']
    scaler = md['scaler']
    city_encoder = md['city_encoder']
    resident_type_encoder = md['resident_type_encoder']
    model = md['model']
    errors = ''
    price = None
    if request.method == 'POST':
        city = request.form.get('city')
        rt = request.form.get('rt')
        beds = request.form.get('beds')
        baths = request.form.get('baths')
        size = request.form.get('sqft')
        if beds.isnumeric() and baths.isnumeric() and size.isnumeric():
            beds = int(beds)
            baths = int(baths)
            size = int(size)
            city_encoded = city_encoder.transform([[city]]).toarray()
            rt_encoded = resident_type_encoder.transform([[rt]]).toarray()
            X = np.array([[beds, baths, size]])
            X = np.concatenate((X, city_encoded, rt_encoded), axis=1)   
            X = scaler.transform(X)
            price = model.predict(X)
            price = int(price[0])
        else:
            errors = 'Please enter valid numbers for beds, baths, and size' 
    return render_template('index.html',cities = cities,res_types = restype, errors = errors, price=price)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 