import copy

from Cell import Cell


class Spreadsheet:
    def __init__(self, rows, columns):
        if isinstance(rows, int) and isinstance(columns, int) and rows > 0 and columns > 0:
            self._row = rows
            self._columns = columns
            self._sh = [[Cell() for y in range(columns)] for x in range(rows)]
        else:
            raise "No Valid Size"

    def setCellAt(self, row, columns, value):
        if row < 0 or row >= self._row or columns < 0 or columns >= self._columns:
            print("Out of range")
            return

        if isinstance(value, Cell):
            self._sh[row][columns] = copy.deepcopy(value)
        else:
            self._sh[row][columns].setValue(value)

    def getCellAt(self, row, columns):
        return self._sh[row][columns]

    def addRow(self, row):
        if row > self._row:
            print('Out of range!')
            return
        self._sh.insert(row, [Cell() for y in range(len(self._sh[0]))])

    def addColumn(self, column):
        if column > self._columns:
            print('Out of range!')
            return

        for x in self._sh:
            x.insert(column, Cell())

    def removeRow(self, row):
        if row > self._row:
            print('Out of range!')
            return

        del self._sh[row]

    def removeColumn(self, column):
        if column >= self._columns:
            print('Out of range!')
            return

        for x in self._sh:
            del x[column]

    def swapRows(self, first_row, second_row):
        if first_row >= self._row or second_row >= self._row:
            print('Out of range!')
            return

        self._sh[first_row], self._sh[second_row] = self._sh[second_row], self._sh[first_row]

    def swapColumns(self, first_column, second_column):
        if first_column >= self._columns or second_column >= self._columns:
            print('Out of range!')
            return

        for x in self._sh:
            x[first_column], x[second_column] = x[second_column], x[first_column]

    def print_sheet(self):
        for x in self._sh:
            print(x)
