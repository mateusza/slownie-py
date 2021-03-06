#!/usr/bin/env python3

"""slownie.py - Konwertuj liczby na zapis słowny w języku polskim"""

RZEDY = [
        ['', '', ''],
        ['tysiąc', 'tysiące', 'tysięcy'],
        ['milion', 'miliony', 'milionów'],
        ['miliard', 'miliardy', 'miliardów'],
        ['bilion', 'biliony', 'bilionów'],
        ['biliard', 'biliardy', 'biliardów'],
        ['trylion', 'tryliony', 'trylionów'],
        ['tryliard', 'tryliardy', 'tryliardów'],
        ['kwadrylion', 'kwadryliony', 'kwadrylionów'],
        ['kwadryliard', 'kwadryliardy', 'kwadryliardów'],
        ['kwintylion', 'kwintyliony', 'kwintylionów'],
        ['kwintyliard', 'kwintyliardy', 'kwintyliardów']
]

LICZEBNIKI = [
        ['zero', 'jeden', 'dwa', 'trzy', 'cztery', 'pięć',
         'sześć', 'siedem', 'osiem', 'dziewięć', 'dziesięć',
         'jedenaście', 'dwanaście', 'trzynaście', 'czternaście', 'piętnaście',
         'szesnaście', 'siedemnaście', 'osiemnaście', 'dziewiętnaście'],
        ['', 'dziesięć', 'dwadzieścia', 'trzydzieści', 'czterdzieści',
         'pięćdziesiąt', 'sześćdziesiąt', 'siedemdziesiąt', 'osiemdziesiąt', 'dziewięćdziesiąt'],
        ['', 'sto', 'dwieście', 'trzysta', 'czterysta',
         'pięćset', 'sześćset', 'siedemset', 'osiemset', 'dziewięćset']
]


def grupa(liczba: int, wysoka: bool = False) -> str:
    """Zamień 3-cyfrową grupę na zapis słowny. (0-999)"""
    if not isinstance(liczba, int):
        raise TypeError
    if liczba == 0:
        return LICZEBNIKI[0][0]
    if not 0 <= liczba <= 999:
        raise ValueError
    j, d, s = ((liczba // n) % 10 for n in [1, 10, 100])
    if d == 1:
        d, j = 0, j + 10
    if liczba == 1 and wysoka:
        return ''
    return ' '.join((LICZEBNIKI[n][x] for (x, n) in [(s, 2), (d, 1), (j, 0)] if x > 0))


def odmien(liczba: int, slowa: list) -> str:
    """Odmień rzeczownik w odpowiednim przypadku zależnym od liczby."""
    liczba = abs(liczba)
    if isinstance(slowa, str):
        raise TypeError
    slowo_jeden, slowo_dwa, slowo_piec = slowa
    if liczba == 1:
        return slowo_jeden
    if liczba % 10 in {2, 3, 4} and liczba % 100 not in {12, 13, 14}:
        return slowo_dwa
    return slowo_piec


def slownie(liczba: int) -> str:
    """Zapis słowny dowolnie dużej liczby"""
    try:
        assert liczba == int(liczba)
    except (AssertionError, ValueError) as ex:
        raise TypeError from ex

    if liczba < 0:
        return "minus " + slownie(-liczba)
    if liczba == 0:
        return LICZEBNIKI[0][0]

    segmenty = []
    while liczba > 0:
        segmenty.append(liczba % 1000)
        liczba //= 1000
    odmienione = [
        ' '.join((
            x for x in (
                grupa(int(segment), rzad > 0),
                odmien(segment, RZEDY[rzad]) if rzad > 0 and segment != 0 else ''
            )
            if len(x) > 0
        ))
        for (rzad, segment) in [*enumerate(segmenty)][::-1]
        if segment != 0
    ]
    return ' '.join([o for o in odmienione if len(o) > 0])


if __name__ == '__main__':
    import sys
    for arg in sys.argv[1:]:
        print(slownie(int(arg)))
