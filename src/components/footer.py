import streamlit as st

def footer_home():

    logo_url = "https://images.seeklogo.com/logo-png/45/1/national-institute-of-technology-calicut-logo-png_seeklogo-458279.png"
    st.markdown(f"""
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-top:2rem; gap:3px;">
            <p style='font-weight:bold; color:white;'>Created with ❤️ by</p>
            <img src='{logo_url}' style='max-height:50px' />
        </div>
    """, unsafe_allow_html=True)

def footer_dashboard():

    logo_url = "https://images.seeklogo.com/logo-png/45/1/national-institute-of-technology-calicut-logo-png_seeklogo-458279.png"
    st.markdown(f"""
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-top:2rem; gap:3px;">
            <p style='font-weight:bold; color:black;'>Created with ❤️ by</p>
            <img src='{logo_url}' style='max-height:50px' />
        </div>
    """, unsafe_allow_html=True)