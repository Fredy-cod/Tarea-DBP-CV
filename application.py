from flask import Flask, render_template, request

app= Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")


@app.route("/templateGen", methods=["POST"])
def templateGen():
  noContacto = int(request.form.get("noContact"))
  noPrograma = int(request.form.get("noProgram"))
  noIdioma = int(request.form.get("noLanguage"))
  noTrabajo = int(request.form.get("noWorks"))
  noEducacion = int(request.form.get("noEducation"))
  listContact= range(noContacto)
  listProgram= range(noPrograma)
  listLanguage= range(noIdioma)
  listWorks= range(noTrabajo)
  listEducation= range(noEducacion)
  print(listContact)
  return render_template("templateGen.html", noTrabajo=listWorks, noContacto= listContact, noPrograma=listProgram, noIdioma=listLanguage, noEducacion=listEducation)

@app.route("/generated", methods=["POST"])
def generated():
  return render_template("generated.html")


if __name__=="__main__":
    app.run(debug=True)