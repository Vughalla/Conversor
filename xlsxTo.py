

import pandas as pd
from xlsxwriter.workbook import Workbook


def xslxToCsv(xlsxInput, csvOutput):
    #readFile = pd.read_excel(xlsxInput)
    readFile = pd.read_excel(xlsxInput, engine='openpyxl')
    readFile.to_csv(csvOutput, index = None, header=True)

