import logging
logging.basicConfig(format='%(filename)s:%(lineno)s:%(levelname)s -- %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests


st.set_page_config(layout='wide')
SideBarLinks()

logger.info("finding open coop positions...")

# Charlie Stout's userId from your database
API_BASE_URL = f"http://web-api:4000"

# 🔍 Get the user_id from session state
charlie_user_id = st.session_state.get("user_id", None)

if charlie_user_id is None:
    st.error("User not logged in. Please return to home and log in.")
    st.stop()

# Function to fetch user data from API
def fetch_user_data(user_id):
    try:
        response = requests.get(f"{API_BASE_URL}/users/{user_id}")
        logger.info(f"Fetching user data from API: status_code={response.status_code}")
        if response.status_code == 200:
            data = response.json()
            logger.info(f"User data received: {data}")
            return data
        else:
            logger.error(f"Failed to fetch user data, status code: {response.status_code}, response: {response.text}")
        return None
    except Exception as e:
        logger.error(f"Error fetching user data: {e}")
        # Fallback data if API is not available
        return {
            'userId': 1,
            'firstName': 'Charlie',
            'lastName': 'Stout',
            'email': 'c.stout@student.edu',
            'phone': '555-0101',
            'major': 'Computer Science',
            'minor': 'Mathematics',
            'college': 'Khoury College of Computer Sciences',
            'gradYear': '2026',
            'grade': 'Junior',
            'gender': None,
            'race': None,
            'nationality': None,
            'sexuality': None,
            'disability': None
        }

# Function to fetch user skills from API
def fetch_user_skills(user_id):
    try:
        response = requests.get(f"{API_BASE_URL}/users/{user_id}/skills")
        if response.status_code == 200:
            return response.json()
        return []
    except Exception as e:
        logger.error(f"Error fetching user skills: {e}")
        return []

# Function to fetch application summary from API
def fetch_application_summary(user_id):
    try:
        response = requests.get(f"{API_BASE_URL}/app/student/{user_id}/applications/summary")
        if response.status_code == 200:
            return response.json()
        return []
    except Exception as e:
        logger.error(f"Error fetching application summary: {e}")
        return []

# Function to fetch recent applications from API
def fetch_recent_applications(user_id):
    try:
        response = requests.get(f"{API_BASE_URL}/users/{user_id}/recent-applications")
        if response.status_code == 200:
            return response.json()
        return []
    except Exception as e:
        logger.error(f"Error fetching recent applications: {e}")
        return []

# Function to update user data via API
def update_user_data(user_data):
    try:
        response = requests.put(f"{API_BASE_URL}/users", json=user_data)
        return response.status_code == 200
    except Exception as e:
        logger.error(f"Error updating user data: {e}")
        return False

# Function to fetch all available skills from API
def fetch_all_skills():
    try:
        response = requests.get(f"{API_BASE_URL}/skills")
        if response.status_code == 200:
            return response.json()
        return []
    except Exception as e:
        logger.error(f"Error fetching all skills: {e}")
        return []

# Function to update user skills
def update_user_skills(user_id, updated_skills, removed_skills):
    try:
        update_data = {
            "updated_skills": list(updated_skills.values()),
            "removed_skills": removed_skills
        }
        response = requests.put(f"{API_BASE_URL}/users/{user_id}/skills", json=update_data)
        return response.status_code == 200
    except Exception as e:
        logger.error(f"Error updating user skills: {e}")
        return False

# Function to add new skills to user profile
def add_user_skills(user_id, new_skills):
    try:
        response = requests.post(f"{API_BASE_URL}/users/{user_id}/skills", json={"skills": new_skills})
        return response.status_code == 200
    except Exception as e:
        logger.error(f"Error adding user skills: {e}")
        return False

# # Function to fetch all coop positions from the Flask REST API
# def fetch_all_positions():
#     try:
#         response = requests.get(f"{API_BASE_URL}/coopPositions/all")
#         if response.status_code == 200:
#             return response.json()
#         else:
#             logger.error(f"Failed to fetch positions, status code: {response.status_code}, response: {response.text}")
#             return []
#     except Exception as e:
#         logger.error(f"Error fetching coop positions: {e}")
#         return []

# def fetch_all_positions():
#     try:
#         url = f"{COOP_API_URL}/all"
#         print("LOOOK HERERERER PRINT HERE" + repr(COOP_API_URL))
#         logger.info(f"Fetching from URL: {url}")  # Log the full URL

#         response = requests.get(url)

#         logger.info(f"Status code: {response.status_code}")  # Log HTTP status
#         logger.info(f"Response body: {response.text}")       # Log raw response body

#         if response.status_code == 200:
#             return response.json()
#         else:
#             logger.error(f"Failed to fetch positions, status code: {response.status_code}, response: {response.text}")
#             return []
#     except Exception as e:
#         logger.error(f"Error fetching coop positions: {e}")
#         return []

def fetch_all_positions():
    try:
        # url = f"{API_BASE_URL}/api/backend/coopPositions/allPositions"
        # logger.info(f"Fetching all positions from: {url}")
        response = requests.get(f"{API_BASE_URL}/coopPositions/allPositions")
        if response.status_code == 200:
            return response.json()
        else:
            logger.error(f"Failed to fetch positions, status code: {response.status_code}, response: {response.text}")
            return []
    except Exception as e:
        logger.error(f"Error fetching all positions: {e}")
        return []
    
# def fetch_all_skills():
#     try:
#         response = requests.get(f"{API_BASE_URL}/skills")
#         if response.status_code == 200:
#             return response.json()
#         return []
#     except Exception as e:
#         logger.error(f"Error fetching all skills: {e}")
#         return []

# Fetch user data and related information
user_data = fetch_user_data(charlie_user_id)
if isinstance(user_data, list) and len(user_data) > 0:
    user_data = user_data[0]

user_skills = fetch_user_skills(charlie_user_id)
app_summary = fetch_application_summary(charlie_user_id)
recent_applications = fetch_recent_applications(charlie_user_id)

if user_data:
    # Header
    st.title("Browse Positions")
    
    # Create tabs for better organization
    tab1, tab2, tab3 = st.tabs(["All", "Favorites", "Not Interested"])
    
    with tab1:
        
        st.header("🔍 All Positions")
        
        # Fetch all positions from the API
        positions = fetch_all_positions()
        
        if not positions:
            st.warning("No positions available at the moment.")
        else:
            # Display positions in a table format
            for position in positions:
                st.subheader(position['title'])
                st.write(f"**Company:** {position['company']}")
                st.write(f"**Location:** {position['location']}")
                st.write(f"**Description:** {position['description']}")
                st.write(f"**Posted On:** {position['postedOn']}")
                st.write(f"**Application Deadline:** {position['applicationDeadline']}")
                st.write("---")


    with tab2:
        st.header("❤️ Favorites")

    with tab3:
        # Skills Management Section
        st.header("Not Interested")

else:
    st.error("Unable to load user data. Please try again later.")


# import logging
# import streamlit as st
# import requests
# from modules.nav import SideBarLinks

# logger = logging.getLogger(__name__)

# st.set_page_config(layout='wide')
# SideBarLinks()

# st.title("Browse Co-op Positions")

# API_BASE = "http://localhost:4000/coopPositions"

# def fetch_all_positions():
#     try:
#         res = requests.get(f"{API_BASE}/all")
#         res.raise_for_status()
#         data = res.json()
#         if not isinstance(data, list):
#             st.warning("API did not return a list. Check your Flask route.")
#             return []
#         return data
#     except requests.exceptions.RequestException as e:
#         st.error(f"❌ Error fetching positions: {e}")
#         return []

# def show_job_grid(jobs):
#     if not jobs:
#         st.info("No co-op positions available.")
#         return

#     cols_per_row = 3
#     for i in range(0, len(jobs), cols_per_row):
#         cols = st.columns(cols_per_row)
#         for col, job in zip(cols, jobs[i:i+cols_per_row]):
#             with col:
#                 with st.container(border=True):
#                     st.markdown(f"### {job.get('title', 'Untitled')}")
#                     st.write(f"📍 {job.get('location', 'N/A')}")
#                     st.write(f"💵 ${job.get('hourlyPay', 'N/A')}/hr")
#                     st.write(f"Industry: {job.get('industry', 'N/A')}")
#                     st.caption(job.get('description', '')[:120] + ("..." if len(job.get('description', '')) > 120 else ""))
#                     if st.button("View Details", key=f"details_{job.get('coopPositionId', i)}"):
#                         st.session_state.selected_job = job

# # === SESSION STATE ===
# if "selected_job" not in st.session_state:
#     st.session_state.selected_job = None

# # === PAGE LOGIC ===
# if st.session_state.selected_job:
#     job = st.session_state.selected_job
#     st.markdown(f"## {job.get('title', 'Untitled')}")
#     st.write(f"📍 {job.get('location', 'N/A')}")
#     st.write(f"💵 ${job.get('hourlyPay', 'N/A')}/hr")
#     st.write(f"Industry: {job.get('industry', 'N/A')}")
#     st.write(job.get('description', 'No description provided'))
#     st.write(f"Required GPA: {job.get('desiredGPA', 'N/A')}")
#     st.write(f"Deadline: {job.get('deadline', 'N/A')}")
#     st.write(f"Start Date: {job.get('startDate', 'N/A')}")
#     st.write(f"End Date: {job.get('endDate', 'N/A')}")
#     st.divider()
#     if st.button("⬅ Back to Listings"):
#         st.session_state.selected_job = None
# else:
#     jobs = fetch_all_positions()
#     show_job_grid(jobs)
