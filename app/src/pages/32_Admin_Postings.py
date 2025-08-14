import os, requests, pandas as pd, streamlit as st
from modules.nav import SideBarLinks

# ---- Config ----
BASE_API = os.getenv("BASE_API", "http://web-api:4000")
COOP_API = f"{BASE_API}/api/coopPositions"
TIMEOUT = 10

st.set_page_config(page_title="Review Job Postings • Coopalytics", layout="wide", initial_sidebar_state="expanded")
SideBarLinks()
st.title("📝 Review Job Postings")

# ---- Helpers ----
def get_json(url):
    r = requests.get(url, timeout=TIMEOUT); r.raise_for_status(); return r.json()

def put_json(url, payload=None):
    r = requests.put(url, json=payload or {}, timeout=TIMEOUT); r.raise_for_status(); return r.json()

def delete_json(url):
    r = requests.delete(url, timeout=TIMEOUT); r.raise_for_status(); return r.json()

def flag_json(pos_id, value: int):
    r = requests.put(f"{COOP_API}/{pos_id}/flag/{value}", timeout=TIMEOUT); r.raise_for_status(); return r.json()

def unflag_json(pos_id):
    r = requests.put(f"{COOP_API}/{pos_id}/unflag", timeout=TIMEOUT); r.raise_for_status(); return r.json()

# ---- Load pending ----
try:
    pending = pd.DataFrame(get_json(f"{COOP_API}/pending"))
except Exception as e:
    st.error(f"Could not load pending positions: {e}")
    pending = pd.DataFrame()

# ---- Top bar (metrics + filters) ----
c1, c2, c3, c4 = st.columns([1,1,2,2])
total_pending = 0 if pending.empty else len(pending)
c1.metric("Pending", total_pending)
try:
    avg_pay = pd.DataFrame(get_json(f"{COOP_API}/industryAveragePay"))
    c2.metric("Industries", 0 if avg_pay.empty else len(avg_pay))
except Exception:
    c2.metric("Industries", "—")

# Filters
q = c3.text_input("Search title/company/location", "")
industry_filter = c4.selectbox(
    "Industry filter",
    ["All"] + (sorted(pending["industry"].dropna().unique().tolist()) if not pending.empty else ["All"]),
    index=0
)

# Apply filters
view = pending.copy()
if not view.empty:
    view["companyName"] = view.get("companyName", "")
    if q:
        ql = q.lower()
        view = view[
            view["title"].str.lower().str.contains(ql, na=False) |
            view["companyName"].astype(str).str.lower().str.contains(ql, na=False) |
            view["location"].str.lower().str.contains(ql, na=False)
        ]
    if industry_filter != "All":
        view = view[view["industry"] == industry_filter]

st.divider()

# ---- Table + actions ----
left, right = st.columns([2.2, 1])

with left:
    st.subheader("📌 Pending Positions")
    if view.empty:
        st.info("No pending positions match your filters.")
    else:
        show = view[[
            "coopPositionId","title","companyName","location","hourlyPay","deadline","startDate","endDate","industry"
        ]].sort_values(["deadline","coopPositionId"], ascending=[True, False])
        st.dataframe(show, use_container_width=True, height=420)

with right:
    st.subheader("⚡ Quick Actions")
    pos_id = st.number_input("Position ID", min_value=0, step=1, value=0)
    a1, a2 = st.columns(2)
    a3, a4 = st.columns(2)

    if a1.button("Approve", type="primary", use_container_width=True, disabled=pos_id<=0):
        try:
            put_json(f"{COOP_API}/{int(pos_id)}/approve")
            st.success(f"Approved {int(pos_id)}"); st.rerun()
        except Exception as e:
            st.error(f"Approve failed: {e}")

    if a2.button("Delete", use_container_width=True, disabled=pos_id<=0):
        try:
            delete_json(f"{COOP_API}/{int(pos_id)}")
            st.success(f"Deleted {int(pos_id)}"); st.rerun()
        except Exception as e:
            st.error(f"Delete failed: {e}")

    if a3.button("Flag", use_container_width=True, disabled=pos_id<=0):
        try:
            flag_json(int(pos_id), 1)
            st.success(f"Flagged {int(pos_id)}"); st.rerun()
        except Exception as e:
            st.error(f"Flag failed: {e}")

    if a4.button("Unflag", use_container_width=True, disabled=pos_id<=0):
        try:
            unflag_json(int(pos_id))
            st.success(f"Unflagged {int(pos_id)}"); st.rerun()
        except Exception as e:
            st.error(f"Unflag failed: {e}")

st.divider()

# ---- Industry averages (optional context) ----
st.subheader("💸 Industry Average Hourly Pay")
try:
    if 'avg_pay' not in locals():
        avg_pay = pd.DataFrame(get_json(f"{COOP_API}/industryAveragePay"))
    if avg_pay.empty:
        st.caption("No data.")
    else:
        st.dataframe(avg_pay.rename(columns={"industry":"Industry","industryAvgHourlyPay":"Avg $/hr"}), use_container_width=True)
except Exception as e:
    st.caption(f"Could not load averages: {e}")
