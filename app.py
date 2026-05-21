"""
Pesquisa de Clima Organizacional — Maxfio
Streamlit + Google Sheets (via Apps Script)
"""

import streamlit as st
import requests
from datetime import datetime

# URL do Web App (Google Apps Script)
APPS_SCRIPT_URL = "https://script.google.com/a/macros/maxfiocondutoreseletricos.com.br/s/AKfycbw32UzWTSpXHN3QE60a1a9s82FE8sFf7lp9Y7k_upP1eMA7hflm1OR0zGTabSZQAB2kJg/exec"

def salvar_sheets(dados: dict):
    """Envia as respostas para o Google Sheets via Apps Script."""
    requests.post(APPS_SCRIPT_URL, json=dados, timeout=10)

# ----------------------------------------------------------------
st.set_page_config(
    page_title="Pesquisa de Clima — Maxfio",
    page_icon="🌿",
    layout="centered"
)

# CSS personalizado
st.markdown("""
<style>
    /* Fundo e fonte geral */
    .stApp { background-color: #f4f6f4; }

    /* Cabeçalho da pesquisa */
    .header-box {
        background: #fff;
        border: 1px solid #dde8e3;
        border-top: 4px solid #1D9E75;
        border-radius: 12px;
        padding: 1.5rem 1.75rem;
        margin-bottom: 1.5rem;
    }
    .header-box h1 { color: #0F6E56; font-size: 22px; margin-bottom: 6px; }
    .header-box p  { color: #555; font-size: 14px; line-height: 1.65; }
    .badge {
        display: inline-block;
        background: #e6f5ee;
        color: #0F6E56;
        font-size: 12px;
        font-weight: 600;
        padding: 4px 14px;
        border-radius: 20px;
        margin-top: 10px;
    }

    /* Títulos de seção */
    .sec-title {
        font-size: 11px;
        font-weight: 700;
        color: #0F6E56;
        text-transform: uppercase;
        letter-spacing: .08em;
        margin: 1.5rem 0 .5rem;
    }

    /* Card de pergunta */
    .card {
        background: #fff;
        border: 1px solid #dde8e3;
        border-radius: 10px;
        padding: 1.1rem 1.4rem;
        margin-bottom: .6rem;
    }

    /* Botão de envio */
    div.stButton > button {
        background: #1D9E75 !important;
        color: #fff !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 0.65rem 2.5rem !important;
        font-size: 15px !important;
        font-weight: 600 !important;
        width: 100%;
    }
    div.stButton > button:hover { background: #0F6E56 !important; }

    /* Esconder o menu padrão */
    #MainMenu, footer, header { visibility: hidden; }
</style>
""", unsafe_allow_html=True)


# ----------------------------------------------------------------
# FUNÇÕES AUXILIARES
# ----------------------------------------------------------------

def secao(emoji, texto):
    st.markdown(f'<div class="sec-title">{emoji} {texto}</div>', unsafe_allow_html=True)

def escala(label, key):
    st.markdown(f'<div class="card">', unsafe_allow_html=True)
    opcoes = {"1 — Muito insatisfeito": "1", "2": "2", "3": "3", "4": "4", "5 — Muito satisfeito": "5"}
    resp = st.radio(label, list(opcoes.keys()), index=None, key=key, horizontal=True, label_visibility="visible")
    st.markdown('</div>', unsafe_allow_html=True)
    return opcoes.get(resp, "") if resp else ""

def simNao(label, key, opcoes=("Sim", "Parcialmente", "Não")):
    return st.radio(label, opcoes, index=None, key=key, horizontal=True, label_visibility="visible")


# ----------------------------------------------------------------
# ESTADO: controla se já enviou
# ----------------------------------------------------------------
if "enviado" not in st.session_state:
    st.session_state.enviado = False

# ----------------------------------------------------------------
# TELA DE SUCESSO
# ----------------------------------------------------------------
if st.session_state.enviado:
    st.markdown("""
    <div style="text-align:center; padding: 3rem 1rem;">
        <div style="font-size:56px;">✅</div>
        <h2 style="color:#0F6E56; margin: 1rem 0 .5rem;">Obrigado pela sua participação!</h2>
        <p style="color:#555; font-size:14px; line-height:1.7;">
            Suas respostas foram registradas com <strong>total confidencialidade</strong>.<br>
            Sua contribuição é fundamental para melhorarmos o ambiente de trabalho na Maxfio.
        </p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("↩ Responder novamente"):
        st.session_state.enviado = False
        st.rerun()
    st.stop()


# ----------------------------------------------------------------
# CABEÇALHO
# ----------------------------------------------------------------
st.markdown("""
<div class="header-box">
    <h1>Pesquisa de Clima Organizacional</h1>
    <p>Sua opinião é fundamental para construirmos um ambiente de trabalho cada vez melhor.
    Todas as respostas são tratadas com <strong>total confidencialidade</strong>.
    Os resultados são analisados de forma agregada e nenhum respondente é identificado.</p>
    <div class="badge">🔒 Anônimo e confidencial</div>
</div>
""", unsafe_allow_html=True)


# ----------------------------------------------------------------
# FORMULÁRIO
# ----------------------------------------------------------------
with st.form("pesquisa", clear_on_submit=False):

    # --- Identificação opcional ---
    secao("👤", "Identificação (opcional)")
    nome  = st.text_input("Nome completo", placeholder="Deixe em branco para manter o anonimato", key="nome")
    setor = st.text_input("Setor", placeholder="Ex: Financeiro, Operações, RH...", key="setor")

    # --- Bloco 1 ---
    secao("🏢", "Imagem e satisfação geral")
    q1 = escala("**1.** Qual o seu nível de satisfação geral com a empresa?", "q1")
    q2 = simNao("**2.** Você acredita que a empresa possui uma boa imagem perante parceiros, clientes e colaboradores?", "q2")
    q3 = simNao("**3.** Você sente orgulho de trabalhar aqui?", "q3", ("Sim", "Às vezes", "Não"))

    # --- Bloco 2 ---
    secao("❤️", "Clima, cultura e relacionamentos")
    q4 = escala("**4.** Nível de satisfação com o clima e a cultura organizacional na Maxfio", "q4")
    q8 = escala("**5.** Nível de satisfação com o relacionamento profissional com colegas de trabalho", "q8")
    q9 = escala("**6.** Nível de satisfação com o relacionamento profissional com seus superiores", "q9")

    # --- Bloco 3 ---
    secao("👥", "Liderança e gestão")
    q5  = escala("**7.** Nível de satisfação com o reconhecimento do bom desempenho e valorização de colaboradores", "q5")
    q7  = escala("**8.** Nível de satisfação com a orientação para a realização das tarefas diárias", "q7")
    q12 = escala("**9.** Nível de satisfação com a transparência na tomada de decisões pelos superiores", "q12")
    q13 = escala("**10.** Nível de satisfação com sua autonomia para propor novas ideias e soluções", "q13")

    # --- Bloco 4 ---
    secao("⚙️", "Estrutura, comunicação e ética")
    q6  = escala("**11.** Nível de satisfação com os recursos materiais (mesas, cadeiras, computadores, ferramentas)", "q6")
    q10 = escala("**12.** Nível de satisfação com a comunicação interna, procedimentos e processos da empresa", "q10")
    q11 = escala("**13.** Nível de satisfação com a política de ética e conduta", "q11")

    # --- Bloco 5 ---
    secao("💰", "Cargo, remuneração e benefícios")
    q14 = escala("**14.** Nível de satisfação com sua carga de trabalho diária", "q14")
    q15 = escala("**15.** Nível de satisfação com seu cargo e salário", "q15")
    q16 = simNao("**16.** Você acredita que seu salário está de acordo com o mercado?", "q16")
    q17 = simNao("**17.** Suas qualificações e habilidades técnicas estão de acordo com o exigido para o seu cargo?", "q17")
    q18 = escala("**18.** Nível de satisfação com os benefícios que você recebe", "q18")

    beneficios_opcoes = [
        "Plano de saúde", "Vale-alimentação / refeição", "Plano odontológico",
        "Auxílio educação", "Gympass / academia", "Vale-combustível / transporte",
        "Flexibilidade de horário", "Home office parcial"
    ]
    st.markdown("**19.** Selecione até 2 benefícios interessantes como possibilidade futura")
    beneficios_sel = st.multiselect(
        "Selecione até 2 opções",
        beneficios_opcoes,
        max_selections=2,
        key="beneficios",
        label_visibility="collapsed"
    )

    # --- Bloco 6 ---
    secao("📚", "Desenvolvimento e crescimento")
    q20      = simNao("**20.** Você tem interesse em desempenhar outras funções dentro da Maxfio?", "q20", ("Sim", "Não"))
    q20_area = st.text_input("Se sim, informe a área de interesse:", key="q20_area", placeholder="Ex: Comercial, Logística, TI...")
    q21      = escala("**21.** Nível de satisfação com os treinamentos e desenvolvimento interno (cursos, workshops, palestras)", "q21")
    q22      = st.text_area("**22.** Dentre as iniciativas do programa já realizadas, qual(is) você percebeu melhor eficácia ou benefícios?", key="q22", placeholder="Descreva sua percepção...")

    # --- Bloco 7 ---
    secao("💬", "Percepções e sugestões")
    q23 = st.text_area("**23.** O que você sugere como próximas ações da empresa para o próximo semestre?", key="q23", placeholder="Sua sugestão é muito importante...")
    q24 = st.text_area("**24.** O que faz você se sentir confiante e seguro na Maxfio? O que te faz bem aqui?", key="q24", placeholder="Compartilhe o que você valoriza...")
    q25 = st.text_area("**25.** Campo livre — observações, sugestões, críticas ou elogios", key="q25", placeholder="Escreva livremente...", height=130)

    st.markdown("")
    st.caption("🔒 Suas respostas são anônimas. Nenhuma informação de identificação é coletada sem sua permissão.")
    enviar = st.form_submit_button("Enviar pesquisa")


# ----------------------------------------------------------------
# PROCESSAMENTO DO ENVIO
# ----------------------------------------------------------------
if enviar:
    dados = {
        "timestamp":                datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "nome":                     nome or "Anônimo",
        "setor":                    setor or "Não informado",
        "q1_satisfacao_geral":      q1,
        "q2_imagem_empresa":        q2 or "",
        "q3_orgulho":               q3 or "",
        "q4_clima_cultura":         q4,
        "q5_reconhecimento":        q5,
        "q6_recursos_materiais":    q6,
        "q7_orientacao_tarefas":    q7,
        "q8_relacionamento_colegas":q8,
        "q9_relacionamento_superiores": q9,
        "q10_comunicacao_interna":  q10,
        "q11_etica_conduta":        q11,
        "q12_transparencia_decisoes": q12,
        "q13_autonomia_ideias":     q13,
        "q14_carga_trabalho":       q14,
        "q15_cargo_salario":        q15,
        "q16_salario_mercado":      q16 or "",
        "q17_qualificacoes_cargo":  q17 or "",
        "q18_beneficios_recebidos": q18,
        "q19_beneficios_desejados": ", ".join(beneficios_sel) or "Nenhum selecionado",
        "q20_outras_funcoes":       q20 or "",
        "q20_area_interesse":       q20_area,
        "q21_treinamentos":         q21,
        "q22_iniciativas_eficazes": q22,
        "q23_sugestoes_semestre":   q23,
        "q24_o_que_te_faz_bem":     q24,
        "q25_observacoes_livres":   q25,
    }

    try:
        salvar_sheets(dados)
    except Exception as e:
        st.warning(f"Aviso: não foi possível salvar no Google Sheets ({e}).")

    st.session_state.enviado = True
    st.rerun()
