from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd
model = pickle.load(open('../model.pkl', 'rb'))
fine_tuned_model = pickle.load(open('../fine_tuned_model.pkl', 'rb'))

app = Flask(__name__)



@app.route('/')
def man():
    return render_template('home.html')

def rating_classification(total_reviews, pred):
    tt_reviews = int(total_reviews)
    if tt_reviews >= 500:
        if pred >= 0.95:
            return 'Overwhelmingly Positive!'
        if pred >= 0.80:
            return 'Very Positive!'
        if pred < 0.20:
            return 'Overwhelmingly Negative!'
    if tt_reviews >= 50 and tt_reviews < 500:
        if pred < 0.20:
            return 'Very Negative!'
        if pred >= 0.8:
            return 'Very Positive!'
    if tt_reviews < 0.50:
        if pred >= 0.80:
            return 'Postitive!'
        if pred < 0.20:
            return 'Negative!'
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
    data6 = request.form['f']
    data7 = request.form['g']
    data8 = request.form['j']
    data9 = request.form['i']
    data10 = request.form['k']
    data11 = request.form['l']
    data12 = request.form['m']
    discounted_price = int(data9) - int(data9) * float(data8)
    negative_reviews = int(data7) - int(data6)
    data = {
        'Genre': data1,
        'withDLC': data2,
        'isMature': data3,
        'Developer': data4,
        'Publisher': data5,
        'PositiveReviews': data6,
        'TotalReviews': data7,
        'NegativeReviews': negative_reviews,
        'DiscountPercent': data8,
        'DiscountedPrice': discounted_price,
        'OriginalPrice': data9,
        'ReleaseYear': data10,
        'ReleaseMonth': data11,
        'ReleaseDay': data12,
    }
    df = pd.DataFrame(data=data, index=[0])
    pred = model.predict(df)
    ft_pred = fine_tuned_model.predict(df)
    classified = rating_classification(pred=pred, total_reviews=data7)
    return render_template('after.html', data={'pred': pred, 'class': classified, 'ft_pred': ft_pred})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)














