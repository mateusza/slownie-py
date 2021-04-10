#!/usr/bin/env python3

import pytest

import slownie


class Test_Odmien():
    odmiana_kota = ['kot', 'koty', 'kotów']

    odmiana_testy = [
        (0, odmiana_kota, 'kotów'),
        (1, odmiana_kota, 'kot'),
        (2, odmiana_kota, 'koty'),
        (3, odmiana_kota, 'koty'),
        (4, odmiana_kota, 'koty'),
        (5, odmiana_kota, 'kotów'),
        (6, odmiana_kota, 'kotów'),
        (10, odmiana_kota, 'kotów'),
        (11, odmiana_kota, 'kotów'),
        (12, odmiana_kota, 'kotów'),
        (13, odmiana_kota, 'kotów'),
        (14, odmiana_kota, 'kotów'),
        (19, odmiana_kota, 'kotów'),
        (20, odmiana_kota, 'kotów'),
        (21, odmiana_kota, 'kotów'),
        (22, odmiana_kota, 'koty'),
        (23, odmiana_kota, 'koty'),
        (24, odmiana_kota, 'koty'),
        (25, odmiana_kota, 'kotów'),
        (29, odmiana_kota, 'kotów'),
        (30, odmiana_kota, 'kotów'),
        (31, odmiana_kota, 'kotów'),
        (32, odmiana_kota, 'koty'),
        (33, odmiana_kota, 'koty'),
        (34, odmiana_kota, 'koty'),
        (35, odmiana_kota, 'kotów'),
        (39, odmiana_kota, 'kotów'),
        (40, odmiana_kota, 'kotów'),
        (41, odmiana_kota, 'kotów'),
        (42, odmiana_kota, 'koty'),
        (43, odmiana_kota, 'koty'),
        (44, odmiana_kota, 'koty'),
        (45, odmiana_kota, 'kotów'),
        (49, odmiana_kota, 'kotów'),
        (99, odmiana_kota, 'kotów'),
        (100, odmiana_kota, 'kotów'),
        (101, odmiana_kota, 'kotów'),
        (102, odmiana_kota, 'koty'),
        (103, odmiana_kota, 'koty'),
        (105, odmiana_kota, 'kotów'),
        (112, odmiana_kota, 'kotów'),
        (115, odmiana_kota, 'kotów'),
        (122, odmiana_kota, 'koty'),
        (125, odmiana_kota, 'kotów'),
        (200, odmiana_kota, 'kotów'),
        (201, odmiana_kota, 'kotów'),
        (202, odmiana_kota, 'koty'),
        (203, odmiana_kota, 'koty'),
        (205, odmiana_kota, 'kotów'),
        (215, odmiana_kota, 'kotów'),
        (222, odmiana_kota, 'koty'),
        (905, odmiana_kota, 'kotów')
    ]

    @pytest.mark.parametrize('n,o,s', odmiana_testy)
    def test_zakres_0_9(self, n, o, s):
        print(f"{n} {slownie.odmien(n, o)} vs {s}")
        assert slownie.odmien(n, o) == s

    bledne_typy_wartosci = [
        'abc',
        'abcdef',
        1234,
        True,
        int,
        bool
    ]

    @pytest.mark.parametrize('w', bledne_typy_wartosci)
    def test_bledny_typ_zestawu_slow(self, w):
        print(f"Odmieniam: {repr(w)}")
        with pytest.raises(TypeError):
            assert slownie.odmien(42, w)

    prawidlowe_wartosci = [
        ('mysz', 'myszy', 'myszy'),
        'dom domy domów'.split(),
        (f'dom{x}' for x in ('', 'y', 'ów'))
    ]

    @pytest.mark.parametrize('w', prawidlowe_wartosci)
    def test_prawidlowy_typ_zestawu_slow(self, w):
        assert slownie.odmien(7, w)

    bledne_wartosci = [
        [],
        ['pies'],
        ['pies', 'psy'],
        ['pies', 'psy', 'psów', 'psami'],
        range(1, 10),
        list(range(1, 10))
    ]

    @pytest.mark.parametrize('w', bledne_wartosci)
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

    liczby_spoza_zakresu = [
        -1,
        -2,
        -100,
        1000,
        1001
    ]

    @pytest.mark.parametrize('n', liczby_spoza_zakresu)
    def test_wartosci_spoza_zakresu(self, n):
        with pytest.raises(ValueError):
            slownie.grupa(n)

    liczby_zlych_typow = [
        -2.5,
        "123",
        "qwe",
        [100]
    ]

    @pytest.mark.parametrize('n', liczby_zlych_typow)
    def test_wartosci_innych_typow(sel, n):
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

