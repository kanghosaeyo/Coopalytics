import os, requests, pandas as pd, streamlit as st

st.title("System Admin Home Page")
st.write("Hi")

API_BASE = os.getenv("API_BASE", "http://api:4000/api")  # in Docker: http://api:4000/api

st.header("Pending Co-op Positions (First 5)")

try:
    r = requests.get(f"{API_BASE}/coopPositions/pending", timeout=10)
    r.raise_for_status()
    df = pd.DataFrame(r.json())
    if not df.empty:
        st.dataframe(df.head(5), use_container_width=True)  # only show first 5 rows
    else:
        st.info("No pending positions 🎉")
except Exception as e:
    st.error(f"Could not load pending positions: {e}")