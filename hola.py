from flask import Flask
from flask import render_template

app= Flask(__name__)

@app.route("/")
def url_principal():
	return render_template("templante.html", nombre="Leilani")

if __name__ == "__main__":
	app.run(debug=True)

pass

#nombre=input("Introduce tu nombre: ")
#print(f"mucho gusto, {nombre}")