import os, requests, pandas as pd, streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(page_title="Admin • Coopalytics", layout="wide")
SideBarLinks()
st.title("System Admin Home Page")

BASE_API = os.getenv("BASE_API", "http://web-api:4000")
COOP_API = f"{BASE_API}/api/coopPositions"

st.header("Pending Co-op Positions (First 5)")
try:
    r = requests.get(f"{COOP_API}/pending", timeout=10)
    r.raise_for_status()
    df = pd.DataFrame(r.json())
    st.dataframe(df.head(5), use_container_width=True) if not df.empty else st.info("No pending positions")
except Exception as e:
    st.error(f"Could not load pending positions: {e}")