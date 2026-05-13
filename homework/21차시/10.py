from openpyxl import load_workbook

wb = load_workbook("data.xlsx")
sheet = wb.active

sheet.append(["Doosan", "Rokey", "Bootcamp", "Fighting"])
sheet.append(["짱구", "철수", "훈이", 10])

wb.save("data.xlsx")