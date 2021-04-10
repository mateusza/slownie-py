#!/usr/bin/env python3

import pytest

import slownie

class Test_Odmien():
    odmiana_kota = ['kot', 'koty', 'kotów']

    odmiana_testy = [
        (0, odmiana_kota,'kotów'),
        (1, odmiana_kota,'kot'),
        (2, odmiana_kota,'koty'),
        (3, odmiana_kota,'koty'),
        (4, odmiana_kota,'koty'),
        (5, odmiana_kota,'kotów'),
        (6, odmiana_kota,'kotów'),
        (10, odmiana_kota,'kotów'),
        (11, odmiana_kota,'kotów'),
        (12, odmiana_kota,'kotów'),
        (13, odmiana_kota,'kotów'),
        (14, odmiana_kota,'kotów'),
        (19, odmiana_kota,'kotów'),
        (20, odmiana_kota,'kotów'),
        (21, odmiana_kota,'kotów'),
        (22, odmiana_kota,'koty'),
        (23, odmiana_kota,'koty'),
        (24, odmiana_kota,'koty'),
        (25, odmiana_kota,'kotów'),
        (29, odmiana_kota,'kotów'),
        (30, odmiana_kota,'kotów'),
        (31, odmiana_kota,'kotów'),
        (32, odmiana_kota,'koty'),
        (33, odmiana_kota,'koty'),
        (34, odmiana_kota,'koty'),
        (35, odmiana_kota,'kotów'),
        (39, odmiana_kota,'kotów'),
        (40, odmiana_kota,'kotów'),
        (41, odmiana_kota,'kotów'),
        (42, odmiana_kota,'koty'),
        (43, odmiana_kota,'koty'),
        (44, odmiana_kota,'koty'),
        (45, odmiana_kota,'kotów'),
        (49, odmiana_kota,'kotów'),
        (99, odmiana_kota,'kotów'),
        (100, odmiana_kota,'kotów'),
        (101, odmiana_kota,'kotów'),
        (102, odmiana_kota,'koty'),
        (103, odmiana_kota,'koty'),
        (105, odmiana_kota,'kotów'),
        (112, odmiana_kota,'kotów'),
        (115, odmiana_kota,'kotów'),
        (122, odmiana_kota,'koty'),
        (125, odmiana_kota,'kotów'),
        (200, odmiana_kota,'kotów'),
        (201, odmiana_kota,'kotów'),
        (202, odmiana_kota,'koty'),
        (203, odmiana_kota,'koty'),
        (205, odmiana_kota,'kotów'),
        (215, odmiana_kota,'kotów'),
        (222, odmiana_kota,'koty'),
        (905, odmiana_kota,'kotów')
    ]

    @pytest.mark.parametrize('n,o,s', odmiana_testy)
    def test_zakres_0_9(self, n, o, s):
        assert slownie.odmien(n, o) == s

    bledne_typy_wartosci = [
        'abc',
        'abcdef',
        1234,
        True,
        int,
        bool,
        {},
        set([1, 2, 34])
    ]

    @pytest.mark.parametrize('w', bledne_typy_wartosci)
    def test_bledny_typ_zestawu_slow(self, w):
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
    def test_bledny_typ_zestawu_slow(self, w):
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
        (400, 'czterysta')
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
    def test_zakres_0_999(self):
        assert slownie.slownie(0) == 'zero'
        assert slownie.slownie(1) == 'jeden'
        assert slownie.slownie(11) == 'jedenaście'
        assert slownie.slownie(111) == 'sto jedenaście'

    def test_zakres_1000_999999(self):
        assert slownie.slownie(1000) != 'jeden tysiąc'
        assert slownie.slownie(1000) == 'tysiąc'
        assert slownie.slownie(1001) == 'tysiąc jeden'
        assert slownie.slownie(1011) == 'tysiąc jedenaście'
        assert slownie.slownie(1100) == 'tysiąc sto'
        assert slownie.slownie(1111) == 'tysiąc sto jedenaście'
        assert slownie.slownie(2000) == 'dwa tysiące'
        assert slownie.slownie(2001) == 'dwa tysiące jeden'
        assert slownie.slownie(2002) == 'dwa tysiące dwa'
        assert slownie.slownie(2003) == 'dwa tysiące trzy'
        assert slownie.slownie(2013) == 'dwa tysiące trzynaście'
        assert slownie.slownie(5000) == 'pięć tysięcy'
        assert slownie.slownie(6000) == 'sześć tysięcy'
        assert slownie.slownie(6008) == 'sześć tysięcy osiem'
        assert slownie.slownie(12000) == 'dwanaście tysięcy'
        assert slownie.slownie(12001) == 'dwanaście tysięcy jeden'
        assert slownie.slownie(12010) == 'dwanaście tysięcy dziesięć'
        assert slownie.slownie(112033) == 'sto dwanaście tysięcy trzydzieści trzy'

    def test_ujemne(self):
        assert slownie.slownie(-1) == "minus jeden"
        assert slownie.slownie(-2) == "minus dwa"
        assert slownie.slownie(-10) == "minus dziesięć"
        assert slownie.slownie(-100) == "minus sto"
        assert slownie.slownie(-1000) == "minus tysiąc"

    def test_wartosci_innych_typow(self):
        from decimal import Decimal as D
        from fractions import Fraction as F

        with pytest.raises(TypeError):
            slownie.slownie(1234.5)
        with pytest.raises(TypeError):
            slownie.slownie([1234])
        with pytest.raises(TypeError):
            slownie.slownie("1234")
        with pytest.raises(TypeError):
            slownie.slownie("qwe")
        with pytest.raises(TypeError):
            slownie.slownie(D(10) / D(3))
        with pytest.raises(TypeError):
            slownie.slownie(F(10) / F(3))
        with pytest.raises(TypeError):
            slownie.slownie(D(0.8) + D(0.2))

        assert slownie.slownie(4.0)
        assert slownie.slownie(4.5 * 2)
        assert slownie.slownie(D(10))
        assert slownie.slownie(D(10.0))
        assert slownie.slownie(D(10.25) * D(100)) 
        assert slownie.slownie(D('10.40') * D(10)) 
        assert slownie.slownie(F(100, 4))
        assert slownie.slownie(F(100) / F(5)) 

