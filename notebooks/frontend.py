
import streamlit as st
import requests

st.title("SuperKart Sales Prediction")

product_weight = st.number_input("Product Weight", value=12.66)

product_sugar_content = st.selectbox(
    "Product Sugar Content",
    ["Low Sugar", "Regular", "No Sugar"]
)

product_allocated_area = st.number_input(
    "Product Allocated Area",
    value=0.027
)

product_mrp = st.number_input("Product MRP", value=117.08)

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

product_id_char = st.selectbox(
    "Product ID Category",
    ["FD", "DR", "NC"]
)

store_age_years = st.number_input(
    "Store Age (Years)",
    min_value=0,
    value=16
)

product_type_category = st.selectbox(
    "Product Type Category",
    ["Perishables", "Non Perishables"]
)

if st.button("Predict Sales"):

    payload = {
        "Product_Weight": product_weight,
        "Product_Sugar_Content": product_sugar_content,
        "Product_Allocated_Area": product_allocated_area,
        "Product_MRP": product_mrp,
        "Store_Size": store_size,
        "Store_Location_City_Type": store_location_city_type,
        "Store_Type": store_type,
        "Product_Id_char": product_id_char,
        "Store_Age_Years": store_age_years,
        "Product_Type_Category": product_type_category
    }

    response = requests.post(
        "http://127.0.0.1:5000/v1/predict",
        json=payload
    )

    if response.status_code == 200:
        st.success(response.json())
    else:
        st.error(
            f"Prediction failed: {response.status_code} - {response.text}"
        )
