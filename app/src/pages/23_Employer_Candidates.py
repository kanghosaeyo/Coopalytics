import logging
logging.basicConfig(format='%(filename)s:%(lineno)s:%(levelname)s -- %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout='wide')
SideBarLinks()

logger.info("Loading Employer Candidates page")

# API configuration
API_BASE_URL = "http://web-api:4000"

# Check if a student was selected from the applications page
selected_student_id = st.session_state.get("selected_student_id", None)
selected_application_id = st.session_state.get("selected_application_id", None)

st.title('👤 Student Profile')

if selected_student_id:
    st.subheader(f"Profile for Student ID: {selected_student_id}")

    # Display application context if available
    if selected_application_id:
        st.info(f"📋 Viewing profile from Application ID: {selected_application_id}")

    # Placeholder for student profile information
    st.markdown("### 📊 Student Information")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**Personal Details:**")
        st.write("• Name: John Doe")
        st.write("• Email: j.doe@student.edu")
        st.write("• Major: Computer Science")
        st.write("• Graduation Year: 2025")
        st.write("• GPA: 3.7")

    with col2:
        st.markdown("**Application Details:**")
        st.write("• Application Status: Under Review")
        st.write("• Date Applied: 2025-02-01")
        st.write("• Resume: Available")
        st.write("• Cover Letter: Available")

    st.markdown("---")

    # Navigation back to applications
    if st.button("← Back to Applications", use_container_width=True):
        # Clear the selected student from session state
        if "selected_student_id" in st.session_state:
            del st.session_state["selected_student_id"]
        if "selected_application_id" in st.session_state:
            del st.session_state["selected_application_id"]

        st.switch_page("pages/22_Employer_Applications.py")

else:
    st.info("No student selected. Please navigate from the Application Management page to view a specific student profile.")

    if st.button("Go to Application Management", use_container_width=True):
        st.switch_page("pages/22_Employer_Applications.py")