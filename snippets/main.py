from openpyxl import Workbook
from pydictxl.pydictxl import gerenerate_data, generate_header
from data_set import data_set

header = ['Name', 'Age', 'Sex', 'City']
values = ['name', 'age', 'sex', 'city']

wb = Workbook()
ws = wb.active

generate_header(header, ws, 1)
gerenerate_data(data_set, values, ws, 2)

wb.save(filename='snippet.xlsx')
