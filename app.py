import streamlit as st

st.title("🏦 Divya ATM Web App")

# ஆரம்ப balance
if "balance" not in st.session_state:
    st.session_state.balance = 5000

st.write("### Current Balance:", st.session_state.balance)

st.write("---")

# Deposit section
st.subheader("💰 Deposit Money")
deposit = st.number_input("Enter deposit amount", min_value=0, step=100)

if st.button("Deposit"):
    st.session_state.balance += deposit
    st.success(f"✅ Deposit Successful! New Balance: {st.session_state.balance}")

st.write("---")

# Withdraw section
st.subheader("💸 Withdraw Money")
withdraw = st.number_input("Enter withdraw amount", min_value=0, step=100)

if st.button("Withdraw"):
    if withdraw <= st.session_state.balance:
        st.session_state.balance -= withdraw
        st.success(f"✅ Withdraw Successful! Remaining Balance: {st.session_state.balance}")
    else:
        st.error("❌ Insufficient Balance!")

st.write("---")

# Exit button
if st.button("Exit"):
    st.warning("👋 Thank you for using Divya ATM!")
