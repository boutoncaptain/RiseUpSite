from flask import Flask, render_template_string
from pyngrok import ngrok

# Crée l'application Flask
app = Flask(__name__)

# Menu commun
menu = """
<nav style="background-color:#e63946; padding:15px; text-align:center;">
    <a href="/" style="margin:15px; color:white; text-decoration:none; font-weight:bold;">Accueil</a>
    <a href="/agenda" style="margin:15px; color:white; text-decoration:none; font-weight:bold;">Agenda</a>
    <a href="/team" style="margin:15px; color:white; text-decoration:none; font-weight:bold;">La Team Rise Up</a>
    <a href="/contact" style="margin:15px; color:white; text-decoration:none; font-weight:bold;">Contacts</a>
</nav>
"""

# Page Accueil
home_html = f"""
<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<title>Rise Up</title>
<style>
body {{ font-family: Arial, sans-serif; background-color: #0d0d0d; color: #fff; margin:0; padding:0; text-align:center; }}
h1 {{ color:#e63946; margin-top:50px; }}
p {{ font-size:18px; }}
</style>
</head>
<body>
{menu}
<h1>Bienvenue chez Rise Up !</h1>
<p>Vivez la musique, sentez la vibe !</p>
</body>
</html>
"""

# Page Agenda
agenda_html = f"""
<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<title>Agenda - Rise Up</title>
<style>body {{ font-family: Arial; background-color:#0d0d0d; color:#fff; text-align:center; }} h1 {{color:#e63946;}} ul {{list-style:none;}}</style>
</head>
<body>
{menu}
<h1>Agenda des concerts</h1>
<ul>
<li>Concert 1 - 12 Octobre 2025</li>
<li>Concert 2 - 25 Octobre 2025</li>
<li>Concert 3 - 5 Novembre 2025</li>
</ul>
</body>
</html>
"""

# Page Team
team_html = f"""
<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<title>La Team Rise Up</title>
<style>body {{ font-family: Arial; background-color:#0d0d0d; color:#fff; text-align:center; }} h1 {{color:#e63946;}} ul {{list-style:none;}}</style>
</head>
<body>
{menu}
<h1>Notre équipe</h1>
<ul>
<li>Alex - Fondateur</li>
<li>Lisa - Communication</li>
<li>Marc - Production</li>
</ul>
</body>
</html>
"""

# Page Contact
contact_html = f"""
<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<title>Contacts - Rise Up</title>
<style>body {{ font-family: Arial; background-color:#0d0d0d; color:#fff; text-align:center; }} h1 {{color:#e63946;}}</style>
</head>
<body>
{menu}
<h1>Contactez-nous</h1>
<form>
<input type="text" placeholder="Nom"><br>
<input type="email" placeholder="Email"><br>
<textarea placeholder="Message"></textarea><br>
<button type="submit">Envoyer</button>
</form>
</body>
</html>
"""

# Routes Flask
@app.route("/")
def home():
    return render_template_string(home_html)

@app.route("/agenda")
def agenda():
    return render_template_string(agenda_html)

@app.route("/team")
def team():
    return render_template_string(team_html)

@app.route("/contact")
def contact():
    return render_template_string(contact_html)

# Crée un tunnel ngrok HTTPS pour accéder au site depuis Colab
public_url = ngrok.connect(5000, bind_tls=True)
print("🌐 Ton site Rise Up est accessible ici :", public_url)

# Lancer le serveur Flask sur toutes les interfaces
app.run(host="0.0.0.0", port=5000)
