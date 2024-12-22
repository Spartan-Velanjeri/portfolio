import streamlit as st
from streamlit_option_menu import option_menu
import requests
#import smtplib
#from email.mime.text import MIMEText
#from email.mime.multipart import MIMEMultipart

# Load Lottie Animations
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Page Configuration
st.set_page_config(
    page_title="Parthan Manisekaran Portfolio",
    page_icon="🤖",
    layout="wide"
)

# Sidebar with Image, Social Links, and Languages
with st.sidebar:
    st.image("assets/indicon.png", width=150)
    st.title("Parthan Manisekaran")
    st.write("Robotics | Vision | AI ")
    
    st.markdown("### Language Proficiency")
    st.write("English (Professional)")
    st.progress(0.9)
    st.write("German (A2)")
    st.progress(0.4)
    st.write("Tamil (Native)")
    st.progress(1.0)
    st.write("Kannada (Native)")
    st.progress(1.0)
    st.write("Hindi (Professional)")
    st.progress(0.6)



# Horizontal Menu
selected = option_menu(
    menu_title=None,
    options=["About Me", "Experience", "Education", "Projects", "Publications", "Contact"],
    icons=["person", "briefcase", "book", "folder", "book", "envelope"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
)

# About Me Section
if selected == "About Me":
    st.title("👋 About Me")
    st.write("""
    🚀 Bridging the gap between imagination and innovation, I’m Parthan Manisekaran – a robotics engineer and software developer with hands-on expertise in AI, computer vision, and embedded systems. From building autonomous robots for greenhouse monitoring to optimizing CI/CD pipelines for robotics software, I thrive on solving complex challenges with smart technology. With roots in mechanical engineering and wings in deep learning, I craft impactful solutions that drive efficiency and innovation. 🌟
    """)
    st.header("🏆 Notable Achievements")
    st.write("### **Innovation and Excellence Awards**")
    st.write("- **Runners-Up, Bots and Bento Competition (IEEE ICRA 2024, Yokohama, Japan):** Built an autonomous physical robot in three days from scratch.")
    st.write("- **RWTH Student Project Grant 2023:** Built a deep learning model for Solar Soiling Detection using an Aerial Vehicle.")
    st.write("- **Runners-Up, CTO Pitch Battle (Deutsche Telekom):** Developed 'Deutsche Telespots' to revamp telephone booths into data + service centers.")

    st.header("🧠 Skills")
    st.write("**Languages:**")
    languages = ["🐍 Python", "💻 C++"]
    st.write(" | ".join(languages))
    
    st.write("**Frameworks:**")
    frameworks = ["🤖 PyTorch", "🔍 TensorFlow", "🛠️ OpenCV"]
    st.write(" | ".join(frameworks))
    
    st.write("**Tools:**")
    tools = ["🐳 Docker", "🐙 GitHub Actions", "🐧 Linux"]
    st.write(" | ".join(tools))
    
    st.write("**Robotics Frameworks:**")
    robotics = ["🤖 ROS2", "🛰️ Gazebo", "🦾 MoveIt!", "🌐 Nav2"]
    st.write(" | ".join(robotics))

# Experience Section
if selected == "Experience":
    st.title("💼 Experience")
    st.subheader("Computer Vision Thesis Student at Hexafarms, Berlin")
    st.write("**Duration:** Jul 2024 - Dec 2024")
    st.write("- Working on Monocular Depth Estimation and Deep learning based Stereo Matching.")
    st.write("- Specializing in Computer Vision applications for Greenhouse solutions.")
    st.write("**Skills:** PyTorch, OpenCV, RPi + Stereo Vision")

    st.subheader("Robotics Software Developer (R&D Intern) at Robert Bosch Power Tools GmbH, Leinfelden")
    st.write("**Duration:** Oct 2023 - Mar 2024")
    st.write("- Migrated Robot Software Stack from ROS Galactic to Humble.")
    st.write("- Implemented CI/CD tools for robotics software deployment.")
    st.write("**Skills:** ROS2, Gazebo Sim, URSim, MoveIt!, Nav2, Docker")

# Education Section
if selected == "Education":
    st.title("🎓 Education")
    st.subheader("M.Sc. Robotic Systems Engineering at RWTH Aachen University, Aachen")
    st.write("**Duration:** Oct 2021 - Present")
    st.write("- Courses: Robotic Sensor Systems, Computer Vision, Machine Learning.")

    st.subheader("Bachelors in Mechanical Engineering at PES University, Bangalore")
    st.write("**Duration:** Aug 2016 - Aug 2020")
    st.write("- Specialization in Aerospace Engineering.")
    st.write("- Awarded Merit Scholarships for Top 20% students.")
    st.write("- Patent: Multi-drone integration for heavy payloads.")
    st.write("**GPA:** 8.43/10")

# Projects Section
if selected == "Projects":
    st.title("🛠️ Projects")
    st.write("Filter projects by skills:")
    selected_skills = st.multiselect(
        "Select Skills:",
        options=["Python", "ROS2", "TensorFlow", "Docker", "OpenCV"],
        default=[]
    )
    
    projects = [
        {"title": "Autonomous Greenhouse Monitoring System", "skills": ["Python", "OpenCV"], "year": "2023",  "image": "assets/indicon.png", "description": "Built an autonomous greenhouse monitoring system using deep learning and IoT."},
        {"title": "Robot Arm Pick-and-Place Automation", "skills": ["ROS2", "Docker"], "year": "2023", "image": "assets/indicon.png", "description": "Designed a robotic arm control system for pick-and-place automation."},
        {"title": "Solar Soiling Detection via Aerial Drones", "skills": ["TensorFlow", "Python"], "year": "2023", "image": "assets/indicon.png", "description": "Developed deep learning models for detecting solar panel soiling via drone imagery."},
        {"title": "Solar Soiling Detection via Aerial Drones", "skills": ["TensorFlow", "Python"], "year": "2023", "image": "assets/indicon.png", "description": "Developed deep learning models for detecting solar panel soiling via drone imagery."}
    ]
    
    filtered_projects = [p for p in projects if set(selected_skills).issubset(p['skills'])] if selected_skills else projects
    
    for i in range(0, len(filtered_projects), 3):
        cols = st.columns(3)
        for col, project in zip(cols, filtered_projects[i:i+3]):
            with col:
                st.image(project['image'], use_container_width=True)
                st.write(f"**{project['title']} ({project['year']})**")
                st.write(project['description'])
                st.write("**Key Skills:**")
                skill_tags = " ".join([f"<span style='background-color:#e1bee7; color:#000; padding:4px 8px; border-radius:5px; margin-right:4px;'>{skill}</span>" for skill in project['skills']])
                st.markdown(skill_tags, unsafe_allow_html=True)

# Publications Section
if selected == "Publications":
    st.title("📚 Research Publications")
    col1, col2 = st.columns(2)
    
    with col1:
        st.image("assets/armer_paper.png", use_container_width=True)
        st.write("**ARMER: Modular and Semi-Autonomous Supernumerary Robotic Limbs for Disaster Relief**")
        st.write("**Published In:** ACM Advances in Robotics 2021")
        st.write("- Developed modular robotic limbs for disaster relief scenarios.")
    
    with col2:
        st.image("assets/indicon.png", use_container_width=True)
        st.write("**Supernumerary Robotic Limbs for the Blind**")
        st.write("**Published In:** IEEE INDICON 2020")
        st.write("- Designed robotic limbs to assist visually impaired individuals.")

    st.header("🔑 Patent")
    st.image("assets/patent.png", use_container_width=True)
    st.write("**Patent:** Multi-drone Integration for Heavy Payloads")
    st.write("- Developed a system enabling coordinated control of multiple drones for heavy payload lifting.")
# Contact Section
if selected == "Contact":
    st.title("📬 Get in Touch")
    st.write("Feel free to leave me a message!")
    #with st.form(key='contact_form'):
        #user_name = st.text_input("Your Name")
        #user_email = st.text_input("Your Email")
        #user_message = st.text_area("Your Message")
        #submit_button = st.form_submit_button("Send Message")
        
        #if submit_button:
            #if user_name and user_email and user_message:
                #try:
                    #sender_email = "your_email@example.com"
                    #receiver_email = "parthan@example.com"
                    #password = "your_password"
                    
                    #message = MIMEMultipart()
                    #message['From'] = sender_email
                    #message['To'] = receiver_email
                    #message['Subject'] = f"New Message from {user_name}"
                    
                    #body = f"Name: {user_name}\nEmail: {user_email}\nMessage: {user_message}"
                    #message.attach(MIMEText(body, 'plain'))
                    
                    #with smtplib.SMTP('smtp.example.com', 587) as server:
                        #server.starttls()
                        #server.login(sender_email, password)
                        #server.send_message(message)
                    
                    #st.success("Your message has been sent successfully!")
                #except Exception as e:
                    #st.error(f"Failed to send message: {e}")
            #else:
                #st.warning("Please fill in all fields before submitting.")


# Footer
st.markdown("---")
st.write("© 2024 Parthan Manisekaran. All Rights Reserved.")
