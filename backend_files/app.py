
import joblib
import pandas as pd
from flask import Flask, request, jsonify

superkart_api = Flask("SuperKart")

# Load the trained Random Forest model
model = joblib.load("random_forest_sales_model.pkl")


@superkart_api.get("/")
def home():
    return "Welcome to the SuperKart Sales Prediction API"


@superkart_api.post("/v1/predict")
def predict_sales():

    data = request.get_json()

    sample = {
        "Product_Weight": data["Product_Weight"],
        "Product_Sugar_Content": data["Product_Sugar_Content"],
        "Product_Allocated_Area": data["Product_Allocated_Area"],
        "Product_Type": data["Product_Type"],
        "Product_MRP": data["Product_MRP"],
        "Store_Id": data["Store_Id"],
        "Store_Establishment_Year": data["Store_Establishment_Year"],
        "Store_Size": data["Store_Size"],
        "Store_Location_City_Type": data["Store_Location_City_Type"],
        "Store_Type": data["Store_Type"],
    }

    input_df = pd.DataFrame([sample])

    prediction = model.predict(input_df)[0]

    return jsonify({"Predicted Sales": float(prediction)})


@superkart_api.post("/v1/predictbatch")
def predict_batch():

    file = request.files["file"]

    input_df = pd.read_csv(file)

    predictions = model.predict(input_df)

    return {
        str(i): round(float(pred), 2)
        for i, pred in enumerate(predictions)
    }


if __name__ == "__main__":
    superkart_api.run(debug=True)
