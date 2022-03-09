#Importing Libraries:
import streamlit as st 
from gramformer import Gramformer
#import tensorflow
from PIL import Image
import pandas as pd

st.set_page_config(page_title="App-Grammer-Checker",page_icon="random",layout="wide",
                       menu_items={'Get Help': 'https://www.linkedin.com/in/vinoth24',
                                   'Report a bug': "https://github.com/Vinoth-24/Grammer_checker",
                                   'About': "# This is a Grammer Corrector App based on Gramformer Pretrained model built with Streamlit."})
    

@st.cache(show_spinner=False, suppress_st_warning=True, allow_output_mutation=True)
def load_model():
    #Load Gramformer model
    gf = Gramformer(models=1, use_gpu=False)
    return gf
    
with st.spinner('Loading model..'):
            gf = load_model()
        

def upload_df():
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:

        # Can be used wherever a "file-like" object is accepted:
        dataframe = pd.read_csv(uploaded_file)
        st.write(dataframe)
        return dataframe
    else:
        return None
    
def apply_model(df):    
    df['text'] = df['text'].astype(str)
    df['corrected_text'] = df['text'].map(lambda text: correct_grammer(text))
    return df

def correct_grammer(text):
    corrected_sentences = gf.correct(text, max_candidates=1)
    return ', '.join(corrected_sentences)

def get_edit_instances(corrected_df):
    corrected_df['edit_instances'] = corrected_df.apply(lambda x: gf.get_edits(x["text"], x["corrected_text"]), axis=1)
    return corrected_df

def gram_acc(corrected_df_with_edit):
    corrected_df_with_edit["accuracy %"] = corrected_df_with_edit.apply(lambda x: ((len(x["text"].split()) - len(x["edit_instances"]))/len(x["text"].split()))*100, axis=1)
    corrected_df_with_edit = corrected_df_with_edit.drop('edit_instances', 1)
    corrected_df_with_edit[corrected_df_with_edit["accuracy %"] < 0] = 0
    #corrected_df_with_edit = corrected_df_with_edit['accuracy %'].round(decimals = 1)
    corrected_df_with_edit['accuracy %'] = corrected_df_with_edit['accuracy %'].round(decimals = 1)
    return corrected_df_with_edit

# Decor Func:    
def decor():
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Grammer Checker for NEXTLABS </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    image = Image.open('How-to-improve-grammar.jpg')
    st.image(image, caption='')  
    
def convert_df(df):
    return df.to_csv().encode('utf-8')
    
def main():

    decor()
    df = upload_df()
    if df is not None:
        st.info("Take a nap if you have uploaded the full YELP dataset.")
        with st.spinner('Grammer correction in progress.. ...'):
            corrected_df = apply_model(df)
            corrected_df_with_edit = get_edit_instances(corrected_df)
            df_with_gram_acc = gram_acc(corrected_df_with_edit)
        df_with_gram_acc = df_with_gram_acc.astype(str) # bcoz of some bug with streamlit df
        st.write("Output dataset")
        st.dataframe(df_with_gram_acc) 
        csv = convert_df(df_with_gram_acc)   
        st.download_button(
                    label="Download data as CSV",
                    data=csv,
                    file_name='corrected_review.csv',
                    mime='text/csv',
                    )

        st.success("Review Text has been corrected and Grammatical accuracy has been measured!")
    else:
        pass
    st.markdown("---")
    
# My Details:

    expander=st.expander("My Details",expanded=False)
    with expander:
        st.write("Kasi Vinoth S")
        st.write("LinkedIn [link](https://www.linkedin.com/in/vinoth24)")
        st.write("Github repo for this app [link](https://github.com/Vinoth-24/Grammer_checker)")
        st.write("Medium [link](https://medium.com/@vino24995)")

# Program Starts:
if __name__=='__main__':
    main()
