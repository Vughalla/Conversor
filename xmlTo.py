import os
import re
import json
import pprint
import xmltodict
import pandas as pd
import xml.etree.ElementTree as et

CURRENT_WORK_PATH = os.path.dirname(os.path.abspath(__file__))
INPUT_PATH = CURRENT_WORK_PATH + '/Input'
OUTPUT_PATH = CURRENT_WORK_PATH + '/Output'

def limpiarJson(camposNumericos):
    with open(OUTPUT_PATH + "/casos_covid19_OrigenXML.json", encoding="UTF-8") as jsonCrudo:
        with open(OUTPUT_PATH + "/casos_covid19_OrigenXMLCOCIDOPAPA.json", "w", encoding="UTF-8") as jsonCocido:
            for line in jsonCrudo:
                corte = line.split(":")[0].rstrip().replace(" ","").replace('"','')
                if (corte in camposNumericos):
                    jsonCocido.write(line.replace(line,str(line.split(":")[0]) + ":" +line.split(":")[1].replace('"','')))
                else:
                    jsonCocido.write(line)
    os.remove(OUTPUT_PATH + "/casos_covid19_OrigenXML.json")
    os.rename(OUTPUT_PATH + "/casos_covid19_OrigenXMLCOCIDOPAPA.json", OUTPUT_PATH + "/casos_covid19_OrigenXML.json")


def xmlToJson(xmlInput, jsonOutput):
    with open(xmlInput, encoding="UTF-8") as xmlFile:
        #tree = et.parse(xmlFile)
        #xml_data = tree.getroot()
        #xmlstr = et.tostring(xml_data, encoding='utf-8', method='xml')#
        #data_dict = json.dumps((xmltodict.parse(xmlstr))) #HASTA ACÁ LO DE LA DOC OFICIAL. A PARTIR DE ACA SE HACE UNA EDICIÓN DEL JSON RESULTANTE PARA DEJARLO COMO SERIA ORIGINALMENTE SIN LOS DATOS EXTRAS QUE TIENE UN XML.

        data = xmltodict.parse(xmlFile.read())
        data_dict = json.dumps(data, ensure_ascii=False)

        #EXPERIMENTAL:
        datoLnd = data_dict.replace('"@type": "dict", ', "").replace('"@type": "int", ', "").replace('"@type": "str", ', "").replace('"@type": "float", ', "").replace  ('"#text": ', "").replace('"@type": ',"").replace('": {"','": "').replace('"}, "','", "').replace('"}}, {','"}, {').split("[")[1].split("]")[0]

        datoStg = datoLnd[:-1]
        datoFnl = "[" + datoStg + "]" # -> FUNCIONÓ CON LOS XML GENERADOS DESDE jsonToXml.
        #datoFnl = "[" + datoStg + "}]" # -> FUNCIONÓ CON LOS XML BAJADOS DE INTERNET.

        data = json.loads(datoFnl)
        json_pretty = json.dumps(data, indent=4, ensure_ascii=False)

        with open(jsonOutput, "w", encoding="UTF-8") as f:
           f.write(json_pretty)
    camposNumericos = ["numero_de_caso", "comuna", "edad"] #PONER TODOS LOS CAMPOS QUE SEAN INT O FLOAT
    limpiarJson(camposNumericos)
    


xmlToJson(INPUT_PATH + "/casos_covid19_OrigenXML.xml", OUTPUT_PATH + "/casos_covid19_OrigenXML.json")








#------------------------------------------------------------------------

#
#xmlData = """<table name="ShippedItems">
#  <column name="ItemNumber" value="primaryKey"/>
#  <column name="Weight"/>
#  <column name="Dimension"/>
#  <column name="InsuaranceAmt"/>
#  <column name="Destination"/>
#  <column name="FinalDeliveryDate"/>
#  <column name="UniqueID" value="foreignKey"/>
#</table>
#"""
#print(json.dumps(xmltodict.parse(xmlData,encoding="latin")))
#
#print("----------------------------------------------------------------------------------------")
#
#mydict={"relation": {"member": [{"@name": "ShippedItems", "@rel": "Shipped_Via"}, {"@name": "TranspotationEvent", "@rel": "Shipped_Via"}], "cardinality": {"card": [#{"@name": "ShippedItems", "@value": "many"}, {"@name": "TranspotationEvent", "@value": "many"}]}}}
#print(xmltodict.unparse(mydict, pretty=True))
#
