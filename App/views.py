from django.shortcuts import render
from .forms import RFCForm
import random
import string

def obtener_primera_vocal_interna(paterno):
    vocales = "AEIOU"
    paterno = paterno.upper()
    for letra in paterno[1:]:
        if letra in vocales:
            return letra
    return "X"

def generar_homoclave():
    caracteres = string.ascii_uppercase + string.digits
    return ''.join(random.choice(caracteres) for _ in range(3))


def formulario(request):
    rfc_resultado = None

    if request.method == "POST":
        form = RFCForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre'].upper().split()
            apellido_paterno = form.cleaned_data['apellido_paterno'].upper()
            apellido_materno = form.cleaned_data['apellido_materno'].upper() if form.cleaned_data['apellido_materno'] else "X"
            fecha = form.cleaned_data['fecha_nacimiento']

            # Nombre especial José o María) 
            nombres_comunes = ["JOSE", "MARIA"]
            if nombre[0] in nombres_comunes and len(nombre) > 1:
                nombre_final = nombre[1]
            else:
                nombre_final = nombre[0]

            # Iniciales del usuario
            inicial1 = apellido_paterno[0]
            inicial2 = obtener_primera_vocal_interna(apellido_paterno)
            inicial3 = apellido_materno[0] if apellido_materno else "X"
            inicial4 = nombre_final[0]

            iniciales = inicial1 + inicial2 + inicial3 + inicial4

            # Fecha en la que nacio el usuario 
            yy = str(fecha.year)[2:]
            mm = f"{fecha.month:02d}"
            dd = f"{fecha.day:02d}"

            fecha_rfc = yy + mm + dd

            # Homoclave random para generar los 3 faltantes del RFC
            homoclave = generar_homoclave()

            rfc_resultado = iniciales + fecha_rfc + homoclave

    else:
        form = RFCForm()

    return render(request, "formulario.html", {
        "form": form,
        "rfc_resultado": rfc_resultado
    })

