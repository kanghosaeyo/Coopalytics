import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout='wide')

SideBarLinks()

# API endpoint configuration
API_BASE_URL = "http://web-api:4000"
RATING_ENDPOINT = f"{API_BASE_URL}/cprof/companyProfiles/rating"
ALL_COMPANIES_ENDPOINT = f"{API_BASE_URL}/cprof/companyProfiles"

st.title('Company Partnerships')

st.markdown("""
This page displays company partnerships sorted by their average student ratings.
Companies with higher ratings appear first, followed by companies without ratings yet.
""")

# Add refresh button
col1, col2 = st.columns([1, 4])
with col1:
    if st.button("🔄 Refresh Data"):
        st.rerun()
with col2:
    st.markdown("*Click refresh to get the latest company data*")

# Test API connection
if st.button("🧪 Test API Connection"):
    try:
        test_response = requests.get(f"{API_BASE_URL}/cprof/companyProfiles", timeout=5)
        if test_response.status_code == 200:
            st.success("✅ API connection successful!")
            st.info(f"Response status: {test_response.status_code}")
        else:
            st.error(f"❌ API responded with status: {test_response.status_code}")
    except Exception as e:
        st.error(f"❌ API connection failed: {str(e)}")

st.divider()

def fetch_company_ratings():
    """Fetch company profiles sorted by rating from the API"""
    try:
        st.info(f"Fetching from: {RATING_ENDPOINT}")
        response = requests.get(RATING_ENDPOINT, timeout=10)
        if response.status_code == 200:
            data = response.json()
            st.success(f"Successfully fetched {len(data)} rated companies")
            return data
        else:
            st.error(f"Failed to fetch rating data: {response.status_code}")
            st.error(f"Response: {response.text}")
            return []
    except requests.exceptions.RequestException as e:
        st.error(f"Error connecting to API: {str(e)}")
        return []
    except Exception as e:
        st.error(f"Unexpected error: {str(e)}")
        return []

def fetch_all_companies():
    """Fetch all company profiles from the API"""
    try:
        st.info(f"Fetching from: {ALL_COMPANIES_ENDPOINT}")
        response = requests.get(ALL_COMPANIES_ENDPOINT, timeout=10)
        if response.status_code == 200:
            data = response.json()
            st.success(f"Successfully fetched {len(data)} total companies")
            return data
        else:
            st.error(f"Failed to fetch company data: {response.status_code}")
            st.error(f"Response: {response.text}")
            return []
    except requests.exceptions.RequestException as e:
        st.error(f"Error connecting to API: {str(e)}")
        return []
    except Exception as e:
        st.error(f"Unexpected error: {str(e)}")
        return []

def display_company_ratings():
    """Display company ratings in a table format"""
    # Fetch data from API
    with st.spinner("Fetching company data..."):
        rated_companies = fetch_company_ratings()
        all_companies = fetch_all_companies()
    
    if not rated_companies and not all_companies:
        st.warning("No company data available or unable to connect to API.")
        st.info("Please ensure the backend API is running and accessible.")
        return
    
    # Debug: Show raw data for troubleshooting
    if st.checkbox("🔍 Show Debug Info"):
        st.subheader("Debug Information")
        st.write("**Rated Companies Data:**")
        st.json(rated_companies)
        st.write("**All Companies Data:**")
        st.json(all_companies)
        st.divider()
    
    # Display summary statistics
    if rated_companies:
        total_rated = len(rated_companies)
        
        # Ensure ratings are converted to float and handle any None values
        ratings = []
        for comp in rated_companies:
            rating = comp.get('avgCompanyRating')
            if rating is not None:
                try:
                    ratings.append(float(rating))
                except (ValueError, TypeError):
                    continue
        
        if ratings:
            avg_rating = sum(ratings) / len(ratings)
            top_company = max(rated_companies, key=lambda x: float(x.get('avgCompanyRating', 0)) if x.get('avgCompanyRating') is not None else 0)
        else:
            avg_rating = 0
            top_company = rated_companies[0] if rated_companies else None
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Companies with Ratings", total_rated)
        with col2:
            st.metric("Overall Average Rating", f"{avg_rating:.1f}/5.0")
        with col3:
            company_name = top_company.get('companyName', 'N/A') if top_company else 'N/A'
            st.metric("Top Rated Company", company_name)
        
        st.divider()
    
    # Add filtering options
    if rated_companies:
        industries = list(set(comp.get('companyIndustry', 'Unknown') for comp in rated_companies))
        industries.sort()
        
        col1, col2 = st.columns([1, 3])
        with col1:
            selected_industry = st.selectbox("Filter by Industry", ["All Industries"] + industries)
        
        # Filter companies by industry if selected
        if selected_industry != "All Industries":
            filtered_companies = [comp for comp in rated_companies if comp.get('companyIndustry') == selected_industry]
            st.info(f"Showing {len(filtered_companies)} companies in {selected_industry}")
        else:
            filtered_companies = rated_companies
    else:
        filtered_companies = []
    
    # Display companies with ratings
    if filtered_companies:
        st.subheader("🏆 Companies with Student Ratings")
        st.markdown("*Sorted by average rating (highest first)*")
        
        # Create a DataFrame-like display using Streamlit
        col1, col2, col3, col4, col5 = st.columns([3, 1, 1, 1, 2])
        
        with col1:
            st.write("**Company Name**")
        with col2:
            st.write("**Avg Rating**")
        with col3:
            st.write("**Count**")
        with col4:
            st.write("**Industry**")
        with col5:
            st.write("**Website**")
        
        st.divider()
        
        for company in filtered_companies:
            col1, col2, col3, col4, col5 = st.columns([3, 1, 1, 1, 2])
            
            with col1:
                st.write(f"**{company.get('companyName', 'N/A')}**")
            with col2:
                avg_rating = company.get('avgCompanyRating', 0)
                if avg_rating is not None:
                    try:
                        avg_rating = float(avg_rating)
                        # Display rating with color coding
                        if avg_rating >= 4.0:
                            st.success(f"{avg_rating:.1f}/5.0 ⭐")
                        elif avg_rating >= 3.0:
                            st.info(f"{avg_rating:.1f}/5.0")
                        else:
                            st.warning(f"{avg_rating:.1f}/5.0")
                    except (ValueError, TypeError):
                        st.write("Invalid rating")
                else:
                    st.write("No ratings")
            with col3:
                rating_count = company.get('ratingCount', 0)
                st.write(f"{rating_count}")
            with col4:
                industry = company.get('companyIndustry', 'N/A')
                st.write(industry)
            with col5:
                website = company.get('companyWebsite', 'N/A')
                if website and website != 'N/A':
                    st.write(f"[{website}](https://{website})")
                else:
                    st.write("N/A")
            
            st.divider()
    
    # Display companies without ratings
    if all_companies:
        # Find companies without ratings
        rated_company_names = {comp.get('companyName') for comp in rated_companies}
        unrated_companies = [comp for comp in all_companies if comp.get('name') not in rated_company_names]
        
        if unrated_companies:
            st.subheader("📋 Companies Awaiting Student Feedback")
            st.markdown("*Companies that haven't received ratings yet*")
            
            col1, col2, col3 = st.columns([3, 2, 2])
            
            with col1:
                st.write("**Company Name**")
            with col2:
                st.write("**Industry**")
            with col3:
                st.write("**Website**")
            
            st.divider()
            
            for company in unrated_companies:
                col1, col2, col3 = st.columns([3, 2, 2])
                
                with col1:
                    st.write(company.get('name', 'N/A'))
                with col2:
                    st.write(company.get('industry', 'N/A'))
                with col3:
                    website = company.get('websiteLink', 'N/A')
                    if website and website != 'N/A':
                        st.write(f"[{website}](https://{website})")
                    else:
                        st.write("N/A")
                
                st.divider()

# Main content
try:
    display_company_ratings()
except Exception as e:
    st.error(f"An error occurred: {str(e)}")
    logger.error(f"Error in display_company_ratings: {str(e)}")

# Add some additional information
st.markdown("---")
st.markdown("""
**Note:** This data is based on student feedback from completed co-op experiences.
Companies are sorted by their average rating to help identify the most successful partnerships.
Companies without ratings may be new partners or haven't had students complete co-ops yet.
""")


