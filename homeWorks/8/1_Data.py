class Date:
    __mm = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6, "Jul": 7, "Aug": 8, "Sep": 9, "Okt": 10,
            "Nov": 11, "Dec": 12}
    __data_format = "day-month-year"

    def __init__(self, data):
        self.date = data

    def __str__(self):
        return str(f"{self.date}")

    @classmethod
    def transform_date(cls, data):
        tmp_data = str(data).split("-")
        date = {"d": int(tmp_data[0]), "m": Date.__mm.get(tmp_data[1]), "y": int(tmp_data[2])}
        return cls(date)

    @staticmethod
    def validate_date(data):
        data = dict(data)
        if data.get("d") not in range(1, 32):
            print("Wrong day")
        if data.get("y") <= 0:
            print("Wrong Year")


d_1 = Date("12-Jun-2020")
print(d_1)
d_2 = Date.transform_date("12-Jun-2021")
print(d_2)
Date.validate_date(d_2.date)

d_3 = Date.transform_date("34-Jul-2023")
Date.validate_date(d_3.date)

d_4 = Date.transform_date("34-Jul-0")
Date.validate_date(d_4.date)