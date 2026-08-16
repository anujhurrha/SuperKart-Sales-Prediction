
import streamlit as st
import requests

st.title("SuperKart Sales Prediction")

product_weight = st.number_input("Product Weight")
product_sugar_content = st.selectbox(
    "Product Sugar Content",
    ["Low Sugar", "Regular", "No Sugar"]
)

product_allocated_area = st.number_input("Product Allocated Area")

product_type = st.selectbox(
    "Product Type",
    [
        "Dairy",
        "Soft Drinks",
        "Meat",
        "Fruits and Vegetables",
        "Household",
        "Baking Goods",
        "Snack Foods",
        "Frozen Foods",
        "Breakfast",
        "Health and Hygiene",
        "Hard Drinks",
        "Canned",
        "Breads",
        "Starchy Foods",
        "Others",
        "Seafood"
    ]
)

product_mrp = st.number_input("Product MRP")

store_id = st.selectbox(
    "Store Id",
    [
        "OUT010","OUT013","OUT017","OUT018",
        "OUT019","OUT027","OUT035","OUT045",
        "OUT046","OUT049"
    ]
)

store_establishment_year = st.number_input("Store Establishment Year")

store_size = st.selectbox(
    "Store Size",
    ["Small", "Medium", "High"]
)

store_location_city_type = st.selectbox(
    "Store Location City Type",
    ["Tier 1", "Tier 2", "Tier 3"]
)

store_type = st.selectbox(
    "Store Type",
    [
        "Supermarket Type1",
        "Supermarket Type2",
        "Supermarket Type3",
        "Grocery Store"
    ]
)

if st.button("Predict Sales"):

    payload = {
        "Product_Weight": product_weight,
        "Product_Sugar_Content": product_sugar_content,
        "Product_Allocated_Area": product_allocated_area,
        "Product_Type": product_type,
        "Product_MRP": product_mrp,
        "Store_Id": store_id,
        "Store_Establishment_Year": store_establishment_year,
        "Store_Size": store_size,
        "Store_Location_City_Type": store_location_city_type,
        "Store_Type": store_type
    }

    response = requests.post(
        "http://127.0.0.1:5000/v1/predict",
        json=payload
    )

    st.success(response.json())
