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

if user_data:
    # Header
    st.title("Employer Dashboard")
    st.subheader(f"Welcome back, {user_data['firstName']}!")
    
    # Create tabs for better organization
    tab1, tab2, tab3 = st.tabs(["📋 Company Profile", "📊 Quick Stats", "🛠️ Skills Management"])
    
    with tab1:
        st.header("Your Profile")
        
        with st.form("profile_form"):
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("Personal Information")
                first_name = st.text_input("First Name", value=user_data.get("firstName", ""))
                last_name = st.text_input("Last Name", value=user_data.get("lastName", ""))
                email = st.text_input("Email", value=user_data.get("email", ""))
                phone = st.text_input("Phone", value=user_data.get("phone", ""))
                
            with col2:
                st.subheader("Academic Information")
                major_options = ["Computer Science", "Data Science", "Information Systems", "Cybersecurity", 
                               "Business", "Marketing", "Finance", "International Business", "Mechanical Engineering", 
                               "Biomedical Engineering", "Electrical Engineering", "Environmental Engineering", 
                               "Physics", "Biology", "Chemistry", "Psychology", "Design", "Mathematics", 
                               "Economics", "Art", "Spanish", "Sociology", "History"]
                
                major_index = 0
                if user_data.get("major") in major_options:
                    major_index = major_options.index(user_data.get("major"))
                major = st.selectbox("Major", major_options, index=major_index)
                
                minor_options = ["None"] + major_options
                minor_index = 0
                if user_data.get("minor") in minor_options:
                    minor_index = minor_options.index(user_data.get("minor"))
                minor = st.selectbox("Minor", minor_options, index=minor_index)
                
                college_options = ["College of Arts, Media and Design", "Bouvé College of Health Sciences", 
                                 "D'Amore-McKim School of Business", "Khoury College of Computer Sciences", 
                                 "College of Engineering", "College of Science", "College of Social Sciences and Humanities"]
                college_index = 0
                current_college = user_data.get("college", "")
                if current_college in college_options:
                    college_index = college_options.index(current_college)
                college = st.selectbox("College", college_options, index=college_index)
                
                grad_year_options = ["2024", "2025", "2026", "2027"]
                grad_year_index = 0
                if user_data.get("gradYear") in grad_year_options:
                    grad_year_index = grad_year_options.index(user_data.get("gradYear"))
                grad_year = st.selectbox("Graduation Year", grad_year_options, index=grad_year_index)
                
                grade_options = ["Sophomore", "Junior", "Senior"]
                grade_index = 0
                if user_data.get("grade") in grade_options:
                    grade_index = grade_options.index(user_data.get("grade"))
                grade = st.selectbox("Current Grade", grade_options, index=grade_index)
            
            st.subheader("Demographics")
            demo_col1, demo_col2 = st.columns(2)

            with demo_col1:
                gender_options = ["Male", "Female", "Non-binary", "Prefer not to say", "Other"]
                gender_index = 0
                if user_data.get("gender") in gender_options:
                    gender_index = gender_options.index(user_data.get("gender"))
                gender = st.selectbox("Gender", gender_options, index=gender_index)

                race_options = ["White", "Asian", "Black/African American", "Hispanic/Latino",
                               "Native American", "Pacific Islander", "Mixed", "Prefer not to say"]
                race_index = 0
                if user_data.get("race") in race_options:
                    race_index = race_options.index(user_data.get("race"))
                race = st.selectbox("Race/Ethnicity", race_options, index=race_index)

            with demo_col2:
                nationality_options = ["American", "International", "Prefer not to say"]
                nationality_index = 0
                if user_data.get("nationality") in nationality_options:
                    nationality_index = nationality_options.index(user_data.get("nationality"))
                nationality = st.selectbox("Nationality", nationality_options, index=nationality_index)

                sexuality_options = ["Heterosexual", "LGBTQ+", "Prefer not to say"]
                sexuality_index = 0
                if user_data.get("sexuality") in sexuality_options:
                    sexuality_index = sexuality_options.index(user_data.get("sexuality"))
                sexuality = st.selectbox("Sexual Orientation", sexuality_options, index=sexuality_index)

            disability_options = ["None", "ADHD", "Anxiety", "Dyslexia", "Depression", "Autism", "Prefer not to say"]
            disability_index = 0
            if user_data.get("disability") in disability_options:
                disability_index = disability_options.index(user_data.get("disability"))
            disability = st.selectbox("Disability Status", disability_options, index=disability_index)
            
            submitted = st.form_submit_button("Update Profile", type="primary", use_container_width=True)
            
            if submitted:
                update_data = {
                    "userId": charlie_user_id,
                    "firstName": first_name,
                    "lastName": last_name,
                    "email": email,
                    "phone": phone,
                    "major": major,
                    "minor": minor if minor != "None" else None,
                    "college": college,
                    "gradYear": grad_year,
                    "grade": grade,
                    "gender": gender,
                    "race": race,
                    "nationality": nationality,
                    "sexuality": sexuality,
                    "disability": disability if disability != "None" else None
                }
                
                if update_user_data(update_data):
                    st.success("✅ Profile updated successfully!")
                    st.rerun()
                else:
                    st.error("❌ Failed to update profile")


    with tab2:
        st.header("📊 Quick Stats")

        # Calculate metrics from real data
        total_applications = sum(item['ApplicationCount'] for item in app_summary)
        under_review = next((item['ApplicationCount'] for item in app_summary if item['status'] == 'Under Review'), 0)
        submitted = next((item['ApplicationCount'] for item in app_summary if item['status'] == 'Submitted'), 0)

        # Get GPA from most recent application
        latest_gpa = "N/A"
        if recent_applications:
            latest_gpa = recent_applications[0].get('gpa', 'N/A')

        # Display metrics in a clean layout
        metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)

        with metric_col1:
            st.metric(label="📝 Applications Submitted", value=str(total_applications), delta="Total")

        with metric_col2:
            st.metric(label="👁️ Under Review", value=str(under_review), delta="Pending")

        with metric_col3:
            st.metric(label="📄 Recently Submitted", value=str(submitted), delta="Awaiting Review")

        with metric_col4:
            st.metric(label="⭐ GPA", value=str(latest_gpa), delta="Latest Application")
        
        # Skills section
        st.subheader("🛠️ Your Skills Profile")
        st.caption("Based on your profile and experience")

        if user_skills:
            # Group skills by category
            skills_by_category = {}
            for skill in user_skills:
                category = skill['category']
                if category not in skills_by_category:
                    skills_by_category[category] = []
                skills_by_category[category].append(skill)

            # Display skills in columns
            categories = list(skills_by_category.keys())
            if len(categories) >= 3:
                skill_col1, skill_col2, skill_col3 = st.columns(3)
                cols = [skill_col1, skill_col2, skill_col3]
            elif len(categories) == 2:
                skill_col1, skill_col2 = st.columns(2)
                cols = [skill_col1, skill_col2]
            else:
                cols = [st]

            for i, category in enumerate(categories):
                col = cols[i % len(cols)]
                with col:
                    st.markdown(f"**{category}**")
                    for skill in skills_by_category[category]:
                        proficiency = skill['proficiencyLevel']
                        progress_value = proficiency / 5.0  # Convert 1-5 scale to 0-1

                        # Convert proficiency to text
                        proficiency_text = {1: "Beginner", 2: "Basic", 3: "Intermediate", 4: "Advanced", 5: "Expert"}
                        level_text = proficiency_text.get(proficiency, "Unknown")

                        st.write(f"{skill['name']} ({level_text})")
                        st.progress(progress_value)
        else:
            st.info("No skills data available. Please contact your advisor to update your skills profile.")

    with tab3:
        # Skills Management Section
        st.header("🛠️ Skills Management")

        if user_skills:
            # Group skills by category
            skills_by_category = {}
            for skill in user_skills:
                category = skill['category']
                if category not in skills_by_category:
                    skills_by_category[category] = []
                skills_by_category[category].append(skill)

            # Create skills management form
            with st.form("skills_form"):
                st.subheader("📝 Edit Your Skills & Proficiency Levels")

                # Display skills grouped by category
                updated_skills = {}
                skills_to_remove = []

                for category, skills in skills_by_category.items():
                    st.markdown(f"**{category}**")

                    for skill in skills:
                        col1, col2, col3 = st.columns([3, 2, 1])

                        with col1:
                            st.write(f"• {skill['name']}")

                        with col2:
                            # Proficiency level slider (1-5)
                            proficiency = st.slider(
                                f"Level",
                                min_value=1,
                                max_value=5,
                                value=skill['proficiencyLevel'],
                                key=f"skill_{skill['skillId']}_proficiency",
                                help="1=Beginner, 2=Novice, 3=Intermediate, 4=Advanced, 5=Expert"
                            )
                            updated_skills[skill['skillId']] = {
                                'skillId': skill['skillId'],
                                'proficiencyLevel': proficiency
                            }

                        with col3:
                            # Remove skill checkbox
                            if st.checkbox("Remove", key=f"remove_skill_{skill['skillId']}"):
                                skills_to_remove.append(skill['skillId'])

                    st.markdown("")  # Add spacing between categories

                # Save skills changes button
                skills_submitted = st.form_submit_button("💾 Save Skills Changes", type="primary", use_container_width=True)

                if skills_submitted:
                    # Filter out skills marked for removal
                    final_skills = {k: v for k, v in updated_skills.items() if k not in skills_to_remove}

                    if update_user_skills(charlie_user_id, final_skills, skills_to_remove):
                        st.success("✅ Skills updated successfully!")
                        st.rerun()
                    else:
                        st.error("❌ Failed to update skills")

        # Add New Skills Section
        st.markdown("---")
        st.subheader("➕ Add New Skills")

        # Fetch all available skills for adding
        all_skills = fetch_all_skills()
        if all_skills:
            # Filter out skills user already has
            current_skill_ids = [skill['skillId'] for skill in user_skills] if user_skills else []
            available_skills = [skill for skill in all_skills if skill['skillId'] not in current_skill_ids]

            if available_skills:
                with st.form("add_skills_form"):
                    # Group available skills by category for easier selection
                    available_by_category = {}
                    for skill in available_skills:
                        category = skill['category']
                        if category not in available_by_category:
                            available_by_category[category] = []
                        available_by_category[category].append(skill)

                    selected_skills = []

                    for category, skills in available_by_category.items():
                        st.markdown(f"**{category}**")

                        for skill in skills:
                            col1, col2 = st.columns([3, 2])

                            with col1:
                                if st.checkbox(skill['name'], key=f"add_skill_{skill['skillId']}"):
                                    with col2:
                                        proficiency = st.slider(
                                            "Proficiency",
                                            min_value=1,
                                            max_value=5,
                                            value=3,
                                            key=f"new_skill_{skill['skillId']}_proficiency",
                                            help="1=Beginner, 2=Novice, 3=Intermediate, 4=Advanced, 5=Expert"
                                        )
                                        selected_skills.append({
                                            'skillId': skill['skillId'],
                                            'proficiencyLevel': proficiency
                                        })

                        st.markdown("")  # Add spacing

                    # Add selected skills button
                    add_skills_submitted = st.form_submit_button("➕ Add Selected Skills", type="secondary", use_container_width=True)

                    if add_skills_submitted and selected_skills:
                        if add_user_skills(charlie_user_id, selected_skills):
                            st.success(f"✅ Added {len(selected_skills)} new skills!")
                            st.rerun()
                        else:
                            st.error("❌ Failed to add skills")
                    elif add_skills_submitted and not selected_skills:
                        st.warning("⚠️ Please select at least one skill to add")
            else:
                st.info("🎉 You have all available skills! Great job!")
        else:
            st.error("❌ Unable to load available skills")


else:
    st.error("Unable to load user data. Please try again later.")