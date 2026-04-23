import streamlit as st
import pandas as pd
import numpy as np
from src.inventory import inventory_policy

# ---------- Page Config ----------
st.set_page_config(
    page_title="Retail Forecast & Inventory",
    page_icon="🛒",
    layout="wide"
)

# ---------- Data Loading ----------
@st.cache_data
def load_data():
    # Load historical data for analytics
    df = pd.read_csv("data/retail_timeseries.csv", parse_dates=["date"], dayfirst=True)
    return df

df_raw = load_data()

# ---------- Sidebar Filters ----------
st.sidebar.header("🔍 Dashboard Filters")

# Store Slicer
stores = sorted(df_raw['store_id'].unique())
selected_store = st.sidebar.selectbox("🏬 Select Store", ["All"] + list(stores))

# Product Slicer
items = sorted(df_raw['item_id'].unique())
selected_item = st.sidebar.selectbox("🍎 Select Product (SKU)", ["All"] + list(items))

# Year Slicer
years = sorted(df_raw['date'].dt.year.unique())
selected_year = st.sidebar.selectbox("📅 Select Year", ["All"] + [int(y) for y in years])

# Month Slicer
months = list(range(1, 13))
selected_month = st.sidebar.selectbox("🗓️ Select Month", ["All"] + months)

# Apply Filters
df_filtered = df_raw.copy()
if selected_store != "All":
    df_filtered = df_filtered[df_filtered['store_id'] == selected_store]
if selected_item != "All":
    df_filtered = df_filtered[df_filtered['item_id'] == selected_item]
if selected_year != "All":
    df_filtered = df_filtered[df_filtered['date'].dt.year == selected_year]
if selected_month != "All":
    df_filtered = df_filtered[df_filtered['date'].dt.month == selected_month]

# ---------- Main Header ----------
st.markdown(
    """
    <h1 style='text-align: center;'>🛒 Retail Performance & Inventory Dashboard</h1>
    <hr>
    """,
    unsafe_allow_html=True
)

# ---------- Top KPI Row ----------
st.subheader("📈 Key Performance Indicators")
col_kpi1, col_kpi2, col_kpi3, col_kpi4 = st.columns(4)

total_sales = df_filtered['qty_sold'].sum()
avg_daily_sales = round(df_filtered['qty_sold'].mean(), 2) if not df_filtered.empty else 0
best_selling_item = df_filtered.groupby('item_id')['qty_sold'].sum().idxmax() if not df_filtered.empty else "N/A"
promo_intensity = round((df_filtered['on_promo'].sum() / len(df_filtered)) * 100, 1) if len(df_filtered) > 0 else 0

with col_kpi1:
    st.metric("Total Units Sold", f"{total_sales:,}")
with col_kpi2:
    st.metric("Top Product", best_selling_item)
with col_kpi3:
    st.metric("Avg Daily Demand", avg_daily_sales)
with col_kpi4:
    st.metric("Promo Sales %", f"{promo_intensity}%")

st.markdown("---")

# ---------- Sales Trend Section ----------
st.subheader("📊 Product Sales Trend")
if not df_filtered.empty:
    trend_data = df_filtered.groupby('date')['qty_sold'].sum().reset_index()
    st.line_chart(data=trend_data, x='date', y='qty_sold', use_container_width=True)
else:
    st.warning("No data available for the selected filters.")

st.markdown("---")

# ---------- Inventory Replenishment Section ----------
st.subheader("📦 Inventory Replenishment Tool")
st.info("Selection-based replenishment for specific Store-Item combinations.")

col_inv1, col_inv2 = st.columns(2)

with col_inv1:
    # Use specific selection for ROP logic (cannot be "All")
    target_store = st.selectbox("Pick Store for Order", stores)
    target_item = st.selectbox("Pick Item for Order", items)
    on_hand = st.number_input("🧺 Current On-hand Inventory", min_value=0, value=20)

with col_inv2:
    service_level = st.slider("🎯 Desired Service Level (%)", 80, 99, 95)
    lead_time = st.number_input("🚚 Lead Time (days)", min_value=1, value=2)

if st.button("🛍️ Get Replenishment Recommendation"):
    # Simulated forecast for selected item/store
    avg_demand = df_raw[(df_raw['store_id']==target_store) & (df_raw['item_id']==target_item)]['qty_sold'].mean()
    if np.isnan(avg_demand): avg_demand = 10
    
    forecast = np.full(30, avg_demand) + np.random.normal(0, 2, 30)
    resid_std = 3.5 

    result = inventory_policy(
        forecast=forecast,
        resid_std=resid_std,
        on_hand=on_hand,
        lead_time=lead_time,
        service_level=(service_level / 100.0)
    )

    st.markdown("### 📋 Order Summary")
    c1, c2 = st.columns(2)
    with c1:
        st.success(f"**Reorder Point (ROP):** {round(float(result['ROP']), 2)} units")
    with c2:
        st.info(f"**Suggested Order Qty:** {int(result['order_qty'])} units")

# ---------- Footer ----------
st.markdown(
    """
    <hr>
    <p style='text-align:center; font-size:14px;'>
    🥦 Grocery Retail • 📦 Inventory Optimization • 📈 Demand Forecasting
    </p>
    """,
    unsafe_allow_html=True
)
