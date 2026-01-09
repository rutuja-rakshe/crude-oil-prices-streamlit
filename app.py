import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ---------- Page Config ----------
st.set_page_config(
    page_title="Crude Oil Prices (1997–2025)",
    page_icon="🛢️",
    layout="wide"
)

# ---------- Title ----------
st.title("🛢️ Crude Oil Prices [1997–2025]")
st.write("Data about commodities influencing the global economy")

# ---------- Load Data ----------
@st.cache_data
def load_data():
    df = pd.read_csv("commodities_dataset.csv")
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    return df

df = load_data()

# ---------- Sidebar ----------
st.sidebar.header("Filters")

oil_columns = [col for col in df.columns if "Crude_Oil" in col]

selected_oil = st.sidebar.selectbox(
    "Select Crude Oil Type",
    oil_columns
)

# ---------- Data Preview ----------
st.subheader("📊 Dataset Preview")
st.dataframe(df.head(20), use_container_width=True)

# ---------- Line Chart ----------
st.subheader(f"📈 Price Trend: {selected_oil}")

fig, ax = plt.subplots(figsize=(12, 5))
ax.plot(df["Date"], df[selected_oil], linewidth=2)
ax.set_xlabel("Year")
ax.set_ylabel("Price")
ax.grid(True)

st.pyplot(fig)

# ---------- Statistics ----------
st.subheader("📌 Summary Statistics")

st.write(df[selected_oil].describe())

# ---------- Footer ----------
st.markdown("---")
st.caption("Source: Crude Oil Prices Dataset (1997–2025)")
