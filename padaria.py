import streamlit as st
from groq import Groq

# CONFIG DA PÁGINA
st.set_page_config(
    page_title="Padaria Pão Quentinho", 
    page_icon="🥖", 
    layout="centered"
)

# ESCONDE MENU, RODAPÉ E CABEÇALHO DO STREAMLIT
st.markdown(
    """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True
)

# COLOCA SUA CHAVE DA GROQ AQUI DENTRO DAS ASPAS
client = Groq(api_key="gsk_COLE_SUA_CHAVE_AQUI")

# PERSONALIDADE DO BOT
PROMPT_DO_SISTEMA = """
Você é o atendente virtual da PADARIA PÃO QUENTINHO 🥖

INFORMAÇÕES DA PADARIA:
Endereço: Rua das Flores, 123 - Centro, Morada Nova - CE
Horário: SEG A SEX: 5H-20H | SAB: 5H-18H | DOM: 5H-12H
WhatsApp: (88) 9 9999-8888
Entrega: SIM. Taxa de R$5,00.

CARDÁPIO E PREÇOS:
Pão Francês: R$ 0,90
Pão Doce: R$ 1,50
Café Pequeno: R$ 4,50
Café Grande: R$ 6,00
Bolo de Pote: R$ 8,00
Salgado: R$ 6,00

REGRAS IMPORTANTES:
1. Seja educado, rápido e use emoji 🥖
2. NUNCA use crase ` nem asterisco ** nem negrito. 
3. Escreva preço sempre assim: R$ 0,90
4. Para fazer pedido: peça NOME COMPLETO, PEDIDO e ENDERECO COM NUMERO.
5. Depois de pegar o pedido, confirme tudo e informe o valor + taxa.
"""

# TÍTULO
st.title("Atendente Virtual Padaria Pão Quentinho 🥖")
st.write("Olá! Posso te ajudar com cardápio, preços e pedidos.")

# HISTÓRICO DO CHAT
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": PROMPT_DO_SISTEMA}]

for message in st.session_state.messages[1:]:
    with st.chat_message(message["role"]):
        st.write(message["content"]) # usei write pra não ficar verde

# CAIXA DE INPUT
if prompt := st.chat_input("Digite sua mensagem..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    # CHAMA A IA
    chat_completion = client.chat.completions.create(
        messages=st.session_state.messages,
        model="llama-3.1-8b-instant",
    )
    
    response = chat_completion.choices[0].message.content

    # LIMPA TUDO QUE DEIXA VERDE
    response = response.replace("`", "")
    response = response.replace("**", "")
    response = response.replace("*", "")

    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.write(response)
