from flask import Flask, render_template, request          
import pickle
import numpy as np

app=Flask(__name__)               

@app.route('/')   
def hello():
    return render_template('social.html')       

@app.route('/prediction', methods=['POST'])     
def predict():
    
        gend=request.form['Gender']
        if gend=='Male':
            Gender=1
        elif gend=='Female':
            Gender=0
        Age=int(request.form['Age'])
        EstimatedSalary=int(request.form['EstimatedSalary'])
        print(Gender,Age,EstimatedSalary)
        social_model=pickle.load(open('socialnew.pkl','rb'))
        print(Gender,Age,EstimatedSalary)
        feature=np.array([[Gender,Age,EstimatedSalary]])
        print(feature)
        social=social_model.predict(feature)
        print(social)
        print(social[0])
        
        return render_template('prediction.html',predicted=social[0])

if __name__=='__main__':
    app.run()
