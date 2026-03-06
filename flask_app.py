from flask import Flask

app = Flask(__name__)

# Спільний стиль
style = """
<style>
body{
    font-family: Arial;
    margin:0;
    background:#f4f6f9;
}
nav{
    background:#2c3e50;
    padding:15px;
}
nav a{
    color:white;
    text-decoration:none;
    margin-right:20px;
    font-weight:bold;
}
nav a:hover{
    text-decoration:underline;
}
.container{
    padding:40px;
}
h1{
    color:#2c3e50;
}
.card{
    background:white;
    padding:20px;
    border-radius:10px;
    box-shadow:0 0 10px rgba(0,0,0,0.1);
    margin-top:20px;
}
footer{
    margin-top:40px;
    padding:20px;
    background:#2c3e50;
    color:white;
    text-align:center;
}
</style>
"""

# Навігація
nav = """
<nav>
<a href="/">Головна</a>
<a href="/about/">Про нас</a>
<a href="/services/">Послуги</a>
<a href="/contact/">Контакти</a>
</nav>
"""

@app.route("/")
def home():
    return f"""
    {style}
    {nav}
    <div class="container">
        <h1>Ласкаво просимо 👋</h1>
        <div class="card">
        <p>Це головна сторінка Flask-додатку.</p>
        <p>Тут ви можете перейти до інших сторінок сайту.</p>
        </div>
    </div>
    <footer>Flask Web App | 2026</footer>
    """

@app.route("/about/")
def about():
    return f"""
    {style}
    {nav}
    <div class="container">
        <h1>Про нас</h1>
        <div class="card">
        <p>Ми команда розробників, що створює веб-додатки на Python.</p>
        <p>Використовуємо Flask для створення швидких і легких сайтів.</p>
        </div>
    </div>
    <footer>Flask Web App | 2026</footer>
    """

@app.route("/services/")
def services():
    return f"""
    {style}
    {nav}
    <div class="container">
        <h1>Наші послуги</h1>
        <div class="card">
        <ul>
            <li>Розробка веб-сайтів</li>
            <li>Створення REST API</li>
            <li>Python автоматизація</li>
            <li>Підтримка веб-проєктів</li>
        </ul>
        </div>
    </div>
    <footer>Flask Web App | 2026</footer>
    """

@app.route("/contact/")
def contact():
    return f"""
    {style}
    {nav}
    <div class="container">
        <h1>Контакти</h1>
        <div class="card">
        <p>Email: example@email.com</p>
        <p>Телефон: +380 00 000 00 00</p>
        <p>Адреса: Україна</p>
        </div>
    </div>
    <footer>Flask Web App | 2026</footer>
    """

if __name__ == "__main__":
    app.run(debug=True)
