from Types import DataType


class StudentsGood:
    def __init__(self, data: DataType) -> None:
        self.data: DataType = data
        self.goodCount = 0
        self.count = 0

    def calc(self) -> int:
        for key in self.data:
            self.goodCount = 0
            for subject in self.data[key]:
                if subject[1] >= 76:
                    self.goodCount += 1
            if self.goodCount == len(self.data[key]):
                self.count += 1
        return self.count
