import streamlit as st
from groq import Groq

st.set_page_config(page_title="Padaria Pão Quentinho", page_icon="🥖", layout="centered")
st.markdown('<style>#MainMenu,footer,header{visibility:hidden;}</style>', unsafe_allow_html=True)

try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
except:
    st.error("Erro: GROQ_API_KEY não encontrada nos Secrets. Vai em Manage app > Settings > Secrets")
    st.stop()

PROMPT_DO_SISTEMA = """Você é o atendente da PADARIA PÃO QUENTINHO 🥖
CARDAPIO: Pão Francês R$ 0,90 | Café R$ 4,50
REGRA: NUNCA use crase ` nem asterisco. Escreva preco: R$ 0,90
Para pedido: peca NOME, PEDIDO e ENDERECO
"""
st.title("Atendente Virtual Padaria Pão Quentinho 🥖")

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": PROMPT_DO_SISTEMA}]

for message in st.session_state.messages[1:]:
    with st.chat_message(message["role"]):
        st.write(message["content"]) # troquei markdown por write pra não bugar

if prompt := st.chat_input("Digite sua mensagem..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    chat_completion = client.chat.completions.create(
        messages=st.session_state.messages,
        model="llama-3.1-8b-instant",
    )
    response = chat_completion.choices[0].message.content
    response = response.replace("`", "").replace("**", "").replace("*", "")

    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.write(response)
