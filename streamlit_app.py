import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Blog Arthur Fernandes", layout="wide")

# --- Mock data ---
POSTS = [
    {
        "id": 1,
        "title": "Melhores albuns Black Sabbath",
        "author": "Regis Tadeu",
        "date": "2025-11-01",
        "summary": "Interessando em desbravar a discografia de Black Sabbath? Leia essa materia para saber por onde começar!!!",
        "image": "https://lastfm.freetls.fastly.net/i/u/770x0/dbbba7e5fdce4303c3f1921c79950c17.jpg#dbbba7e5fdce4303c3f1921c79950c17",
    },
    {
        "id": 2,
        "title": "Alice in Chains e sua tristeza cativante",
        "author": "Gilberto Gil",
        "date": "2025-10-15",
        "summary": "Princípios básicos de tipografia, espaçamento e hierarquia visual para posts técnicos.",
        "image": "https://whiplash.net/imagens_promo_22/aliceinchains_jarofflies.jpg",
    },
]

# --- Helpers ---

def render_post_card(post):
    st.image(post["image"], use_container_width=True)
    st.markdown(f"### {post['title']}")
    st.markdown(f"_por {post['author']} — {post['date']}_")
    st.write(post["summary"])
    st.markdown("[Leia mais](#)")


# --- Layout ---

if "theme" not in st.session_state:
    st.session_state.theme = "dark"


selected_theme = st.toggle("Tema claro", value=(st.session_state.theme == "light"))
st.session_state.theme = "light" if selected_theme else "dark"


# Apply CSS for light/dark theme
if st.session_state.theme == "light":
    st.markdown(
    """
    <style>
    body, .stApp { background-color: #FFFFFF !important; color: #000000 !important; }
    .stButton>button { background-color:#f0f0f0!important; color:#000!important; }
    .stTextInput>div>div>input, textarea { background-color:#f9f9f9!important; color:#000!important; }
    </style>
    """,
    unsafe_allow_html=True,
    )
    

# Top bar / hero
col1, col2 = st.columns([3, 1])
with col1:
    st.title("Meu Blog — Arthur Fernandes")
    st.markdown("## Meu nome é Arthur Fernandes e eu sou auxiliar de sala do curso technovation")
with col2:
    st.image("https://ih1.redbubble.net/image.3149141987.1714/flat,750x1000,075,t.jpg")

st.markdown("---")

# Main + sidebar
main, sidebar = st.columns([3, 1])

with sidebar:
    st.header("Navegação")
    page = st.radio("Ir para", ["Início", "Sobre", "Contato"]) 
    st.header("Pesquisar")
    query = st.text_input("Buscar por título ou autor")
    st.markdown("---")
    st.write("Siga nas redes:")
    st.write("• Twitter / X: @exemplo")
    st.write("• Mastodon: @exemplo@instance")

with main:
    if page == "Início":
        st.header("Posts recentes")

        # Simple search filter
        filtered = POSTS
        if query:
            q = query.lower()
            filtered = [p for p in POSTS if q in p['title'].lower() or q in p['author'].lower()]

        for post in filtered:
            with st.container():
                render_post_card(post)
                st.markdown("---")

    elif page == "Sobre":
        st.header("Sobre este blog")
        st.markdown(
            "Feito para mostrar os gostos do autor quanto a musica e ser usado como template para aula de streamlit"
        )
        st.subheader("Missão")
        st.write("Compartilhar conteúdo técnico de forma clara e acessível.")

    elif page == "Contato":
        with st.form("fale_conosco"):
            st.header("Fale comigo")
            st.write("Formulário fictício — substitua por integração real conforme necessário.")
            name = st.text_input("Seu nome")
            email = st.text_input("Seu e-mail")
            message = st.text_area("Mensagem")
            if st.form_submit_button("Enviar"):
                if not name or not email or not message:
                    st.warning("Preencha todos os campos antes de enviar.")
                else:
                    st.success("Obrigado! Sua mensagem foi enviada (simulada).")

# Footer
st.markdown("---")
colf1, colf2 = st.columns([1, 3])
with colf1:
    st.write(f"© {datetime.now().year} Meu Blog")
with colf2:
    st.write("Template de exemplo para aulas — personalize cores, fontes e layout conforme a necessidade.")
