import streamlit as st
import warnings
from streamlit import components
import docx2txt
from PyPDF2 import PdfFileReader

def read_pdf(pdf_file):
    pdfReader = PdfFileReader(pdf_file)
    count = pdfReader.numPages
    all_page_text = ""
    for i in range(count):
        page = pdfReader.getPage(i)
        all_page_text += page.extractText()
    return all_page_text


def main():
    
    st.title("Hrops")
    # backend = nlp_backend()

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
    st.subheader("Upload the Resumes")
    pdf_file = st.file_uploader("Resumes",accept_multiple_files=True)
    if st.button("Submit"):
        if pdf_file is not None:
#             file_details = {"filename":pdf_file.name,"filetype":pdf_file.type,"filesize":pdf_file.size}
#             st.write(file_details)
            if pdf_file.type == "text/pdf":
                raw_text = str(pdf_file.read(),"utf-8")
                st.text(raw_text)
        elif pdf_file.type == "application/pdf":
            pass
        raw_text = read_pdf(pdf_file)
        st.write(raw_text)









if __name__ == "__main__":
    main()
