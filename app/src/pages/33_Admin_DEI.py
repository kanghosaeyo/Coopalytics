# Admin_DEI.py
import os, requests, pandas as pd, streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(page_title="DEI Metrics • Coopalytics", layout="wide")
SideBarLinks()
st.title("DEI Metrics")

BASE_API = os.getenv("BASE_API", "http://web-api:4000")

def fetch_json(path):
    r = requests.get(f"{BASE_API}{path}", timeout=10)
    r.raise_for_status()
    return r.json()

# Try a single summary endpoint first; fall back to per-dimension endpoints if needed
data = {}
try:
    # EXPECTED SHAPE:
    # {"gender":[{"label":"Female","count":120},...],
    #  "race":[{"label":"Asian","count":90},...],
    #  "nationality":[...],
    #  "disability":[...]}
    data = fetch_json("/api/dei/metrics")
except Exception:
    # Fallback to separate endpoints if your API exposes them
    for dim in ["gender", "race", "nationality", "disability"]:
        try:
            data[dim] = fetch_json(f"/api/dei/{dim}")
        except Exception:
            data[dim] = []

dims = [k for k,v in data.items() if isinstance(v, list) and len(v) > 0]
if not dims:
    st.info("No DEI data available.")
    st.stop()

# Selector
colA, colB = st.columns([2,1])
with colA:
    dim = st.selectbox("Select metric", dims, index=0)
with colB:
    show_table = st.toggle("Show table", value=False)

# Prep dataframe
df = pd.DataFrame(data[dim])
if "label" not in df.columns or "count" not in df.columns:
    st.error(f"Endpoint for '{dim}' must return items with 'label' and 'count'.")
    st.stop()

df = df.groupby("label", as_index=False)["count"].sum().sort_values("count", ascending=False)
total = int(df["count"].sum())

# KPIs
k1,k2,k3 = st.columns(3)
k1.metric("Total records", f"{total}")
k2.metric("Distinct categories", f"{df.shape[0]}")
coverage = 100 if total > 0 else 0
k3.metric("Coverage (%)", f"{coverage:.0f}%")

# Chart + (optional) table
st.subheader(dim.capitalize())
st.bar_chart(df.set_index("label")["count"])

if show_table:
    st.dataframe(df, use_container_width=True)