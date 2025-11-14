import streamlit as st
def show_about():
    st.title("ℹ️ About Us")
    
    # Hero Section
    st.markdown("""
    <div style='background: rgba(255, 255, 255, 0.02); 
                padding: 2rem; border-radius: 12px; margin-bottom: 2rem;
                border: 1px solid rgba(255, 255, 255, 0.05);
                box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);'>
        <h2 style='color: #667eea; margin: 0; font-weight: 600;'>Revolutionizing Agricultural Monitoring</h2>
        <p style='color: #ddd; margin-top: 0.5rem; font-size: 1.1rem; line-height: 1.6;'>
            Empowering farmers and agricultural professionals with cutting-edge AI technology
            for smarter, more efficient plantation management.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Mission & Vision
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style='background: rgba(255, 255, 255, 0.02); 
                    padding: 2rem; border-radius: 12px; margin-bottom: 2rem;
                    border: 1px solid rgba(255, 255, 255, 0.05);
                    border-left: 4px solid #667eea;
                    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
                    transition: transform 0.3s ease;'>
            <h3 style='color: #fff; margin-top: 0; font-weight: 600;'>🎯 Our Mission</h3>
            <p style='color: #ddd; line-height: 1.6;'>
                To transform agricultural practices through innovative AI-powered solutions,
                making plantation monitoring accessible, accurate, and efficient for everyone.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style='background: rgba(255, 255, 255, 0.02); 
                    padding: 2rem; border-radius: 12px; margin-bottom: 2rem;
                    border: 1px solid rgba(255, 255, 255, 0.05);
                    border-left: 4px solid #764ba2;
                    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
                    transition: transform 0.3s ease;'>
            <h3 style='color: #fff; margin-top: 0; font-weight: 600;'>👁️ Our Vision</h3>
            <p style='color: #ddd; line-height: 1.6;'>
                A future where every farmer has access to intelligent tools that maximize
                crop yields, reduce waste, and promote sustainable agricultural practices.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Technology Section
    st.subheader("🔬 Our Technology")
    
    st.markdown("""
    <p style='color: #ddd; font-size: 0.95rem; margin-bottom: 1.5rem;'>
        Our system combines state-of-the-art artificial intelligence models to deliver 
        unparalleled accuracy in crop monitoring and analysis:
    </p>
    """, unsafe_allow_html=True)
    
    tech_col1, tech_col2 = st.columns(2)
    
    with tech_col1:
        st.markdown("""
        <div style='background: rgba(255, 255, 255, 0.02); 
                padding: 1.5rem; border-radius: 12px; margin-bottom: 1rem;
                border: 1px solid rgba(255, 255, 255, 0.05);
                box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);'>
            <h4 style='margin-top: 0; color: #667eea; font-weight: 600;'>🎭 Meta's SAM</h4>
            <p style='color: #888; font-size: 0.85rem; margin-bottom: 1rem;'>Segment Anything Model</p>
            <ul style='margin-bottom: 0; color: #ddd; line-height: 1.8;'>
                <li>Advanced image segmentation</li>
                <li>Precise boundary detection</li>
                <li>Individual plant identification</li>
                <li>High accuracy across diverse crops</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with tech_col2:
        st.markdown("""
        <div style='background: rgba(255, 255, 255, 0.02); 
                padding: 1.5rem; border-radius: 12px; margin-bottom: 1rem;
                border: 1px solid rgba(255, 255, 255, 0.05);
                box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);'>
            <h4 style='margin-top: 0; color: #764ba2; font-weight: 600;'>🧠 ResNet50</h4>
            <p style='color: #888; font-size: 0.85rem; margin-bottom: 1rem;'>Deep Learning Architecture</p>
            <ul style='margin-bottom: 0; color: #ddd; line-height: 1.8;'>
                <li>Robust crop classification</li>
                <li>Disease detection capabilities</li>
                <li>Multi-crop recognition</li>
                <li>Real-time analysis</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Key Features
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.subheader("✨ Key Features")
    
    feature_cols = st.columns(3)
    
    with feature_cols[0]:
        st.markdown("""
        <div style='background: rgba(255, 255, 255, 0.02); 
                padding: 1.5rem; border-radius: 12px; margin-bottom: 1rem;
                border: 1px solid rgba(255, 255, 255, 0.05);
                box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
                text-align: center;
                transition: transform 0.3s ease;'
                onmouseover='this.style.transform="translateY(-5px)"; this.style.boxShadow="0 8px 25px rgba(102, 126, 234, 0.2)";'
                onmouseout='this.style.transform="translateY(0)"; this.style.boxShadow="0 4px 15px rgba(0, 0, 0, 0.1)";'>
            <div style='font-size: 2.5rem; margin-bottom: 0.5rem;'>📊</div>
            <h4 style='margin: 0.5rem 0; color: #667eea; font-weight: 600;'>Real-time Analytics</h4>
            <p style='margin: 0; font-size: 0.9rem; color: #ddd;'>Instant insights into crop health and plantation status</p>
        </div>
        """, unsafe_allow_html=True)
    
    with feature_cols[1]:
        st.markdown("""
        <div style='background: rgba(255, 255, 255, 0.02); 
                padding: 1.5rem; border-radius: 12px; margin-bottom: 1rem;
                border: 1px solid rgba(255, 255, 255, 0.05);
                box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
                text-align: center;
                transition: transform 0.3s ease;'
                onmouseover='this.style.transform="translateY(-5px)"; this.style.boxShadow="0 8px 25px rgba(102, 126, 234, 0.2)";'
                onmouseout='this.style.transform="translateY(0)"; this.style.boxShadow="0 4px 15px rgba(0, 0, 0, 0.1)";'>
            <div style='font-size: 2.5rem; margin-bottom: 0.5rem;'>🎯</div>
            <h4 style='margin: 0.5rem 0; color: #667eea; font-weight: 600;'>High Accuracy</h4>
            <p style='margin: 0; font-size: 0.9rem; color: #ddd;'>AI-powered precision for reliable crop identification</p>
        </div>
        """, unsafe_allow_html=True)
    
    with feature_cols[2]:
        st.markdown("""
        <div style='background: rgba(255, 255, 255, 0.02); 
                padding: 1.5rem; border-radius: 12px; margin-bottom: 1rem;
                border: 1px solid rgba(255, 255, 255, 0.05);
                box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
                text-align: center;
                transition: transform 0.3s ease;'
                onmouseover='this.style.transform="translateY(-5px)"; this.style.boxShadow="0 8px 25px rgba(102, 126, 234, 0.2)";'
                onmouseout='this.style.transform="translateY(0)"; this.style.boxShadow="0 4px 15px rgba(0, 0, 0, 0.1)";'>
            <div style='font-size: 2.5rem; margin-bottom: 0.5rem;'>🚀</div>
            <h4 style='margin: 0.5rem 0; color: #667eea; font-weight: 600;'>Easy to Use</h4>
            <p style='margin: 0; font-size: 0.9rem; color: #ddd;'>Intuitive interface designed for all skill levels</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Our Team/Organization
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.subheader("🏛️ Our Team")
    
    st.markdown("""
    <div style='background: rgba(255, 255, 255, 0.02); 
                padding: 2rem; border-radius: 12px; margin-bottom: 2rem;
                border: 1px solid rgba(255, 255, 255, 0.05);
                border-left: 4px solid #667eea;
                box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);'>
        <p style='font-size: 1.05rem; line-height: 1.8; margin: 0; color: #ddd;'>
            Developed at <strong style='color: #667eea;'>Indian Institute of Statistics (ISI), Kolkata</strong>, this project represents
            the intersection of agricultural expertise and cutting-edge artificial intelligence.
            Our team of researchers, developers, and agricultural scientists work together to create
            solutions that address real-world challenges faced by the farming community.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Statistics/Impact
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.subheader("📈 Our Impact")
    
    impact_cols = st.columns(4)
    
    with impact_cols[0]:
        st.markdown("""
        <div style='background: rgba(255, 255, 255, 0.02); 
                padding: 1.5rem; border-radius: 12px; margin-bottom: 1rem;
                border: 1px solid rgba(255, 255, 255, 0.05);
                box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
                text-align: center;'>
            <h2 style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                       -webkit-background-clip: text;
                       -webkit-text-fill-color: transparent;
                       background-clip: text;
                       margin: 0; font-weight: 700;'>95%+</h2>
            <p style='margin: 0.5rem 0 0 0; color: #ddd; font-weight: 600;'>Accuracy Rate</p>
        </div>
        """, unsafe_allow_html=True)
    
    with impact_cols[1]:
        st.markdown("""
        <div style='background: rgba(255, 255, 255, 0.02); 
                padding: 1.5rem; border-radius: 12px; margin-bottom: 1rem;
                border: 1px solid rgba(255, 255, 255, 0.05);
                box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
                text-align: center;'>
            <h2 style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                       -webkit-background-clip: text;
                       -webkit-text-fill-color: transparent;
                       background-clip: text;
                       margin: 0; font-weight: 700;'>10+</h2>
            <p style='margin: 0.5rem 0 0 0; color: #ddd; font-weight: 600;'>Crop Types</p>
        </div>
        """, unsafe_allow_html=True)
    
    with impact_cols[2]:
        st.markdown("""
        <div style='background: rgba(255, 255, 255, 0.02); 
                padding: 1.5rem; border-radius: 12px; margin-bottom: 1rem;
                border: 1px solid rgba(255, 255, 255, 0.05);
                box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
                text-align: center;'>
            <h2 style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                       -webkit-background-clip: text;
                       -webkit-text-fill-color: transparent;
                       background-clip: text;
                       margin: 0; font-weight: 700;'>Fast</h2>
            <p style='margin: 0.5rem 0 0 0; color: #ddd; font-weight: 600;'>Processing</p>
        </div>
        """, unsafe_allow_html=True)
    
    with impact_cols[3]:
        st.markdown("""
        <div style='background: rgba(255, 255, 255, 0.02); 
                padding: 1.5rem; border-radius: 12px; margin-bottom: 1rem;
                border: 1px solid rgba(255, 255, 255, 0.05);
                box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
                text-align: center;'>
            <h2 style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                       -webkit-background-clip: text;
                       -webkit-text-fill-color: transparent;
                       background-clip: text;
                       margin: 0; font-weight: 700;'>24/7</h2>
            <p style='margin: 0.5rem 0 0 0; color: #ddd; font-weight: 600;'>Available</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Call to Action
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                padding: 2rem; border-radius: 12px; text-align: center;
                box-shadow: 0 6px 20px rgba(102, 126, 234, 0.3);'>
        <h3 style='color: white; margin-top: 0; font-weight: 600;'>Ready to Transform Your Plantation Monitoring?</h3>
        <p style='color: rgba(255,255,255,0.95); margin-bottom: 0; font-size: 1.05rem;'>
            Join us in revolutionizing agriculture with AI-powered insights
        </p>
    </div>
    """, unsafe_allow_html=True)
    
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