from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My First Page", page_icon=":jack_o_lantern:",layout="wide")
# Head to WebFX for simple page icons.

def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ---LOAD ASSETS ---
lottie_space = load_lottie("https://lottie.host/75fbc781-23cf-44b8-b58e-cf9c2293031a/UPiOzEeyeU.json")
python_image = """
    <image src="https://images.unsplash.com/photo-1515879218367-8466d910aaa4?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1169&q=80" alt="python" width=450 style ="border-radius: 15px;">
"""
Voice_assistant_image = """
    <image src="https://images.unsplash.com/photo-1613632826230-09e39f7306b4?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1170&q=80" alt="Siri" width=450 style ="border-radius: 15px">
"""
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}        
</style>
""",unsafe_allow_html=True)
contact_form = """
    <form action="https://formsubmit.co/aryansingh.as235@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name here" required>
        <input type="email" name="email" placeholder="Your email here" required>
        <textarea name='message' placeholder="Your message here" required></textarea><br/>
        <button type="submit">Send</button>
        <style>
            input[type=message], input[type=email], input[type=text], textarea {
                width: 100%;padding: 12px; border: 1px solid #ccc; border-radius: 4px;
                box-sizing: border-box; margin-top: 6px; margin-bottom: 16px; resize: vertical
            }
            button[type=submit] {
                background-color: #04AA6D; color: white; padding: 12px 20px;
                border: none; border-radius: 4px; cursor: pointer;
            }
            button[type=submit]:hover {
                background-color: #45a049;
            }
        </style>
    </form>
"""

# ---HEADER SECTION ---
with st.container():
    st.subheader("Hi, I am Aryan :wave:")
    st.title("I am a student:student: from Mumbai.")
    st.write("I am passionate about learning about new softwares and using them in real-life scenarios.")
    st.write("[Learn more-->](https://www.google.co.in/)")

# --- What I Do ---
with st.container():
    st.write("---")
    left_column,right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")            
        st.write(
            """
            Lorem ipsum dolor sit amet consectetur adipisicing elit:
            - Voluptas nisi mollitia quam, repellendus dolorem quis sunt ullam provident ipsum quos.
            - Perspiciatis reiciendis minima a facilis nostrum velit quidem veniam.
            - Dignissimos vel libero consequuntur placeat quas quos quia illo cum quo debitis, dolorem totam hic!
            - Vero commodi cumque aliquid assumenda culpa aspernatur, dolorem in dicta aperiam vitae

            Eos qui temporibus laboriosam esse veniam sint ut inventore facilis nulla est nemo debitis.
            """
        )
        st.write("[Watch-->](https://youtube.com)")

    with right_column:
        st_lottie(lottie_space, height=400, key="astronaut")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.markdown(python_image,unsafe_allow_html=True)
    with text_column:
        st.subheader("Python Object Oriented Programming")
        st.write(
            """
            Ipsam earum voluptate sequi, reiciendis, sit !
            Accusantium nulla fuga illo assumenda sed est, aspernatur ullam tenetur veritatis esse hic fugit quaerat blanditiis.
            Fugit deleniti architecto quos doloremque assumenda veritatis
            """
        )
        st.markdown("[Repository...](https://github.com/Aryan-webp/antariksh-py-lectures)")
st.write("##")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column :
        st.markdown(Voice_assistant_image,unsafe_allow_html=True)
    with text_column:
        st.subheader("How To Automate Your Work With A Voice Assistant")
        st.write(
            """
            Corporis eum rerum praesentium facilis eius perspiciatis quasi?
            dignissimos voluptatibus sunt laboriosam! Inventore dolore in, sit magni, aliquam, harum iste atque nihil ‘doloribus architecto’ sequi sapiente maiores.
            """
        )
        st.markdown("[Repository...](https://github.com/Aryan-webp/Voice_Assistant)")
    
# ---CONTACT---
with st.container():
    st.write("---")
    st.subheader("Get in touch with me:")
    st.write("##")
    left_column,right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()

