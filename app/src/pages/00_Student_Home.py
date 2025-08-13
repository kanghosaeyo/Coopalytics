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

st.markdown(f'<p class="welcome-message">Welcome back, Charlie! 🎓</p>', unsafe_allow_html=True)

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
            first_name = st.text_input("First Name", value="Charlie")
            last_name = st.text_input("Last Name", value="Stout")
            email = st.text_input("Email", value="c.stout@student.edu")
            phone = st.text_input("Phone", value="555-0101")
            
        with col_right:
            major = st.selectbox("Major", ["Computer Science", "Engineering", "Business", "Data Science", "Information Systems"], index=0)
            minor = st.selectbox("Minor", ["Mathematics", "None", "Business", "Psychology", "Statistics"], index=0)
            college = st.selectbox("College", ["NEU", "Khoury College", "College of Engineering", "D'Amore-McKim School of Business"], index=0)
            grad_year = st.selectbox("Graduation Year", ["2026", "2024", "2025", "2027"], index=0)
            
        grade = st.selectbox("Current Grade", ["Junior", "Sophomore", "Senior"], index=0)
        
        st.markdown("### Demographics")
        
        demo_col1, demo_col2 = st.columns(2)
        
        with demo_col1:
            gender = st.selectbox("Gender", ["Male", "Female", "Non-binary", "Prefer not to say", "Other"], index=0)
            race = st.selectbox("Race/Ethnicity", ["White", "Asian", "Black/African American", "Hispanic/Latino", "Native American", "Pacific Islander", "Mixed", "Prefer not to say"], index=0)
            
        with demo_col2:
            nationality = st.selectbox("Nationality", ["American", "International", "Prefer not to say"], index=0)
            sexuality = st.selectbox("Sexual Orientation", ["Heterosexual", "LGBTQ+", "Prefer not to say"], index=0)
            
        disability = st.selectbox("Disability Status", ["None", "ADHD", "Anxiety", "Dyslexia", "Depression", "Autism", "Prefer not to say"], index=0)
        
        submitted = st.form_submit_button("Update Profile", type="primary", use_container_width=True)
        
        if submitted:
            user_data = {
                "userId": 1,
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
                st.success("✅ Profile updated successfully!")
            except Exception as e:
                st.error(f"❌ Error updating profile: {str(e)}")

with col2:
    st.markdown("""
    <div class="quick-stats">
        <div class="section-title">📊 Quick Stats</div>
        <div class="stat-item">
            <div class="stat-number">2</div>
            <div class="stat-label">Applications Submitted</div>
        </div>
        <div class="stat-item">
            <div class="stat-number">1</div>
            <div class="stat-label">Under Review</div>
        </div>
        <div class="stat-item">
            <div class="stat-number">1</div>
            <div class="stat-label">Previous Co-op</div>
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
    st.metric(label="📝 Submitted", value="2", delta="Recent activity")
    
with status_col2:
    st.metric(label="👁️ Under Review", value="1", delta="Software Dev")
    
with status_col3:
    st.metric(label="✅ Previous Experience", value="1", delta="QA Co-op")
    
with status_col4:
    st.metric(label="⭐ GPA", value="3.7", delta="Strong")

st.markdown("""
<div class="info-section">
    <div class="section-title">🏢 Recent Application Activity</div>
</div>
""", unsafe_allow_html=True)

col_app1, col_app2 = st.columns(2)

with col_app1:
    st.markdown("""
    **Software Developer Intern** - TechNova Inc  
    📅 Applied: Jan 15, 2025  
    📍 Boston, MA | 💰 $22.50/hr  
    🔍 Status: **Under Review**  
    📋 GPA Submitted: 3.7
    """)

with col_app2:
    st.markdown("""
    **Backend Developer Intern** - TechNova Inc  
    📅 Applied: Jan 24, 2025  
    📍 Portland, OR | 💰 $24.00/hr  
    🔍 Status: **Submitted**  
    📋 GPA Submitted: 3.7
    """)

st.markdown("""
<div class="info-section">
    <div class="section-title">🛠️ Your Skills Profile</div>
    <p style="color: #64748b;">Based on your major and experience</p>
</div>
""", unsafe_allow_html=True)

skill_col1, skill_col2, skill_col3 = st.columns(3)

with skill_col1:
    st.markdown("**Programming Languages**")
    st.progress(0.8, text="Python (Advanced)")
    st.progress(0.9, text="JavaScript (Expert)")
    st.progress(0.6, text="Java (Intermediate)")

with skill_col2:
    st.markdown("**Web Development**")
    st.progress(0.8, text="React (Advanced)")
    st.progress(0.6, text="Node.js (Intermediate)")
    st.progress(0.8, text="Git (Advanced)")

with skill_col3:
    st.markdown("**Database & Tools**")
    st.progress(0.8, text="SQL (Advanced)")
    st.progress(0.8, text="Communication (Advanced)")
    st.progress(0.9, text="Teamwork (Expert)")

st.markdown("""
<div class="info-section">
    <div class="section-title">💡 Personalized Recommendations</div>
    <ul style="color: #64748b;">
        <li>🎯 <strong>Great match:</strong> You have strong skills in Python and JavaScript - perfect for the positions you're applying to</li>
        <li>📊 <strong>Competitive advantage:</strong> Your 3.7 GPA exceeds the requirements for most positions</li>
        <li>⏰ <strong>Upcoming deadlines:</strong> 3 positions closing soon that match your CS background</li>
        <li>🌟 <strong>Past success:</strong> Your QA Co-op experience at TechNova will help with future applications</li>
        <li>📈 <strong>Industry insight:</strong> CS majors in Technology earn an average of $24.50/hr in co-ops</li>
    </ul>
</div>
""", unsafe_allow_html=True)