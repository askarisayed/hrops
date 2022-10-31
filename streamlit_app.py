import streamlit as st
import warnings
from streamlit import components
from nlp_backend import nlp_backend
from pathlib import Path


def main():
    
    st.title("Hrops")
    backend = nlp_backend()

    #Upload the JD in Word Document Format
    uploadfile = st.file_uploader("Upload the Job Description",accept_multiple_files=False)
    if uploadfile is not None:
        JD = backend.JD_process('uploadfile')
    else:
        print("File Not Found Error")

    #upload the Resumes in PDF Format
    uploaded_file1 = st.file_uploader("Upload the Resumes here" , accept_multiple_files=True)
    if uploaded_file1 is not None:
        resumes1 = backend.Resumes_process('uploaded_file1')
    else:
        print('Check the Uploaded File')

    #Checking the Simlarity Score between JD and Resumes
    sim = backend.check_sim(JD,resume_res)

    if st.button("Get the Top Resumes"):
        st.write("here are top resumes",sim)
    else:
        st.write("Error")


if __name__ == "__main__":
    main()
