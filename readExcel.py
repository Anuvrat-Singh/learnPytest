from openpyxl import load_workbook


workbook = load_workbook('testXLSX.xlsx')
sheet_ranges = workbook['Sheet1']

print(sheet_ranges['A1'].value)