import streamlit as st
import numpy as np
import pickle

# Custom CSS for background image and other styling
page_bg_img = '''
<style>
body {
    background-image: url("https://example.com/your_background_image.jpg");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
    font-family: 'Arial', sans-serif;
}
.stApp {
    background: rgba(255, 255, 255, 0.9);  /* Adding a white transparent overlay for readability */
    border-radius: 15px;
    padding: 20px;
}
.stButton>button {
    background-color: #008CBA;
    color: white;
    padding: 10px 20px;
    text-align: center;
    border-radius: 12px;
    border: none;
    font-size: 16px;
}
.stNumberInput>div>input {
    padding: 10px;
    border-radius: 8px;
    border: 1px solid #ccc;
}
.stNumberInput>div>label {
    font-weight: bold;
    color: #333;
}
h1, h2 {
    color: #333;
    text-align: center;
}
footer {
    text-align: center;
    padding: 10px 0;
    color: #888;
    font-size: 14px;
}
</style>
'''

# Inject the custom CSS into the Streamlit app
st.markdown(page_bg_img, unsafe_allow_html=True)

# Load the machine learning model
model_filename = r'gold.pkl'
with open(model_filename, 'rb') as file:
    model = pickle.load(file)

# Set a fixed USD to INR exchange rate (you can update this value)
usd_to_inr = 82.5  # Example: 1 USD = 82.5 INR

# Title of the app
st.title("💰 Gold Price Prediction App (INR)")

# Subheader to explain the app
st.subheader("📊 Enter the financial data to predict the Gold price (GLD) in Indian Rupees (INR)")

# Layout for better organization
col1, col2 = st.columns(2)

# Input fields for the user to enter values based on the features in the dataset
with col1:
    spx = st.number_input('S&P 500 (SPX)', min_value=0.0, step=1.0, format="%.2f")
    uso = st.number_input('United States Oil Fund (USO)', min_value=0.0, step=1.0, format="%.2f")
    
with col2:
    slv = st.number_input('iShares Silver Trust (SLV)', min_value=0.0, step=1.0, format="%.2f")
    eur_usd = st.number_input('EUR/USD Exchange Rate', min_value=0.0, step=0.01, format="%.4f")

# Date is not used in prediction, so we skip it in input
st.write("📅 Note: The 'Date' field is excluded from predictions")

# Prediction button with a custom look
if st.button('🔍 Predict'):
    # Prepare the input as a numpy array with features (excluding GLD)
    input_data = np.array([[spx, uso, slv, eur_usd]])
    
    # Make predictions using the loaded model
    prediction_usd = model.predict(input_data)[0]  # Prediction in USD
    
    # Convert prediction to INR
    prediction_inr = prediction_usd * usd_to_inr
    
    # Display the prediction result with some formatting
    st.success(f"💵 Predicted Gold Price (GLD) in USD: ${prediction_usd:.2f}")
    st.success(f"₹ Predicted Gold Price (GLD) in INR: ₹{prediction_inr:.2f}")

# Footer with custom styling
st.markdown("<hr><footer>Developed by Your Name</footer>", unsafe_allow_html=True)
