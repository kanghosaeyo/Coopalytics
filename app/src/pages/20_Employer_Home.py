import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

SideBarLinks()

st.title('Employer Home Page')

# Phoebe Hwang's userId from your database
CHARLIE_USER_ID = 4
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