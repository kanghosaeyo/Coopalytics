import logging
import streamlit as st
import requests
import pandas as pd
from modules.nav import SideBarLinks

# Logging setup
logging.basicConfig(format='%(filename)s:%(lineno)s:%(levelname)s -- %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Page setup
st.set_page_config(layout='wide')
SideBarLinks()

logger.info("Loading Calendar page")

# Constants
API_BASE_URL = "http://web-api:4000"

# Get user ID from session state
charlie_user_id = st.session_state.get("user_id", None)

if charlie_user_id is None:
    st.error("🚫 User not logged in. Please return to the home page and log in.")
    st.stop()

# Fetch deadlines for flagged (preferred) positions
def fetch_flagged_deadlines(user_id):
    try:
        url = f"{API_BASE_URL}/views_position/{user_id}/deadlines"
        logger.info(f"Fetching deadlines from: {url}")
        response = requests.get(url)

        if response.status_code == 200:
            deadlines = response.json()
            logger.info(f"Fetched {len(deadlines)} deadline entries.")
            return deadlines
        else:
            logger.error(f"Failed to fetch deadlines: {response.status_code} {response.text}")
            return []
    except Exception as e:
        logger.error(f"Exception occurred while fetching deadlines: {e}")
        return []

# UI
st.title("📅 Your Position Deadline Calendar")

# Fetch data
deadlines = fetch_flagged_deadlines(charlie_user_id)

if deadlines:
    st.subheader("🔖 Flagged Positions and Their Deadlines")

    # Convert to DataFrame
    df = pd.DataFrame(deadlines)
    df['deadline'] = pd.to_datetime(df['deadline'])
    df = df.sort_values(by='deadline')

    # Show nicely formatted list
    for _, row in df.iterrows():
        st.markdown(f"🔹 **{row['title']}** — 🗓️ Deadline: `{row['deadline'].date()}`")

    st.markdown("---")
    st.subheader("📋 Tabular View")

    # Show table
    st.dataframe(df.rename(columns={
        "title": "Position Title",
        "deadline": "Application Deadline"
    }), use_container_width=True)
else:
    st.info("📭 You haven’t flagged any positions yet. Flag some positions to see their deadlines here!")

