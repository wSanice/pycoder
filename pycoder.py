import os
import streamlit as st

from groq import Groq

st.set_page_config(
    page_title="Ophiuchus", 
    page_icon="⛎",
    layout="wide",
    initial_sidebar_state="expanded"
)

CUSTOM_PROMPT = """
você é o Ophiuchus, um assistente de programação especializado em Python.
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
    st.title("Ophiuchus")
    st.markdown("Assistente de IA focado em programação Python.")
    groq_api_key = st.text_input(
        "insira sua Groq API Key:", 
        type="password", 
        help="Obtenha sua chave em https://console.groq.com/keys"
    )
    st.markdown("---")
    st.markdown("Desenvolvido para auxiliar em suas duvidas de programação com Linguagem Python.")
    st.markdown("Toda IA pode cometer erros, por favor, revise o código gerado antes de usar em produção.")

    st.markdown("---")
    st.markdown("Veja meus Outros Projetos:")
    st.link_button("GitHub", url="https://github.com/wSanice")

st.title("Ophiuchus IA")
st.subheader("Assistente Pessoal de Programação Python")
st.caption("Faça sua pergunta sobre linguagem Python e obtenha códigos, aplicações e referências.")

if"messages" not in st.session_state:
    st.session_state.messages = []
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

client = None

if groq_api_key:
    try:
        client = Groq(api_key = groq_api_key)
    except Exception as e:
        st.sidebar.error(f"Erro ao conectar com Groq: {e}")
        st.stop()
elif st.session_state.messages:
    st.warning("Por favor, insira sua Groq API Key na barra lateral para continuar.")
if prompt := st.chat_input("Digite sua pergunta sobre Python aqui..."):
    if not client:
        st.warning("Por favor, insira sua Groq API Key na barra lateral para continuar.")
        st.stop()
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)
    message_for_api = [{"role": "system", "content": CUSTOM_PROMPT}]
    for msg in st.session_state.messages:
        message_for_api.append(msg)
    with st.chat_message("assistant"):
        with st.spinner("Analisando sua pergunta..."):
            try:
                chat_completion = client.chat.completions.create(
                    messages=message_for_api,
                    model = "openai/gpt-oss-20b",
                    max_tokens=2048,
                    temperature=0.2,
                    top_p=0.9,
                )

                pycoder_resposta = chat_completion.choices[0].message.content
                st.markdown(pycoder_resposta)
                st.session_state.messages.append({"role": "assistant", "content": pycoder_resposta})
            except Exception as e:
                st.error(f"Erro ao obter resposta da sua API da Groq: {e}")
st.markdown(
    """
    <div style="text-align: center; color: gray;">
    <hr>
    <p>Feito por [wSanice](https://github.com/wSanice)</p>
    <p>Ophiuchus é um projeto de estudo desenvolvido no curso da DSA e não é afiliado a Groq ou OpenAI.</p>
</div>
""", unsafe_allow_html=True
)
#Obrigado DSA ❤️!