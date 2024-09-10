import streamlit as st
import numpy as np
import pickle

# Custom CSS for styling the app
page_bg_img = '''
<style>
body {
    background-color: #f0f2f6;
    font-family: 'Helvetica', sans-serif;
}
.stButton>button {
    background-color: #4CAF50;
    color: white;
    padding: 10px 20px;
    text-align: center;
    border-radius: 12px;
    border: none;
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
h1 {
    color: #4CAF50;
    text-align: center;
}
h2 {
    color: #4CAF50;
    text-align: center;
}
footer {
    text-align: center;
    padding: 10px 0;
    color: #888;
}
</style>
'''

# Inject the custom CSS into the Streamlit app
st.markdown(page_bg_img, unsafe_allow_html=True)

# Load the machine learning model
model_filename = 'gold.pkl'
with open(model_filename, 'rb') as file:
    model = pickle.load(file)

# Title of the app
st.title("Gold Price Prediction App")

# Subheader to explain the app
st.subheader("Enter the financial data to predict the Gold price (GLD)")

# Layout using columns for better structure
col1, col2 = st.columns(2)

with col1:
    spx = st.number_input('S&P 500 (SPX)', min_value=0.0, step=1.0, format="%.2f")
    uso = st.number_input('United States Oil Fund (USO)', min_value=0.0, step=1.0, format="%.2f")
    
with col2:
    slv = st.number_input('iShares Silver Trust (SLV)', min_value=0.0, step=1.0, format="%.2f")
    eur_usd = st.number_input('EUR/USD Exchange Rate', min_value=0.0, step=0.01, format="%.4f")

# Note about date exclusion
st.write("Note: The 'Date' field is excluded from predictions")

# Prediction button
if st.button('Predict'):
    # Prepare the input as a numpy array with features (excluding GLD)
    input_data = np.array([[spx, uso, slv, eur_usd]])
    
    # Make predictions using the loaded model
    prediction = model.predict(input_data)
    
    # Display the prediction result with styling
    st.markdown(f"<h2>Predicted Gold Price (GLD): ${prediction[0]:.2f}</h2>", unsafe_allow_html=True)

# Footer
st.markdown("<hr><footer>Developed by Your Name</footer>", unsafe_allow_html=True)
