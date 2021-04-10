class Slownie:
    rzedy = (
            ('', '', ''),
            ('tysiąc', 'tysiące', 'tysięcy'),
            ('milion', 'miliony', 'milionów'),
            ('miliard', 'miliardy', 'miliardów'),
            ('bilion', 'biliony', 'bilionów'),
            ('biliard', 'biliardy', 'biliardów'),
            ('trylion', 'tryliony', 'trylionów'),
            ('tryliard', 'tryliardy', 'tryliardów'),
            ('kwadrylion', 'kwadryliony', 'kwadrylionów'),
            ('kwadryliard', 'kwadryliardy', 'kwadryliardów'),
            ('kwintylion', 'kwintyliony', 'kwintylionów'),
            ('kwintyliard', 'kwintyliardy', 'kwintyliardów')
    )

    slowa = (
            ('', 'jeden', 'dwa', 'trzy', 'cztery', 'pięć',
             'sześć', 'siedem', 'osiem', 'dziewięć', 'dziesięć',
             'jedenaście', 'dwanaście', 'trzynaście', 'czternaście', 'piętnaście',
             'szesnaście', 'siedemnaście', 'osiemnaście', 'dziewiętnaście'),
            ('', 'dziesięć', 'dwadzieścia', 'trzydzieści', 'czterdzieści',
             'pięćdziesiąt', 'sześćdziesiąt', 'siedemdziesiąt', 'osiemdziesiąt', 'dziewięćdziesiąt'),
            ('', 'sto', 'dwieście', 'trzysta', 'czterysta',
             'pięćset', 'sześćset', 'siedemset', 'osiemset', 'dziewięćset')
    )

    @classmethod
    def grupa(cls, liczba: int, zero: bool = True, wysoka: bool = False) -> str:
        if type(liczba) != int:
            raise TypeError
        if liczba < 0:
            raise ValueError
        if liczba > 999:
            raise ValueError
        j, d, s = ((liczba//n)%10 for n in (1, 10, 100))
        if d == 1:
            d = 0
            j += 10
        if liczba == 0 and zero:
            return 'zero'
        if liczba == 1 and wysoka:
            return ''
        return ' '.join((cls.slowa[n][x] for (n,x) in ((2, s), (1, d), (0, j)) if x > 0))

    @staticmethod
    def odmien(liczba: int, slowa: list) -> str:
        if liczba < 0:
            liczba = -liczba
        jeden, dwa, piec = slowa
        slowo = piec
        if liczba == 1:
            slowo = jeden
        jednosc = liczba % 10
        reszta = liczba % 100
        if jednosc in (2, 3, 4) and reszta not in range(11, 20):
            slowo = dwa
        return slowo

    @classmethod
    def liczba(cls, liczba: int) -> str:
        try:
            assert liczba == int(liczba)
        except:
            raise TypeError

        if liczba < 0:
            return "minus " + str(cls.liczba(-liczba))
        segmenty = []
        if liczba == 0:
            segmenty.append(0)
        while liczba > 0:
            segmenty.append(liczba%1000)
            liczba //= 1000
        odmienione = [
            ' '.join([
                x for x in [
                    cls.grupa(int(segment), (rzad, len(segmenty)) == (0, 1), rzad > 0),
                    cls.odmien(segment, cls.rzedy[rzad]) if rzad > 0 and segment != 0 else ''
                ]
                if len(x) > 0
            ])
            for (rzad, segment) in list(enumerate(segmenty))[::-1]
        ]
        return ' '.join([o for o in odmienione if len(o) > 0])

