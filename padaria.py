import streamlit as st
from groq import Groq

st.set_page_config(page_title="Bot Padaria", layout="centered")
st.title("🥖 Bot Atendente - Padaria Pão Quentinho")

client = Groq(api_key="gsk_COLA_SUA_CHAVE_AQUI")

DADOS_PADARIA = """
Nome: Padaria Pão Quentinho
Horário: Segunda a Domingo, 05:00 às 20:00

CARDÁPIO OFICIAL:
- Pão francês: R$ 0,90
- Bolo fatia: R$ 6,00 
- Bolo inteiro: R$ 25,00
- Sonho: R$ 3,50
- Café: R$ 3,00

PROMOÇÃO: Compre 10 pães franceses e ganhe 1 café grátis.

REGRA: 
1. Use SEMPRE os preços exatos acima.
2. Escreva frases completas com R$ e vírgula. Ex: R$ 6,00
3. Seja educado e termine com uma pergunta.
"""

SYSTEM = {"role": "system", "content": DADOS_PADARIA}

if "msgs" not in st.session_state:
    st.session_state.msgs = [SYSTEM]

for m in st.session_state.msgs:
    if m["role"]!= "system":
        with st.chat_message(m["role"]):
            st.markdown(m["content"])

if prompt := st.chat_input("Olá! Em que posso ajudar?"):
    st.session_state.msgs.append({"role": "user", "content": prompt})
    with st.chat_message("user"): st.markdown(prompt)

    resposta = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=st.session_state.msgs,
        temperature=0.1, # <- Bem baixo pra não inventar
        max_tokens=300 # <- Aumentei pra não cortar a frase
    ).choices[0].message.content

    st.session_state.msgs.append({"role": "assistant", "content": resposta})
    with st.chat_message("assistant"):
        st.markdown(resposta)