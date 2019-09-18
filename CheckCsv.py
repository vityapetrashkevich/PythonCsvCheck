import pandas as pd


class CheckCsv:
    DateN = "None"
    rez = True
    ErrorListCsv = "Не совподает имена и/или количетво столбцов"
    ErrorTypeCsv = 0

    def __index__(self):
        self.rez = True
        self.ErrorListCsv = "Не совподает имена и/или количетво столбцов"
        self.ErrorTypeCsv = 0

    def initDate(self):
        fl = input("Есть ли дата в проверяемых файлах? (y/n): ")
        if fl == "y":
            self.DateN = input("Введите имя поля с датой: ")
        return

    def OutRez(self):
        if self.rez == True:
            print("Проверка пройдена успешно")
            return 0
        else:
            print("Файл содержит ошибки!!!")
            print(self.ErrorListCsv)
            return self.ErrorTypeCsv

    def StartCheck(self, NameCheck, MocupCheck):
        self.initDate()
        with open(NameCheck) as CheckCsvFl:
            DataFl = pd.read_csv(CheckCsvFl, sep=",", encoding="windows1251", parse_dates=[self.DateN], dayfirst=True)
            with open(MocupCheck) as MockupFl:
                Mockup = pd.read_csv(MockupFl, sep=',', encoding="windows1251", parse_dates=[self.DateN], dayfirst=True)
                if self.CheckCol(Mockup.columns, DataFl.columns) == False:
                    self.rez = False
                    self.ErrorTypeCsv = 1
                    self.OutRez()

                elif self.CheckRow() == False:
                    self.rez = False
                    self.ErrorTypeCsv = 2
                    self.OutRez()
                else:
                    self.OutRez()

        return 0

    def CheckCol(self, Col1, Col2):
        if Col1==Col2:
            return True
        else:
            return False
