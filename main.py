import os
import sys
import json
import pandas as pd
from datetime import datetime

from csvTo import csvToJson, csvToTxt, csvToXlsx, csvToXml
from jsonTo import jsonToCsv, jsonToXml
from xlsxTo import xslxToCsv

def main(extension):
    CURRENT_WORK_PATH = os.path.dirname(os.path.abspath(__file__))
    INPUT_PATH = CURRENT_WORK_PATH + '/Input'
    OUTPUT_PATH = CURRENT_WORK_PATH + '/Output'

    for file in os.listdir(INPUT_PATH):
        inputFile = INPUT_PATH + '/' + file
        outputFile = OUTPUT_PATH + '/' + file.split(".")[0] + '.' + extension
        if (file.endswith(".csv")):
            if (extension == "json"):
                csvToJson(inputFile, outputFile, "records", OUTPUT_PATH)
            elif (extension == "xlsx"):
                csvToXlsx(inputFile, outputFile)
#            elif (extension == "txt"):
#                csvToTxt(inputFile, outputFile)
#            elif (extension == "xml"):
#                csvToXml(inputFile, outputFile)
#
#        elif(file.endswith(".json")):
#            if (extension == "csv"):
#                jsonToCsv(inputFile, outputFile)
#            elif (extension == "xml"):
#                jsonToXml(inputFile, outputFile)

        elif(file.endswith(".xlsx")):
        
            csvOutput = OUTPUT_PATH + '/' + file.split(".")[0] + '.csv'
            xslxToCsv(inputFile, csvOutput)


now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("Inicio del proceso - " + dt_string)

main("csv") #Pasar el formato al que se deseen convertir los archivos en /input

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("Fin del proceso - " + dt_string)