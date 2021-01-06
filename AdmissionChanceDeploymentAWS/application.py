

from flask import Flask,request,render_template,jsonify
from flask_cors import CORS,cross_origin
import pickle
application = Flask(__name__)

@application.route('/',methods=['GET'])
@cross_origin()
def homepage():
    return render_template("index.html")

@application.route('/predict',methods=['POST'])
@cross_origin()

def index():
    if request.method == 'POST':
        try:
            gre_score  = float(request.form['gre_score'])
            toefl_score = float(request.form['toefl_score'])
            university_rating = float(request.form['university_rating'])
            sop = float(request.form['sop'])
            lor = float(request.form['lor'])
            cgpa = float(request.form['cgpa'])

            is_research = request.form['research']
            if (is_research == 'yes'):
                research=1
            else:
                research=0

            filename="FinalisedModel.pickle"
            loaded_model=pickle.load(open(filename, 'rb'))
            #scaler= pickle.load(open('ScalerModel.pickle', 'rb'))
            prediction=loaded_model.predict([[gre_score , toefl_score , university_rating , sop , lor , cgpa , research]])
            print("Prediction is",prediction)

            return render_template('result.html',prediction=round(10*prediction[0]))
        except Exception as e:
            print('The Exception message is:', e)
            return("Something is wrong",e)
    else:
        return render_template('index.html')


if __name__ == "__main__":
    application.run(debug=True)