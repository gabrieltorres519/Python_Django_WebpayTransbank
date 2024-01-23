from PyPDF2 import PdfWriter

pdfs = ["mypdf.pdf", "mypdf-1.pdf", "mypdf-2.pdf"] #Lista de pdfs a unir

nombre_de_salida = "salida.pdf"

fusionador = PdfWriter()

for pdf in pdfs: # Recorrer la lista de pdfs y unirlos
    fusionador.append(open(pdf, 'rb')) # Permisos de lecturas

with open(nombre_de_salida, 'wb') as salida:
    fusionador.write(salida)