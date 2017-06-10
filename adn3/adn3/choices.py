# coding=utf-8
from datetime import datetime


def make_years():
    """
    :return: a range of valid years.
    """
    this_year = datetime.now().year
    return [(i, i) for i in range(this_year - 1, this_year + 1)]


def make_days():
    return [
        (0, 'Lunes'),
        (1, 'Martes'),
        (2, 'Miércoles'),
        (3, 'Jueves'),
        (4, 'Viernes'),
        (5, 'Sábado'),
        (6, 'Domingo'),
    ]


def make_blocks():
    return [
        (0, '1-2'),
        (1, '3-4'),
        (2, '5-6'),
        (3, '7-8'),
        (4, '9-10'),
        (5, '11-12'),
        (6, '13-14'),
    ]


def make_blocks_days():
    return [
        (0, '1-2'),
        (1, '3-4'),
        (2, '5-6'),
        (3, '7-8'),
        (4, '9-10'),
        (5, '11-12'),
        (6, '13-14'),
    ]

def make_session_numbers():
    return [(i, i) for i in range(1, 33)]
