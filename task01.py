class Date:

    def __init__(self, date):
        self.date = date

    @classmethod
    def date_to_number(cls, x):
        cls.x = []
        for el in x:
            if el == '-':
                continue
            cls.x.append(el)
        cls.x = ''.join(cls.x)
        return cls.x

    @staticmethod
    def validation(str_date):
        flag = False
        date = str_date.split('-')
        if date[0].isdigit() and date[1].isdigit() and date[2].isdigit():
            for i in range(3):
                date[i] = int(date[i])
            if date[0] > 0 and date[0] <= 31 and date[1] > 0 and date[1] <= 12 and date[2] > 0 and date[2] <= 9999:
                if date[1] != 2:
                    if date[0] >= 0 and date[0] <= 29:
                        flag = True
                    elif date[0] >= 30:
                        if date[0] == 30:
                            flag = True
                        else:
                            if (1, 3, 5, 7, 8, 10, 12).count(date[1]) > 0:
                                flag = True
                            else:
                                flag = False
                else:
                    if date[0] < 30:
                        if date[0] != 29:
                            flag = True
                        else:
                            if (date[2] % 4 == 0 and date[2] % 100 != 0) or date[2] % 400 == 0:
                                flag = True
                            else:
                                flag = False
                    else:
                        flag = False
            else:
                flag = False
        else:
            flag = False
        if flag:
            print(f"Дата {str_date} корректная")
        else:
            print(f"Дата {str_date} некорректная")

Date.date_to_number("17-01-1999")
Date.validation("17-01-1999")
Date.validation("30-13-2000")
Date.validation("31-04-2000")
Date.validation("30-02-2000")
Date.validation("29-02-2015")
Date.validation("29-02-2016")
Date.validation("29-02-2100")
Date.validation("29-02-2000")

