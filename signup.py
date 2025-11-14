import streamlit as st
from database import Database

# Initialize database
db = Database()

# Custom CSS for enhanced UI
st.markdown("""
<style>
/* Remove default Streamlit padding */
.block-container {
    padding-top: 0rem !important;
    padding-bottom: 2rem !important;
}
.main-container {
    max-width: 500px;
    margin: 0 auto;
    padding: 0 1rem;
}
/* Header styling */
.portal-header {
    text-align: center;
    margin-bottom: 0rem;
    margin-top: 0;
    padding-bottom: 0rem;
    border-bottom: 2px solid rgba(255, 255, 255, 0.1);
}
.portal-header h1 {
    font-size: 2.5rem;
    font-weight: 700;
    margin-bottom: 0.5rem;
    margin-top: 0;
    color: #fff;
}
.portal-subtitle {
    color: #888;
    font-size: 0.95rem;
    margin-top: 0.5rem;
}
/* Main vertical spacing before footer */
.form-bottom-gap { height: 40px !important; }
/* Footer */
.portal-footer {
    text-align: center;
    margin-top: 2rem;
    padding-top: 1.5rem;
    border-top: 1px solid rgba(255, 255, 255, 0.1);
    color: #888;
    font-size: 0.85rem;
}
/* Form container and gap */
.form-container {
    background: rgba(255, 255, 255, 0.02);
    border-radius: 12px;
    padding: 2rem;
    margin-top: 1.5rem;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    border: 1px solid rgba(255, 255, 255, 0.05);
}
.action-link {
    text-align: center;
    margin: 1.5rem 0 2.5rem 0;
}
/* Input field styling */
.stTextInput > div > div > input {
    border-radius: 8px;
    border: 1.5px solid rgba(255, 255, 255, 0.1);
    padding: 0.75rem;
    font-size: 0.95rem;
    transition: all 0.3s ease;
}
.stTextInput > div > div > input:focus {
    border-color: #667eea;
    box-shadow: 0 0 0 2px rgba(102, 126, 234, 0.2);
}
/* Label styling */
.stTextInput > label {
    font-weight: 600;
    font-size: 0.9rem;
    margin-bottom: 0.5rem;
    color: #ddd;
}
/* Submit & main button styling */
.stButton > button, div[data-testid="column"] > div > div > button[kind="primary"] {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    border: none;
    padding: 1rem;
    font-size: 1rem;
    font-weight: 600;
    margin-top: 1rem;
    width: 100%;
    border-radius: 8px;
    box-shadow: 0 1.5px 4px rgba(102, 126, 234, 0.05);
    color: #fff;
    transition: all 0.3s ease;
}
.stButton > button:hover, div[data-testid="column"] > div > div > button[kind="primary"]:hover {
    transform: translateY(-2px) scale(1.03);
    box-shadow: 0 6px 20px rgba(102, 126, 234, 0.3);
}
/* Rounded messages */
.stSuccess, .stWarning, .stError {
    border-radius: 8px;
    margin-top: 1rem;
}
.element-container { margin-bottom: 1rem; }
.main .block-container > div:first-child { margin-top: 0 !important; }
/* Center form submit blocks on small screens */
@media (max-width: 600px) {
    .main-container, .form-container {
        padding: 0 .5rem;
    }
}
</style>
""", unsafe_allow_html=True)


def login_view():
    st.markdown("""
    <div class="portal-header">
        <h1>User Portal</h1>
        <p class="portal-subtitle">Welcome! Please login or create a new account</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("### 👋 Welcome Back")
    st.markdown("<p style='color: #888; margin-bottom: 0.5rem;'>Enter your credentials to continue</p>", unsafe_allow_html=True)
    
    username = st.text_input("Username", key="login_username", placeholder="Enter your username")
    password = st.text_input("Password", type="password", key="login_password", placeholder="Enter your password")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        login_btn = st.button("Login", key="login_submit", use_container_width=True, type="primary")
    
    if login_btn:
        if username and password:
            success, result = db.verify_user(username, password)
            if success:
                st.session_state['logged_in'] = True
                st.session_state['user_data'] = result
                st.success(f"✅ Welcome back, {username}!")
                st.balloons()
                st.session_state['page'] = 'dashboard'
                st.rerun()
            else:
                st.error(f"❌ {result}")
        else:
            st.warning("⚠️ Please fill in all fields.")

    # Optional: Switch to signup if needed
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Don't have an account? Sign Up"):
        st.session_state['page'] = 'signup'
        st.rerun()

    st.markdown("""
    <div class="portal-footer">
        <p>© 2025 Plantation Monitoring System. All rights reserved.</p>
    </div>
    """, unsafe_allow_html=True)

def login_view():
    st.markdown("""
    <div class="portal-header">
        <h1>User Portal</h1>
        <p class="portal-subtitle">Welcome! Please login or create a new account</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("### 👋 Welcome Back")
    st.markdown("<div style='color: #888; margin-bottom: 0.5rem;'>Enter your credentials to continue</div>", unsafe_allow_html=True)
    
    with st.form("login_form", clear_on_submit=False):
        username = st.text_input("Username", key="login_username", placeholder="Enter your username")
        password = st.text_input("Password", type="password", key="login_password", placeholder="Enter your password")
        submitted = st.form_submit_button("Login", type="primary")
        msg_space = st.empty()
    
    if submitted:
        if username and password:
            success, result = db.verify_user(username, password)
            if success:
                st.session_state['logged_in'] = True
                st.session_state['user_data'] = result
                st.success(f"✅ Welcome back, {username}!")
                st.balloons()
                st.session_state['page'] = 'dashboard'
                st.rerun()
            else:
                msg_space.error(f"❌ {result}")
        else:
            msg_space.warning("⚠️ Please fill in all fields.")

    # Centered action-link style
    st.markdown('<div class="action-link">', unsafe_allow_html=True)
    if st.button("✨ Don't have an account? Sign Up", key="to_signup"):
        st.session_state['page'] = 'signup'
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="form-bottom-gap"></div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="portal-footer">
        <p>© 2025 Plantation Monitoring System. All rights reserved.</p>
    </div>
    """, unsafe_allow_html=True)

def signup_view():
    st.markdown("""
    <div class="portal-header">
        <h1>User Portal</h1>
        <p class="portal-subtitle">Welcome! Please login or create a new account</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("### 🚀 Create Account")
    st.markdown("<div style='color: #888; margin-bottom: 0.5rem;'>Fill in the details to get started</div>", unsafe_allow_html=True)
    
    with st.form("signup_form", clear_on_submit=False):
        new_username = st.text_input("Username", key="signup_username", placeholder="Choose a username")
        email = st.text_input("Email", key="signup_email", placeholder="your.email@example.com")
        new_password = st.text_input("Password", type="password", key="signup_password", placeholder="Create a strong password")
        confirm = st.text_input("Confirm Password", type="password", key="signup_confirm", placeholder="Confirm your password")
        submitted = st.form_submit_button("Sign Up", type="primary")
        msg_space = st.empty()

    if submitted:
        if not all([new_username, email, new_password, confirm]):
            msg_space.warning("⚠️ Please fill in all fields.")
        elif new_password != confirm:
            msg_space.warning("⚠️ Passwords do not match.")
        elif len(new_password) < 6:
            msg_space.warning("⚠️ Password must be at least 6 characters long.")
        else:
            success, message = db.create_user(new_username, email, new_password)
            if success:
                msg_space.success(f"✅ {message}")
                st.balloons()
                st.session_state['page'] = 'login'
                st.rerun()
            else:
                msg_space.error(f"❌ {message}")
    
    st.markdown('<div class="action-link">', unsafe_allow_html=True)
    if st.button("🔐 Already have an account? Login", key="to_login"):
        st.session_state['page'] = 'login'
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="form-bottom-gap"></div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="portal-footer">
        <p>© 2025 Plantation Monitoring System. All rights reserved.</p>
    </div>
    """, unsafe_allow_html=True)