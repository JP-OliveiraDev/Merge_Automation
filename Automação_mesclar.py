#Automação para mesclar PDFs
#Para mesclar os PDFs, é so colocar na pasta arquivos
import pyPDF2
import os

merger = pyPDF2.pdfmerger()
list_arquivos =  os.listdir("arquivos")
list_arquivos.sort()
print(list_arquivos)

for arquivo in list_arquivos:
    if ".pdf" in arquivo:
        #nome do arquivo
        merger.append(f"arquivos/{arquivo}")

merger.write("PDF FINAL.pdf")