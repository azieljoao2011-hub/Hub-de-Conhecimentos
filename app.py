import streamlit as st

# 1. Configuração inicial da página
st.set_page_config(
    page_title="Hub de Especialização",
    page_icon="🎓",
    layout="centered"
)

# 2. Segurança: Buscando o link do WhatsApp (st.secrets)
try:
    whatsapp_link = st.secrets["whatsapp"]["link"]
except Exception:
    whatsapp_link = "#"
    st.sidebar.warning("⚠️ Link do WhatsApp não configurado nos Secrets.")

# 3. CSS Customizado (Visual Moderno e Cards)
st.markdown("""
<style>
    .stApp { background-color: #0f172a; color: #f8fafc; }
    h1, h2, h3 { color: #0ea5e9 !important; }
    
    .btn-whatsapp {
        background-color: #25D366;
        color: white !important;
        padding: 15px 30px;
        font-size: 1.2rem;
        font-weight: bold;
        border-radius: 50px;
        text-decoration: none;
        display: block;
        width: fit-content;
        margin: 20px auto;
        text-align: center;
        box-shadow: 0 4px 15px rgba(37, 211, 102, 0.4);
    }

    .custom-card {
        background-color: #1e293b;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #0ea5e9;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR (Navegação) ---
st.sidebar.title("📌 Menu Principal")
paginas = ["🏠 Início", "📅 Cronograma", "📜 Regras", "🤝 Créditos"]
selecao = st.sidebar.radio("Ir para:", paginas)

# --- CONTEÚDO FIXO NO TOPO ---
st.markdown("<h1 style='text-align: center;'>Hub de Especialização 🎓</h1>", unsafe_allow_html=True)
st.markdown(
    f"""<a href="{whatsapp_link}" target="_blank" class="btn-whatsapp">
    📲 Entrar no Grupo do WhatsApp
    </a>""", 
    unsafe_allow_html=True
)
st.write("---")

# --- LÓGICA DE NAVEGAÇÃO ---

if selecao == "🏠 Início":
    st.header("Nossos Pilares")
    st.markdown("<div class='custom-card'>Focamos no ensino gratuito de Programação, Matemática e Inglês para impulsionar carreiras tech.</div>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("<div class='custom-card'><h3>💻 Dev</h3><p>Lógica e Python.</p></div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div class='custom-card'><h3>🔢 Mat</h3><p>Base analítica.</p></div>", unsafe_allow_html=True)
    with col3:
        st.markdown("<div class='custom-card'><h3>🇬🇧 Eng</h3><p>Tech English.</p></div>", unsafe_allow_html=True)

elif selecao == "📅 Cronograma":
    st.header("Rotina Semanal")
    st.markdown("""
    | Dia | Matéria | Formato |
    | :--- | :--- | :--- |
    | **Segunda** | 🇬🇧 Inglês | Vídeo Gravado |
    | **Quarta** | 💻 Programação | Vídeo + Desafio |
    | **Sábado** | 🔢 Matemática | **Live (Google Meet)** |
    """)

elif selecao == "📜 Regras":
    st.header("Regras de Convivência")
    st.markdown("""
    <div class='custom-card'>
    1. Foco em Programação, Matemática e Inglês.<br>
    2. Proibido Spam ou Vendas.<br>
    3. Respeito e colaboração mútua.
    </div>
    """, unsafe_allow_html=True)

elif selecao == "🤝 Créditos":
    st.header("Créditos")
    # Agora apenas uma string como solicitado
    nome_credito = "Aziel"
    email_credito = "azieljoao2011@gmail.com"
    
    st.write("---")
    st.markdown(f"""
    <div class='custom-card' style='border-left-color: #25D366;'>
        <p>Nome do Desemvolverdor: {nome_credito}</p>
        <p>Email para contacto e parceria: {email_credito}</p>
    </div>
    """, unsafe_allow_html=True)

# --- RODAPÉ ---
st.sidebar.markdown("---")
st.sidebar.caption("© 2026 Hub de Especialização")
