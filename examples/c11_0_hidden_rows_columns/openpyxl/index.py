from openpyxl import load_workbook


def hide_row(xlsx_path, row_dimensions=[]):
    wb = load_workbook(xlsx_path)
    ws = wb.active
    for index in row_dimensions:
        ws.row_dimensions[index].hidden = True
    return wb.save(xlsx_path)


def get_hidden_row_dimensions(xlsx_path):
    wb = load_workbook(xlsx_path)
    ws = wb.active
    return [
        rowNum
        for rowNum, rowDimension in ws.row_dimensions.items()
        if rowDimension.hidden
    ]


def hide_col(xlsx_path, column_dimensions=[]):
    wb = load_workbook(xlsx_path)
    ws = wb.active
    for index in column_dimensions:
        ws.column_dimensions[index].hidden = True
    return wb.save(xlsx_path)


def get_hidden_col_dimensions(xlsx_path):
    wb = load_workbook(xlsx_path)
    ws = wb.active
    col_dimensions = [
        colLetter
        for colLetter, colDimension in ws.column_dimensions.items()
        if colDimension.hidden
    ]
    col_dimensions.sort()
    return col_dimensions
