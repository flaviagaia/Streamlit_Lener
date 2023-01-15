# https://medium.com/@groxli/create-a-spacy-visualizer-with-streamlit-8b9b41b36745
# https://gitlab.com/groxli/spacy-visualizer-with-streamlit/-/blob/main/visualizer.py

import streamlit as st
import spacy
from spacy import displacy

st.title("Web APP LeNER-Br")

#Texto:
input_text = st.text_input('Insira o texto a ser analisado:', 'Que causaram evidente transtorno e evidencia a má prestação de serviço, com violação ao princípio da transparência, da confiaça e da boa-fé objetiva insertos nos artigos 4º e 6º do CDC. Por todo o acima exposto, na forma do artigo 269, I do Código de Processo Civil, conhecido e apelação não promovida. (Apelação Cível 2009 01 1 075609-5 APC Relator Desembargador JAIR SOARE.) Em relação ao CONTRATO BANCÁRIO INVERSÃO DO ÔNUS DA PROVA CDC Possibilidade da inversão do ônus da prova com base no artigo 6º, VIII, do CDC Reconhecido que o cliente tem direito de postular a exibição de documentos - Possibilidade de determinação pelo juiz incidentalmente.')

# Função que carrega os modelos:
def load_models():
    sm_model = spacy.load("modelo_lener_sm")
    lg_model = spacy.load("modelo_lener_lg")
    models = {"sm": sm_model, "lg": lg_model}
    return models

models = load_models()
selected_type = st.sidebar.selectbox("Selecione o tipo do modelo", options=["sm", "lg"]) # caixa de seleção do modelo
selected_model = models[selected_type]
doc= selected_model(input_text) # função doc que processa o texto de acordo com a opção escolhida acima

# Cabeçalho
st.header("Visualizador de entidades")

#Cores:
colors = {"LEGISLACAO": "linear-gradient(90deg, #aa9cfc, #fc9ce7)", 'JURISPRUDENCIA': "#ccfbf1", 'LOCAL': "#ffedd5", 'ORGANIZACAO': "#fae8ff", 'PESSOA': "#e0f2fe", 'TEMPO': "#fefde0", }
options = {"ents": ["LEGISLACAO", "JURISPRUDENCIA", "LOCAL", "ORGANIZACAO", "PESSOA", "TEMPO",], "colors": colors}

#Html:
ent_html = displacy.render(doc, style="ent", options=options, jupyter=False) # https://spacy.io/usage/visualizers

st.markdown(ent_html, unsafe_allow_html=True)

# streamlit run render.py