"""
Pesquisa de Clima Organizacional — Maxfio
Streamlit + HTML embutido — POST feito diretamente do navegador do usuário
para o Google Apps Script (resolve problema de CORS com domínio corporativo)
"""

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Pesquisa de Clima — Maxfio",
    page_icon="🌿",
    layout="centered"
)

# Esconde menu e rodapé do Streamlit
st.markdown("""
<style>
    #MainMenu, footer, header { visibility: hidden; }
    .stApp { background-color: #f4f6f4; }
    .block-container { padding: 0 !important; max-width: 100% !important; }
</style>
""", unsafe_allow_html=True)

APPS_SCRIPT_URL = "https://script.google.com/a/macros/maxfiocondutoreseletricos.com.br/s/AKfycbyCFSrdOBLitoqfvhhxWE39Sq7WKXiNQvkBZhoQPEfbmoanFNSopkRlltpCYFKjepyKKg/exec"

html = f"""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<style>
  *,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
  body{{font-family:'Segoe UI',system-ui,sans-serif;background:#f4f6f4;color:#1a1a1a;padding:1.5rem 1rem 4rem}}
  .wrap{{max-width:680px;margin:0 auto}}
  .header{{background:#fff;border:1px solid #dde8e3;border-top:4px solid #1D9E75;border-radius:12px;padding:1.5rem 1.75rem;margin-bottom:1.5rem}}
  .header h1{{font-size:20px;font-weight:600;color:#0F6E56;margin-bottom:6px}}
  .header p{{font-size:13px;color:#555;line-height:1.65}}
  .badge{{display:inline-block;background:#e6f5ee;color:#0F6E56;font-size:11px;font-weight:600;padding:4px 12px;border-radius:20px;margin-top:10px}}
  .progress-bar{{height:4px;background:#dde8e3;border-radius:2px;margin-bottom:1.5rem;overflow:hidden}}
  .progress-fill{{height:100%;background:#1D9E75;width:0%;transition:width .3s}}
  .sec{{font-size:11px;font-weight:700;color:#0F6E56;text-transform:uppercase;letter-spacing:.08em;margin:1.75rem 0 .6rem 2px}}
  .card{{background:#fff;border:1px solid #dde8e3;border-radius:10px;padding:1.1rem 1.4rem;margin-bottom:.6rem}}
  .ql{{font-size:14px;color:#1a1a1a;line-height:1.5;display:block;margin-bottom:.75rem}}
  .ql .n{{color:#1D9E75;font-weight:600;margin-right:3px}}
  .ql .op{{color:#888;font-size:12px;margin-left:4px}}
  .scale{{display:flex;gap:7px;flex-wrap:wrap}}
  .scale input[type=radio]{{display:none}}
  .scale label .sb{{width:44px;height:44px;border-radius:8px;border:1px solid #cdddd6;background:#f4f9f6;font-size:15px;font-weight:500;color:#666;display:flex;align-items:center;justify-content:center;cursor:pointer;transition:all .12s}}
  .scale label .sb:hover{{border-color:#1D9E75;color:#1D9E75;background:#e6f5ee}}
  .scale input[type=radio]:checked+label .sb{{background:#1D9E75;border-color:#1D9E75;color:#fff}}
  .scale-lbl{{display:flex;justify-content:space-between;font-size:11px;color:#888;margin-top:5px}}
  .yn{{display:flex;gap:9px;flex-wrap:wrap}}
  .yn input[type=radio]{{display:none}}
  .yn label .yb{{padding:8px 20px;border-radius:8px;border:1px solid #cdddd6;background:#f4f9f6;font-size:14px;color:#555;cursor:pointer;transition:all .12s}}
  .yn label .yb:hover{{border-color:#1D9E75;color:#1D9E75}}
  .yn input[type=radio]:checked+label .yb{{background:#1D9E75;border-color:#1D9E75;color:#fff}}
  .chk{{display:flex;flex-direction:column;gap:9px}}
  .chk input[type=checkbox]{{display:none}}
  .chk label{{display:flex;align-items:center;gap:9px;cursor:pointer;font-size:14px}}
  .cb{{width:20px;height:20px;min-width:20px;border-radius:5px;border:1px solid #cdddd6;background:#f4f9f6;display:flex;align-items:center;justify-content:center;transition:all .12s}}
  .chk input:checked+label .cb{{background:#1D9E75;border-color:#1D9E75}}
  .chk input:checked+label .cb::after{{content:'';width:11px;height:6px;border-left:2px solid #fff;border-bottom:2px solid #fff;transform:rotate(-45deg) translateY(-1px);display:block}}
  input[type=text],textarea{{width:100%;background:#f9faf9;border:1px solid #cdddd6;border-radius:8px;padding:9px 12px;font-size:14px;color:#1a1a1a;font-family:inherit;outline:none;resize:vertical}}
  input[type=text]:focus,textarea:focus{{border-color:#1D9E75;box-shadow:0 0 0 3px rgba(29,158,117,.12)}}
  textarea{{min-height:88px}}
  .cond{{display:none;margin-top:10px}}
  .cond.on{{display:block}}
  .sub-area{{text-align:center;margin-top:2rem}}
  .anon{{font-size:12px;color:#888;margin-bottom:.85rem}}
  .sub-btn{{background:#1D9E75;color:#fff;border:none;border-radius:8px;padding:13px 44px;font-size:15px;font-weight:600;cursor:pointer;font-family:inherit;transition:background .15s}}
  .sub-btn:hover{{background:#0F6E56}}
  .sub-btn:disabled{{background:#aaa;cursor:not-allowed}}
  .success{{display:none;text-align:center;padding:3rem 1rem}}
  .success .icon{{font-size:52px;display:block;margin-bottom:1rem}}
  .success h2{{color:#0F6E56;font-size:20px;margin-bottom:.5rem}}
  .success p{{color:#555;font-size:14px;line-height:1.7}}
</style>
</head>
<body>
<div class="wrap">
  <div class="header">
    <h1>Pesquisa de Clima Organizacional</h1>
    <p>Sua opinião é fundamental para construirmos um ambiente de trabalho cada vez melhor. Todas as respostas são tratadas com <strong>total confidencialidade</strong>. Os resultados são analisados de forma agregada e nenhum respondente é identificado.</p>
    <div class="badge">🔒 Anônimo e confidencial</div>
  </div>

  <div class="progress-bar"><div class="progress-fill" id="prog"></div></div>

  <div id="form-area">

    <div class="sec">👤 Identificação (opcional)</div>
    <div class="card"><label class="ql">Nome completo <span class="op">(deixe em branco para manter o anonimato)</span></label><input type="text" id="nome" placeholder="Deixe em branco para manter o anonimato"/></div>
    <div class="card"><label class="ql">Setor <span class="op">(não obrigatório)</span></label><input type="text" id="setor" placeholder="Ex: Financeiro, Operações, RH..."/></div>

    <div class="sec">🏢 Imagem e satisfação geral</div>
    <div class="card"><label class="ql"><span class="n">1.</span> Qual o seu nível de satisfação geral com a empresa?</label><div class="scale" id="q1">{' '.join(f'<span><input type="radio" name="q1" id="q1-{v}" value="{v}"><label for="q1-{v}"><span class="sb">{v}</span></label></span>' for v in range(1,6))}</div><div class="scale-lbl"><span>Muito insatisfeito</span><span>Muito satisfeito</span></div></div>
    <div class="card"><label class="ql"><span class="n">2.</span> Você acredita que a empresa possui uma boa imagem perante parceiros, clientes e colaboradores?</label><div class="yn">{' '.join(f'<span><input type="radio" name="q2" id="q2-{v}" value="{v}"><label for="q2-{v}"><span class="yb">{v}</span></label></span>' for v in ['Sim','Parcialmente','Não'])}</div></div>
    <div class="card"><label class="ql"><span class="n">3.</span> Você sente orgulho de trabalhar aqui?</label><div class="yn">{' '.join(f'<span><input type="radio" name="q3" id="q3-{i}" value="{v}"><label for="q3-{i}"><span class="yb">{v}</span></label></span>' for i,v in enumerate(['Sim','Às vezes','Não']))}</div></div>

    <div class="sec">❤️ Clima, cultura e relacionamentos</div>
    <div class="card"><label class="ql"><span class="n">4.</span> Nível de satisfação com o clima e a cultura organizacional na Maxfio</label><div class="scale" id="q4">{' '.join(f'<span><input type="radio" name="q4" id="q4-{v}" value="{v}"><label for="q4-{v}"><span class="sb">{v}</span></label></span>' for v in range(1,6))}</div><div class="scale-lbl"><span>Muito insatisfeito</span><span>Muito satisfeito</span></div></div>
    <div class="card"><label class="ql"><span class="n">5.</span> Nível de satisfação com o relacionamento profissional com colegas de trabalho</label><div class="scale">{' '.join(f'<span><input type="radio" name="q8" id="q8-{v}" value="{v}"><label for="q8-{v}"><span class="sb">{v}</span></label></span>' for v in range(1,6))}</div><div class="scale-lbl"><span>Muito insatisfeito</span><span>Muito satisfeito</span></div></div>
    <div class="card"><label class="ql"><span class="n">6.</span> Nível de satisfação com o relacionamento profissional com seus superiores</label><div class="scale">{' '.join(f'<span><input type="radio" name="q9" id="q9-{v}" value="{v}"><label for="q9-{v}"><span class="sb">{v}</span></label></span>' for v in range(1,6))}</div><div class="scale-lbl"><span>Muito insatisfeito</span><span>Muito satisfeito</span></div></div>

    <div class="sec">👥 Liderança e gestão</div>
    <div class="card"><label class="ql"><span class="n">7.</span> Nível de satisfação com o reconhecimento do bom desempenho e valorização de colaboradores</label><div class="scale">{' '.join(f'<span><input type="radio" name="q5" id="q5-{v}" value="{v}"><label for="q5-{v}"><span class="sb">{v}</span></label></span>' for v in range(1,6))}</div><div class="scale-lbl"><span>Muito insatisfeito</span><span>Muito satisfeito</span></div></div>
    <div class="card"><label class="ql"><span class="n">8.</span> Nível de satisfação com a orientação para a realização das tarefas diárias</label><div class="scale">{' '.join(f'<span><input type="radio" name="q7" id="q7-{v}" value="{v}"><label for="q7-{v}"><span class="sb">{v}</span></label></span>' for v in range(1,6))}</div><div class="scale-lbl"><span>Muito insatisfeito</span><span>Muito satisfeito</span></div></div>
    <div class="card"><label class="ql"><span class="n">9.</span> Nível de satisfação com a transparência na tomada de decisões pelos superiores</label><div class="scale">{' '.join(f'<span><input type="radio" name="q12" id="q12-{v}" value="{v}"><label for="q12-{v}"><span class="sb">{v}</span></label></span>' for v in range(1,6))}</div><div class="scale-lbl"><span>Muito insatisfeito</span><span>Muito satisfeito</span></div></div>
    <div class="card"><label class="ql"><span class="n">10.</span> Nível de satisfação com sua autonomia para propor novas ideias e soluções</label><div class="scale">{' '.join(f'<span><input type="radio" name="q13" id="q13-{v}" value="{v}"><label for="q13-{v}"><span class="sb">{v}</span></label></span>' for v in range(1,6))}</div><div class="scale-lbl"><span>Muito insatisfeito</span><span>Muito satisfeito</span></div></div>

    <div class="sec">⚙️ Estrutura, comunicação e ética</div>
    <div class="card"><label class="ql"><span class="n">11.</span> Nível de satisfação com os recursos materiais (mesas, cadeiras, computadores, ferramentas)</label><div class="scale">{' '.join(f'<span><input type="radio" name="q6" id="q6-{v}" value="{v}"><label for="q6-{v}"><span class="sb">{v}</span></label></span>' for v in range(1,6))}</div><div class="scale-lbl"><span>Muito insatisfeito</span><span>Muito satisfeito</span></div></div>
    <div class="card"><label class="ql"><span class="n">12.</span> Nível de satisfação com a comunicação interna, procedimentos e processos da empresa</label><div class="scale">{' '.join(f'<span><input type="radio" name="q10" id="q10-{v}" value="{v}"><label for="q10-{v}"><span class="sb">{v}</span></label></span>' for v in range(1,6))}</div><div class="scale-lbl"><span>Muito insatisfeito</span><span>Muito satisfeito</span></div></div>
    <div class="card"><label class="ql"><span class="n">13.</span> Nível de satisfação com a política de ética e conduta</label><div class="scale">{' '.join(f'<span><input type="radio" name="q11" id="q11-{v}" value="{v}"><label for="q11-{v}"><span class="sb">{v}</span></label></span>' for v in range(1,6))}</div><div class="scale-lbl"><span>Muito insatisfeito</span><span>Muito satisfeito</span></div></div>

    <div class="sec">💰 Cargo, remuneração e benefícios</div>
    <div class="card"><label class="ql"><span class="n">14.</span> Nível de satisfação com sua carga de trabalho diária</label><div class="scale">{' '.join(f'<span><input type="radio" name="q14" id="q14-{v}" value="{v}"><label for="q14-{v}"><span class="sb">{v}</span></label></span>' for v in range(1,6))}</div><div class="scale-lbl"><span>Muito insatisfeito</span><span>Muito satisfeito</span></div></div>
    <div class="card"><label class="ql"><span class="n">15.</span> Nível de satisfação com seu cargo e salário</label><div class="scale">{' '.join(f'<span><input type="radio" name="q15" id="q15-{v}" value="{v}"><label for="q15-{v}"><span class="sb">{v}</span></label></span>' for v in range(1,6))}</div><div class="scale-lbl"><span>Muito insatisfeito</span><span>Muito satisfeito</span></div></div>
    <div class="card"><label class="ql"><span class="n">16.</span> Você acredita que seu salário está de acordo com o mercado?</label><div class="yn">{' '.join(f'<span><input type="radio" name="q16" id="q16-{i}" value="{v}"><label for="q16-{i}"><span class="yb">{v}</span></label></span>' for i,v in enumerate(['Sim','Parcialmente','Não']))}</div></div>
    <div class="card"><label class="ql"><span class="n">17.</span> Suas qualificações e habilidades técnicas estão de acordo com o exigido para o seu cargo?</label><div class="yn">{' '.join(f'<span><input type="radio" name="q17" id="q17-{i}" value="{v}"><label for="q17-{i}"><span class="yb">{v}</span></label></span>' for i,v in enumerate(['Sim','Parcialmente','Não']))}</div></div>
    <div class="card"><label class="ql"><span class="n">18.</span> Nível de satisfação com os benefícios que você recebe</label><div class="scale">{' '.join(f'<span><input type="radio" name="q18" id="q18-{v}" value="{v}"><label for="q18-{v}"><span class="sb">{v}</span></label></span>' for v in range(1,6))}</div><div class="scale-lbl"><span>Muito insatisfeito</span><span>Muito satisfeito</span></div></div>
    <div class="card">
      <label class="ql"><span class="n">19.</span> Selecione até 2 benefícios interessantes como possibilidade futura</label>
      <div class="chk">
        {''.join(f'<span><input type="checkbox" id="b{i}" value="{v}"><label for="b{i}"><span class="cb"></span>{v}</label></span>' for i,v in enumerate(["Plano de saúde","Vale-alimentação / refeição","Plano odontológico","Auxílio educação","Gympass / academia","Vale-combustível / transporte","Flexibilidade de horário","Home office parcial"]))}
      </div>
    </div>

    <div class="sec">📚 Desenvolvimento e crescimento</div>
    <div class="card">
      <label class="ql"><span class="n">20.</span> Você tem interesse em desempenhar outras funções dentro da Maxfio?</label>
      <div class="yn">
        <span><input type="radio" name="q20" id="q20-s" value="Sim" onchange="document.getElementById('q20area').classList.add('on')"><label for="q20-s"><span class="yb">Sim</span></label></span>
        <span><input type="radio" name="q20" id="q20-n" value="Não" onchange="document.getElementById('q20area').classList.remove('on')"><label for="q20-n"><span class="yb">Não</span></label></span>
      </div>
      <div class="cond" id="q20area"><input type="text" id="q20_area" placeholder="Informe a área de interesse..."/></div>
    </div>
    <div class="card"><label class="ql"><span class="n">21.</span> Nível de satisfação com os treinamentos e desenvolvimento interno (cursos, workshops, palestras)</label><div class="scale">{' '.join(f'<span><input type="radio" name="q21" id="q21-{v}" value="{v}"><label for="q21-{v}"><span class="sb">{v}</span></label></span>' for v in range(1,6))}</div><div class="scale-lbl"><span>Muito insatisfeito</span><span>Muito satisfeito</span></div></div>
    <div class="card"><label class="ql"><span class="n">22.</span> Dentre as iniciativas do programa já realizadas, qual(is) você percebeu melhor eficácia ou benefícios?</label><textarea id="q22" placeholder="Descreva sua percepção..."></textarea></div>

    <div class="sec">💬 Percepções e sugestões</div>
    <div class="card"><label class="ql"><span class="n">23.</span> O que você sugere como próximas ações da empresa para o próximo semestre?</label><textarea id="q23" placeholder="Sua sugestão é muito importante..."></textarea></div>
    <div class="card"><label class="ql"><span class="n">24.</span> O que faz você se sentir confiante e seguro na Maxfio? O que te faz bem aqui?</label><textarea id="q24" placeholder="Compartilhe o que você valoriza..."></textarea></div>
    <div class="card"><label class="ql"><span class="n">25.</span> Campo livre — observações, sugestões, críticas ou elogios</label><textarea id="q25" style="min-height:110px" placeholder="Escreva livremente..."></textarea></div>

    <div class="sub-area">
      <p class="anon">🔒 Suas respostas são anônimas. Nenhuma informação de identificação é coletada sem sua permissão.</p>
      <button class="sub-btn" id="btn" onclick="enviar()">Enviar pesquisa</button>
    </div>
  </div>

  <div class="success" id="success">
    <span class="icon">✅</span>
    <h2>Obrigado pela sua participação!</h2>
    <p>Suas respostas foram registradas com <strong>total confidencialidade</strong>.<br>Sua contribuição é fundamental para melhorarmos o ambiente de trabalho na Maxfio.</p>
  </div>
</div>

<script>
  const URL = "{APPS_SCRIPT_URL}";

  // Limite 2 checkboxes
  document.querySelectorAll('.chk input[type=checkbox]').forEach(cb => {{
    cb.addEventListener('change', function() {{
      const checked = document.querySelectorAll('.chk input:checked');
      if (checked.length > 2) this.checked = false;
    }});
  }});

  // Progresso
  function prog() {{
    const nms = ['q1','q2','q3','q4','q5','q6','q7','q8','q9','q10','q11','q12','q13','q14','q15','q16','q17','q18','q20','q21'];
    let n = nms.filter(n => document.querySelector('[name='+n+']:checked')).length;
    document.getElementById('prog').style.width = Math.round(n/nms.length*100)+'%';
  }}
  document.querySelectorAll('input[type=radio]').forEach(r => r.addEventListener('change', prog));

  function val(name) {{
    const el = document.querySelector('[name='+name+']:checked');
    return el ? el.value : '';
  }}

  function enviar() {{
    const btn = document.getElementById('btn');
    btn.disabled = true;
    btn.textContent = 'Enviando...';

    const now = new Date();
    const ts = now.toLocaleDateString('pt-BR') + ' ' + now.toLocaleTimeString('pt-BR');

    const dados = {{
      timestamp: ts,
      nome: document.getElementById('nome').value || 'Anônimo',
      setor: document.getElementById('setor').value || 'Não informado',
      q1: val('q1'), q2: val('q2'), q3: val('q3'),
      q4: val('q4'), q5: val('q5'), q6: val('q6'),
      q7: val('q7'), q8: val('q8'), q9: val('q9'),
      q10: val('q10'), q11: val('q11'), q12: val('q12'),
      q13: val('q13'), q14: val('q14'), q15: val('q15'),
      q16: val('q16'), q17: val('q17'), q18: val('q18'),
      beneficios_desejados: [...document.querySelectorAll('.chk input:checked')].map(c=>c.value).join(', ') || 'Nenhum',
      q20: val('q20'),
      q20_area: document.getElementById('q20_area').value,
      q21: val('q21'),
      q22: document.getElementById('q22').value,
      q23: document.getElementById('q23').value,
      q24: document.getElementById('q24').value,
      q25: document.getElementById('q25').value,
    }};

    fetch(URL, {{
      method: 'POST',
      mode: 'no-cors',
      headers: {{'Content-Type': 'application/json'}},
      body: JSON.stringify(dados)
    }}).then(() => {{
      document.getElementById('form-area').style.display = 'none';
      document.getElementById('success').style.display = 'block';
    }}).catch(() => {{
      btn.disabled = false;
      btn.textContent = 'Enviar pesquisa';
      alert('Erro ao enviar. Verifique sua conexão e tente novamente.');
    }});
  }}
</script>
</body>
</html>
"""

components.html(html, height=6000, scrolling=True)
