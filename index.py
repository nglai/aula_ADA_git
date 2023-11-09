from flask import Flask, render_template
import json
import os
import codecs

app = Flask(__name__)

with open('data/posts.json', 'r') as json_file:
        posts = json.load(json_file)
        index = len(posts)

for i in posts:
    if os.path.exists(i["id"] + ".html"):
          print("Arquivo já existe")
    else:
        nome_arquivo = i["id"] + ".html"
        filename = f"{nome_arquivo}"
        f = codecs.open(filename, "w", "utf-8")
        html_template = f"""
        <html>
            <head>
                <title>Post {i["id"]}</title>
            </head>
        <body>
            <h1>Titulo {i["titulo"]}!</h1>
            <p>Descrição {i["descricao"]}.</p>
            <p>Autor {i["autor"]}.</p>
        </body>
        </html>
        """
        f.write(html_template)
        f.close()

@app.route("/")
def homepage():
    return render_template("index.html",posts=posts)

@app.route("/<id>")
def postagens(id):
    for i in posts:
        if i["id"] == id:
            post = i
            break
    nome_arquivo = i["id"] + ".html"
    return render_template(nome_arquivo, posts=posts)

# colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)