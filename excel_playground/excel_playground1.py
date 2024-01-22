from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.title = 'MyNewSheet'


ws = wb.create_sheet()
ws.title = 'MyanotherSheet'

wb.save('./excel_playground/practice1.xlsx')
wb.close()