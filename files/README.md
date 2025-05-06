# Virtual Financial Analyst (VFA)

## Overview
The Virtual Financial Analyst (VFA) is a tool designed to:
- Provide rolling financial forecasts based on historical data.
- Automate variance detection and analysis for improved decision-making.

The system integrates with financial APIs, processes data, and presents insights via a Streamlit interface.

## Features
1. **API Integration**: Connects to Alpha Vantage to fetch financial data.
2. **Forecasting Module**: Implements rolling forecasts for financial predictions.
3. **Variance Analysis**: Automatically detects and explains financial variances.
4. **Streamlit Deployment**: Interactive web interface for user engagement.

## Installation
1. Clone or download the project to your computer.
2. Open a terminal and navigate to the project directory.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   streamlit run app/main.py
   ```

## Project Structure
```plaintext
Virtual Financial Analyst/
├── app/
│   ├── api_integration.py  # Fetches data from Alpha Vantage API
│   ├── forecasting.py       # Rolling financial forecasts
│   ├── variance_analysis.py # Variance detection and explanation
│   └── main.py              # Streamlit application entry point
├── requirements.txt         # Python dependencies
├── .gitignore               # Excludes unnecessary files
└── README.md                # Project documentation
```

## Dependencies
Install the dependencies from `requirements.txt`:
- `streamlit`
- `pandas`
- `numpy`
- `requests`

## License
This project is licensed under the MIT License.