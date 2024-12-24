import streamlit as st
from streamlit_option_menu import option_menu
import requests
#import smtplib
#from email.mime.text import MIMEText
#from email.mime.multipart import MIMEMultipart

import json

import feedparser
from bs4 import BeautifulSoup

# Load Projects from JSON
def load_projects():
    with open('projects.json', 'r') as file:
        return json.load(file)
    
# Load Skills from JSON
def load_skills():
    with open('skills.json', 'r') as file:
        return json.load(file)

# Load skills from JSON
skills = load_skills()


# Fetch Medium Blogs with Thumbnails
def fetch_medium_blogs(username, max_posts=5):
    feed_url = f"https://medium.com/feed/@{username}"
    feed = feedparser.parse(feed_url)
    
    blogs = []
    for entry in feed.entries[:max_posts]:
        # Parse the blog content
        summary = BeautifulSoup(entry.summary, 'html.parser')
        text_summary = summary.get_text()
        
        # Extract the first image, if available
        img_tag = summary.find('img')
        thumbnail = img_tag['src'] if img_tag else "assets/default_thumbnail.png"
        
        blogs.append({
            "title": entry.title,
            "link": entry.link,
            "published": entry.published,
            "summary": text_summary,
            "thumbnail": thumbnail
        })
    return blogs


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
    st.markdown(
        """
        <div style="text-align: center;">
            <img src="https://avatars.githubusercontent.com/u/26743932?s=400&u=767b5b8b618ca82e400b1c1bd7163d1cbf4e029c&v=4" style="width: 150px; margin-bottom: 10px;">
            <h1 style="margin: 0;">Parthan Manisekaran</h1>
            <p style="font-size: 18px; margin: 5px 0;">Robotics | Vision | AI</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Social Icons
    st.markdown(
        """
        <div style="display: flex; justify-content: center; gap: 10px; margin: 10px 0;">
            <a href="https://linkedin.com/in/parthan-m" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="30" alt="LinkedIn">
            </a>
            <a href="https://github.com/Spartan-Velanjeri" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" width="30" alt="GitHub">
            </a>
            <a href="https://medium.com/@parthanvelanjeri" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/2111/2111505.png" width="30" alt="Medium">
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Resume Button
    st.markdown("---")
    with open("assets/Parthan_Resume.pdf", "rb") as file:
        st.download_button(
            label="📄 Download Resume",
            data=file,
            file_name="Parthan_Resume.pdf",
            mime="application/pdf"
        )
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

    # Achievement data
    achievements = [
        {
            "title": "Runners-Up, Bots and Bento Competition (IEEE ICRA 2024, Yokohama, Japan)",
            "description": "Built an autonomous physical robot in three days from scratch.",
            "link": "https://www.linkedin.com/posts/parthan-m_we-have-a-winner-after-4-intense-days-activity-7199365789567569920-XTNy?utm_source=share&utm_medium=member_desktop"
        },
        {
            "title": "RWTH Student Project Grant 2023",
            "description": "Built a deep learning model for Solar Soiling Detection using an Aerial Vehicle.",
            "link": "https://www.linkedin.com/posts/vsranjitroshan_scholarship-ceremony-university-activity-7080546301062344704-szaj?utm_source=share&utm_medium=member_desktop"
        },
        {
            "title": "Runners-Up, CTO Pitch Battle (Deutsche Telekom)",
            "description": "Developed 'Deutsche Telespots' to revamp telephone booths into data + service centers.",
            "link": "https://www.linkedin.com/posts/nouranelsherbiny_chieftomorrowofficer-questionsoftomorrow-ugcPost-7129432144312983552-GrGV?utm_source=share&utm_medium=member_desktop"
        }
    ]

    # Display achievements in a grid
    st.header("🏆 Notable Achievements")
    cols = st.columns(3)

    for col, achievement in zip(cols, achievements):
        with col:
            st.write(f"**{achievement['title']}**")
            st.write(achievement['description'])
            st.markdown(
                f"""
                <div style='border: 1px solid #ccc; border-radius: 8px; padding: 10px; text-align: center;'>
                    <a href="{achievement['link']}" target="_blank" style="text-decoration: none;">
                        <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" 
                            alt="LinkedIn Logo" 
                            style="width:50px; margin-bottom:10px;">
                        <p style="font-weight: bold; color: #0077B5;">View on LinkedIn</p>
                    </a>
                </div>
                """,
                unsafe_allow_html=True
            )



    st.header("🧠 Skills")
    st.write("**Languages:**")
    st.write(" | ".join(skills["languages"]))
    
    st.write("**Frameworks:**")
    st.write(" | ".join(skills["frameworks"]))
    
    st.write("**Tools:**")
    st.write(" | ".join(skills["tools"]))
    
    st.write("**Robotics Frameworks:**")
    st.write(" | ".join(skills["robotics"]))

    st.header("📝 Latest Blogs from Medium")
    username = "parthanvelanjeri"  # Replace with your Medium username
    blogs = fetch_medium_blogs(username)

    if blogs:
        for i in range(0, len(blogs), 3):
            cols = st.columns(3)
            for col, blog in zip(cols, blogs[i:i+3]):
                with col:
                    st.image(blog['thumbnail'], use_container_width=True)
                    st.markdown(f"### [{blog['title']}]({blog['link']})")
                    st.write(f"📅 Published on: {blog['published']}")
                    st.write(blog['summary'][:100] + '...')
    else:
        st.write("Unable to show the blogs here! Click on the Medium Icon in the sidebar to view")
        
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
    all_skills = skills["languages"] + skills["frameworks"] + skills["tools"] + skills["robotics"]
    selected_skills = st.multiselect(
        "Select Skills:",
        options=all_skills,
        default=[]
    )
    
    projects = load_projects()
    filtered_projects = [p for p in projects if set(selected_skills).issubset(p['skills'])] if selected_skills else projects
    
    for i in range(0, len(filtered_projects), 3):
        cols = st.columns(3)
        for col, project in zip(cols, filtered_projects[i:i+3]):
            with col:
                st.image(project['image'], use_container_width=True)
                st.write(f"**{project['title']} ({project['year']})**")
                st.write(project['description'])
                if 'link' in project:
                    st.markdown(f"[GitHub Repository]({project['link']})")
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
        st.markdown('[👉 **Check the Paper**](https://dl.acm.org/doi/10.1145/3478586.3480649)', unsafe_allow_html=True)
    
    with col2:
        st.image("assets/indicon.png", use_container_width=True)
        st.write("**Supernumerary Robotic Limbs for the Blind**")
        st.write("**Published In:** IEEE INDICON 2020")
        st.write("- Designed robotic limbs to assist visually impaired individuals.")
        st.markdown('[👉 **Check the Paper**](https://ieeexplore.ieee.org/document/9342553/)', unsafe_allow_html=True)

    st.header("🔑 Patent")
    st.image("assets/patent.png", use_container_width=True)
    st.write("**Patent:** Multi-drone Integration for Heavy Payloads")
    st.write("- Developed a system enabling coordinated control of multiple drones for heavy payload lifting.")
    st.markdown('[👉 **Check the Patent**](https://patentscope.wipo.int/search/en/detail.jsf?docId=IN283284050&_cid=P10-L7VIQO-47821-3)', unsafe_allow_html=True)


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
