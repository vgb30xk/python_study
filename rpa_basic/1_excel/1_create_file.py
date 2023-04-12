from openpyxl import Workbook
wb = Workbook()
ws = wb.active
ws.title = "JaehyunSheet"
wb.save("sample.xlsx")
wb.close()