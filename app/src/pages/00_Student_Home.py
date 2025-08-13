import logging
logging.basicConfig(format='%(filename)s:%(lineno)s:%(levelname)s -- %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

SideBarLinks()

logger.info("Loading Student Home page")

st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 50%, #ef4444 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 3rem;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    
    .welcome-message {
        text-align: center;
        color: #64748b;
        font-size: 1.2rem;
        margin-bottom: 2rem;
    }
    
    .profile-card {
        background: white;
        border-radius: 12px;
        padding: 2rem;
        margin: 1rem 0;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        border-left: 4px solid #3b82f6;
    }
    
    .info-section {
        background: #f8fafc;
        border-radius: 8px;
        padding: 1.5rem;
        margin: 1rem 0;
        border: 1px solid #e2e8f0;
    }
    
    .section-title {
        color: #1e3a8a;
        font-size: 1.3rem;
        font-weight: 600;
        margin-bottom: 1rem;
        border-bottom: 2px solid #3b82f6;
        padding-bottom: 0.5rem;
    }
    
    .field-label {
        color: #374151;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }
    
    .field-value {
        color: #6b7280;
        margin-bottom: 1rem;
        padding: 0.5rem;
        background: white;
        border-radius: 4px;
        border: 1px solid #d1d5db;
    }
    
    .quick-stats {
        background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%);
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
        text-align: center;
    }
    
    .stat-item {
        display: inline-block;
        margin: 0 1rem;
        padding: 1rem;
        background: white;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        min-width: 150px;
    }
    
    .stat-number {
        font-size: 2rem;
        font-weight: bold;
        color: #1e3a8a;
    }
    
    .stat-label {
        color: #64748b;
        font-size: 0.9rem;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-header">Student Dashboard</h1>', unsafe_allow_html=True)

if 'first_name' in st.session_state:
    st.markdown(f'<p class="welcome-message">Welcome back, {st.session_state["first_name"]}! 🎓</p>', unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    <div class="profile-card">
        <div class="section-title">📋 Your Profile</div>
    </div>
    """, unsafe_allow_html=True)
    
    with st.form("profile_form"):
        st.markdown("### Personal Information")
        
        col_left, col_right = st.columns(2)
        
        with col_left:
            first_name = st.text_input("First Name", value="Alex")
            last_name = st.text_input("Last Name", value="Johnson")
            email = st.text_input("Email", value="alex.johnson@northeastern.edu")
            phone = st.text_input("Phone", value="(555) 123-4567")
            
        with col_right:
            major = st.selectbox("Major", ["Computer Science", "Engineering", "Business", "Data Science", "Information Systems"])
            minor = st.selectbox("Minor", ["None", "Mathematics", "Business", "Psychology", "Statistics"])
            college = st.selectbox("College", ["Khoury College", "College of Engineering", "D'Amore-McKim School of Business"])
            grad_year = st.selectbox("Graduation Year", ["2024", "2025", "2026", "2027"])
            
        grade = st.selectbox("Current Grade", ["Sophomore", "Junior", "Senior"])
        
        st.markdown("### Demographics")
        
        demo_col1, demo_col2 = st.columns(2)
        
        with demo_col1:
            gender = st.selectbox("Gender", ["Prefer not to say", "Male", "Female", "Non-binary", "Other"])
            race = st.selectbox("Race/Ethnicity", ["Prefer not to say", "Asian", "Black/African American", "Hispanic/Latino", "White", "Native American", "Pacific Islander", "Mixed"])
            
        with demo_col2:
            nationality = st.selectbox("Nationality", ["American", "International", "Prefer not to say"])
            sexuality = st.selectbox("Sexual Orientation", ["Prefer not to say", "Heterosexual", "LGBTQ+"])
            
        disability = st.selectbox("Disability Status", ["Prefer not to say", "None", "Yes"])
        
        submitted = st.form_submit_button("Update Profile", type="primary", use_container_width=True)
        
        if submitted:
            user_data = {
                "userId": 1,  # This would come from session/auth in real app
                "firstName": first_name,
                "lastName": last_name,
                "email": email,
                "phone": phone,
                "major": major,
                "minor": minor,
                "college": college,
                "gradYear": grad_year,
                "grade": grade,
                "gender": gender,
                "race": race,
                "nationality": nationality,
                "sexuality": sexuality,
                "disability": disability
            }
            
            try:
                # In a real app, you'd make this API call:
                # response = requests.put('http://localhost:5000/users', json=user_data)
                # if response.status_code == 200:
                st.success("✅ Profile updated successfully!")
                # else:
                #     st.error("❌ Failed to update profile")
            except Exception as e:
                st.error(f"❌ Error updating profile: {str(e)}")

with col2:
    st.markdown("""
    <div class="quick-stats">
        <div class="section-title">📊 Quick Stats</div>
        <div class="stat-item">
            <div class="stat-number">5</div>
            <div class="stat-label">Applications Submitted</div>
        </div>
        <div class="stat-item">
            <div class="stat-number">2</div>
            <div class="stat-label">Interviews Scheduled</div>
        </div>
        <div class="stat-item">
            <div class="stat-number">1</div>
            <div class="stat-label">Offers Received</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-section">
        <div class="section-title">🎯 Quick Actions</div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("📝 View My Applications", use_container_width=True):
        st.switch_page('pages/01_Student_Applications.py')
        
    if st.button("🔍 Browse Co-op Positions", use_container_width=True):
        st.switch_page('pages/02_Student_Browse_Positions.py')
        
    if st.button("📈 View Analytics", use_container_width=True):
        st.switch_page('pages/03_Student_Analytics.py')
        
    if st.button("💼 Company Reviews", use_container_width=True):
        st.switch_page('pages/04_Student_Company_Reviews.py')

st.markdown("""
<div class="info-section">
    <div class="section-title">📈 Application Status Overview</div>
    <p style="color: #64748b;">Track your co-op application progress and get insights on your placement journey.</p>
</div>
""", unsafe_allow_html=True)

status_col1, status_col2, status_col3, status_col4 = st.columns(4)

with status_col1:
    st.metric(label="📝 Draft", value="1", delta="New")
    
with status_col2:
    st.metric(label="📤 Submitted", value="3", delta="2 this week")
    
with status_col3:
    st.metric(label="👁️ Under Review", value="2", delta="-1")
    
with status_col4:
    st.metric(label="✅ Accepted", value="1", delta="🎉")

st.markdown("""
<div class="info-section">
    <div class="section-title">💡 Tips & Recommendations</div>
    <ul style="color: #64748b;">
        <li>🎯 <strong>Complete your profile:</strong> Make sure all sections are filled out to improve your application visibility</li>
        <li>📊 <strong>Industry insights:</strong> Check out salary trends for your major in the analytics section</li>
        <li>⏰ <strong>Application deadlines:</strong> You have 3 upcoming deadlines this week</li>
        <li>🌟 <strong>Company reviews:</strong> Read reviews from fellow students about their co-op experiences</li>
    </ul>
</div>
""", unsafe_allow_html=True)