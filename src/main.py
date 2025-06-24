# -----------------------------------------------------------------------------
# Organization: CEDA
# Original Author: Ash Sewnandan
# Contributors: -
# License: MIT
# -----------------------------------------------------------------------------
"""
Main Entrypoint for the 1CIJFERHO App
"""
import streamlit as st

# -----------------------------------------------------------------------------
# Pages Overview - YOU CAN ADD MORE PAGES HERE
# -----------------------------------------------------------------------------
home_page = st.Page("frontend/Overview/Home.py", icon="🏠", title="Home")
documentation_page = st.Page("frontend/Overview/Documentation.py", icon="📚", title="Documentation")

data_upload_page = st.Page("frontend/Files/Upload_Data.py", icon="📁", title="Upload Data")

extract_page = st.Page("frontend/Modules/Extract_Metadata.py", icon="🔍", title="Extract Metadata")
validate_page = st.Page("frontend/Modules/Validate_Metadata.py", icon="🛡️", title="Validate Metadata")
turbo_convert_page = st.Page("frontend/Modules/Turbo_Convert.py", icon="⚡", title="Turbo Convert")

# -----------------------------------------------------------------------------
# Sidebar Configuration
# -----------------------------------------------------------------------------
# Add Logo
LOGO_URL = "src/assets/npuls_logo.png"
st.logo(LOGO_URL)

# Initialize Navigation
pg = st.navigation ( {
    "Overview": [home_page, documentation_page],
    "Files": [data_upload_page],
    "Modules": [extract_page, validate_page, turbo_convert_page],
})

# -----------------------------------------------------------------------------
# Run the app
# -----------------------------------------------------------------------------
pg.run()