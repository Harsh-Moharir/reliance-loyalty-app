import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(page_title="Reliance Loyalty Hub", layout="wide")

# -----------------------------
# CUSTOM CSS
# -----------------------------
st.markdown("""
<style>
.main {
    background-color: #0E1117;
}
.card {
    background: #1c1f26;
    padding: 20px;
    border-radius: 15px;
    border-left: 5px solid #ED1C24;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.4);
}
.card h2, .card h3, .card p {
    color: white;
}
.stButton>button {
    background-color: #ED1C24;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# HEADER
# -----------------------------
st.markdown("<h1 style='color:#ED1C24;'>Reliance Loyalty Hub</h1>", unsafe_allow_html=True)
st.caption("Your rewards, everywhere")

# -----------------------------
# SIDEBAR INPUT
# -----------------------------
st.sidebar.header("Customer Profile")

name = st.sidebar.text_input("Customer Name", "Harsh")
spend = st.sidebar.number_input("Monthly Spend (₹)", value=5000)
visits = st.sidebar.slider("Visits/month", 1, 20, 5)

# -----------------------------
# LOGIC
# -----------------------------
points = spend * 0.1 + visits * 20

def get_tier(points):
    if points > 2000:
        return "🏆 Platinum"
    elif points > 1000:
        return "🥇 Gold"
    else:
        return "🥈 Silver"

tier = get_tier(points)

# -----------------------------
# DASHBOARD CARDS
# -----------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div class="card">
    <h3>💳 Total Points</h3>
    <h2>{int(points)}</h2>
    <p>₹ Value: {int(points/10)}</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="card">
    <h3>🏆 Membership Tier</h3>
    <h2>{tier}</h2>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="card">
    <h3>📊 Visits</h3>
    <h2>{visits}</h2>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# -----------------------------
# PROGRESS + GAMIFICATION
# -----------------------------
st.subheader("📈 Progress to Next Tier")

progress = min(points / 2000, 1.0)
st.progress(progress)

if progress < 1:
    st.info(f"You're {int((1-progress)*100)}% away from Platinum 🚀")
else:
    st.success("You've reached the highest tier! 🎉")

# -----------------------------
# BRANDS
# -----------------------------
st.subheader("🏬 Shop Across Brands")
brands = ["Smart Bazaar", "Reliance Digital", "Trends", "JioMart"]
selected_brand = st.selectbox("Choose Brand", brands)

st.info(f"Showing offers for {selected_brand}")

# -----------------------------
# OFFERS
# -----------------------------
st.subheader("🎁 Offers for You")

if "Platinum" in tier:
    offers = ["20% Off Electronics", "Free Delivery", "VIP Sale Access"]
elif "Gold" in tier:
    offers = ["15% Off Fashion", "Bonus Points"]
else:
    offers = ["10% Cashback", "Welcome Coupon"]

for offer in offers:
    st.success(offer)

st.markdown("---")

# -----------------------------
# ADVANCED ANALYTICS
# -----------------------------
st.subheader("📊 Customer Insights")

col1, col2 = st.columns(2)

# Pie Chart
with col1:
    data1 = pd.DataFrame({
        "Category": ["Groceries", "Electronics", "Fashion", "Others"],
        "Spend": [
            spend * 0.4,
            spend * 0.25,
            spend * 0.2,
            spend * 0.15
        ]
    })

    fig1, ax1 = plt.subplots()
    ax1.pie(data1["Spend"], labels=data1["Category"], autopct='%1.1f%%')
    ax1.set_title("Spending Distribution")

    st.pyplot(fig1)

# Bar Chart
with col2:
    data2 = pd.DataFrame({
        "Metric": ["Spend Score", "Visit Score", "Bonus"],
        "Value": [
            spend / 100,
            visits * 10,
            50
        ]
    })

    fig2, ax2 = plt.subplots()
    ax2.bar(data2["Metric"], data2["Value"])
    ax2.set_title("Engagement Contribution")

    st.pyplot(fig2)

st.markdown("---")

# -----------------------------
# NEW: TREND GRAPH (VERY IMPORTANT)
# -----------------------------
st.subheader("📈 Monthly Spending Trend")

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
trend = np.random.randint(spend * 0.5, spend * 1.2, size=6)

fig3, ax3 = plt.subplots()
ax3.plot(months, trend, marker='o')
ax3.set_title("Spending Trend Over Time")

st.pyplot(fig3)

# -----------------------------
# SAVINGS
# -----------------------------
st.subheader("💰 Savings Summary")
st.metric("Total Savings", f"₹{int(points/10)}")

st.markdown("---")
st.caption("Reliance Loyalty Hub Prototype")