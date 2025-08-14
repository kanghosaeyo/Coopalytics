import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

SideBarLinks()

st.title('Employer Home Page')

# Phoebe Hwang's userId from your database
API_BASE_URL = "http://web-api:4000"

# Get the user_id from session state
phoebe_user_id = 37

if phoebe_user_id is None:
    st.error("User not logged in. Please return to home and log in.")
    st.stop()

# Get the company_profile_id from session state
company_profile_id = 1

if company_profile_id is None:
    st.error("Company not found")
    st.stop()


def fetch_applications_for_position(position_id):
    try:
        resp = requests.get(f"{API_BASE_URL}/applications/{position_id}")
        if resp.status_code == 200:
            return resp.json()
    except Exception as e:
        logger.error(f"Error fetching applications: {e}")
    return []


def post_new_position(position_data):
    try:
        resp = requests.post(f"{API_BASE_URL}/createsPos/coopPosition", json=position_data)
        return resp.status_code in (200, 201)
    except Exception as e:
        logger.error(f"Error posting new position: {e}")
        return False


def filter_student_profiles(student_id, skill1, skill2, skill3, grad_year, major):
    try:
        params = {
            "skill1": skill1,
            "skill2": skill2,
            "skill3": skill3,
            "gradYear": grad_year,
            "major": major
        }
        resp = requests.get(f"{API_BASE_URL}/applications/appliesToApp/{student_id}/users", params=params)
        if resp.status_code == 200:
            return resp.json()
    except Exception as e:
        logger.error(f"Error filtering students: {e}")
    return []

# Function to fetch user data from API
def fetch_user_data(phoebe_user_id):
    try:
        response = requests.get(f"{API_BASE_URL}/u/users/{phoebe_user_id}")
        if response.status_code == 200:
            data = response.json()
            return data[0] if data else None
        return None
    except Exception as e:
        logger.error(f"Error fetching user data: {e}")
        # Fallback data if API is not available
        return {
            'userId': 37,
            'firstName': 'Phoebe',
            'lastName': 'Hwang',
            'email': 'p.hwang@technova.com',
            'phone': '555-0401',
            'companyProfileId': '1',
            'industry': 'Technology'
        }
    
# Function to fetch company data from API
def fetch_company_data(company_profile_id):
    try:
        response = requests.get(f"{API_BASE_URL}/u/users/{company_profile_id}/company-profiles")
        if response.status_code == 200:
            data = response.json()
            return data[0] if data else None
        return None
    except Exception as e:
        logger.error(f"Error fetching user data: {e}")
        # Fallback data if API is not available
        return {
            'companyProfileId': 1,
            'name': 'TechNova Inc',
            'bio': 'Leading software development company specializing in enterprise solutions and cloud infrastructure.',
            'industry': 'Technology',
            'websiteLink': 'www.technova.com'
        }

# Function to update user data via API
def update_user_data(user_data):
    try:
        response = requests.put(f"{API_BASE_URL}/u/users", json=user_data)
        return response.status_code == 200
    except Exception as e:
        logger.error(f"Error updating user data: {e}")
        return False
    
# Function to update company data via API
def update_company_data(company_data):
    try:
        response = requests.put(f"{API_BASE_URL}/u/company-profiles", json=company_data)
        return response.status_code == 200
    except Exception as e:
        logger.error(f"Error updating user data: {e}")
        return False

user_data = fetch_user_data(phoebe_user_id)
company_data = fetch_company_data(company_profile_id)

if user_data:
    # Header
    st.title("Employer Dashboard")
    st.subheader(f"Welcome back, {user_data['firstName']}!")

    st.header("Your Profile")
        
    with st.form("profile_form"):

        st.subheader("Company Information")
        col1 = st.columns(1)[0]
            
        with col1:
            company_name = st.text_input("Company Name", value=user_data.get("name", ""))
            bio = st.text_input("Who Are We", value=user_data.get("bio", ""))
            industry = st.text_input("Industry", value=user_data.get("industry", ""))
            website_link = st.text_input("Phone", value=user_data.get("websiteLink", ""))
        submitted = st.form_submit_button("Update Profile", type="primary", use_container_width=True)
            
        if submitted:
            update_data = {
                "name": company_name,
                "bio": bio,
                "industry": industry,
                "websiteLink": website_link
                }
                
        if update_company_data(company_data):
            st.success("✅ Profile updated successfully!")
            st.rerun()
        else:
                st.error("❌ Failed to update profile")

            
        st.subheader("Personal Information")
        personal_col1 = st.columns(1)[0]

        with personal_col1:
            st.subheader("Personal Information")
            first_name = st.text_input("First Name", value=user_data.get("firstName", ""))
            last_name = st.text_input("Last Name", value=user_data.get("lastName", ""))
            email = st.text_input("Email", value=user_data.get("email", ""))
            phone = st.text_input("Phone", value=user_data.get("phone", ""))
            
        submitted = st.form_submit_button("Update Profile", type="primary", use_container_width=True)
            
        if submitted:
            update_data = {
                "userId": phoebe_user_id,
                "firstName": first_name,
                "lastName": last_name,
                "email": email,
                "phone": phone
                }
                
        if update_user_data(update_data):
            st.success("✅ Profile updated successfully!")
            st.rerun()
        else:
            st.error("❌ Failed to update profile")

else:
    st.error("Unable to load user data. Please try again later.")