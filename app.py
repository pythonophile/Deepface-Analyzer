import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
os.environ['ABSL_LOGGING_LEVEL'] = 'error'

import logging
import warnings

warnings.filterwarnings('ignore')
logging.getLogger('tensorflow').setLevel(logging.ERROR)

import streamlit as st
import cv2
from deepface import DeepFace
import numpy as np
from PIL import Image


st.set_page_config(page_title = "Deep Face Full Analyzer", layout = "wide")
st.title("Full Facial Attribute & Liveness Checker")
st.markdown("This App Detects the Emotons, Age, Gender, and Race using Deep Face Library")

option = st.sidebar.selectbox("Select Input Source:" ,  ['Image Upload' , 
                                                         'Video Upload' , 
                                                         'Live Webcam'])

def perform_full_analysis(frame):
    try:
        results = DeepFace.analyze(
            img_path = frame,
            actions = ['emotion', 'age' , 'gender' , 'race'],
            enforce_detection = False,
            anti_spoofing = True
        )
        if results[0]['face_confidence'] > 0:
            return results[0]
        return None
    except Exception:
        return None

if option == "Image Upload":
    file = st.file_uploader("Upload a Photo", type = ['png' , 'jpeg' , 'png'])
    if file:
        img = Image.open(file)
        img_array = np.array(img)
        st.image(img, caption = "Target Image" , width = 500)
    
    if st.button("Run Full Analysis"):
        with st.spinner("Analyzing all facial Expressions"):
            res = perform_full_analysis(img_array)
            
            if res:
                col1, col2 = st.columns(2)
                with col1:
                    st.subheader("Results")
                    st.write(f"Emotion: {res['dominant_emotion']}")
                    st.write(f"Estimated Age: {int(res['age'])}")
                    st.write(f"Gender: {res['dominant_gender']}")
                    st.write(f"Dominant Race: {res['dominant_race']}")
                with col2:
                    st.subheader("Security Check")
                    is_real = "Real Person" if res.get("is_real") else "Spoof Detected"
                    st.info(f"Liveness Status: {is_real}")
            else:
                st.error("Face is not Recognizable")

elif option == "Live Webcam":
    st.info("The AI will overlay detected data onto the Screen")
    run = st.checkbox("Enable Camera")
    FRAME_WINDOW = st.image([])
    
    if run:
        cam = cv2.VideoCapture(0)
        while run:
            ret, frame = cam.read()
            if not ret: break
            
            display_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            res = perform_full_analysis(display_frame)
            
            if res:
                region = res['region']
                x,y,w,h = region['x'] , region['y'], region['w'], region['h']
                label = f"{res['dominant_emotion']} | {int(res['age'])}yrs | {res['dominant_gender']} | {res['dominant_race']}"
                
                cv2.rectangle(display_frame, (x, y), (x+w, y+h) , (0, 255, 0), 2)
                cv2.putText(display_frame, label, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6,
                            (0, 255, 0), 2)
            FRAME_WINDOW.image(display_frame)
        cam.release()
elif option == "Video Upload":
    video_data = st.file_uploader("Upload Video" , type = ["mp4" , "avi"])
    if video_data:
        st.video(video_data)
        st.warning("Deep Face Analysis for Videos takes a lot of computer Power!")