import os, requests, pandas as pd, streamlit as st

st.title("System Admin Home Page")

API_BASE = API_BASE = os.getenv("API_BASE", "http://api:4000/api")  # in Docker: http://api:4000/api

st.header("Pending Co-op Positions")

# Fetch pending
def fetch_pending():
    r = requests.get(f"{API_BASE}/coopPositions/pending", timeout=10)
    r.raise_for_status()
    return pd.DataFrame(r.json())

try:
    pending_df = fetch_pending()
    if not pending_df.empty:
        col1, col2 = st.columns([2,1])
        search = col1.text_input("Search title/company/location")
        industry = col2.selectbox(
            "Industry",
            ["All"] + sorted([x for x in pending_df["industry"].dropna().unique()])
        )

        filtered = pending_df.copy()
        if search:
            s = search.lower()
            filtered = filtered[
                filtered["title"].str.lower().str.contains(s)
                | filtered["companyName"].fillna("").str.lower().str.contains(s)
                | filtered["location"].fillna("").str.lower().str.contains(s)
            ]
        if industry != "All":
            filtered = filtered[filtered["industry"] == industry]

        st.dataframe(
            filtered[["coopPositionId","title","companyName","location","hourlyPay","deadline","startDate","endDate","industry"]],
            use_container_width=True
        )

        st.subheader("Quick Actions")
        colA, colB, colC = st.columns([2,1,1])
        pos_id = colA.number_input("Select Position ID", step=1, min_value=1)
        if colB.button("Approve"):
            try:
                r = requests.put(f"{API_BASE}/coopPositions/{int(pos_id)}/approve", timeout=10)
                r.raise_for_status()
                st.success(f"Approved position {int(pos_id)}")
                st.rerun()
            except Exception as e:
                st.error(f"Approve failed: {e}")
        if colC.button("Delete (pending only)"):
            try:
                r = requests.delete(f"{API_BASE}/coopPositions/{int(pos_id)}", timeout=10)
                if r.status_code == 200:
                    st.success(f"Deleted position {int(pos_id)}")
                else:
                    st.warning(r.json().get("error","Delete failed"))
                st.rerun()
            except Exception as e:
                st.error(f"Delete failed: {e}")
    else:
        st.info("No pending positions 🎉")
except Exception as e:
    st.error(f"Could not load pending positions: {e}")

st.divider()

st.header("Employer Job Counts")

try:
    r = requests.get(f"{API_BASE}/coopPositions/employerJobCounts", timeout=10)
    r.raise_for_status()
    employers_df = pd.DataFrame(r.json())
    if not employers_df.empty:
        st.dataframe(
            employers_df[["companyName","firstName","lastName","numJobs"]],
            use_container_width=True
        )
    else:
        st.info("No employers found.")
except Exception as e:
    st.error(f"Could not load employer counts: {e}")