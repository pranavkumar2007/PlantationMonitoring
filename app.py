import streamlit as st
from home import show_home
from dashboard import show_dashboard
from about import show_about
from contact import show_contact
from signup import signup_view, login_view

# ---- Custom CSS for sidebar and theme ----
st.markdown("""
<style>
/* Sidebar container */
[data-testid="stSidebar"] > div:first-child {
    background: linear-gradient(135deg, #232946 0%, #2b2c45 100%);
    height: 100%;
    padding: 2.2rem 1.6rem 2.2rem 1.6rem;   /* Top, Right, Bottom, Left */
    box-shadow: 2px 0 20px rgba(60,90,170,0.06);
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: stretch;
}

/* Sidebar logo/title */
.sidebar-logo {
    text-align: left;
    font-size: 1.4rem;
    font-weight: bold;
    color: #f4f4f7;
    letter-spacing: 1px;
    margin-bottom: 2rem;
    padding-bottom: 2rem;
    margin-top: 0;
}
.sidebar-subtitle {
    color: #a6a7b0;
    text-align: center;
    font-size: 1rem;
    margin-bottom: 2.2rem;
}
/* Nav alignment and radio-label clean up */
label[role="radio"] {
    margin-bottom: 0.45rem;
    padding-left: 0.28rem;
}
.stRadio > div { gap: .7rem; }
section[tabindex="0"] div[data-testid="stRadio"] > label {
    justify-content: flex-start !important;
}
div[data-testid="stSidebarNav"] { margin-bottom: 2rem !important; }

.stSidebar .element-container button, .sidebar-nav .nav-btn {
    width: 100%;
    padding: 1rem;
    margin: 1.1rem 0 0.8rem 0;
    font-weight: bold;
    border-radius: 10px;
    color: #f4f4f7;
    background: linear-gradient(90deg,#667eea 0%, #764ba2 100%);
    border: none;
    font-size: 1rem;
    transition: background 0.2s,box-shadow 0.2s;
    box-shadow: 0 2px 8px rgba(102,126,234,0.08);
}
.stSidebar .element-container button:hover, .sidebar-nav .nav-btn:hover {
    background: linear-gradient(90deg,#764ba2 0%,#667eea 100%);
    color: #fff;
    transform: scale(1.04);
}
.sidebar-logout {
    margin-top: 2.7rem;
    background: #232946 !important;
    color: #ff6262 !important;
    border: 2px solid #ff6262 !important;
    font-weight: bold;
    transition: background 0.18s;
}
.sidebar-logout:hover {
    background: #ff6262 !important;
    color: #fff !important;
    border-color: #ff8484 !important;
}
/* Fine-tune icon/social block */
.sidebar-social {
    font-size:1.18rem;
    color:#a6a7b0;
    text-align:center;
    margin-top:2.3rem;
    letter-spacing:0.16em;
}
@media (max-width: 950px) {
    [data-testid="stSidebar"] > div:first-child {
        min-width: 148px !important;
        max-width: 196px !important;
        padding: 1rem 0.7rem 1rem 0.8rem !important;
    }
    .sidebar-logo { font-size: 1.08rem; }
    .sidebar-subtitle { font-size: .90rem; }
    .sidebar-social { font-size: 1rem; }
}
</style>
""", unsafe_allow_html=True)

# --------- SESSION / AUTH MANAGEMENT ----------
if "page" not in st.session_state:
    st.session_state["page"] = "home"
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if "user_data" not in st.session_state:
    st.session_state["user_data"] = None

# --------- ROUTING: Always homepage first ---------
if not st.session_state["logged_in"]:
    if st.session_state["page"] == "home":
        show_home()
    elif st.session_state["page"] == "login":
        login_view()
    elif st.session_state["page"] == "signup":
        signup_view()
    else:
        st.session_state["page"] = "home"
        st.rerun()
else:
    with st.sidebar:
        st.markdown('<div class="sidebar-logo">Plantation Monitoring</div>', unsafe_allow_html=True)
        menu = st.radio(
            "Jump to Page", 
            ["Dashboard", "About Us", "Contact Us"], 
            index=["dashboard", "about", "contact"].index(st.session_state["page"]) 
            if st.session_state["page"] in ["dashboard", "about", "contact"] else 0
        )
        if st.button("Logout", key="sidebar_logout", help="Sign out of your session", use_container_width=True):
            st.session_state["logged_in"] = False
            st.session_state["user_data"] = None
            st.session_state["page"] = "home"
            st.rerun()

    # ---- route to page ----
    if menu == "Dashboard":
        st.session_state["page"] = "dashboard"
    elif menu == "About Us":
        st.session_state["page"] = "about"
    elif menu == "Contact Us":
        st.session_state["page"] = "contact"
    if st.session_state["page"] == "dashboard":
        show_dashboard()
    elif st.session_state["page"] == "about":
        show_about()
    elif st.session_state["page"] == "contact":
        show_contact()
    else:
        show_dashboard()
