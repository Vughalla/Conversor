import os
import csv
import json
import pandas as pd
from datetime import datetime
from xlsxwriter.workbook import Workbook

# Toma un json sin identacion 
def makeJsonPretty(jsonOutput, OUTPUT_PATH):
    jsonFinal = OUTPUT_PATH + '/jsonFinal.json'
    with open(jsonOutput, encoding="UTF-8") as json_data:
        data = json.load(json_data)
        json_pretty = json.dumps(data, indent=4, ensure_ascii=False)
        with open(jsonFinal, "w", encoding="UTF-8") as final_json:
            final_json.write(json_pretty)
    os.remove(jsonOutput)
    os.rename(jsonFinal, jsonOutput)

#Recibe un CSV y lo guarda en formato JSON
def csvToJson(csvInput, jsonOutput, jsonOrient, OUTPUT_PATH):
    df = pd.read_csv(csvInput) #INTENTAR SIN DTYPE, DE SER IMPOSIBLE PONER EN STRING LOS QUE DEN ERROR.
    df.to_json(jsonOutput, orient=jsonOrient) # ORIENT RECORDS, ORDENA EL JSON DE UNA SOLA LINEA A VARIAS, SIN IDENTAR.
    makeJsonPretty(jsonOutput, OUTPUT_PATH) #IDENTA EL JSON PARA QUE SEA MAS LEGIBLE

#Recibe un CSV y lo guarda en formato XLSX.
def csvToXlsx(csvInput, xlsxOutput):
        workbook = Workbook(xlsxOutput)
        worksheet = workbook.add_worksheet()
        with open(csvInput, 'rt', encoding='utf8') as f:
            reader = csv.reader(f)
            for r, row in enumerate(reader):
                for c, col in enumerate(row):
                    worksheet.write_string(r, c, col)
        workbook.close()

def csvToTxt(csvInput, txtOutput):
    df = pd.read_csv(csvInput)
    df.to_csv(txtOutput, index=None, sep=',', mode='a')


def csvToXml(csvInput, xmlOutput):

    
    return True


#FALTA CSV TO EL FORMATO ESE DE WEB

