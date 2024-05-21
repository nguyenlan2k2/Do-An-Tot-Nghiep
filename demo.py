import cv2
import threading
import streamlit as st
import matplotlib.pyplot as plt

def addUser() -> None:
    video = cv2.VideoCapture(0)
    i = 0
    st.text("Getting 500 Image...")
    while(True):
        i += 1
        st.text(f"Number of images : {i} / 500")
        ret, frame = video.read()

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        if st.button("Stop"):
            break

def main() -> None:
    st.title("FACE RECOGNITION SYSTEM")
    addUser()
    st.devider()
    

if __name__ == "__main__":
    main()