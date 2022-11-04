import tensorflow as tf
import numpy as np
import os
import glob 
import tensorflow_hub as hub
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st
import docx2txt

class nlp_backend:

    def load_model():
        model_url = "https://tfhub.dev/google/universal-sentence-encoder/4"
        model = hub.load(model_url)
        return model
    
    def JD_process(docx_file):
        JD1 = docx2txt.process(docx_file)
        return JD_process
    
    def Resumes(uploaded_file):
        resumes = glob.glob('uploaded_file',recursive = True)
        return Resumes
    
    def check_sim(job_desc: str):

        model_obj = nlp_backend.load_model()
        resumes = nlp_backend.Resumes()
        query_vec = model_obj([job_desc])
        for single in resumes:
            with open(single,'rb') as f:
                sentences_list = [f.read()]
                sentence_embeddings = model(sentences_list)
                sim = cosine_similarity(query_vec, sentence_embeddings)
        
        return sim

   
