def main():
    import sys
    import re

    class Massiv():
        def __init__(self) -> None:
            pass

        def NewParam(self):
            self.DlinaMassiva = input('DlinaMassiva=')
            self.Shag = input('Shag=')
            Massiv.ProverkaArg(self)

        def ProverkaArg(self):
            if re.search(r'\d+', self.DlinaMassiva) == None or re.search(r'\d+', self.Shag) == None:
                print('Error Arg, Enter new arg')
                Massiv.NewParam(self)
            else:
                self.DlinaMassiva = int(self.DlinaMassiva)
                self.Shag = int(self.Shag)
            if self.DlinaMassiva < self.Shag:
                print('Длина массива не может быть меньше шага')
                print('Error Arg, Enter new arg')
                Massiv.NewParam(self)
            elif self.DlinaMassiva < 1 or self.Shag < 1:
                print("Длина массива или шаг не может быть < 1")
                Massiv.NewParam(self)

        def InputParam(self):
            try:
                self.DlinaMassiva = sys.argv[1]
                self.Shag = sys.argv[2]
                Massiv.ProverkaArg(self)
            except:
                print("Ошибка аргументов")
                Massiv.NewParam(self)

        def CreateArray(self):
            self.NewMassiv = []
            for i in range(self.DlinaMassiva):
                self.NewMassiv.append(i+1)
            # print(self.NewMassiv)

        def IterateMassiv(self):
            ReadyStr = ''
            self.OutList = []
            while True:
                for i in self.NewMassiv:
                    ReadyStr = ReadyStr+str(i)
                    if len(ReadyStr) == self.Shag:
                        if ReadyStr not in self.OutList:
                            self.OutList.append(ReadyStr)
                            ReadyStr = ''
                            ReadyStr = ReadyStr+str(i)
                        else:
                            break
                if ReadyStr in self.OutList:
                    break
            # print(self.OutList)

        def Result(self):
            ResultStr = ''
            for i in self.OutList:
                ResultStr = ResultStr+i[:1]
            print(ResultStr)
    Task = Massiv()
    Task.InputParam()
    Task.CreateArray()
    Task.IterateMassiv()
    Task.Result()


main()