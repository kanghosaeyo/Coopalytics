import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

SideBarLinks()

st.title('Employer Home Page')

# Phoebe Hwang's userId from your database
PHOEBE_USER_ID = 37
API_BASE_URL = "http://web-api:4000"

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
def fetch_user_data(user_id):
    try:
        response = requests.get(f"{API_BASE_URL}/u/users/{user_id}")
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
def fetch_company_data(user_id):
    try:
        response = requests.get(f"{API_BASE_URL}/u/users/{user_id}/company-profiles")
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
def update_company_data(user_data):
    try:
        response = requests.put(f"{API_BASE_URL}/u/company-profiles", json=user_data)
        return response.status_code == 200
    except Exception as e:
        logger.error(f"Error updating user data: {e}")
        return False

user_data = fetch_user_data(PHOEBE_USER_ID)
