import streamlit as st 
import streamlit.components.v1 as components 
from transformers import pipeline 

components.html(
    """
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

    <style>
        .jumbotron{
            background: lightcoral;
        }
        .display-4{
            display: flex;
            justify-content: center;
            color: black;
            font-weight: bold;
        }
        p{
            display: flex;
            justify-content: center;
        }
    </style>

    <div class="jumbotron">
        <h1 class="display-4">Q&A Model</h1>
        <p class="lead">Find ans to the question of your article!!!</p>
        <hr class="my-4">
        <p>It uses utility classes for typography and spacing to space content out within the larger container.</p>
        <p class="lead">
            <a class="btn btn-primary btn-lg" href="#" role="button">Learn more</a>
        </p>
    </div>


    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
    """,
    height=200,
)

@st.cache(allow_output_mutation=True)
def load_model():
    model = pipeline("question-answering")
    return model

qa = load_model()
st.title("QUESTION-ANSWERING SYSTEM")
articles = st.text_area("Write the Article or the passage") 
quest = st.text_input("Ask the Question")
button = st.button("Answer")
with st.spinner("Finding Answer..."):
    if button and articles:
        answers = qa(question = quest, context = articles)
        st.success(answers)
        
