import os
import google.generativeai as genai

# Configuração da API: Ela busca automaticamente a chave que você salvou no GitHub Secrets
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Usando o modelo 1.5-flash (mais estável para o plano gratuito)
model = genai.GenerativeModel('gemini-1.5-flash')

# LINKS ATUALIZADOS
links = """
- https://revistaoeste.com/brasil/justica-do-df-condena-wilker-leao-por-videos-na-unb-e-impoe-pena-de-quase-2-anos/
- https://revistaoeste.com/brasil/sp-devolve-383-celulares-roubados-e-supera-235-mil-aparelhos-recuperados/
- https://revistaoeste.com/mundo/emirados-arabes-unidos-deixam-opep-e-opep-em-meio-a-tensoes-regionais/
- https://revistaoeste.com/mundo/ira-estaria-em-estado-de-colapso-segundo-trump/
- https://www.instagram.com/p/DXrjCLSFiaj/
"""

prompt = f"""
Atue como editor do site "Fiscal de Minuto". Use os links abaixo para gerar o conteúdo do site.
Siga EXATAMENTE a estrutura HTML que já existe (use as classes .section-header, .news-card, .card-title, .card-body).
O objetivo é manter o mesmo visual: caixas, cores e emojis.
Não coloque introduções, apenas o código HTML.
Links: {links}
"""

response = model.generate_content(prompt)
novo_conteudo = response.text

# Leitura e Substituição no seu index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Substituir o que está entre as tags de controle
inicio = ""
fim = ""

# Monta o arquivo final mantendo o que está fora das tags
html_final = html.split(inicio)[0] + inicio + "\n" + novo_conteudo + "\n" + fim + html.split(fim)[1]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_final)
