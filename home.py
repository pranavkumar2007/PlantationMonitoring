import streamlit as st

def show_home():
    
    # Hero Section
    st.title("🌱 Plantation Monitoring System")
    
    st.markdown("""
    <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                padding: 2rem; border-radius: 12px; margin-bottom: 2rem; text-align: center;
                box-shadow: 0 6px 20px rgba(102, 126, 234, 0.3);'>
        <h3 style='color:white;margin:0;font-size:1.8rem;font-weight:600;'>Smart Agriculture Powered by Artificial Intelligence</h3>
        <p style='color: rgba(255,255,255,0.95); margin-top: 1rem; font-size: 1rem; line-height: 1.6;'>
            Upload drone or aerial images to automatically segment and classify crops using advanced AI models
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Quick Start Guide
    st.subheader("🚀 Quick Start Guide")
    
    st.markdown("""
    <style>
    .corner-login-signup {
        position: absolute;
        top: 0;
        right: 2.5rem;
        z-index: 9999;
        display: flex;
        gap: 0.5rem;
    }
    </style>
    <div class="corner-login-signup"></div>
    """, unsafe_allow_html=True)
    login_col, signup_col = st.columns([1,1])
    with login_col:
        if st.button("🔐 Login", key="corner_login_btn", use_container_width=True):
            st.session_state["page"] = "login"
            st.rerun()
    with signup_col:
        if st.button("✨ Sign Up", key="corner_signup_btn", use_container_width=True):
            st.session_state["page"] = "signup"
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    step_cols = st.columns(3)
    
    with step_cols[0]:
        st.markdown("""
        <div style='background: rgba(255, 255, 255, 0.02); 
                    padding: 1.5rem; border-radius: 12px; margin-bottom: 1rem;
                    border: 1px solid rgba(255, 255, 255, 0.05);
                    border-left: 4px solid #667eea;
                    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
                    text-align: center;
                    transition: transform 0.3s ease;'
                    onmouseover='this.style.transform="translateY(-5px)"; this.style.boxShadow="0 8px 25px rgba(102, 126, 234, 0.2)";'
                    onmouseout='this.style.transform="translateY(0)"; this.style.boxShadow="0 4px 15px rgba(0, 0, 0, 0.1)";'>
            <div style='font-size: 3rem; margin-bottom: 0.5rem;'>📤</div>
            <h4 style='color: #667eea; margin: 0.5rem 0; font-weight: 600;'>Step 1: Upload</h4>
            <p style='color: #ddd; margin: 0; font-size: 0.95rem; line-height: 1.5;'>
                Upload your drone or aerial plantation images in JPG, PNG, or JPEG format
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with step_cols[1]:
        st.markdown("""
        <div style='background: rgba(255, 255, 255, 0.02); 
                    padding: 1.5rem; border-radius: 12px; margin-bottom: 1rem;
                    border: 1px solid rgba(255, 255, 255, 0.05);
                    border-left: 4px solid #667eea;
                    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
                    text-align: center;
                    transition: transform 0.3s ease;'
                    onmouseover='this.style.transform="translateY(-5px)"; this.style.boxShadow="0 8px 25px rgba(102, 126, 234, 0.2)";'
                    onmouseout='this.style.transform="translateY(0)"; this.style.boxShadow="0 4px 15px rgba(0, 0, 0, 0.1)";'>
            <div style='font-size: 3rem; margin-bottom: 0.5rem;'>🔎</div>
            <h4 style='color: #667eea; margin: 0.5rem 0; font-weight: 600;'>Step 2: Analyze</h4>
            <p style='color: #ddd; margin: 0; font-size: 0.95rem; line-height: 1.5;'>
                Our AI models automatically segment and identify individual crops in your images
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with step_cols[2]:
        st.markdown("""
        <div style='background: rgba(255, 255, 255, 0.02); 
                    padding: 1.5rem; border-radius: 12px; margin-bottom: 1rem;
                    border: 1px solid rgba(255, 255, 255, 0.05);
                    border-left: 4px solid #667eea;
                    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
                    text-align: center;
                    transition: transform 0.3s ease;'
                    onmouseover='this.style.transform="translateY(-5px)"; this.style.boxShadow="0 8px 25px rgba(102, 126, 234, 0.2)";'
                    onmouseout='this.style.transform="translateY(0)"; this.style.boxShadow="0 4px 15px rgba(0, 0, 0, 0.1)";'>
            <div style='font-size: 3rem; margin-bottom: 0.5rem;'>📊</div>
            <h4 style='color: #667eea; margin: 0.5rem 0; font-weight: 600;'>Step 3: Review</h4>
            <p style='color: #ddd; margin: 0; font-size: 0.95rem; line-height: 1.5;'>
                Get detailed insights, classifications, and visualizations of your plantation data
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # What We Offer
    st.subheader("💡 What We Offer")
    
    feature_col1, feature_col2 = st.columns(2)
    
    with feature_col1:
        st.markdown("""
        <div style='background: rgba(255, 255, 255, 0.02); 
                    padding: 1.5rem; border-radius: 12px; margin-bottom: 1rem;
                    border: 1px solid rgba(255, 255, 255, 0.05);
                    border-left: 4px solid #667eea;
                    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
                    transition: transform 0.3s ease;'
                    onmouseover='this.style.transform="translateX(5px)"; this.style.boxShadow="0 6px 20px rgba(102, 126, 234, 0.2)";'
                    onmouseout='this.style.transform="translateX(0)"; this.style.boxShadow="0 4px 15px rgba(0, 0, 0, 0.1)";'>
            <h4 style='color: #667eea; margin-top: 0; font-weight: 600;'>🎭 Advanced Image Segmentation</h4>
            <p style='color: #ddd; margin: 0; line-height: 1.6;'>
                Powered by Meta's SAM (Segment Anything Model), we provide pixel-perfect 
                segmentation of individual plants, enabling precise monitoring and analysis 
                of each crop in your plantation.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style='background: rgba(255, 255, 255, 0.02); 
                    padding: 1.5rem; border-radius: 12px; margin-bottom: 1rem;
                    border: 1px solid rgba(255, 255, 255, 0.05);
                    border-left: 4px solid #764ba2;
                    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
                    transition: transform 0.3s ease;'
                    onmouseover='this.style.transform="translateX(5px)"; this.style.boxShadow="0 6px 20px rgba(118, 75, 162, 0.2)";'
                    onmouseout='this.style.transform="translateX(0)"; this.style.boxShadow="0 4px 15px rgba(0, 0, 0, 0.1)";'>
            <h4 style='color: #764ba2; margin-top: 0; font-weight: 600;'>📈 Real-Time Monitoring</h4>
            <p style='color: #ddd; margin: 0; line-height: 1.6;'>
                Track the health and growth of your plantation in real-time. Get instant 
                alerts and insights to make informed decisions quickly and efficiently.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with feature_col2:
        st.markdown("""
        <div style='background: rgba(255, 255, 255, 0.02); 
                    padding: 1.5rem; border-radius: 12px; margin-bottom: 1rem;
                    border: 1px solid rgba(255, 255, 255, 0.05);
                    border-left: 4px solid #667eea;
                    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
                    transition: transform 0.3s ease;'
                    onmouseover='this.style.transform="translateX(5px)"; this.style.boxShadow="0 6px 20px rgba(102, 126, 234, 0.2)";'
                    onmouseout='this.style.transform="translateX(0)"; this.style.boxShadow="0 4px 15px rgba(0, 0, 0, 0.1)";'>
            <h4 style='color: #667eea; margin-top: 0; font-weight: 600;'>🧠 Smart Crop Classification</h4>
            <p style='color: #ddd; margin: 0; line-height: 1.6;'>
                Using ResNet50 deep learning architecture, our system accurately identifies 
                and classifies multiple crop types, helping you maintain organized and 
                efficient plantation records.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style='background: rgba(255, 255, 255, 0.02); 
                    padding: 1.5rem; border-radius: 12px; margin-bottom: 1rem;
                    border: 1px solid rgba(255, 255, 255, 0.05);
                    border-left: 4px solid #764ba2;
                    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
                    transition: transform 0.3s ease;'
                    onmouseover='this.style.transform="translateX(5px)"; this.style.boxShadow="0 6px 20px rgba(118, 75, 162, 0.2)";'
                    onmouseout='this.style.transform="translateX(0)"; this.style.boxShadow="0 4px 15px rgba(0, 0, 0, 0.1)";'>
            <h4 style='color: #764ba2; margin-top: 0; font-weight: 600;'>🌍 Scalable Solution</h4>
            <p style='color: #ddd; margin: 0; line-height: 1.6;'>
                From small farms to large-scale plantations, our system scales to meet 
                your needs. Process thousands of images efficiently with consistent accuracy.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Technology Highlights
    st.subheader("⚡ Powered By Cutting-Edge AI")
    
    tech_cols = st.columns(2)
    
    with tech_cols[0]:
        st.markdown("""
        <div style='background: rgba(255, 255, 255, 0.02); 
                    padding: 2rem; border-radius: 12px; text-align: center;
                    border: 1px solid rgba(255, 255, 255, 0.05);
                    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
                    transition: transform 0.3s ease;'
                    onmouseover='this.style.transform="scale(1.02)"; this.style.boxShadow="0 8px 25px rgba(102, 126, 234, 0.2)";'
                    onmouseout='this.style.transform="scale(1)"; this.style.boxShadow="0 4px 15px rgba(0, 0, 0, 0.1)";'>
            <div style='font-size: 3rem; margin-bottom: 1rem;'>🎭</div>
            <h3 style='color: #667eea; margin: 0.5rem 0; font-weight: 600;'>Meta's SAM</h3>
            <p style='color: #ddd; margin: 0; line-height: 1.6;'>
                Segment Anything Model for precise boundary detection and plant identification
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with tech_cols[1]:
        st.markdown("""
        <div style='background: rgba(255, 255, 255, 0.02); 
                    padding: 2rem; border-radius: 12px; text-align: center;
                    border: 1px solid rgba(255, 255, 255, 0.05);
                    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
                    transition: transform 0.3s ease;'
                    onmouseover='this.style.transform="scale(1.02)"; this.style.boxShadow="0 8px 25px rgba(118, 75, 162, 0.2)";'
                    onmouseout='this.style.transform="scale(1)"; this.style.boxShadow="0 4px 15px rgba(0, 0, 0, 0.1)";'>
            <div style='font-size: 3rem; margin-bottom: 1rem;'>🧠</div>
            <h3 style='color: #764ba2; margin: 0.5rem 0; font-weight: 600;'>ResNet50</h3>
            <p style='color: #ddd; margin: 0; line-height: 1.6;'>
                Deep residual learning for robust crop classification and identification
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Benefits Section
    st.subheader("🌟 Why Choose Our System?")
    
    benefit_cols = st.columns(4)
    
    with benefit_cols[0]:
        st.markdown("""
        <div style='background: rgba(255, 255, 255, 0.02); 
                    padding: 1.5rem; border-radius: 12px; text-align: center;
                    border: 1px solid rgba(255, 255, 255, 0.05);
                    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
                    transition: transform 0.3s ease;'
                    onmouseover='this.style.transform="translateY(-5px)"; this.style.boxShadow="0 8px 25px rgba(102, 126, 234, 0.2)";'
                    onmouseout='this.style.transform="translateY(0)"; this.style.boxShadow="0 4px 15px rgba(0, 0, 0, 0.1)";'>
            <div style='font-size: 2.5rem; margin-bottom: 0.5rem;'>⚡</div>
            <h4 style='color: #667eea; margin: 0.5rem 0; font-weight: 600;'>Fast</h4>
            <p style='color: #ddd; margin: 0; font-size: 0.9rem;'>
                Quick processing and instant results
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with benefit_cols[1]:
        st.markdown("""
        <div style='background: rgba(255, 255, 255, 0.02); 
                    padding: 1.5rem; border-radius: 12px; text-align: center;
                    border: 1px solid rgba(255, 255, 255, 0.05);
                    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
                    transition: transform 0.3s ease;'
                    onmouseover='this.style.transform="translateY(-5px)"; this.style.boxShadow="0 8px 25px rgba(102, 126, 234, 0.2)";'
                    onmouseout='this.style.transform="translateY(0)"; this.style.boxShadow="0 4px 15px rgba(0, 0, 0, 0.1)";'>
            <div style='font-size: 2.5rem; margin-bottom: 0.5rem;'>🎯</div>
            <h4 style='color: #667eea; margin: 0.5rem 0; font-weight: 600;'>Accurate</h4>
            <p style='color: #ddd; margin: 0; font-size: 0.9rem;'>
                95%+ accuracy in crop identification
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with benefit_cols[2]:
        st.markdown("""
        <div style='background: rgba(255, 255, 255, 0.02); 
                    padding: 1.5rem; border-radius: 12px; text-align: center;
                    border: 1px solid rgba(255, 255, 255, 0.05);
                    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
                    transition: transform 0.3s ease;'
                    onmouseover='this.style.transform="translateY(-5px)"; this.style.boxShadow="0 8px 25px rgba(102, 126, 234, 0.2)";'
                    onmouseout='this.style.transform="translateY(0)"; this.style.boxShadow="0 4px 15px rgba(0, 0, 0, 0.1)";'>
            <div style='font-size: 2.5rem; margin-bottom: 0.5rem;'>🔒</div>
            <h4 style='color: #667eea; margin: 0.5rem 0; font-weight: 600;'>Secure</h4>
            <p style='color: #ddd; margin: 0; font-size: 0.9rem;'>
                Your data is safe and private
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with benefit_cols[3]:
        st.markdown("""
        <div style='background: rgba(255, 255, 255, 0.02); 
                    padding: 1.5rem; border-radius: 12px; text-align: center;
                    border: 1px solid rgba(255, 255, 255, 0.05);
                    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
                    transition: transform 0.3s ease;'
                    onmouseover='this.style.transform="translateY(-5px)"; this.style.boxShadow="0 8px 25px rgba(102, 126, 234, 0.2)";'
                    onmouseout='this.style.transform="translateY(0)"; this.style.boxShadow="0 4px 15px rgba(0, 0, 0, 0.1)";'>
            <div style='font-size: 2.5rem; margin-bottom: 0.5rem;'>💰</div>
            <h4 style='color: #667eea; margin: 0.5rem 0; font-weight: 600;'>Cost-Effective</h4>
            <p style='color: #ddd; margin: 0; font-size: 0.9rem;'>
                Reduce manual monitoring costs
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Call to Action
    st.markdown("""
    <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                padding: 2.5rem; border-radius: 12px; text-align: center;
                box-shadow: 0 6px 20px rgba(102, 126, 234, 0.3);'>
        <h3 style='color: white; margin-top: 0; font-weight: 600;'>🚀 Ready to Get Started?</h3>
        <p style='color: rgba(255,255,255,0.95); margin-bottom: 1rem; font-size: 1.1rem; line-height: 1.6;'>
            Navigate to the <strong>Dashboard</strong> page to upload your plantation images
            and experience the power of AI-driven crop monitoring!
        </p>
        <p style='color: rgba(255,255,255,0.9); margin: 0; font-size: 0.95rem;'>
            ⬅️ Use the sidebar to explore all features
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)

    # Footer
    st.markdown("""
    <div style='margin-top: 3rem; padding-top: 2rem; 
                border-top: 1px solid rgba(255, 255, 255, 0.1);'>
        <div style='text-align: center;'>
            <p style='color: #888; margin-bottom: 0.5rem; font-size: 0.9rem;'>Connect with us on social media</p>
            <p style='font-size: 1.5rem; margin: 1rem 0;'>
                🌐 💼 📱 
            </p>
            <p style='color: #888; font-size: 0.85rem; margin-top: 1.5rem;'>
                © 2025 Plantation Monitoring System. All rights reserved.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)