import streamlit as st
from api_integration import APIIntegration
from forecasting import Forecasting
from variance_analysis import VarianceAnalysis

st.title("Virtual Financial Analyst (VFA)")

api_key = st.text_input("Enter your Alpha Vantage API Key", type="password")
symbol = st.text_input("Enter Stock Symbol (e.g., AAPL)")

if st.button("Fetch Data"):
    api = APIIntegration(api_key)
    try:
        data = api.fetch_time_series_data(symbol)
        st.write("Data fetched successfully!")
    except Exception as e:
        st.error(f"Error: {e}")

# Placeholder for additional modules and functionality