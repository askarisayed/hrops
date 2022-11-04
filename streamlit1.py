import streamlit as st
import warnings
from streamlit import components
import docx2txt
import pdfminer
from pdfminer.high_level import extract_pages
from nlp_backend import nlp_backend

def read_pdf(uploaded_file):
    pdfReader = PdfFileReader(uploaded_file)
    count = pdfReader.numPages
    all_page_text = ""
    for i in range(count):
        page = pdfReader.getPage(i)
        all_page_text += page.extractText()
    return all_page_text


def main():
    
    st.title("Hrops")
    backend = nlp_backend()

    #Upload the JD in Word Document Format
    st.subheader("Upload the Job Description")
    docx_file = st.file_uploader("",accept_multiple_files=False)
    if st.button("upload"):
        if docx_file is not None:
            file_details = {"filename":docx_file.name,"filetype":docx_file.type,"filesize":docx_file.size}
            st.write(file_details)
            if docx_file.type == "text/docx":
                raw_text = str(docx_file.read(),"utf-8")
                st.text(raw_text)
            elif docx_file.type == "application/pdf":
                pass
            raw_text = docx2txt.process(docx_file)
            st.write(raw_text)
    
    # Upload the Resumes in PDF or Text Format. 
    uploaded_file = st.file_uploader("Choose a file", "pdf")
    if uploaded_file is not None:
        for page_layout in extract_pages(uploaded_file):
            for element in page_layout:
                st.write(element)
    
    sim = backend.check_sim(docx_file,uploaded_file)
    if st.button("Get the Top Resumes"):
        st.write("here are top resumes",sim)
    else:
        st.write("Error")
        
if __name__ == "__main__":
    main()
