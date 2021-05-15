# -*- coding: utf-8 -*-
"""
Created on Sun May 16 01:53:25 2021

@author: ASUS
"""


import pandas as pd
import streamlit as st
import cv2
from PIL import Image, ImageEnhance
import numpy as np
import os
from io import BytesIO
import base64


def get_image_download(img):
    buffered = BytesIO()
    img.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    href = f'<a href="data:file/jpg;base64,{img_str}">Download result</a>'
    return href

def main():
    st.title("1st web-APP")
    st.text("Build using streamlit")

    activity = ['detetion', 'About']

    im_file = st.file_uploader("upload" , type= ['jpg', 'png'])

    if im_file is not None:
        op_im = Image.open(im_file)
        st.text("Origninal Image")
        st.image(op_im)

    # Adding Enhancement
    enhanceType = st.sidebar.radio("Enhance Type", ["Original","BNW", "Brightness", "Contrast", "Sharpness", "Blurring", "Hsv_split"])
    if enhanceType == "BNW":
        new_im = np.array(op_im.convert('RGB'))
        bnw_img = cv2.cvtColor(new_im , cv2.COLOR_RGB2GRAY)

        st.image(bnw_img)
    #if enhanceType == "Original":
    #   new_im = np.array(op_im.convert('RGB'))

     #   org_img = cv2.cvtColor(new_im , 0)
     #   st.image(org_img)
    if enhanceType == "Contrast":
        rate = st.sidebar.slider("Contrast", 0.5 , 8.5, 4.2)
        enhancer = ImageEnhance.Contrast(op_im)
        im_op = enhancer.enhance(rate)
        st.image(im_op)

    if enhanceType == "Blurring":
        new_img = np.array(op_im.convert('RGB'))
        blur_rate = st.sidebar.slider('Blurring', 0.1, 6.0, 2.1)
        img = cv2.cvtColor(new_img,1)
        gray = cv2.GaussianBlur(img, (11,11), blur_rate)
        st.image(gray)
        result = Image.fromarray(gray)
        st.markdown(get_image_download(result) , unsafe_allow_html= True)


    if enhanceType == "Sharpness":
        rate = st.sidebar.slider("Sharpness", 0, 10, 3)
        enhancer = ImageEnhance.Sharpness(op_im)
        sh_op = enhancer.enhance(rate)
        st.image(sh_op)

    if enhanceType == "Brightness":
        rate = st.sidebar.slider("Brightness", 0, 10, 3)
        enhancer = ImageEnhance.Brightness(op_im)
        br_op = enhancer.enhance(rate)
        st.image(br_op)
    if enhanceType == "Hsv_split":
        new_img = np.array(op_im.convert('RGB'))

        h_rate = st.sidebar.slider("H", 0.1, 1.0, 1.0)
        s_rate = st.sidebar.slider("S", 0.1,1.0,1.0)
        v_rate = st.sidebar.slider("V", 0.1, 1.0, 1.0)
        #hsv=cv2.cvtColor(new_img, cv2.COLOR_BGR2HSV)
        H,S,V = cv2.split(new_img)
        new_pic = cv2.merge([np.uint8(H*h_rate), np.uint8(S*s_rate),np.uint8(V*v_rate)])
        st.image(new_pic)

if __name__ == "__main__":
    main()




