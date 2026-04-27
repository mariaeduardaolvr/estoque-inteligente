from flask import Flask, render_template, request, redirect

app = Flask(__name__)

estoque = []


# 🟢 TELA PRINCIPAL
@app.route("/", methods=["GET", "POST"])

def home():
    if request.method == "POST":
        nome = request.form["nome"]
        quantidade = int(request.form["quantidade"])
        preco = float(request.form["preco"])

        estoque.append({
            "nome": nome,
            "quantidade": quantidade,
            "preco": preco
        })

        return redirect("/")

    total = sum(p["quantidade"] * p["preco"] for p in estoque)

    return render_template("index.html", estoque=estoque, total=total)


# 🔴 REMOVER POR NOME + QUANTIDADE
@app.route("/remover", methods=["POST"])
def remover():
    nome = request.form["nome"]
    quantidade_remover = int(request.form["quantidade"])

    for produto in estoque:
        if produto["nome"] == nome:
            produto["quantidade"] -= quantidade_remover

            if produto["quantidade"] <= 0:
                estoque.remove(produto)
            break

    return redirect("/")


# 🟡 REPOR POR NOME + QUANTIDADE
@app.route("/repor", methods=["POST"])
def repor():
    nome = request.form["nome"]
    quantidade_add = int(request.form["quantidade"])

    for produto in estoque:
        if produto["nome"] == nome:
            produto["quantidade"] += quantidade_add
            break

    return redirect("/")


# 🚀 START
if __name__ == "__main__":
    app.run(debug=True)