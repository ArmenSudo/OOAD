from Cell import Cell
from Spreadsheet import Spreadsheet
from datetime import datetime


def print_result(state, f_name):
    print(f'{f_name} is {"pass" if state else "fail"}')


def test_setValue():
    obj = Cell()
    obj.setValue(13)
    print_result(obj.getValue() == '13', 'Cell setValue')


def test_toInt():
    obj = Cell()
    obj.setValue(13)
    print_result(obj.toInt() == 13, 'Cell toInt')


def test_toDouble():
    obj = Cell()
    obj.setValue('13.3')
    print_result(obj.toDouble() == 13.3, 'Cell toDouble')


def test_toDate():
    obj = Cell()
    obj.setValue('02-12-2022')
    print_result(obj.toDate() == datetime.strptime('02-12-2022', '%m-%d-%Y').date(), 'Cell toDate')


def test_reset():
    obj = Cell(12)
    obj.reset()
    print_result(obj.getValue() is None and obj.getColor() == '#000000', 'Cell reset')


def test_setColor():
    obj = Cell()
    obj.setColor('Black')
    print_result(obj.getColor() == '#000000', 'Cell setColor')


def test_setCellAt():
    obj = Spreadsheet(3, 5)
    obj.setCellAt(1, 2, 'Armen')
    print_result(obj.getCellAt(1, 2).getValue() == 'Armen', 'Spreadsheet setCellAt for value')

    obj.setCellAt(0, 0, 'Anna')
    obj.setCellAt(1, 2, obj.getCellAt(0, 0))
    print_result(obj.getCellAt(1, 2).getValue() == "Anna", 'Spreadsheet setCellAt for obj')


def test_addRow():
    obj = Spreadsheet(3, 5)
    obj.setCellAt(1, 2, 'Armen')
    obj.addRow(1)
    print_result(obj.getCellAt(2, 2).getValue() == "Armen", 'Spreadsheet addRow')


def test_addColumn():
    obj = Spreadsheet(3, 5)
    obj.setCellAt(1, 2, 'Armen')
    obj.addColumn(2)
    print_result(obj.getCellAt(1, 3).getValue() == "Armen", 'Spreadsheet addColumn')


def test_removeRow():
    obj = Spreadsheet(3, 5)
    obj.setCellAt(1, 2, 'Armen')
    obj.removeRow(0)
    print_result(obj.getCellAt(0, 2).getValue() == "Armen", 'Spreadsheet removeRow')


def test_removeColumn():
    obj = Spreadsheet(3, 5)
    obj.setCellAt(1, 2, 'Armen')
    obj.removeColumn(1)
    print_result(obj.getCellAt(1, 1).getValue() == "Armen", 'Spreadsheet removeColumn')


def test_swapRows():
    obj = Spreadsheet(3, 5)
    obj.setCellAt(0, 2, 'Armen')
    obj.setCellAt(2, 2, 'Anna')
    obj.swapRows(0, 2)
    print_result(obj.getCellAt(0, 2).getValue() == "Anna" and obj.getCellAt(2, 2).getValue() == "Armen",
                 'Spreadsheet swapRows')


def test_swapColumns():
    obj = Spreadsheet(3, 5)
    obj.setCellAt(0, 2, 'Armen')
    obj.setCellAt(0, 0, 'Anna')
    obj.swapColumns(0, 2)
    print_result(obj.getCellAt(0, 2).getValue() == "Anna" and obj.getCellAt(0, 0).getValue() == "Armen",
                 'Spreadsheet swapColumns')


def test_Cell():
    test_setValue()
    test_toInt()
    test_toDouble()
    test_toDate()
    test_reset()
    test_setColor()


def test_Spreadsheet():
    test_setCellAt()
    test_addRow()
    test_addColumn()
    test_removeRow()
    test_removeColumn()
    test_swapRows()
    test_swapColumns()


test_Cell()
print()
test_Spreadsheet()
