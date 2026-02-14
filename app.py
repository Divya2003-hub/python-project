import streamlit as st

st.title("🏦 Divya ATM Web App (Upgraded)")

# --- Multi-user data ---
if "users" not in st.session_state:
    st.session_state.users = {
        "divya": {"password": "1234", "balance": 5000, "history": []},
        "test": {"password": "0000", "balance": 3000, "history": []}
    }

# --- Login ---
if "logged_in_user" not in st.session_state:
    st.session_state.logged_in_user = None

if st.session_state.logged_in_user is None:
    st.subheader("🔑 Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        if username in st.session_state.users and st.session_state.users[username]["password"] == password:
            st.session_state.logged_in_user = username
            st.success(f"✅ Welcome {username}!")
        else:
            st.error("❌ Invalid username or password")
else:
    user = st.session_state.logged_in_user
    st.subheader(f"👋 Hello {user}")
    st.write("### Current Balance:", st.session_state.users[user]["balance"])
    
    # --- Deposit ---
    st.subheader("💰 Deposit Money")
    deposit = st.number_input("Enter deposit amount", min_value=0, step=100)
    if st.button("Deposit"):
        if deposit > 0:
            st.session_state.users[user]["balance"] += deposit
            st.session_state.users[user]["history"].append(f"Deposited: {deposit}")
            st.success(f"✅ Deposit Successful! New Balance: {st.session_state.users[user]['balance']}")

    st.write("---")
    
    # --- Withdraw ---
    st.subheader("💸 Withdraw Money")
    withdraw = st.number_input("Enter withdraw amount", min_value=0, step=100)
    if st.button("Withdraw"):
        if withdraw <= st.session_state.users[user]["balance"] and withdraw > 0:
            st.session_state.users[user]["balance"] -= withdraw
            st.session_state.users[user]["history"].append(f"Withdrew: {withdraw}")
            st.success(f"✅ Withdraw Successful! Remaining Balance: {st.session_state.users[user]['balance']}")
        elif withdraw > st.session_state.users[user]["balance"]:
            st.error("❌ Insufficient Balance!")

    st.write("---")
    
    # --- Transaction History ---
    st.subheader("📜 Transaction History")
    history = st.session_state.users[user]["history"]
    if history:
        for h in history:
            st.write(h)
    else:
        st.write("No transactions yet.")

    st.write("---")
    
    # --- Logout ---
    if st.button("Logout"):
        st.session_state.logged_in_user = None
        st.success("👋 Logged out successfully!")
