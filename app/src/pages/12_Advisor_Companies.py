import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout='wide')

SideBarLinks()

st.title('Company Partnerships')

# Fetch companies from backend
API_URL = "http://web-api:4000/companyProfiles/rating"  # Update if your backend runs elsewhere

try:
    response = requests.get("http://web-api:4000/companyProfiles/rating")
    response.raise_for_status()
    companies = response.json()
except Exception as e:
    st.error(f"Failed to fetch companies: {e}")
    companies = []

# Display companies
if companies:
    st.subheader("companies list not empty")
    for company in companies:
        st.write(
            f"- {company.get('companyName', 'Unknown Company')}"
            f"(Avg. Rating: {company.get('avgCompanyRating', 'N/A')})"
        )
else:
    st.info("No company data available.")




