from flask import request,Flask,render_template
import pickle

# app = Flask(__name__,template_folder='~/Desktop/ML_study/salary_pred/templates')
app = Flask(__name__,template_folder='templates')

"www.facebook.com"
@app.route("/",methods=["GET","POST"])
def first_function():
    # return "Hello Mohamed"
    return render_template("index.html")

"www.facebook.com/get_label"
@app.route("/get_label",methods=["GET","POST"])
def get_label():
    name = request.args.get("name")
    age = int(request.args.get("age"))
    workclass = int(request.args.get("workclass"))
    education = int(request.args.get("education"))
    gender = int(request.args.get("gender"))
    mstatus = int(request.args.get("mstatus"))
    occupation = int(request.args.get("occupation"))

    # capitalgain = int(request.args.get("capitalgain"))
    # capitalloss = int(request.args.get("capitalloss"))

    relationship = int(request.args.get("relationship"))
    race = int(request.args.get("race"))
    country = int(request.args.get("country"))
    hoursperweek = int(request.args.get("hoursperweek"))

    try:
        capitalgain = int(request.args.get("capitalgain"))
    except ValueError:
        capitalgain=0

    try:
        capitalloss = int(request.args.get("capitalloss"))
    except ValueError:
        capitalloss=0

    model = pickle.load(open("training_model_downsampling_random_forest.pk",'rb'))
    result = model.predict([[age,workclass,education,mstatus,occupation,relationship,race,gender,capitalgain,capitalloss,hoursperweek,country]])[0]
    if result == 0:
        result=" <= 50K"
    else:
        result=" > 50K"
        # $('div#printdirec').text('tttt');
    return render_template('result.html',name=name,result=result)



if __name__ == '__main__':
    app.run(host="127.0.0.1",port=9090)
