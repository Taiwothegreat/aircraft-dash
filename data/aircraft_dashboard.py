import pandas as pd
import streamlit as st
from sklearn.linear_model import LinearRegression

data = {
    "airlines": ["alaska airlines", "allegiant air", "american airlines", "avelo airlines", "breeze airways"],
    "Year": [1932, 1997, 1926, 1987, 2018],
    "avg_pre_owned_price": [5000, 6000, 7000, 8000, 10000]
}

df = pd.DataFrame(data)

X = df[['Year', 'avg_pre_owned_price']]
y = df['Year'] * df['avg_pre_owned_price']

model = LinearRegression()
model.fit(X, y)

def convert_currency(total_cost, currency):
    exchange_rates = {
        "USD": 1,
        "GBP": 0.72,
        "CAD": 1.2,
        "AUD": 1.3,
    }
    return total_cost * exchange_rates[currency]

currencies = {
    "USD": {"country": "United States", "logo": "🇺🇸"},
    "GBP": {"country": "United Kingdom", "logo": "🇬🇧"},
    "CAD": {"country": "Canada", "logo": "🇨🇦"},
    "AUD": {"country": "Australia", "logo": "🇦🇺"},
}
def main():
    st.title("Flight Cost per nm Calculator")
    
    # Currency selection
    selected_currency = st.selectbox("Select currency:", list(currencies.keys()), format_func=lambda currency: f"{currency} {currencies[currency]['logo']}")
    
    # Distance input
    distance = st.number_input("Distance in nm:", value=1000)
    
    # Age and average pre-owned price input
    age = st.number_input("Year:", value=2000)
    avg_pre_owned_price = st.number_input("Average Pre-owned Price:", value=5000)
    
    # Calculate total cost, convert currency and cost per nm
    total_cost = age * avg_pre_owned_price
    converted_cost = convert_currency(total_cost, selected_currency)
    cost_per_nm = converted_cost / distance
    
    # Display results
    st.subheader("Results")
    st.write(f"Total Cost: {converted_cost} {selected_currency} {currencies[selected_currency]['logo']}")
    st.write(f"Cost per nm: {cost_per_nm} {selected_currency} {currencies[selected_currency]['logo']}")

if __name__ == "__main__":
    main()
