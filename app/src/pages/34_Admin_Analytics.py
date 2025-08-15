import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import time

import logging
logging.basicConfig(format='%(filename)s:%(lineno)s:%(levelname)s -- %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

from modules.nav import SideBarLinks

st.set_page_config(layout='wide')
SideBarLinks()

st.title("📊Admin Analytics Dashboard")
