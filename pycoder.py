import os
import streamlit as st

from groq import Groq

st.set_page_config(
    page_title="Pycoder", 
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

CUSTOM_PROMPT = """
você é o Pycoder, um assistente de programação especializado em Python.
Seu objetivo é ajudar os usuários a escrever, entender e depurar código Python.
REGRAS DE OPERAÇÃO:
1. **Foco em progamação python**: Responda apenas a perguntas relacionadas a programação, algoritimos, estruturas de dados, bibliotecas e frameworks Python.
2. **Estrutura de Resposta**: Sempre formate suas respostas da seguinte maneira:
* **Explicação Clara**: Comece com uma explicação conceitual sobre o topico perguntado. Seja direto e didático.
* **Exemplos de Código**: Forneça um ou mais blocos de código em Python com a sintaxe correta . O codigo deve ser bem comentado para explicar as partes importantes.
* **Detalhes do código**: Após o bloco do código, descreva em detalhes o que cada parte o código faz, explicando a lógica e funções utilizadas.
* **Melhores Práticas**: Inclua dicas sobre melhores práticas, padrões de codificação e armadilhas comuns a serem evitadas.
* **Documentação de Referência**: Ao final, incluam uma sessção chamda "Documentação de Referência" com links direto  para a documentação oficial ou recursos adicionais relevantes.
3. **Clareza e Precisão**: Mantenha suas respostas claras, concisas e focadas no tópico. Evite informações irrelevantes e jargões desnecessários, sua  resposta deve ser tecnicamente precisa.
"""

with st.sidebar:
    st.title("Pycoder")
    st.markdown("Um assistente de IA focado em programação Python para ajudar iniciantes e desenvolvedores experientes.")
    groq_api_key = st.text_input(
        "insira sua Groq API Key:", 
        type="password", 
        help="Obtenha sua chave em https://console.groq.com/keys"
    )
    st.markdown("---")
    st.markdown("Desenvolvido para auxiliar em suas duvidas de programação com Linguagem Python. Toda IA pode cometer erros, por favor, revise o código gerado antes de usar em produção.")

    st.markdown("---")
    st.markdown("Veja meus Outros Projetos:")

    st.markdown("[wSanice](https://github.com/wSanice)")

    st.link_button("GitHub", url="https://github.com/wSanice")

st.title("Pycoder IA")
st.title("Assistente Pessoal de Programação Python")
st.caption("Faça sua pergunta sobre linguagem Python e obtenha código, aplicações e referencias.")

if"messages" not in st.session_state:
    st.session_state.messages = []
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])