import streamlit as st
from groq import Groq

st.set_page_config(page_title="Padaria", page_icon="🥖")
st.markdown('<style>#MainMenu,footer,header{visibility:hidden;}</style>', unsafe_allow_html=True)

# COLA TUA CHAVE AQUI DENTRO DAS ASPAS
client = Groq(api_key="gsk_COLE_SUA_CHAVE_AQUI")

st.title("Atendente Padaria Pão Quentinho 🥖")

if "msg" not in st.session_state: 
    st.session_state.msg = []

for m in st.session_state.msg:
    with st.chat_message(m["role"]): 
        st.write(m["content"])

if txt := st.chat_input("Digite aqui..."):
    st.session_state.msg.append({"role":"user","content":txt})
    with st.chat_message("user"): st.write(txt)
    
    resposta = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role":"system","content":"Você é atendente de padaria. NUNCA use ` ou **. Preco: R$ 0,90"}] + st.session_state.msg
    )
    resp = resposta.choices[0].message.content.replace("`","")
    
    st.session_state.msg.append({"role":"assistant","content":resp})
    with st.chat_message("assistant"): st.write(resp)
