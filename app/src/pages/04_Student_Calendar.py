import calendar
import datetime
import streamlit as st
import pandas as pd
import requests
from modules.nav import SideBarLinks

# Setup
st.set_page_config(layout="wide")
SideBarLinks()
API_BASE_URL = "http://web-api:4000"
charlie_user_id = st.session_state.get("user_id", None)
if charlie_user_id is None:
    st.error("🚫 User not logged in. Please return to the home page and log in.")
    st.stop()

# Fetch deadlines
def fetch_flagged_deadlines(user_id):
    try:
        url = f"{API_BASE_URL}/{user_id}/deadlines"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Failed to fetch deadlines: {response.status_code}")
            return []
    except Exception as e:
        st.error(f"Error fetching deadlines: {e}")
        return []

deadlines = fetch_flagged_deadlines(charlie_user_id)

# Convert to DataFrame and preprocess
if deadlines:
    df = pd.DataFrame(deadlines)
    df['deadline'] = pd.to_datetime(df['deadline']).dt.date
else:
    df = pd.DataFrame(columns=["title", "deadline"])

st.title("📅 Your Position Deadline Calendar")

# Select month and year for calendar view
col1, col2 = st.columns(2)
today = datetime.date.today()
with col1:
    year = st.number_input("Year", min_value=2000, max_value=2100, value=today.year)
with col2:
    month = st.selectbox("Month", list(calendar.month_name)[1:], index=today.month - 1)

# Now use the selected month and year
st.subheader(f"{month} {year}")

month_num = list(calendar.month_name).index(month)

# Generate calendar matrix for the selected month and year
cal = calendar.monthcalendar(year, month_num)

# Helper: group positions by deadline date
positions_by_date = {}
for _, row in df.iterrows():
    positions_by_date.setdefault(row['deadline'], []).append(row['title'])

# Display calendar grid
days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
cols = st.columns(7)
for i, day in enumerate(days_of_week):
    cols[i].markdown(f"**{day}**")

for week in cal:
    cols = st.columns(7)
    for i, day in enumerate(week):
        if day == 0:
            # Empty cell (day belongs to adjacent month)
            cols[i].markdown(" ")
        else:
            date_obj = datetime.date(year, month_num, day)
            pos_titles = positions_by_date.get(date_obj, [])
            # Show date number
            day_str = f"**{day}**"
            # Show position titles (up to 2, else show count)
            if pos_titles:
                if len(pos_titles) <= 2:
                    events_str = "\n".join([f"- {title}" for title in pos_titles])
                else:
                    events_str = "\n".join([f"- {title}" for title in pos_titles[:2]])
                    events_str += f"\n- +{len(pos_titles)-2} more"
                cols[i].markdown(f"{day_str}\n{events_str}")
            else:
                cols[i].markdown(day_str)

if df.empty:
    st.info("📭 You haven’t flagged any positions yet. Flag some positions to see their deadlines here!")
