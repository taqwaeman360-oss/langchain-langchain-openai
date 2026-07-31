import streamlit as st
from email_generator import generate_email

st.set_page_config(page_title="AI Email Generator", page_icon="✉️")
st.title("✉️ AI Email Generator")

st.markdown("Generate tailored professional emails powered by LangChain & monitored via LangSmith.")

with st.form("email_form"):
    topic = st.text_input("Email Subject / Topic", placeholder="Project status update")
    recipient_role = st.text_input("Recipient Role", placeholder="Engineering Manager")
    tone = st.selectbox("Tone", ["Professional", "Friendly", "Urgent", "Persuasive"])
    
    submitted = st.form_submit_button("Generate Email")

if submitted:
    if not topic or not recipient_role:
        st.error("Please fill in all required fields.")
    else:
        with st.spinner("Drafting your email..."):
            result = generate_email(topic, recipient_role, tone)
            st.success("Generated Successfully!")
            st.text_area("Generated Email", value=result, height=250)
