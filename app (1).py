"""
Pesquisa de Clima Organizacional — Maxfio
Flask + Google Sheets (via Apps Script)

Como rodar:
  1. pip install flask requests
  2. Defina a variável APPS_SCRIPT_URL abaixo com a URL do seu Web App
  3. python app.py
  4. Acesse http://localhost:5000
"""

from flask import Flask, render_template, request, jsonify
import requests
from datetime import datetime

app = Flask(__name__)

# ================================================================
# ✏️  COLE AQUI A URL DO SEU WEB APP (Google Apps Script)
# ================================================================
APPS_SCRIPT_URL = "COLE_AQUI_A_URL_DO_SEU_WEB_APP"


@app.route("/")
def index():
    """Exibe o formulário."""
    return render_template("index.html")


@app.route("/enviar", methods=["POST"])
def enviar():
    """Recebe os dados do formulário e repassa ao Google Sheets via Apps Script."""
    form = request.form

    # Monta o dicionário com todos os campos
    dados = {
        "timestamp": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "nome":                form.get("nome", "Anônimo") or "Anônimo",
        "setor":               form.get("setor", "Não informado") or "Não informado",
        "q1":                  form.get("q1", ""),
        "q2":                  form.get("q2", ""),
        "q3":                  form.get("q3", ""),
        "q4":                  form.get("q4", ""),
        "q5":                  form.get("q5", ""),
        "q6":                  form.get("q6", ""),
        "q7":                  form.get("q7", ""),
        "q8":                  form.get("q8", ""),
        "q9":                  form.get("q9", ""),
        "q10":                 form.get("q10", ""),
        "q11":                 form.get("q11", ""),
        "q12":                 form.get("q12", ""),
        "q13":                 form.get("q13", ""),
        "q14":                 form.get("q14", ""),
        "q15":                 form.get("q15", ""),
        "q16":                 form.get("q16", ""),
        "q17":                 form.get("q17", ""),
        "q18":                 form.get("q18", ""),
        "beneficios_desejados": ", ".join(form.getlist("beneficios")) or "Nenhum selecionado",
        "q20":                 form.get("q20", ""),
        "q20_area":            form.get("q20_area", ""),
        "q21":                 form.get("q21", ""),
        "q22":                 form.get("q22", ""),
        "q23":                 form.get("q23", ""),
        "q24":                 form.get("q24", ""),
        "q25":                 form.get("q25", ""),
    }

    # Envia para o Google Sheets via Apps Script
    try:
        requests.post(
            APPS_SCRIPT_URL,
            json=dados,
            timeout=10
        )
    except requests.exceptions.RequestException as e:
        print(f"[AVISO] Falha ao enviar para o Sheets: {e}")
        # Não bloqueia o usuário — mostra sucesso mesmo assim
        # (você pode logar localmente se quiser)

    return render_template("sucesso.html")


if __name__ == "__main__":
    app.run(debug=True)
