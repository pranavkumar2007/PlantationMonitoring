import streamlit as st
def show_contact():
    st.title("📞 Contact Us")
    
    # Introduction
    st.markdown("""
    <div style='background: rgba(255, 255, 255, 0.02); 
                padding: 2rem; border-radius: 12px; margin-bottom: 2rem;
                border: 1px solid rgba(255, 255, 255, 0.05);
                border-left: 4px solid #667eea;
                box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);'>
        <h3 style='color: #667eea; margin: 0; font-weight: 600;'>Get in Touch</h3>
        <p style='color: #ddd; margin-top: 0.5rem; line-height: 1.6;'>
            We'd love to hear from you! Whether you have questions, feedback, or need support,
            our team is here to help.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Two-column layout
    col1, col2 = st.columns([1.5, 1])
    
    with col1:
        
        st.subheader("📬 Send us a Message")
        
        # Contact form
        with st.form("contact_form", clear_on_submit=True):
            name = st.text_input("Full Name *", placeholder="Enter your name")
            email = st.text_input("Email Address *", placeholder="your.email@example.com")
            subject = st.selectbox(
                "Subject *",
                ["General Inquiry", "Technical Support", "Partnership Opportunity", 
                 "Bug Report", "Feature Request", "Other"]
            )
            message = st.text_area(
                "Message *", 
                placeholder="Tell us how we can help you...",
                height=150
            )
            
            submitted = st.form_submit_button("Send Message 📤", use_container_width=True)
            
            if submitted:
                if name and email and message:
                    st.success("✅ Thank you! Your message has been sent successfully. We'll get back to you soon!")
                    # Here you would typically integrate with an email service or database
                else:
                    st.error("⚠️ Please fill in all required fields marked with *")
    
    with col2:
        
        st.subheader("📍 Contact Information")
        
        # Contact details in styled boxes
        st.markdown("""
        <div style='background: rgba(255, 255, 255, 0.02); 
                    padding: 1.5rem; border-radius: 12px; margin-bottom: 1rem;
                    border: 1px solid rgba(255, 255, 255, 0.05);
                    border-left: 4px solid #667eea;
                    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
                    transition: transform 0.3s ease;'
                    onmouseover='this.style.transform="translateX(5px)"; this.style.boxShadow="0 6px 20px rgba(102, 126, 234, 0.2)";'
                    onmouseout='this.style.transform="translateX(0)"; this.style.boxShadow="0 4px 15px rgba(0, 0, 0, 0.1)";'>
            <h4 style='margin-top: 0; color: #667eea; font-weight: 600;'>📧 Email</h4>
            <p style='margin: 0; color: #ddd;'>
                <a href='mailto:plantationmonitoring@gmail.com' 
                   style='color: #ddd; text-decoration: none; transition: color 0.3s;'
                   onmouseover='this.style.color="#667eea"'
                   onmouseout='this.style.color="#ddd"'>
                    plantationmonitoring@gmail.com
                </a>
            </p>
        </div>
        
        """, unsafe_allow_html=True)
        
        # Quick response card
        st.markdown("""
        <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    padding: 1.5rem; border-radius: 12px; margin-top: 1rem;
                    box-shadow: 0 6px 20px rgba(102, 126, 234, 0.3);
                    text-align: center;'>
            <h4 style='margin: 0; color: white; font-weight: 600;'>⚡ Quick Response</h4>
            <p style='margin: 0.5rem 0 0 0; color: rgba(255,255,255,0.95); font-size: 0.9rem;'>
                We typically respond within<br><strong>24-48 hours</strong>
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    # FAQ Section
    st.markdown("""
    <div style='margin: 3rem 0 2rem 0; padding-top: 2rem; 
                border-top: 1px solid rgba(255, 255, 255, 0.1);'>
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("❓ Frequently Asked Questions")
    
    with st.expander("How quickly will I receive a response?"):
        st.markdown("""
        <p style='color: #ddd; line-height: 1.6;'>
            We typically respond to all inquiries within <strong style='color: #667eea;'>24-48 hours</strong> 
            during business days. For urgent matters, please mark your subject as "Urgent" and we'll prioritize your request.
        </p>
        """, unsafe_allow_html=True)
    
    with st.expander("Can I schedule a demo of the plantation monitoring system?"):
        st.markdown("""
        <p style='color: #ddd; line-height: 1.6;'>
            Absolutely! Please mention <strong style='color: #667eea;'>'Demo Request'</strong> in your message subject, 
            and we'll arrange a convenient time for you. Our demos typically last 30-45 minutes and cover all major features.
        </p>
        """, unsafe_allow_html=True)
    
    with st.expander("Do you offer technical support?"):
        st.markdown("""
        <p style='color: #ddd; line-height: 1.6;'>
            Yes, we provide comprehensive technical support for all users. Select 
            <strong style='color: #667eea;'>'Technical Support'</strong> in the subject field when contacting us, 
            and our technical team will assist you promptly.
        </p>
        """, unsafe_allow_html=True)
    
    with st.expander("How can I report a bug or suggest a feature?"):
        st.markdown("""
        <p style='color: #ddd; line-height: 1.6;'>
            We welcome bug reports and feature suggestions! Please use the 
            <strong style='color: #667eea;'>'Bug Report'</strong> or 
            <strong style='color: #764ba2;'>'Feature Request'</strong> subject options in the contact form above. 
            Your feedback helps us improve our system.
        </p>
        """, unsafe_allow_html=True)
    
    with st.expander("What information should I include in my message?"):
        st.markdown("""
        <p style='color: #ddd; line-height: 1.6;'>
            For faster resolution, please include:<br>
            • A clear description of your issue or question<br>
            • Any relevant screenshots or error messages<br>
            • Your system/browser information (if technical)<br>
            • Steps to reproduce the issue (for bug reports)
        </p>
        """, unsafe_allow_html=True)
    
    # Social and Footer
    st.markdown("""
    <div style='margin-top: 3rem; padding-top: 2rem; 
                border-top: 1px solid rgba(255, 255, 255, 0.1);'>
        <div style='text-align: center;'>
            <p style='color: #888; margin-bottom: 1rem; font-size: 0.9rem;'>Connect with us on social media</p>
            <p style='font-size: 1.5rem; margin: 1rem 0;'>
                🌐 💼 📱 
            </p>
            <p style='color: #888; font-size: 0.85rem; margin-top: 1.5rem;'>
                © 2025 Plantation Monitoring System. All rights reserved.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)