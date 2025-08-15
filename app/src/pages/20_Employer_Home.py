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


# Function to fetch user data from API
def fetch_user_data(phoebe_user_id):
    try:
        response = requests.get(f"{API_BASE_URL}/users/{phoebe_user_id}")
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
        response = requests.get(f"{API_BASE_URL}/users/{company_profile_id}/companyProfiles")
        if response.status_code == 200:
            data = response.json()
            return data[0] if data else None
        return None
    except Exception as e:
        logger.error(f"Error fetching company data: {e}")
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
        response = requests.put(f"{API_BASE_URL}/users", json=user_data)
        return response.status_code == 200
    except Exception as e:
        logger.error(f"Error updating user data: {e}")
        return False
   
# Function to update company data via API /users/<companyProfileId>/companyProfiles/update /cprof/companyProfiles/update/{company_profile_id}
def update_company_data(company_data):
    try:
        response = requests.put(f"{API_BASE_URL}/users/{company_profile_id}/companyProfiles/update", json=company_data)
        return response.status_code == 200
    except Exception as e:
        logger.error(f"Error updating company data: {e}")
        return False

user_data = fetch_user_data(phoebe_user_id)
company_data = fetch_company_data(company_profile_id)

if user_data:
    # Header
    st.subheader(f"Welcome back, {user_data['firstName']}!")
   
    # Company Information Form
    with st.form("company_form"):
        st.subheader("Company Information")
        col1 = st.columns(1)[0]
           
        with col1:
            # Add null check for company_data
            company_name = st.text_input("Company Name", value=company_data.get("name", "") if company_data else "")
            bio = st.text_input("Who Are We", value=company_data.get("bio", "") if company_data else "")
            industry = st.text_input("Industry", value=company_data.get("industry", "") if company_data else "")
            website_link = st.text_input("Website", value=company_data.get("websiteLink", "") if company_data else "")

            company_submitted = st.form_submit_button("Update Company Profile", type="primary", use_container_width=True)
           
            if company_submitted:
                company_update_data = {
                    "name": company_name,
                    "bio": bio,
                    "industry": industry,
                    "websiteLink": website_link
                }

                if update_company_data(company_update_data):
                    st.success("✅ Profile updated successfully!")
                    st.rerun()
                else:
                    st.error("❌ Failed to update profile")

    # Personal Information Form (separate form)
    with st.form("personal_form"):
        st.subheader("Personal Information")
        personal_col1 = st.columns(1)[0]

        with personal_col1:
            first_name = st.text_input("First Name", value=user_data.get("firstName", ""))
            last_name = st.text_input("Last Name", value=user_data.get("lastName", ""))
            email = st.text_input("Email", value=user_data.get("email", ""))
            phone = st.text_input("Phone", value=user_data.get("phone", ""))
           
            personal_submitted = st.form_submit_button("Update Personal Profile", type="primary", use_container_width=True)
           
            if personal_submitted:
                personal_update_data = {
                    "userId": phoebe_user_id,
                    "firstName": first_name,
                    "lastName": last_name,
                    "email": email,
                    "phone": phone
                }
               
                if update_user_data(personal_update_data):
                    st.success("✅ Personal profile updated successfully!")
                    st.rerun()
                else:
                    st.error("❌ Failed to update personal profile")

else:
    st.error("Unable to load user data. Please try again later.")