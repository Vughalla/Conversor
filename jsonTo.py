import pandas as pd
from json2xml import json2xml
from json2xml.utils import readfromurl, readfromstring, readfromjson


#Recibe un JSON y lo guarda en formato CSV.
def jsonToCsv(jsonInput, csvOutput):
    df = pd.read_json(jsonInput)
    df.to_csv(csvOutput, index = None)

def jsonToXml(jsonInput, xmlOutput):
    data = readfromjson(jsonInput)
    xmlFile = json2xml.Json2xml(data).to_xml()
    with open(xmlOutput, "w", encoding="UTF-8") as f:
        for line in xmlFile:
            f.write(line)
