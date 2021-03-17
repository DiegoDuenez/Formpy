from formpy import Form

fu = Form("Users", formId="frmukers", action="/holas.php", method="get")
fw = Form("Work", onlyForm=True)
fw.setId("frmwork")
a = {"type":"text","name":"n"}
b = {"type":"number", "name":"e", "min":"1"}
c = {"type":"radio","name":"hm"}
d = {"type":"submit"}
e = {"type":"reset"}
cb = {"type":"checkbox", "name":"casilla"}
sel = {"name":"menu"}
op = {"value":"1"}
op2 = {"value":"2"}
ft = {"type":"text", "name":"t"}
styles = [
    "../styles/estilos.css"
]


fu.openSection("div").input(a, "Nombre:").input(b, "Edad:").openSection("p", text="Sexo:").input(c, text="Hombre").input(c, text="Mujer").closeSection("p").openSelect(sel).withOption(op, "uno").withOption(op2, "dos").closeSelect().input(cb, text="Acepto los terminos y condiciones").br().openSection("p").button(d, "Enviar").button(e, "Borrar").closeSection("p").closeSection("div").openSection("!-", "Hola esto es un comentario").input(a, "Nombre:").closeSection("-!").toHTML()
fw.input(ft, "Nombre del trabajo").toMerge("Users")


