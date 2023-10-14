# -*- coding: utf-8 -*-
from typing import Tuple
from src.Types import DataType
from src.StudentsGood import StudentsGood
import pytest


class TestStudentsGood():
    @pytest.fixture()
    def input_data(self) -> Tuple[DataType, int]:
        data: DataType = {
            "Абрамов Петр Сергеевич":
            [
                ("математика", 80),
                ("русский язык", 76),
                ("программирование", 100)
            ],
            "Петров Игорь Владимирович":
            [
                ("математика", 50),
                ("русский язык", 40),
                ("программирование", 78),
                ("литература", 97)
            ]
        }

        students_good = 1

        return data, students_good

    def test_init_calc_good(self, input_data:
                            Tuple[DataType, int]) -> None:

        calc_debt = StudentsGood(input_data[0])
        assert input_data[0] == calc_debt.data

    def test_calc(self, input_data:
                  Tuple[DataType, int]) -> None:
        count = StudentsGood(input_data[0]).calc()
        assert count == input_data[1]
