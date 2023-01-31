from flask import Flask, render_template , request
import pickle

app = Flask(__name__)
rf_model = pickle.load(open("rf_model.pkl", "rb"))

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST", "GET"])
def result():
    Item_Weight = float(request.form["Item_Weight"])
    Item_Fat_Content = int(request.form["Item_Fat_Content"])
    Item_Type = int(request.form["Item_Type"])
    Item_MRP = float(request.form["Item_MRP"])
    Outlet_Size = int(request.form["Outlet_Size"])
    Outlet_Location_Type = int(request.form["Outlet_Location_Type"])
    Outlet_Type	= int(request.form["Outlet_Type"])

    
    data = ([[Item_Weight, Item_Fat_Content , Item_Type, Item_MRP , Outlet_Size , Outlet_Location_Type , Outlet_Type]])

    prediction = rf_model.predict(data)

    return render_template('pred.html', prediction=prediction)


if __name__ == '__main__':
    app.run(debug=True)