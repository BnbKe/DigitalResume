from pathlib import Path
import streamlit as st
from PIL import Image


#path settings
current_dir = Path(__path__).parent if "_file_" in locals() else Path.cwd()
css_file = current_dir/"styles"/"main.css"
resume_file = current_dir/"assets"/"cv.pdf"
profile_pic = current_dir/"assets"/"bnb.png"








#--general settings
Page_title = "Digital CV | Banabas Kariuki"
Page_Icon = 👨🏾‍💻
Name = "Banabas Kariuki"
Description = """
Aspiring Data Scientist, Data driven professional with background in data analytics, risk management, IT services, and banking.
"""
Email = "banabsnk@gmail.com"
Social_media = {
    "GitHub": "https://github.com/BnbKe",
    "linkedIn": "https://www.linkedin.com/in/banabas-kariuki-30b30324b/",
    "Twitter" : "https://twitter.com/Banabas_Kariuki"
}
Project_1 = {"OpenAI-Powered ChatBot" : "https://github.com/BnbKe/Publish-ACN"}
Project_2 = {"Customized OpenAI-Powered Data Analyst GPT" : "https://onlygpt.streamlit.app/"}

st.set_page_config(page_title=Page_title, page_icon=Page_Icon)

#--load CSS, PDF, and Prof_pic

with open(css_file) as f:
    st.markdown("<style>{}</style".format(f.read()), unsafe_allow_html=True)
    with open(resume_file, "rb") as pdf_file:
        PDFbyte = pdf_file.read()
    profile_pic = Image.open(profile_pic)

# -- Hero Section---

col1, col2 = st.columns(2, gap = "small")
with col1:
    st.image(profile_pic, width = 230)
with col2:
    st.title(Name)
    st.write(Description)
    st.download_button(
        label=" Download Resume",
        data=PDFbyte,
        file_name= resume_file.name,
        mime="application/octet-stream",
    )

    st.write("📧", Email)

    #---Social Links---

    st.write("#")
    cols = st.columns(len(Social_media))
    for index, (platform, link) in enumerate(Social_media.items()):
        cols[index].write(f"[{platform}]({link})")

#---Experience and Qualifications---

st.write("#")
st.subheader("Experience and Qualifictions")
st.write(
    """
 - ⦿ Experience in designing and implementing a user-friendly chatbot to efficiently 
        extract insights from textual data.
 - ⦿ Strong hand on experience with Python, R programming, Tableau, and SAS
 - ⦿ Excellent knowledge of Machine Learning algorithms and their implementation using 
    Scikit learn, TensorFlow, Keras etc.
 - ⦿ Good understanding of statistical principles and their respective applications
 - ⦿ Experience in building OpenAI-powered ChatBot that uses advanced Natural 
    Language Processing (NLP) techniques to generate and analyze data
"""
)


#---List of Skills---

st.write("#")
st.subheader("Hard Skills")
st.write(
    """
- ⦿ Programming: Python (Scikit-learn, Pandas, Keras,TensorFlow), SQL, VBA, SAS, R
- ⦿ Data Visualizatio: PowerBi, Tableau, MS Excel, Plotly
- ⦿ Modeling: Logistical regression, linear regression, dicition trees
- ⦿ Databases: Postgres, MongoDB, Redis, MySQL
"""
)




#---Work History---
st.write("#")
st.subheader("Work History")
st.write("---")

#--Intern- Data Analyst--
st.write("Intern: Data Analyst")
st.write("07/2023 - 10/2023")
st.write(
    """
- •	Curate primary research papers to monitor industry trends and identify best practices.
- •	Designed and implemented a user-friendly chatbot to efficiently extract insights from textual data.
- •	Advanced NLP Techniques: Enhanced chatbot capabilities using advanced Natural Language Processing (NLP) techniques.
- •	Seamlessly integrated the chatbot into the data analysis workflow, enabling well-informed decision-making.
- •	Spearheaded the development of an advanced in-house data analysis system.
- •	Forged a seamless integration between the data analysis system and the chatbot, providing a comprehensive solution.
- •	Collaborated across teams to ensure the system's functionality aligns with requirements and user satisfaction.
- •	Conducted user training sessions to empower effective navigation within the system.
- •	Continuously refined and improved both the chatbot and the data analysis system based on valuable user feedback.
"""
)

#--Student Technician- IT Services--
st.write("Student Technician- IT Services")
st.write("11/2022 - 07/2023")
st.write(
    """
- •	Provided help-desk support to students, faculty, and staff.
- •	Collaborated closely with professional IT staff and fellow student IT workers.
- •	Delivered technical support for classroom and conference room technology.
- •	Conducted troubleshooting for classroom presentation technology, including minor maintenance.
- •	Managed and maintained computer labs, resolving printer issues and restocking supplies.

"""
)

#--Junior Business Analyst--
st.write("Junior Business Analyst")
st.write("06/2019 - 07/2022")
st.write(
    """
- •	Analyzed key aspects of business to evaluate factors driving results and summarized into presentations.
- •	Created detailed financial reports from banking data for review by the development team.
- •	Analyzed open orders, backlog, and sales data to provide sales team with insights.
- •	Evaluated trends to understand competitive environments and assess current strategies.
- •	Researched competitors to build report of rising trends in the banking market.

"""
)

#--Junior Business Analyst--
st.write("Junior Business Analyst")
st.write("06/2019 - 07/2022")
st.write(
    """
- •	Analyzed key aspects of business to evaluate factors driving results and summarized into presentations.
- •	Created detailed financial reports from banking data for review by the development team.
- •	Analyzed open orders, backlog, and sales data to provide sales team with insights.
- •	Evaluated trends to understand competitive environments and assess current strategies.
- •	Researched competitors to build report of rising trends in the banking market.

"""
)

#--Junior Business Analyst--
st.write("Junior Business Analyst - Nairobi")
st.write("06/2019 - 07/2022")
st.write(
    """
- •	Analyzed key aspects of business to evaluate factors driving results and summarized into presentations.
- •	Created detailed financial reports from banking data for review by the development team.
- •	Analyzed open orders, backlog, and sales data to provide sales team with insights.
- •	Evaluated trends to understand competitive environments and assess current strategies.
- •	Researched competitors to build report of rising trends in the banking market.

"""
)

#--Business Risk Officer, Nairobi --
st.write("Business Risk Officer, Nairobi ")
st.write("02/2016 - 03/2019")
st.write(
    """
- •	Identified process inefficiencies through gap analysis and outlined sensible solutions.
- •	Conducted interviews with key business users to collect information on business processes and user requirements.
- •	Collaborated with teams in product line transition to streamline manufacturing footprint.
- •	Executed analysis of risks and identified risk mitigation strategies
"""
)

#---Projects
#st.write("Projects")
st.subheader("Projects")
st.write(f"[OpenAI-Powered ChatBot](https://github.com/BnbKe/Publish-ACN)")
st.write(f"[Customized OpenAI-Powered Data Analyst GPT](https://onlygpt.streamlit.app/)")
