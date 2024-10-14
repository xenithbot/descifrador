import streamlit as st
import requests
from streamlit_option_menu import option_menu
from streamlit_lottie import  st_lottie
import os
import toml
import google.generativeai as genai

api_key = st.secrets["settings"]["GOOGLE_API_KEY"]

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

st.set_page_config(page_title="Descifrador")

def  load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

with st.sidebar:
    selected_page = option_menu(
        "Navigation",
        ["About Me", "Skills", "Chat Bot"],
        icons = ['house','briefcase','robot'],
        menu_icon="gear",
        default_index=0,
    )

def about_me():
    st.markdown('''# About Me

Hello! I'm **Krishna**, also known as **descifrador93**. I'm 17 years old and currently a student in 11th grade, focusing on the science stream with Physics, Chemistry, and Mathematics (PCM), along with Computer Science. I'm preparing for the JEE to pursue my passion for engineering.

I have been programming for 5 years now, starting during the lockdowns of COVID-19. I consider myself a versatile developer and I'm always eager to learn and explore new technologies.

## Location
I'm from **Delhi, India**.
''')

    # lottie_url = "https://lottie.host/eee3dbab-2db1-47ff-8517-bbe523b2e542/DJxtNRMpWw.json"
    # lottie_animation = load_lottieurl(lottie_url)
    # if lottie_animation:
    #     st_lottie(lottie_animation, speed=1, height=300, key="home")
    # else:
    #     st.error("Failed to load Lottie animation.")

    with st.container():
        col1, col2 = st.columns(2)

        with col1:
            st.markdown('''## Connect with Me
- GitHub: [descifrador93](https://github.com/descifrador93)
- Instagram: [descifrador93](https://instagram.com/descifrador93)
- Discord: [descifrador93](https://discord.com/users/1040483999421833226)''')
            st.write("## I Like To Talk About")
            st.markdown("""
                        - **Technology Trends**
                        - **Programming Languages**
                        - **Personal Development**
                        - **Video Games**
                        - **Discord**
                        - **Creative Projects** 
                        """) 
        with col2:
            st.image('image.png')

    st.warning("While I may not excel in design, I'm opting for Streamlit to create a straightforward and user-friendly interface.")

def skills():
    
    with st.container():
        st.write("## 💼 My Skills")
        col1, col2 = st.columns(2)
        with col1:
            st.write("""
                    - **Languages**: Python, Java, JavaScript
                    - **Libraries**: Pandas, Numpy, Matplotlib, Metasploit, Google-Generativeai, Pycord
                    - **Frameworks**: Streamlit, Bootstrap CSS, Django
                    - **Tools**: Git, VS Code
                    - **Machine Learning**: Scikit-learn
                    - **Deep Learning**: Tensorflow, OpenCV, Torch
                    - **Others**: Linux, Web Automation, Natural Language Processing
                """)
        with col2:
            lottie_url = "https://lottie.host/e0f72cc9-db24-4eac-a85e-19bb821629f9/mumuEVoTHL.json"
            lottie_animation = load_lottieurl(lottie_url)
            if lottie_animation:
                st_lottie(lottie_animation, speed=1, height=300, key="skills")
            else:
                st.error("Failed to load Lottie animation.")    

def chatbot():
    def get_gemini_response(question):
        response = chat.send_message(question)
        return response
    
    st.header("Powered by Gemini ChatBot Application")

    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []

    input = st.text_input("Query:", key="input")
    submit = st.button("Ask XenithBot")

    if submit and input:
        response = get_gemini_response(input)
        st.subheader("Response:")
        st.write(response.text)
    
if selected_page ==  "About Me":
    about_me()
elif selected_page ==  "Skills":
    skills()
elif selected_page == "Chat Bot":
    chatbot()
