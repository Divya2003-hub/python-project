import streamlit as st

st.title("🏦 Divya ATM Web App (Fast Version)")

# Initialize balance if not already
if "balance" not in st.session_state:
    st.session_state.balance = 5000

st.write("### Current Balance:", st.session_state.balance)

# Deposit Section
st.subheader("💰 Deposit Money")
deposit = st.number_input("Enter deposit amount", min_value=0)
if st.button("Deposit"):
    st.session_state.balance += deposit
    st.success(f"✅ Deposit Successful! New Balance: {st.session_state.balance}")

st.write("---")

# Withdraw Section
st.subheader("💸 Withdraw Money")
withdraw = st.number_input("Enter withdraw amount", min_value=0)
if st.button("Withdraw"):
    if withdraw <= st.session_state.balance:
        st.session_state.balance -= withdraw
        st.success(f"✅ Withdraw Successful! Remaining Balance: {st.session_state.balance}")
    else:
        st.error("❌ Insufficient Balance")
