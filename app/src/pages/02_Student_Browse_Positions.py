import logging
import streamlit as st
import requests
from modules.nav import SideBarLinks

# Logging setup
logging.basicConfig(format='%(filename)s:%(lineno)s:%(levelname)s -- %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Page setup
st.set_page_config(layout='wide')
SideBarLinks()

logger.info("Loading Coop Positions page")

# Constants
API_BASE_URL = "http://web-api:4000"

# Get user ID from session state
charlie_user_id = st.session_state.get("user_id", None)

if charlie_user_id is None:
    st.error("🚫 User not logged in. Please return to the home page and log in.")
    st.stop()

# Sidebar filter
filter_option = st.selectbox(
    "View positions by:",
    options=["All", "Liked", "Disliked", "Matches Desired Skills"]
)

# Function to fetch and display positions
def fetch_positions():
    if filter_option == "All":
        url = f"{API_BASE_URL}/positions"  # ✔ this is from coopPositions blueprint

    elif filter_option == "Liked":
        url = f"{API_BASE_URL}/vp/viewpos/{charlie_user_id}?preference=true"  # ✔ matches blueprint + route

    elif filter_option == "Disliked":
        url = f"{API_BASE_URL}/vp/viewpos/{charlie_user_id}?preference=false"

    elif filter_option == "Matches Desired Skills":
        url = f"{API_BASE_URL}/{charlie_user_id}/desiredSkills"
    else:
        st.warning("Unknown filter selected.")
        return []

    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Failed to fetch data: {response.status_code}")
            return []
    except requests.exceptions.RequestException as e:
        st.error(f"API request error: {e}")
        return []

# Load and display data
positions = fetch_positions()
for pos in positions:
    with st.expander(pos["title"]):
        st.write(f"**Location**: {pos.get('location', 'N/A')}")
        st.write(f"**Description**: {pos.get('description', 'N/A')}")
        st.write(f"**Pay**: ${pos.get('hourlyPay', 'N/A')}/hr")

        # Like/Dislike buttons
        col1, col2 = st.columns([1, 1])
        with col1:
            if st.button("👍 Like", key=f"like_{pos['coopPositionId']}"):
                response = requests.post(f"{API_BASE_URL}/vp/position", json={
                    "studentId": charlie_user_id,
                    "coopPositionId": pos["coopPositionId"],
                    "preference": True
                })
                if response.status_code == 200:
                    st.success("Marked as liked.")
                    st.rerun()
                else:
                    st.error("Failed to save preference.")

        with col2:
            if st.button("👎 Dislike", key=f"dislike_{pos['coopPositionId']}"):
                requests.post(f"{API_BASE_URL}/vp/position", json={
                    "studentId": charlie_user_id,
                    "coopPositionId": pos["coopPositionId"],
                    "preference": False
                })
                st.warning("Marked as disliked.")