import streamlit as st

st.set_page_config(page_title="HUNT: Profit Predictor", page_icon="🎯")

st.title("🏹 HUNT: Order Analyzer")
st.subheader("Lalamove KL Profit Scalper")

# --- INPUTS ---
col1, col2 = st.columns(2)
with col1:
    fare = st.number_input("Order Fare (RM)", min_value=0.0, value=32.0)
    km = st.number_input("Distance (KM)", min_value=0.0, value=20.0)
with col2:
    mins = st.number_input("Estimated Mins", min_value=1, value=60)
    vehicle = st.selectbox("Vehicle", ["Motorcycle", "Car"])

# --- LOGIC ---
commission = 0.16
cost_per_km = 0.15 if vehicle == "Motorcycle" else 0.25
    
net_fare = fare * (1 - commission)
fuel_total = km * cost_per_km
profit = net_fare - fuel_total
hourly_rate = profit / (mins / 60)

# --- RESULTS ---
st.divider()
st.metric(label="Net Take-Home Profit", value=f"RM {profit:.2f}")
st.write(f"**Hourly Rate:** RM {hourly_rate:.2f}/hr")

if hourly_rate >= 30:
    st.success("🔥 STRONG BUY: High Profit Trade")
elif hourly_rate >= 20:
    st.info("✅ BUY: Solid Daily Trade")
else:
    st.error("❌ AVOID: Low ROI / Bad Spread")

st.caption("Calculation: (Fare - 16%) - (KM * Fuel) / Time")