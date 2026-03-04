import streamlit as st

# 1. Configuração inicial da página (DEVE ser o primeiro comando)
st.set_page_config(
    page_title="Hub de Especialização",
    page_icon="🎓",
    layout="centered"
)

# 2. Segurança: Buscando o link do WhatsApp dos Segredos
try:
    # O Streamlit vai procurar no arquivo .streamlit/secrets.toml
    whatsapp_link = st.secrets["whatsapp"]["link"]
except Exception as e:
    # Fallback de segurança se o arquivo não existir localmente
    whatsapp_link = "#"
    st.warning("⚠️ Link do WhatsApp não encontrado. Configure o arquivo `.streamlit/secrets.toml`.")

# 3. CSS Customizado para o visual moderno (Dark Mode + Cards)
custom_css = """
<style>
    /* Fundo da aplicação e cor do texto geral */
    .stApp {
        background-color: #0f172a;
        color: #f8fafc;
    }
    /* Estilização dos Títulos */
    h1, h2, h3 {
        color: #0ea5e9 !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    /* Estilização do Botão de WhatsApp */
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
        transition: transform 0.3s, box-shadow 0.3s;
    }
    .btn-whatsapp:hover {
        transform: translateY(-3px);
        box-shadow: 0 6px 20px rgba(37, 211, 102, 0.6);
    }
    /* Estilo de Cartões (Cards) */
    .custom-card {
        background-color: #1e293b;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #0ea5e9;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# --- CABEÇALHO ---
st.markdown("<h1 style='text-align: center;'>Hub de Especialização 🎓</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1.2rem; color: #cbd5e1;'>Programação, Matemática e Inglês. Conhecimento que transforma, oportunidade gratuita.</p>", unsafe_allow_html=True)

# Botão do WhatsApp (usando a variável segura)
st.markdown(
    f"""<a href="{whatsapp_link}" target="_blank" class="btn-whatsapp">
    📲 Entrar no Grupo do WhatsApp
    </a>""", 
    unsafe_allow_html=True
)

st.write("---")

# --- ABAS (TABS) ---
tab1, tab2, tab3, tab4 = st.tabs(["🏠 Início", "📅 Dinâmica & Cronograma", "📜 Regras", "🤝 Créditos"])

# --- ABA 1: INÍCIO ---
with tab1:
    st.header("Nossos Pilares")
    st.markdown("""
    <div class='custom-card'>
        Este espaço foi criado para partilhar cursos gratuitos com certificado, workshops e recursos de alta qualidade. Nosso foco é o <strong>"trio de ferro"</strong> do mercado moderno.
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("<div class='custom-card'><h3>💻 Programação</h3><p>Lógica de programação, desenvolvimento Web, Python e ferramentas de código.</p></div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div class='custom-card'><h3>🔢 Matemática</h3><p>Foco na base analítica necessária para algoritmos e resolução de problemas complexos.</p></div>", unsafe_allow_html=True)
    with col3:
        st.markdown("<div class='custom-card'><h3>🇬🇧 Inglês</h3><p>Vocabulário técnico (Technical English), leitura de documentações e gramática essencial.</p></div>", unsafe_allow_html=True)

# --- ABA 2: DINÂMICA & CRONOGRAMA ---
with tab2:
    st.header("Nossa Rotina de Aulas")
    st.write("Para não sobrecarregar ninguém, dividimos os nossos estudos durante a semana misturando aulas gravadas e encontros ao vivo.")
    
    cronograma = """
    | Dia da Semana | Disciplina | Formato | O que fazemos? |
    | :--- | :--- | :--- | :--- |
    | **Segunda-feira** | 🇬🇧 Inglês | Vídeo Gravado | Pílulas de conhecimento, termos em tech e gramática básica. |
    | **Quarta-feira** | 💻 Programação | Vídeo + Desafio | Aula teórica curta e envio de exercícios práticos (GitHub). |
    | **Sábado** | 🔢 Matemática | **Videochamada (Ao Vivo)** | 1 hora de foco total para tirar dúvidas e resolver problemas em grupo. |
    """
    st.markdown(cronograma)

# --- ABA 3: REGRAS ---
with tab3:
    st.header("Regras do Grupo")
    st.markdown("""
    <div class='custom-card'>
        <ul>
            <li><strong>Foco Total:</strong> Apenas conteúdos sobre Programação, Matemática e Inglês.</li>
            <li><strong>Proibido Spam:</strong> Sem correntes, política ou venda de cursos/produtos.</li>
            <li><strong>Colaboração:</strong> Ajude os colegas com dúvidas. A aprendizagem é coletiva!</li>
            <li><strong>Respeito:</strong> Mantenha um ambiente cordial e profissional.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# --- ABA 4: CRÉDITOS ---
with tab4:
    st.header("Créditos e Organização")
    st.write("Preencha os campos abaixo para gerar os créditos da sua página:")
    
    # Inputs do usuário
    nome_idealizador = "Aziel"
    nomes_moderadores = "Aziel"
    email_contacto = "azieljoao2011@gmail.com"
    
    st.write("---")
    st.subheader("Visualização Final:")
    
    # Cartão gerado dinamicamente
    html_creditos = f"""
    <div class='custom-card' style='border-left-color: #25D366;'>
        <p><strong>Idealizado e mantido por:</strong> {nome_idealizador}</p>
        <p><strong>Agradecimentos aos moderadores:</strong> {nomes_moderadores}</p>
        <p><strong>Contacto para parcerias:</strong> <a href="mailto:{email_contacto}" style="color: #0ea5e9;">{email_contacto}</a></p>
    </div>
    """
    st.markdown(html_creditos, unsafe_allow_html=True)

# --- RODAPÉ ---
st.markdown("<br><hr><p style='text-align: center; color: #64748b; font-size: 0.9rem;'>© 2026 Hub de Especialização. O conhecimento é livre.</p>", unsafe_allow_html=True)
