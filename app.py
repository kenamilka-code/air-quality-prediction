import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("air_quality_xgboost_model.pkl")

st.title("🌍 Air Quality Prediction")

st.write(
    "Enter the air-quality and environmental measurements below "
    "to predict carbon monoxide (CO) concentration."
)

pt08_s1 = st.number_input("CO Sensor Measurement (PT08.S1)", value=1000.0)

c6h6 = st.number_input("Benzene Concentration (mg/m³)", value=10.0)

pt08_s2 = st.number_input("NMHC Sensor Measurement (PT08.S2)", value=900.0)

nox = st.number_input("Nitrogen Oxides (NOx) (µg/m³)", value=150.0)

pt08_s3 = st.number_input("NOx Sensor Measurement (PT08.S3)", value=800.0)

no2 = st.number_input("Nitrogen Dioxide (NO2) (µg/m³)", value=100.0)

pt08_s4 = st.number_input("NO2 Sensor Measurement (PT08.S4)", value=1200.0)

pt08_s5 = st.number_input("Ozone Sensor Measurement (PT08.S5)", value=1000.0)

temperature = st.number_input("Temperature (°C)", value=20.0)

humidity = st.number_input("Relative Humidity (%)", value=50.0)

absolute_humidity = st.number_input("Absolute Humidity (g/m³)", value=1.0)

if st.button("Predict Air Quality"):

    input_data = pd.DataFrame([{
        "PT08.S1(CO)": pt08_s1,
        "C6H6(GT)": c6h6,
        "PT08.S2(NMHC)": pt08_s2,
        "NOx(GT)": nox,
        "PT08.S3(NOx)": pt08_s3,
        "NO2(GT)": no2,
        "PT08.S4(NO2)": pt08_s4,
        "PT08.S5(O3)": pt08_s5,
        "T": temperature,
        "RH": humidity,
        "AH": absolute_humidity
    }])

    # Make prediction
    prediction = model.predict(input_data)[0]

    # Display predicted CO
    st.metric(
        "Predicted CO Concentration",
        f"{prediction:.2f} mg/m³"
    )

    # Interpret the prediction
    if prediction < 2:
        st.success("🟢 Lower CO Concentration")
        st.write(
            "The predicted CO concentration is relatively low. "
            "This suggests lower pollution from carbon monoxide "
            "and conditions that are more likely to be suitable "
            "for normal daily activities."
        )

    elif prediction < 4:
        st.warning("🟡 Moderate CO Concentration")
        st.write(
            "The predicted CO concentration is moderate. "
            "This suggests that some carbon monoxide pollution "
            "may be present. Consider reducing prolonged exposure "
            "to major pollution sources such as heavy traffic."
        )

    else:
        st.error("🔴 High CO Concentration")
        st.write(
            "The predicted CO concentration is relatively high. "
            "This suggests elevated carbon monoxide pollution. "
            "Extra caution around major pollution sources is recommended."
        )

    st.caption(
        "The interpretation is based on simplified project-level "
        "CO ranges and is not an official health-standard classification."
    )
