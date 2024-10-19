import streamlit as st
import pandas as pd  

# Personal Information
name = "Sreeram Nithin"
title = "Business Analyst | Data Enthusiast"
description = """
I am a Business Analyst with over a year of experience in data analytics, specializing in Business Intelligence (BI) using Power BI. 
I have hands-on experience with Power BI, Python, SQL, and Excel, delivering insights through executive-level dashboards and 
helping businesses make data-driven decisions. I enjoy leveraging data to uncover hidden insights and drive business performance.
"""
profile_pic = "assets/WhatsApp Image 2024-10-19 at 4.07.28 PM.jpeg"
background_image = "assets/background.jpg"  # Background image placeholder

# Set background image
st.markdown(
    f"""
    <style>
    .reportview-container {{
        background: url({background_image});
        background-size: cover;
        background-position: center;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Social Media Links
social_media = {
    "LinkedIn": "https://www.linkedin.com/in/nithin-sreeram-a191a4212/",
    "GitHub": "https://github.com/SreeramNithin",
}

# Project Information
projects_info = [
    {
        "title": "Fifa Players Wage Predictor",
        "description": "Using Python and machine learning algorithms, I developed a predictive model to estimate player wages based on performance and attributes, combining my passion for data science and football.",
    },
    {
        "title": "Executive-Level Sales Dashboard in Power BI",
        "description": "Developed a comprehensive sales performance dashboard in Power BI for executive stakeholders. The dashboard includes KPI tracking, sales trends, and actionable insights.",
    },
    {
        "title": "Customer Segmentation Analysis",
        "description": "Used SQL and Python for a customer segmentation project, identifying key customer groups for targeted marketing. The insights helped improve customer engagement and sales strategies.",
    },
]

# Experience Information
experiences = pd.DataFrame({
    "Company": ["Lognormal Analytics", "UNP"],
    "Title": ["Business Analyst", "Teaching Assistant"],
    "Dates": ["August 2023 - Present", "January 2022 - April 2023"],
    "Description": [
        "As a Business Analyst at Lognormal Analytics, I focus on delivering business intelligence solutions, primarily using Power BI, SQL, and Python. I have developed executive-level dashboards for multiple clients, enabling data-driven decision-making.",
        "Assisted in teaching Data Science and Analytics courses, focusing on projects involving Python, Power BI, and machine learning, helping students build foundational skills."
    ],
})

# Academics Information
academics_info = [
    {
        "Degree": "BSc Hons Data Science",
        "Institution": "Bhavans Vivekanand College, Hyderabad",
        "Score": "CGPA: 9.51",
    },
    {
        "Degree": "11th and 12th Grade (MPC - Math, Physics, Chemistry)",
        "Institution": "State Board",
        "Score": "971/1000",
    },
    {
        "Degree": "10th Grade",
        "Institution": "State Board",
        "Score": "CGPA: 9.8",
    }
]

# Blog Information
blog_posts = [
    {
        "title": "The Power of Power BI: DAX Functions for Business Intelligence",
        "summary": "This article dives deep into essential DAX functions for Power BI, explaining how they can be used to create powerful, dynamic reports for business insights.",
        "link": "https://medium.com/@nithin.sreeram2002",
    },
]

# Skills Information
skills = [
    "Power BI (DAX and data visualization)",
    "Python (Data analysis and machine learning)",
    "SQL (Database querying and optimization)",
    "Microsoft Excel (Advanced analytics and reporting)",
]

# Helper Functions for Pages
def about_me():
    """
    Displays the About Me page.
    """
    st.image(profile_pic, width=150)
    st.subheader(name)
    st.subheader(title)
    st.write(description)

    st.markdown("### Connect with Me")
    for platform, link in social_media.items():
        st.markdown(f"- [{platform}]({link})")


def display_projects():
    """
    Displays the Projects page.
    """
    st.header("Projects")
    for project in projects_info:
        st.subheader(project["title"])
        st.write(project["description"])


def experience():
    """
    Displays the Experience page.
    """
    st.header("Experience")
    st.write("I have hands-on experience in Business Analytics and Intelligence, with a focus on Power BI, Python, and SQL.")
    st.dataframe(experiences)


def display_academics():
    """
    Displays the Academics page.
    """
    st.header("Academics")
    for academic in academics_info:
        st.subheader(academic["Degree"])
        st.write(f"Institution: {academic['Institution']}")
        st.write(f"Score: {academic['Score']}")


def blog():
    """
    Displays the Blog page.
    """
    st.header("Blog")
    for post in blog_posts:
        st.subheader(post["title"])
        st.write(post["summary"])
        st.markdown(f"[Read More]({post['link']})")


def display_skills():
    """
    Displays the Skills page.
    """
    st.header("Skills")
    st.write(", ".join(skills))


def resume():
    """
    Provides a download link for the resume.
    """
    resume_file = "assets/Sreeram_Nithin_Resume.pdf"
    st.header("Resume")

    try:
        with open(resume_file, "rb") as f:
            resume_bytes = f.read()
            st.download_button(
                label="Download Resume",
                data=resume_bytes,
                file_name="Sreeram_Nithin_Resume.pdf",
                mime="application/pdf"
            )
    except FileNotFoundError:
        st.error("Resume file not found. Please check the path.")

# Streamlit App with Sidebar Navigation
st.sidebar.title("Navigation")
pages = st.sidebar.radio("Go to", ["About Me", "Projects", "Experience", "Academics", "Blog", "Skills", "Resume"])

# Display the correct page based on sidebar selection
if pages == "About Me":
    about_me()
elif pages == "Projects":
    display_projects()
elif pages == "Experience":
    experience()
elif pages == "Academics":
    display_academics()
elif pages == "Blog":
    blog()
elif pages == "Skills":
    display_skills()
elif pages == "Resume":
    resume()
