import streamlit as st
from PIL import Image

image_path = "images/profile_pic.png"
# Function to inject custom CSS
def inject_css():
    st.markdown("""
    <style>
    body {
        font-family: 'Arial', sans-serif;
        background-color: #f7f7f7;
        color: #fff;
        text-decoration: none;
    }

    .profile-container {
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 20px;
        gap: 40px; /* Increased gap between columns */
        text-align: center;
        max-width: 900px;
        margin: 0 auto; /* Center the container */
    }

    .text-container {
        text-align: left;
        color: #fff;
    }

    h1, h3 {
        margin: 5px 0;
    }

    .profile-container img {
        border-radius: 50%;
        object-fit: cover;
    }

    .links {
        display: flex;
        justify-content: center;
        gap: 20px; /* Adjusted gap between links */
        margin-top: 20px;
        color: white;
    }

    .links a {
        text-decoration: none;
        color: #ffffff;
        font-weight: bold;
        padding-right: 200px;
    }

    .links a:hover {
        color: #d33682
    }

     .stDownloadButton button {
        color: white;
        background-color: transparent;
        border: 2px solid white;
        padding: 10px 20px;
        border-radius: 20px;
        cursor: pointer;
    }

    .stDownloadButton button:hover{
       color: #d33682;
       border: 2px solid #d33682;
    }

    footer {
        visibility: hidden;
    }

    header {
        visibility: hidden;
    }

    /* Responsive Design */
    @media (max-width: 768px) {
        .profile-container {
            flex-direction: column;
            text-align: center;
        }

        .links a {
            padding-right: 0;
        }
    }
    </style>
    """, unsafe_allow_html=True)


# Function to add a horizontal line
def add_line_break():
    st.markdown("<hr style='margin: 10px 0;'>", unsafe_allow_html=True)


# Function to display the download button
def display_download_button():
    with open(r"C:\Python\YoungDevInterns_Python_Tasks\Soojal_kumar_Resume.pdf", "rb") as file:
        btn = st.download_button(
            label="Download Resume",
            data=file,
            file_name="Soojal_kumar_Resume.pdf",
            mime="application/octet-stream",
            key="download_button"
        )


# Function to display profile image and contact information
def display_profile_and_contact():
    st.markdown("<div class='profile-container'>", unsafe_allow_html=True)

    col1, col2 = st.columns([1, 2], gap="large")

    with col1:
        image = Image.open(image_path)
        st.image(image, width=230, use_column_width=False)

    with col2:
        st.markdown("<div class='text-container'>", unsafe_allow_html=True)
        st.markdown("<h1>Soojal Kumar</h1>", unsafe_allow_html=True)
        st.markdown("<h3>Python Developer</h3>", unsafe_allow_html=True)
        st.markdown("<p><strong>Email:</strong> soojalsachdev2@gmail.com</p>", unsafe_allow_html=True)
        display_download_button()
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown(
        """
        <div class='links'>
            <a class="Linkedin" href='https://www.linkedin.com/in/soojal-kumar/' target='_blank'>LinkedIn</a>
            <a class="Github" href='https://github.com/SoojalSachdev' target='_blank'>GitHub</a>
        </div>
        """,
        unsafe_allow_html=True
    )


# Function to display the rest of the resume
def display_resume_sections():
    add_line_break()
    st.header("About Me")
    st.write("""
        I am a passionate Python Developer and Computer Science student with a strong foundation in programming and web development. My journey into the world of coding began in 2019 when I was in the 10th grade. Driven by curiosity, I moved to Karachi and completed a one-year diploma at Aptech, where I honed my skills in HTML5, CSS3, Bootstrap, JavaScript, C Language, C#, .NET, SQL, and Microsoft Office.

    Currently, I am pursuing a Bachelor of Computer Science at DHA Suffa University and have successfully completed my 4th semester. During my 2nd semester, I took on the role of IT Manager at Intellect Consultancy, where I managed tech-related activities, developed websites, and gained hands-on experience with WordPress. My expertise extends to e-commerce, where I am currently exploring Shopify, building and customizing user-friendly online stores.

    With a strong command over Java, Python, and C, I am dedicated to creating efficient and innovative solutions. I am excited to continue growing my skills and contributing to impactful projects in the tech industry.
        """)


    add_line_break()
    st.header("Education")
    st.write("*Bachelor of Computer Science*")
    st.write("DHA Suffa University – 2022 - 2026")
    st.write("Completed 4th semesters")

    add_line_break()
    st.header("Programming Proficiency")
    st.write("- *Java*: Mastery in crafting robust, efficient applications (2023 - present)")
    st.write("- *Python*: Proficient in developing efficient applications (2022 - 2024)")
    st.write("- *C Language*: Expertise in creating low-level applications (2021 - 2023)")

    add_line_break()
    st.header("Web Development Mastery")
    st.write("- *HTML*: Proficient in creating structured web content (2019 - present)")
    st.write("- *CSS*: Expertise in enhancing visual appeal (2019 - present)")
    st.write("- *Bootstrap*: Skillful in designing responsive websites (2020 - 2021)")
    st.write("- *JavaScript*: Command in building dynamic web applications (2020 - 2021)")

    add_line_break()
    st.header("Work Experience")
    st.subheader("*IT Manager | Intellect Consultancy | Remote Job* (Aug 2023 - July 2024)")
    st.write("""
    Managed all tech-related activities, ensured smooth operation, and 
    set up systems to boost productivity. Developed and managed websites:
    - [www.intellectacc.com](http://www.intellectacc.com/)
    - [takadaassetmanagement.com/gu](https://takadaassetmanagement.com/gu)
    - [scentdaze.com](https://scentdaze.com/)
    """)

    st.subheader("*Python Developer internship| YoungDev Interns | Remote Job* (Aug 2024 - Present)")
    st.write("""
        I am currently completing a 1-month internship as a Python Developer at YoungDev Interns. During this internship, I am focused on:

       - Collaborating on real-world projects, leveraging industry-standard tools and best practices.
       - Creating and refining Python-based solutions in a dynamic remote work environment.
       - Building a diverse portfolio that showcases my technical expertise and problem-solving skills.
       - Gaining hands-on experience in a supportive, collaborative team environment.
        """)

    add_line_break()
    st.header("Shopify Experience")
    st.write("""
    - *Shopify (May 2024 - July 2024)*: Created and customized websites using Shopify.
    - 2 months of hands-on experience with the Shopify platform.
    - Built and designed user-friendly online stores, improved layouts, and added features.
    """)

    add_line_break()
    st.header("Contact Information")
    st.write("*Phone*: +92 333 7301936")
    st.write("*Email*: soojalsachdev2@gmail.com")
    st.write("*LinkedIn*: [linkedin.com/in/soojal-kumar](https://www.linkedin.com/in/soojal-kumar/)")
    st.write("*Address*: Clifton, Karachi.")

# Main function to display the resume
def main():
    st.set_page_config(page_title="Soojal Kumar | Resume ", layout="wide", initial_sidebar_state="collapsed")
    inject_css()
    display_profile_and_contact()
    display_resume_sections()


if __name__ == "__main__":
    main()
