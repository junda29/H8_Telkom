import flask
import numpy as np
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

model = pickle.load(open('model/model_regresiPoly_NPS_FP.pkl', 'rb'))

app = flask.Flask(__name__, template_folder='template')

@app.route('/')
def main():
    return(flask.render_template('main.html'))

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in flask.request.form.values()]
    transformer = PolynomialFeatures(include_bias=False)
    int_features2 = (transformer.fit(int_features))
    final_features = [transformer.transform(int_features)]
    #final_features = [np.array(int_features2)]
    prediction = model.predict([final_features])

    #output = {'Nilai Y anda adalah :'}
    #output = {0: 'Cluster 1', 1: 'Cluster 2', 2: 'Cluster 3', 3: 'Cluster 4',4: 'Cluster 5'}

    return flask.render_template('main.html', int_features2)
    #return flask.render_template('main.html',
    #prediction_text=' Prediksi Nilai NPS Pelatihan: {} '.format([prediction[0]]))

    #prediction_text=' {} '.format(output[prediction[0]] ))
if __name__ == '__main__':
    app.run()