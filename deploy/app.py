from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd
import math
model = pickle.load(open('model.pkl', 'rb'))

app = Flask(__name__)



@app.route('/')
def man():
    return render_template('home.html')

def rating_classification(pred):
    
    if pred >= 0.95:
        return 'Overwhelmingly Positive!'
    if pred >= 0.80:
        return 'Very Positive!'
    if pred < 0.20:
        return 'Overwhelmingly Negative!'
    
    if pred >= 0.7 and pred < 0.8:
        return 'Mostly Positive!'
    if pred >= 0.4 and pred < 0.7:
        return 'Mixed!'
    if pred >= 0.2 and pred < 0.4:
        return 'Mostly Negative!'
    
    

@app.route('/predict', methods=['POST'])
def home():
    data1 = request.form['a']
    data2 = request.form['b']
    data3 = request.form['c']
    data4 = request.form['d']
    data5 = request.form['e']
    data8 = request.form['j']
    data9 = request.form['i']
    data10 = request.form['k']
    data11 = request.form['l']
    data12 = request.form['m']
    data13 = request.form['u']
    discounted_price = int(data9) - int(data9) * float(data8)
    data = {
        'Genre': data1,
        'withDLC': data2,
        'isMature': data3,
        'Developer': data4,
        'Publisher': data5,
        'DiscountPercent': data8,
        'DiscountedPrice': discounted_price,
        'OriginalPrice': data9,
        'Languages': data13,
        'ReleaseYear': data10,
        'ReleaseMonth': data11,
        'ReleaseDay': data12,
    }
    df = pd.DataFrame(data=data, index=[0])
    pred = model.predict(df)
    classified = rating_classification(pred=pred)
    return render_template('after.html', data={'pred': np.round(pred, 3), 'class': classified})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)