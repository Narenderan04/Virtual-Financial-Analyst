import streamlit as st
import pandas as pd
import requests

# Title
st.title("Virtual Financial Analyst (VFA)")

# Input: API Key and Stock Symbol
api_key = st.text_input("Enter your Alpha Vantage API Key:")
stock_symbol = st.text_input("Enter Stock Symbol (e.g., AAPL, MSFT):")

# Fetch Data Button
if st.button("Fetch Data"):
    if not api_key or not stock_symbol:
        st.error("Please enter both the API Key and Stock Symbol.")
    else:
        # Fetch data from Alpha Vantage API
        url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock_symbol}&apikey={api_key}"
        response = requests.get(url)
        data = response.json()

        # Debug: Display the raw API response
        st.write("Raw API Response:", data)

        # Check for errors in response
        if "Error Message" in data:
            st.error("Invalid Stock Symbol or API Key.")
        elif "Time Series (Daily)" in data:
            # Parse the data
            time_series = data["Time Series (Daily)"]
            st.write("Time Series (Daily):", time_series)  # Debugging

            df = pd.DataFrame.from_dict(time_series, orient="index")
            df = df.rename(columns={
                "1. open": "Open",
                "2. high": "High",
                "3. low": "Low",
                "4. close": "Close",
                "5. volume": "Volume"
            })
            df.index = pd.to_datetime(df.index)  # Convert index to datetime
            df = df.sort_index()  # Sort by date

            # Display the data
            st.success("Data fetched successfully!")
            st.dataframe(df)  # Display as table
            st.line_chart(df[["Open", "High", "Low", "Close"]])  # Display as chart
        else:
            st.error("Unexpected response. Please try again later.")
