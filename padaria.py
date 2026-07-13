import streamlit as st
from groq import Groq

# TIRA MENU E RODAPÉ
st.set_page_config(page_title="Padaria Pão Quentinho", page_icon="🥖", layout="centered")
hide_st_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

# CONECTA COM A CHAVE
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# INFORMAÇÕES DA PADARIA - EDITA AQUI
PROMPT_DO_SISTEMA = """
Você é o atendente virtual da PADARIA PÃO QUENTINHO 🥖

INFORMAÇÕES DA PADARIA:
Endereço: Rua das Flores, 123 - Centro, Morada Nova - CE
Horário: SEG A SEX: 5H-20H | SAB: 5H-18H | DOM: 5H-12H
WhatsApp: (88) 9 9999-8888
Entrega: SIM. Taxa de R$5,00. Bairros: Centro, Planalto, São Francisco

CARDÁPIO E PREÇOS:
Pão Francês: R$ 0,90 a unidade
Pão de Queijo: R$ 2,50 por unidade
Café Pequeno: R$ 3,00 | Grande: R$ 4,50
Bolo Fatia: R$ 5,00 | Bolo Inteiro: R$ 30,00
Leite: R$ 6,00

PROMOÇÃO: SEGUNDA-FEIRA: 10 PÃES + 1 CAFÉ GRÁTIS

REGRAS:
1. Seja educado, rápido e use emoji de pão 🥖 e café ☕
2. REGRA MAIS IMPORTANTE: JAMAIS use o símbolo `crase`. Escreva preços assim: R$ 0,90 e R$ 14,00. NUNCA escreva assim: `R$ 0,90`
3. Se o cliente quiser fazer pedido: Peça NOME, PEDIDO e ENDEREÇO.
   Depois responda: "Anotado [NOME]! Seu pedido de [PEDIDO] para [ENDEREÇO] foi enviado. O pessoal da padaria vai te chamar no WhatsApp pra confirmar."
4. Se não souber: "Deixa eu ver com o pessoal e te retorno no WhatsApp (88) 9 9999-8888"
"""

st.title("Atendente Virtual Padaria Pão Quentinho 🥖")
st.write("Olá! Posso te ajudar com cardápio, preços, pedidos e entrega.")

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": PROMPT_DO_SISTEMA}]

for message in st.session_state.messages[1:]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Digite sua mensagem..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    chat_completion = client.chat.completions.create(
        messages=st.session_state.messages,
        model="llama-3.1-8b-instant",
    )
    response = chat_completion.choices[0].message.content
   response.replace("", ""
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)
