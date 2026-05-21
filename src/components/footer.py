import streamlit as st

def footer_home():

    logo_url = "https://ninahands.in/wp-content/uploads/2019/12/NIT-calicut-LOGO.jpg"
    st.markdown("""
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-top:2rem; gap:6px;">
            <p style='font-weight:bold; color:white;'>Created with ❤️ by</p>
            <img src='{logo_url}' style='max-height:25px' />
        </div>
    """, unsafe_allow_html=True)

def footer_dashboard():

    logo_url = "https://ninahands.in/wp-content/uploads/2019/12/NIT-calicut-LOGO.jpg"
    st.markdown("""
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-top:2rem; gap:6px;">
            <p style='font-weight:bold; color:black;'>Created with ❤️ by</p>
            <img src='{logo_url}' style='max-height:25px' />
        </div>
    """, unsafe_allow_html=True)