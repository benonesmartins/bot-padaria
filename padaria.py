import streamlit as st
from groq import Groq

st.set_page_config(page_title="Padaria Pão Quentinho", page_icon="🥖", layout="centered")
st.markdown('<style>#MainMenu,footer,header{visibility:hidden;}</style>', unsafe_allow_html=True)

# COLA TUA CHAVE AQUI
client = Groq(api_key="gsk_COLE_SUA_CHAVE_AQUI")

PROMPT = """Você é o atendente virtual da PADARIA PÃO QUENTINHO 🥖

INFORMAÇÕES:
Endereço: Rua das Flores, 123 - Centro, Morada Nova - CE
Horário: SEG A SEX: 5H-20H | SAB: 5H-18H | DOM: 5H-12H
WhatsApp: (88) 9 9999-8888
Entrega: SIM. Taxa de R$5,00.

CARDÁPIO:
Pão Francês: R$ 0,90
Café Pequeno: R$ 4,50
Café Grande: R$ 6,00
Bolo de Pote: R$ 8,00

REGRAS:
1. Seja educado e use emoji 🥖
2. NUNCA use crase ` nem asterisco **. Escreva preco assim: R$ 0,90
3. Para pedido: peca NOME, PEDIDO e ENDERECO. Depois confirme.
"""

st.title("Atendente Virtual Padaria Pão Quentinho 🥖")
st.write("Olá! Posso te ajudar com cardápio, preços e pedidos.")

if "msg" not in st.session_state: 
    st.session_state.msg = [{"role":"system","content":PROMPT}]

for m in st.session_state.msg[1:]:
    with st.chat_message(m["role"]): 
        st.write(m["content"])

if txt := st.chat_input("Digite sua mensagem..."):
    st.session_state.msg.append({"role":"user","content":txt})
    with st.chat_message("user"): st.write(txt)
    
    resposta = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=st.session_state.msg
    )
    resp = resposta.choices[0].message.content.replace("`","").replace("**","")
    
    st.session_state.msg.append({"role":"assistant","content":resp})
    with st.chat_message("assistant"): st.write(resp)
