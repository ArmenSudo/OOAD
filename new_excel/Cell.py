from datetime import datetime


class Cell:
    __colors = {'Black': '#000000', 'Orange': '#F86F15', 'Fuchsia': '#F51663'}

    def __init__(self, value=None, color='Black'):
        self._value = value
        self._color = self.__colors[color]

    def setValue(self, value):
        self._value = str(value)

    def setColor(self, color):
        self._color = self.__colors[color]

    def getColor(self):
        return self._color

    def getValue(self):
        return self._value

    def toInt(self):
        try:
            return int(self._value)
        except ValueError:
            print("No casting to int")

    def toDouble(self):
        try:
            return float(self._value)
        except ValueError:
            print("No casting to double")

    def toDate(self):
        try:
            return datetime.strptime(self._value, '%m-%d-%Y').date()
        except ValueError:
            print("No casting to date")

    def reset(self):
        self._value = None
        self._color = self.__colors['Black']
