from logging import currentframe
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Image, Spacer,Paragraph
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY

file = open('sinbloqueo.txt','r')
file2 = open('conbloqueo.txt','r')
filas = file.readlines()
filas2 = file2.readlines()

# Data to be stored on table
data = [
   ["Timeline","T0","T1","T2","T3","T4"],
]
data2 = [
   ["Timeline","T0","T1","T2","T3","T4"],
]

tokens = []
array = []
for fila in filas:
    tokens = fila.split("|")
    array.append(tokens)

tokens2 = []
array2 = []
for fila in filas2:
    tokens2 = fila.split("|")
    array2.append(tokens2)


def ordenarPorNumeroTransaccion(array):
  return array[0]

array.sort(key=ordenarPorNumeroTransaccion)
array2.sort(key=ordenarPorNumeroTransaccion)

currentLine = 1
for i in array:
    #print(i[0])
    lineData =["","","",""]
    timeline = i[0]
    nroTransaccion = i[2]
    transaccion = i[3]

    if(nroTransaccion == ' T#0 '):
        lineData.insert(0,timeline)
        lineData.insert(1,transaccion)
        data.insert(currentLine, lineData)
    elif (nroTransaccion == ' T#1 '):
        lineData.insert(0,timeline)
        lineData.insert(2,transaccion)
        data.insert(currentLine, lineData)
    elif (nroTransaccion == ' T#2 '):
        lineData.insert(0,timeline)
        lineData.insert(3,transaccion)
        data.insert(currentLine, lineData)
    elif (nroTransaccion == ' T#3 '):
        lineData.insert(0,timeline)
        lineData.insert(4,transaccion)
        data.insert(currentLine, lineData)
    elif (nroTransaccion == ' T#4 '):
        lineData.insert(0,timeline)
        lineData.insert(5,transaccion)
        data.insert(currentLine, lineData)


    currentLine= currentLine +1

currentLine = 1
for i in array2:
    #print(i[0])
    lineData =["","","",""]
    timeline = i[0]
    nroTransaccion = i[2]
    transaccion = i[3]

    if(nroTransaccion == ' T#0 '):
        lineData.insert(0,timeline)
        lineData.insert(1,transaccion)
        data2.insert(currentLine, lineData)
    elif (nroTransaccion == ' T#1 '):
        lineData.insert(0,timeline)
        lineData.insert(2,transaccion)
        data2.insert(currentLine, lineData)
    elif (nroTransaccion == ' T#2 '):
        lineData.insert(0,timeline)
        lineData.insert(3,transaccion)
        data2.insert(currentLine, lineData)
    elif (nroTransaccion == ' T#3 '):
        lineData.insert(0,timeline)
        lineData.insert(4,transaccion)
        data2.insert(currentLine, lineData)
    elif (nroTransaccion == ' T#4 '):
        lineData.insert(0,timeline)
        lineData.insert(5,transaccion)
        data2.insert(currentLine, lineData)


    currentLine= currentLine +1
        

# creating a pdf file to add tablesl
document = SimpleDocTemplate("tp7DistriTransacciones.pdf", pagesize=letter,rightMargin=72,leftMargin=72, topMargin=72, bottomMargin=18)
items = []



# Creating the table with 6 rows
t = Table(data)
t2 = Table(data2)
# setting up style and alignments of borders and grids
t.setStyle(
   TableStyle(
       [
           #the first coordinate 
           ("ALIGN", (0, 0), (5, 0), "CENTER"), #all row with align center
           #("BACKGROUND", (0, 0), (5,2), colors.green), #the title align is center
           #("VALIGN", (-1, -1), (-1, -1), "TOP"),
           #("ALIGN", (-1, -1), (-1, -1), "RIGHT"),
           #("VALIGN", (-1, -1), (-1, -1), "TOP"),
           ("INNERGRID", (0, 0), (-1, -1), 1, colors.black), #lineas de adentro de la tabla
           ("FONTSIZE", (0, 0), (-1, -1), 4), #lineas de adentro de la tabla
           ('FONTNAME', (0,0), (5,0), 'Helvetica-Bold'), #primera fila en negrita
           ('FONTNAME', (0,0), (-6,-1), 'Helvetica-Bold'), #primera columna en negrita
           ("BOX", (0, 0), (-1, -1), 1, colors.black), #lineas del borde de la tabla
       ]
   )
)
t2.setStyle(
   TableStyle(
       [
           #the first coordinate 
           ("ALIGN", (0, 0), (5, 0), "CENTER"), #all row with align center
           #("BACKGROUND", (0, 0), (5,2), colors.green), #the title align is center
           #("VALIGN", (-1, -1), (-1, -1), "TOP"),
           #("ALIGN", (-1, -1), (-1, -1), "RIGHT"),
           #("VALIGN", (-1, -1), (-1, -1), "TOP"),
           ("INNERGRID", (0, 0), (-1, -1), 1, colors.black), #lineas de adentro de la tabla
           ("FONTSIZE", (0, 0), (-1, -1), 4), #lineas de adentro de la tabla
           ('FONTNAME', (0,0), (5,0), 'Helvetica-Bold'), #primera fila en negrita
           ('FONTNAME', (0,0), (-6,-1), 'Helvetica-Bold'), #primera columna en negrita
           ("BOX", (0, 0), (-1, -1), 1, colors.black), #lineas del borde de la tabla
       ]
   )
)

estilos = getSampleStyleSheet()
estilos.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))

linkGithub = titulo5 = Paragraph("Codigo Fuente para generar el Pdf en: https://github.com/MateoGuillen/distritp7",estilos["Normal"])
logSinBloqueo1 = Image("sinbloqueo1.png", 7* inch,  4* inch)
logConBloqueo1 = Image("conbloqueo1.png", 7* inch,  4* inch)
titulo1 = Paragraph("Log de ejecución de transacciones generado (Sin Bloqueo)",estilos["Justify"])
titulo2 = Paragraph("Log de ejecución de transacciones generado (Con Bloqueo)",estilos["Normal"])
titulo3 = Paragraph("Tabulación de datos de la consola (Sin Bloqueo)",estilos["Normal"])
titulo4 = Paragraph("Tabulación de datos de la consola (Con Bloqueo)",estilos["Normal"])
titulo5 = Paragraph("Pregunta de Desafio (Sin Bloqueo):",estilos["Normal"])
titulo6 = Paragraph("Pregunta de Desafio (Con Bloqueo):",estilos["Normal"])
preguntadesafio1 = Paragraph("El estado inicial de las cuentas son persona 1: 500 y persona 2: 0. Luego de realizar las cinco transacciones correspondientes las cuales son (--- EXTRAER P1 (150)---, -- EXTRAER P1 (100) Y DEPOSITAR P2 (100)---, --- EXTRAER P1 (100) Y DEPOSITAR P2 (100)---, --- EXTRAER P1 (150)---, --- EXTRAER P1 (100) Y DEPOSITAR P2 (100)---).",estilos["Normal"])
preguntadesafio1_2 = Paragraph("Al Ejecutar el programa sin bloqueos, el resultado final es: Estado Final Persona 1: 400, Persona 2: 100, el cual es un resultado inconsistente ya que se esperaba que al finalizar las cinco transacciones la Persona 1 tenga saldo un saldo insuficiente al realizar las transacciones y la Persona 2 tenga un saldo de 300 (3 operaciones de DEPOSITAR P2), en cambio solo se ejecuto una transacción de --- EXTRAER P1 (100) Y DEPOSITAR P2 (100)--- que dió como resultado el estado final. Esto se debe a que hubieron transacciones que hicieron caso omiso a lo que estaban haciendo las demás transacciones, solo se refleja la actualización de la última transacción que se ejecuto, las otras fueron ignoradas.",estilos["Normal"])
preguntadesafio1_3 = Paragraph("Especificamente se debe a que la T2 predomino en la ejecución del programa, sin considerar al final a las T0,T1,T3,T4.",estilos["Normal"])
preguntadesafio2 = Paragraph("El estado inicial de las cuentras son persona 1: y persona 2: . Luego de realizar las cinco transacciones correspondientes las cuales son --- EXTRAER P1 (100) Y DEPOSITAR P2 (100)---, --- EXTRAER P1 (100) Y DEPOSITAR P2 (100)--, --- EXTRAER P1 (150)---, --- EXTRAER P1 (150)---, --- EXTRAER P1 (100) Y DEPOSITAR P2 (100)---.",estilos["Normal"])
preguntadesafio2_2 = Paragraph("Al Ejecutar el programa con bloqueos, el resultado final es : Estado Final Persona 1: 50, Persona 2: 300, el cual es un resultado consistente ya que la persona 1 tiene saldo 500 inicialmente y se intenta extraer un total de 600. ",estilos["Normal"])
preguntadesafio2_3 = Paragraph("Especificamente se debe a que la T3 al intentar realizar la operación de --- EXTRAER P1 (150)--- da como resultado un Rollback, a causa de que la cuenta P1 posee solo un saldo de 50 (Saldo Insuficiente), ya que se van ejecutando las transacciones una por una (con bloqueo). Además que las transacciones que implican depositar se ejecutaron correcatmente (Persona 2: 300)",estilos["Normal"])
items.append(titulo1)
items.append(Spacer(1, 12))
items.append(logSinBloqueo1)
items.append(Spacer(1, 12))
items.append(titulo2)
items.append(Spacer(1, 12))
items.append(logConBloqueo1)
items.append(Spacer(1, 48))
items.append(titulo3)
items.append(Spacer(1, 12))
items.append(t)
items.append(Spacer(1, 36))
items.append(titulo4)
items.append(Spacer(1, 12))
items.append(t2)
items.append(Spacer(1, 48))
items.append(titulo5)
items.append(Spacer(1, 12))
items.append(preguntadesafio1)
items.append(Spacer(1, 12))
items.append(preguntadesafio1_2)
items.append(Spacer(1, 12))
items.append(preguntadesafio1_3)
items.append(Spacer(1, 12))
items.append(titulo6)
items.append(Spacer(1, 12))
items.append(preguntadesafio2)
items.append(Spacer(1, 12))
items.append(preguntadesafio2_2)
items.append(Spacer(1, 12))
items.append(preguntadesafio2_3)
items.append(Spacer(1, 12))
items.append(linkGithub)



document.build(items)





