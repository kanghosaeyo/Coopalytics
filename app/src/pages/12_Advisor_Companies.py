import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout='wide')

SideBarLinks()

st.title('Company Partnerships')

# Fetch companies sorted by rating from backend
API_URL = "http://web-api:4000/cprof/companyProfiles/rating"  # Update if your backend runs elsewhere

try:
    response = requests.get(API_URL)
    response.raise_for_status()
    companies = response.json()
except Exception as e:
    st.error(f"Failed to fetch companies: {e}")
    companies = []

# Display companies in a table
if companies:
    st.subheader("Top Rated Companies")
    st.dataframe(companies)
else:
    st.info("No company data available.")

