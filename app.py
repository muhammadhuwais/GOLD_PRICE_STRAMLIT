import streamlit as st
import numpy as np
import pickle

# Load the machine learning model
model_filename = 'gold.pkl'
with open(model_filename, 'rb') as file:
    model = pickle.load(file)

# Title of the app
st.title("Gold Price Prediction App")

# Subheader to explain the app
st.subheader("Enter the financial data to predict the Gold price (GLD)")

# Input fields for the user to enter values based on the features in the dataset
spx = st.number_input('S&P 500 (SPX)', min_value=0.0, step=1.0, format="%.2f")
uso = st.number_input('United States Oil Fund (USO)', min_value=0.0, step=1.0, format="%.2f")
slv = st.number_input('iShares Silver Trust (SLV)', min_value=0.0, step=1.0, format="%.2f")
eur_usd = st.number_input('EUR/USD Exchange Rate', min_value=0.0, step=0.01, format="%.4f")

# Date is not used in prediction, so we skip it in input
st.write("Note: The 'Date' field is excluded from predictions")

# Prediction button
if st.button('Predict'):
    # Prepare the input as a numpy array with features (excluding GLD)
    input_data = np.array([[spx, uso, slv, eur_usd]])
    
    # Make predictions using the loaded model
    prediction = model.predict(input_data)
    
    # Display the prediction result
    st.write(f"Predicted Gold Price (GLD): ${prediction[0]:.2f}")

# Footer
st.markdown("<hr><footer style='text-align: center;'>Developed by Your Name</footer>", unsafe_allow_html=True)
