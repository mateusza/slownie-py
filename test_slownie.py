#!/usr/bin/env python3

import pytest

import slownie


class Test_Odmien():
    @pytest.mark.parametrize(
        'n,o,s',
        [(n, ['kot', 'koty', 'kotów'], s)
            for (n,s) in [
                (0, 'kotów'),
                (1, 'kot'),
                (2, 'koty'),
                (3, 'koty'),
                (4, 'koty'),
                (5, 'kotów'),
                (6, 'kotów'),
                (10, 'kotów'),
                (11, 'kotów'),
                (12, 'kotów'),
                (13, 'kotów'),
                (14, 'kotów'),
                (19, 'kotów'),
                (20, 'kotów'),
                (21, 'kotów'),
                (22, 'koty'),
                (23, 'koty'),
                (24, 'koty'),
                (25, 'kotów'),
                (29, 'kotów'),
                (30, 'kotów'),
                (31, 'kotów'),
                (32, 'koty'),
                (33, 'koty'),
                (34, 'koty'),
                (35, 'kotów'),
                (39, 'kotów'),
                (40, 'kotów'),
                (41, 'kotów'),
                (42, 'koty'),
                (43, 'koty'),
                (44, 'koty'),
                (45, 'kotów'),
                (49, 'kotów'),
                (99, 'kotów'),
                (100, 'kotów'),
                (101, 'kotów'),
                (102, 'koty'),
                (103, 'koty'),
                (105, 'kotów'),
                (112, 'kotów'),
                (115, 'kotów'),
                (122, 'koty'),
                (125, 'kotów'),
                (200, 'kotów'),
                (201, 'kotów'),
                (202, 'koty'),
                (203, 'koty'),
                (205, 'kotów'),
                (215, 'kotów'),
                (222, 'koty'),
                (905, 'kotów')
            ]
        ]
    )
    def test_zakres_0_9(self, n, o, s):
        print(f"{n} {slownie.odmien(n, o)} vs {s}")
        assert slownie.odmien(n, o) == s

    @pytest.mark.parametrize('w', [
        'abc',
        'abcdef',
        1234,
        True,
        int,
        bool
    ])
    def test_bledny_typ_zestawu_slow(self, w):
        print(f"Odmieniam: {repr(w)}")
        with pytest.raises(TypeError):
            assert slownie.odmien(42, w)

    @pytest.mark.parametrize('w', [
        ('mysz', 'myszy', 'myszy'),
        'dom domy domów'.split(),
        (f'dom{x}' for x in ('', 'y', 'ów'))
    ])
    def test_prawidlowy_typ_zestawu_slow(self, w):
        assert slownie.odmien(7, w)

    @pytest.mark.parametrize('w', [
        [],
        ['pies'],
        ['pies', 'psy'],
        ['pies', 'psy', 'psów', 'psami'],
        range(1, 10),
        list(range(1, 10))
    ])

    def test_bledny_zestawu_slow(self, w):
        with pytest.raises(ValueError):
            assert slownie.odmien(42, w)


class Test_Grupa():
    liczby_slownie = [
        (0, 'zero'),
        (1, 'jeden'),
        (2, 'dwa'),
        (3, 'trzy'),
        (4, 'cztery'),
        (5, 'pięć'),
        (9, 'dziewięć'),
        (10, 'dziesięć'),
        (11, 'jedenaście'),
        (12, 'dwanaście'),
        (13, 'trzynaście'),
        (19, 'dziewiętnaście'),
        (20, 'dwadzieścia'),
        (21, 'dwadzieścia jeden'),
        (22, 'dwadzieścia dwa'),
        (32, 'trzydzieści dwa'),
        (33, 'trzydzieści trzy'),
        (43, 'czterdzieści trzy'),
        (53, 'pięćdziesiąt trzy'),
        (99, 'dziewięćdziesiąt dziewięć'),
        (100, 'sto'),
        (200, 'dwieście'),
        (300, 'trzysta'),
        (400, 'czterysta'),
        (501, 'pięćset jeden'),
        (512, 'pięćset dwanaście'),
        (550, 'pięćset pięćdziesiąt'),
        (555, 'pięćset pięćdziesiąt pięć')
    ]

    @pytest.mark.parametrize('n,s', liczby_slownie)
    def test_jednostki(self, n, s):
        assert slownie.grupa(n) == s

    @pytest.mark.parametrize('n,s', liczby_slownie)
    def test_jednostki_z_pominieta_jedynka(self, n, s):
        assert slownie.grupa(n, True) == '' if n == 1 else s

    @pytest.mark.parametrize('n', [
        -1,
        -2,
        -100,
        1000,
        1001
    ])
    def test_wartosci_spoza_zakresu(self, n):
        with pytest.raises(ValueError):
            slownie.grupa(n)

    @pytest.mark.parametrize('n', [
        -2.5,
        "123",
        "qwe",
        [100]
    ])
    def test_wartosci_innych_typow(self, n):
        with pytest.raises(TypeError):
            slownie.grupa(n)


class Test_Liczba():
    import decimal
    import fractions

    D = decimal.Decimal
    F = fractions.Fraction

    liczby_slownie = [
        (0, 'zero'),
        (1, 'jeden'),
        (11, 'jedenaście'),
        (111, 'sto jedenaście'),
        (1000, 'tysiąc'),
        (1001, 'tysiąc jeden'),
        (1011, 'tysiąc jedenaście'),
        (1100, 'tysiąc sto'),
        (1111, 'tysiąc sto jedenaście'),
        (2000, 'dwa tysiące'),
        (2001, 'dwa tysiące jeden'),
        (2002, 'dwa tysiące dwa'),
        (2003, 'dwa tysiące trzy'),
        (2013, 'dwa tysiące trzynaście'),
        (5000, 'pięć tysięcy'),
        (6000, 'sześć tysięcy'),
        (6008, 'sześć tysięcy osiem'),
        (12000, 'dwanaście tysięcy'),
        (12001, 'dwanaście tysięcy jeden'),
        (12010, 'dwanaście tysięcy dziesięć'),
        (112033, 'sto dwanaście tysięcy trzydzieści trzy'),
        (1000000, 'milion'),
        (2000000, 'dwa miliony'),
        (3000007, 'trzy miliony siedem'),
        (4007000, 'cztery miliony siedem tysięcy'),
        (100e6, 'sto milionów'),
        (1e8, 'sto milionów'),
        (1e9, 'miliard'),
        (2e9, 'dwa miliardy'),
        (5e9, 'pięć miliardów'),
        (1e12, 'bilion')
    ]

    @pytest.mark.parametrize('n,s', liczby_slownie)
    def test_liczby(self, n, s):
        assert slownie.slownie(n) == s

    @pytest.mark.parametrize('n,s', ((-n, f"minus {s}") for (n, s) in liczby_slownie if n > 0))
    def test_liczby_ujemne(self, n, s):
        assert slownie.slownie(n) == s

    bledne_typy = [
        1234.5, [1234], "1234", "qwe",
        D(10) / D(3),
        F(10) / F(3),
        D(0.8) + D(0.2)
    ]

    @pytest.mark.parametrize('v', bledne_typy)
    def test_wartosci_innych_typow(self, v):
        with pytest.raises(TypeError):
            slownie.slownie(v)

    prawidlowe_typy = [
        4.0,
        4.5 * 2,
        D(10),
        D(10.0),
        D(10.25) * D(100),
        D('10.40') * D(10),
        F(100, 4),
        F(100) / F(5)
    ]

    @pytest.mark.parametrize('v', prawidlowe_typy)
    def test_wartosci_prawidlowych_typow(self, v):
        print(v, slownie.slownie(v))
        assert slownie.slownie(v)
