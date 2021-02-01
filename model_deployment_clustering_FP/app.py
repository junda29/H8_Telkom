import flask
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler

model = pickle.load(open('model/model_clustering_FP.pkl', 'rb'))

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
    final_features = [np.array(int_features)]
    prediction = model.predict(StandardScaler().fit_transform(final_features))

    output = {0: 'Cluster 1', 1: 'Cluster 2', 2: 'Cluster 3', 3: 'Cluster 4',4: 'Cluster 5'}

    return flask.render_template('main.html',
    prediction_text=' {} '.format(output[prediction[0]]))

if __name__ == '__main__':
    app.run()
