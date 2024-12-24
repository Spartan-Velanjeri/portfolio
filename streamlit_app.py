import streamlit as st
from streamlit_option_menu import option_menu
import requests
import os
import json
import feedparser
from bs4 import BeautifulSoup


# Page Configuration
st.set_page_config(
    page_title="Parthan Manisekaran Portfolio",
    page_icon="🤖",
    layout="wide"
)

# Load JSON data
def load_json(file_name):
    try:
        base_path = os.path.dirname(__file__)  # Get the current script's directory
        file_path = os.path.join(base_path, 'utils', file_name)  # Construct the file path

        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"File {file_name} not found in utils folder.")
    except json.JSONDecodeError:
        raise ValueError(f"File {file_name} contains invalid JSON.")

# Predefined Colors for Skill Boxes (Dark Theme Friendly)
SKILL_COLORS = [
    "#4DA8DA",  # Sky Blue (matches primaryColor)
    "#6AAFE6",  # Soft Blue
    "#1B98E0",  # Bright Blue
    "#2A9D8F",  # Deep Teal
    "#E76F51",  # Warm Red
    "#F4A261",  # Muted Orange
    "#264653",  # Dark Teal
    "#8D99AE",  # Steel Blue
    "#457B9D",  # Deep Sky Blue
    "#F4BFDB",  # Muted Pink
    "#9C6644",  # Earthy Brown
    "#2E4053",  # Dark Slate
    "#556270",  # Charcoal Blue
    "#6C757D",  # Neutral Grey
    "#A53860",  # Burgundy
    "#3A506B",  # Midnight Blue
    "#2C3E50",  # Navy Blue
    "#0F4C75"   # Deep Ocean Blue
]


# Skill-to-Color Mapping
skill_color_map = {}

# Function to get consistent color for a skill
def get_skill_color(skill):
    if skill not in skill_color_map:
        skill_color_map[skill] = SKILL_COLORS[len(skill_color_map) % len(SKILL_COLORS)]
    return skill_color_map[skill]

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




# Load skills from JSON
skills = load_json('skills.json')

# Load projects from JSON
projects = load_json('projects.json')

# Load education from JSON
education_data = load_json('education.json')

# Load experience from JSON
experience_data = load_json('experience.json')

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

    # Style for uniform height
    card_style = """
    <style>
        .achievement-card {
            border: 1px solid #ccc;
            border-radius: 8px;
            padding: 20px;
            text-align: center;
            background-color: #1B263B;
            height: 450px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }
        .achievement-card img {
            width: 100%;
            height: 250px;
            object-fit: cover;
            border-radius: 8px;
        }
        .achievement-card h3 {
            color: #E0E1DD;
            font-size: 1rem;
        }
        .achievement-card p {
            color: #E0E1DD;
            font-size: 0.9rem;
            margin: 10px 0;
        }
        .achievement-card a {
            text-decoration: none;
            font-weight: bold;
            color: #4DA8DA;
            margin-top: auto;
        }
        .achievement-card a:hover {
            text-decoration: underline;
        }
    </style>
    """
    st.markdown(card_style, unsafe_allow_html=True)

    # Achievement Data
    achievements = [
        {
            "title": "Runners-Up, Bots and Bento Competition (IEEE ICRA 2024, Yokohama, Japan)",
            "description": "Built an autonomous physical robot in three days from scratch.",
            "link": "https://www.linkedin.com/posts/parthan-m_we-have-a-winner-after-4-intense-days-activity-7199365789567569920-XTNy?utm_source=share&utm_medium=member_desktop",
            "image": "https://raw.githubusercontent.com/Spartan-Velanjeri/spartan-velanjeri.github.io/refs/heads/main/images/a1.jpeg"
        },
        {
            "title": "Runners-Up, CTO Pitch Battle 2023 (Deutsche Telekom)",
            "description": "Developed 'Deutsche Telespots' to revamp telephone booths into data + service centers.",
            "link": "https://www.linkedin.com/posts/nouranelsherbiny_chieftomorrowofficer-questionsoftomorrow-ugcPost-7129432144312983552-GrGV?utm_source=share&utm_medium=member_desktop",
            "image": "https://raw.githubusercontent.com/Spartan-Velanjeri/spartan-velanjeri.github.io/refs/heads/main/images/a2.jpeg"
        }
    ]

    # Display achievements side-by-side
    st.header("🏆 Recent Achievements")

    cols = st.columns(2)

    for col, achievement in zip(cols, achievements):
        with col:
            st.markdown(
                f"""
                <div class='achievement-card'>
                    <img src="{achievement['image']}" alt="Achievement Image">
                    <h3>{achievement['title']}</h3>
                    <p>{achievement['description']}</p>
                    <a href="{achievement['link']}" target="_blank">🔗 View on LinkedIn</a>
                </div>
                """,
                unsafe_allow_html=True
            )


    st.header("🧠 Skills")
    
    categories = [
        {"icon": "🐍", "title": "Languages", "skills": skills["languages"]},
        {"icon": "🔧", "title": "Frameworks", "skills": skills["frameworks"]},
        {"icon": "🛠️", "title": "Tools", "skills": skills["tools"]},
        {"icon": "🤖", "title": "Robotics Frameworks", "skills": skills["robotics"]}
    ]
    
    for category in categories:
        st.subheader(f"{category['icon']} {category['title']}")
        skill_tags = " ".join([
            f"<span style='background-color:{get_skill_color(skill)}; color:#FFFFFF; padding:6px 10px; border-radius:5px; margin:4px; display:inline-block;'>{skill}</span>"
            for skill in category['skills']
        ])
        st.markdown(
            f"<div style='margin-bottom:16px;'>{skill_tags}</div>", 
            unsafe_allow_html=True
        )

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
    
    for exp in experience_data:
        st.subheader(exp["title"])
        st.write(f"**Duration:** {exp['duration']}")
        
        # Display Description
        for desc in exp['description']:
            st.write(f"- {desc}")
        
        # Display Skills with Consistent Colors
        st.write("**Skills:**")
        skill_tags = " ".join([
            f"<span style='background-color:{get_skill_color(skill)}; color:#FFFFFF; padding:4px 8px; border-radius:5px; margin-right:4px; display:inline-block; margin-bottom:4px;'>{skill}</span>"
            for skill in exp['skills']
        ])
        st.markdown(f"<div style='margin-top:8px;'>{skill_tags}</div>", unsafe_allow_html=True)
        
        st.markdown("---")




# Education Section
if selected == "Education":
    st.title("🎓 Education")
    for edu in education_data:
        st.subheader(edu["title"])
        st.write(f"**Duration:** {edu['duration']}")
        for desc in edu['description']:
            st.write(f"- {desc}")
        if "GPA" in edu:
            st.write(f"**GPA:** {edu['GPA']}")

# Projects Section
if selected == "Projects":
    st.title("🛠️ Projects")
    st.write("Filter projects by skills:")
    all_skills = sorted(set(skill for project in projects for skill in project['skills']))

        
    selected_skills = st.multiselect(
        "Select Skills:",
        options=all_skills,
        default=[]
    )
        
    
    filtered_projects = [p for p in projects if set(selected_skills).issubset(p['skills'])] if selected_skills else projects
    
    # Display projects in grid format
    for i in range(0, len(filtered_projects), 3):
        cols = st.columns(3)
        for col, project in zip(cols, filtered_projects[i:i+3]):
            with col:
                st.image(project['image'], use_container_width=True)
                st.write(f"**{project['title']} ({project['year']})**")
                st.write(project['description'])
                if 'link' in project:
                    st.markdown(f"[🔗 GitHub Repository]({project['link']})")
                st.write("**Key Skills:**")
                skill_tags = " ".join([
                    f"<span style='background-color:{get_skill_color(skill)}; color:#FFFFFF; padding:4px 8px; border-radius:5px; margin-right:4px; display:inline-block; margin-bottom:4px;'>{skill}</span>"
                    for skill in project['skills']
                ])
                st.markdown(f"<div style='margin-top:8px;'>{skill_tags}</div>", unsafe_allow_html=True)



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
    st.write("Feel free to reach out directly via email!")

    st.markdown(
        """
        <div style='text-align: center; margin-top: 20px;'>
            <a href="mailto:parthan.manisekaran@rwth-aachen.de" 
               style="text-decoration: none;">
                <button style="background-color:#4CAF50; color:white; padding:10px 20px; 
                               text-align:center; border:none; border-radius:5px; cursor:pointer;
                               font-size:16px;">
                    📧 Contact Me via Email
                </button>
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )


# Footer
st.markdown("---")
st.write("© 2024 Parthan Manisekaran. All Rights Reserved.")
