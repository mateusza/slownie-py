#!/usr/bin/env python3

import pytest

from slownie import Slownie

class Test_Odmien():
    odmiana = ['kot', 'koty', 'kotów']

    def test_zakres_0_9(self):
        assert Slownie.odmien(0, self.odmiana) == 'kotów'
        assert Slownie.odmien(1, self.odmiana) == 'kot'
        assert Slownie.odmien(2, self.odmiana) == 'koty'
        assert Slownie.odmien(3, self.odmiana) == 'koty'
        assert Slownie.odmien(4, self.odmiana) == 'koty'
        assert Slownie.odmien(5, self.odmiana) == 'kotów'
        assert Slownie.odmien(6, self.odmiana) == 'kotów'

    def test_zakres_10_19(self):
        assert Slownie.odmien(10, self.odmiana) == 'kotów'
        assert Slownie.odmien(11, self.odmiana) == 'kotów'
        assert Slownie.odmien(12, self.odmiana) == 'kotów'
        assert Slownie.odmien(13, self.odmiana) == 'kotów'
        assert Slownie.odmien(14, self.odmiana) == 'kotów'
        assert Slownie.odmien(19, self.odmiana) == 'kotów'

    def test_zakres_20_99(self):
        assert Slownie.odmien(20, self.odmiana) == 'kotów'
        assert Slownie.odmien(21, self.odmiana) == 'kotów'
        assert Slownie.odmien(22, self.odmiana) == 'koty'
        assert Slownie.odmien(23, self.odmiana) == 'koty'
        assert Slownie.odmien(24, self.odmiana) == 'koty'
        assert Slownie.odmien(25, self.odmiana) == 'kotów'
        assert Slownie.odmien(29, self.odmiana) == 'kotów'
        assert Slownie.odmien(30, self.odmiana) == 'kotów'
        assert Slownie.odmien(31, self.odmiana) == 'kotów'
        assert Slownie.odmien(32, self.odmiana) == 'koty'
        assert Slownie.odmien(33, self.odmiana) == 'koty'
        assert Slownie.odmien(34, self.odmiana) == 'koty'
        assert Slownie.odmien(35, self.odmiana) == 'kotów'
        assert Slownie.odmien(39, self.odmiana) == 'kotów'
        assert Slownie.odmien(40, self.odmiana) == 'kotów'
        assert Slownie.odmien(41, self.odmiana) == 'kotów'
        assert Slownie.odmien(42, self.odmiana) == 'koty'
        assert Slownie.odmien(43, self.odmiana) == 'koty'
        assert Slownie.odmien(44, self.odmiana) == 'koty'
        assert Slownie.odmien(45, self.odmiana) == 'kotów'
        assert Slownie.odmien(49, self.odmiana) == 'kotów'
        assert Slownie.odmien(99, self.odmiana) == 'kotów'

    def test_zakres_100_199(self):
        assert Slownie.odmien(100, self.odmiana) == 'kotów'
        assert Slownie.odmien(101, self.odmiana) == 'kotów'
        assert Slownie.odmien(102, self.odmiana) == 'koty'
        assert Slownie.odmien(103, self.odmiana) == 'koty'
        assert Slownie.odmien(105, self.odmiana) == 'kotów'
        assert Slownie.odmien(112, self.odmiana) == 'kotów'
        assert Slownie.odmien(115, self.odmiana) == 'kotów'
        assert Slownie.odmien(122, self.odmiana) == 'koty'
        assert Slownie.odmien(125, self.odmiana) == 'kotów'

    def test_zakres_od_200(self):
        assert Slownie.odmien(200, self.odmiana) == 'kotów'
        assert Slownie.odmien(201, self.odmiana) == 'kotów'
        assert Slownie.odmien(202, self.odmiana) == 'koty'
        assert Slownie.odmien(203, self.odmiana) == 'koty'
        assert Slownie.odmien(205, self.odmiana) == 'kotów'
        assert Slownie.odmien(215, self.odmiana) == 'kotów'
        assert Slownie.odmien(222, self.odmiana) == 'koty'
        assert Slownie.odmien(905, self.odmiana) == 'kotów'

    def test_str_zamiast_zestawu_slow(self):
        with pytest.raises(TypeError):
            assert Slownie.odmien(1, 'abc')
        with pytest.raises(TypeError):
            assert Slownie.odmien(1, 'abcdef')

    def test_inny_typ_zamiast_zestawu_slow(self):
        assert Slownie.odmien(7, ('mysz', 'myszy', 'myszy'))
        assert Slownie.odmien(9, 'dom domy domów'.split())

        with pytest.raises(TypeError):
            assert Slownie.odmien(1, 1234)
        with pytest.raises(TypeError):
            assert Slownie.odmien(1, bool)

    def test_za_krotki_zestaw_slow(self):

        with pytest.raises(ValueError):
            assert Slownie.odmien(1, [])
        with pytest.raises(ValueError):
            assert Slownie.odmien(1, ['pies'])
        with pytest.raises(ValueError):
            assert Slownie.odmien(1, ['pies', 'psy'])

    def test_za_dlugi_zestaw_slow(self):
        with pytest.raises(ValueError):
            assert Slownie.odmien(1, ['pies', 'psy', 'psów', 'psami'])
        with pytest.raises(ValueError):
            assert Slownie.odmien(1, range(1,10))

class Test_Grupa():
    def test_jednostki(self):
        assert Slownie.grupa(0) == 'zero'
        assert Slownie.grupa(1) == 'jeden'
        assert Slownie.grupa(2) == 'dwa'
        assert Slownie.grupa(3) == 'trzy'
        assert Slownie.grupa(4) == 'cztery'
        assert Slownie.grupa(5) == 'pięć'
        assert Slownie.grupa(9) == 'dziewięć'

    def test_jednostki_z_pominietym_zerem(self):
        assert Slownie.grupa(0, False) == ''
        assert Slownie.grupa(1, False) == 'jeden'
        assert Slownie.grupa(2, False) == 'dwa'
        assert Slownie.grupa(8, False) == 'osiem'

    def test_jednostki_z_pominietym_zerem_i_jedynka(self):
        assert Slownie.grupa(0, False, True) == ''
        assert Slownie.grupa(1, False, True) == ''
        assert Slownie.grupa(2, False, True) == 'dwa'

    def test_zakres_10_20(self):
        assert Slownie.grupa(10) == 'dziesięć'
        assert Slownie.grupa(11) == 'jedenaście'
        assert Slownie.grupa(12) == 'dwanaście'
        assert Slownie.grupa(13) == 'trzynaście'
        assert Slownie.grupa(19) == 'dziewiętnaście'
        assert Slownie.grupa(20) != 'dziesiętnaście'

    def test_zakres_20_99(self):
        assert Slownie.grupa(20) == 'dwadzieścia'
        assert Slownie.grupa(21) == 'dwadzieścia jeden'
        assert Slownie.grupa(22) == 'dwadzieścia dwa'
        assert Slownie.grupa(32) == 'trzydzieści dwa'
        assert Slownie.grupa(33) == 'trzydzieści trzy'
        assert Slownie.grupa(43) == 'czterdzieści trzy'
        assert Slownie.grupa(53) == 'pięćdziesiąt trzy'
        assert Slownie.grupa(99) == 'dziewięćdziesiąt dziewięć'

    def test_setki(self):
        assert Slownie.grupa(100) == 'sto'
        assert Slownie.grupa(200) == 'dwieście'
        assert Slownie.grupa(300) == 'trzysta'
        assert Slownie.grupa(400) == 'czterysta'

    def test_wartosci_spoza_zakresu(self):
        assert Slownie.grupa(0)
        assert Slownie.grupa(1)
        assert Slownie.grupa(999)

        with pytest.raises(ValueError):
            Slownie.grupa(-1)
        with pytest.raises(ValueError):
            Slownie.grupa(-2)
        with pytest.raises(ValueError):
            Slownie.grupa(-100)
        with pytest.raises(ValueError):
            Slownie.grupa(1000)
        with pytest.raises(ValueError):
            Slownie.grupa(1002)
        with pytest.raises(ValueError):
            Slownie.grupa(1000000)

    def test_wartosci_innych_typow(self):
        with pytest.raises(TypeError):
            Slownie.grupa(-2.5)
        with pytest.raises(TypeError):
            Slownie.grupa("123")
        with pytest.raises(TypeError):
            Slownie.grupa("qwe")
        with pytest.raises(TypeError):
            Slownie.grupa([100])

class Test_Liczba():
    def test_zakres_0_999(self):
        assert Slownie.liczba(0) == 'zero'
        assert Slownie.liczba(1) == 'jeden'
        assert Slownie.liczba(11) == 'jedenaście'
        assert Slownie.liczba(111) == 'sto jedenaście'

    def test_zakres_1000_999999(self):
        assert Slownie.liczba(1000) != 'jeden tysiąc'
        assert Slownie.liczba(1000) == 'tysiąc'
        assert Slownie.liczba(1001) == 'tysiąc jeden'
        assert Slownie.liczba(1011) == 'tysiąc jedenaście'
        assert Slownie.liczba(1100) == 'tysiąc sto'
        assert Slownie.liczba(1111) == 'tysiąc sto jedenaście'
        assert Slownie.liczba(2000) == 'dwa tysiące'
        assert Slownie.liczba(2001) == 'dwa tysiące jeden'
        assert Slownie.liczba(2002) == 'dwa tysiące dwa'
        assert Slownie.liczba(2003) == 'dwa tysiące trzy'
        assert Slownie.liczba(2013) == 'dwa tysiące trzynaście'
        assert Slownie.liczba(5000) == 'pięć tysięcy'
        assert Slownie.liczba(6000) == 'sześć tysięcy'
        assert Slownie.liczba(6008) == 'sześć tysięcy osiem'
        assert Slownie.liczba(12000) == 'dwanaście tysięcy'
        assert Slownie.liczba(12001) == 'dwanaście tysięcy jeden'
        assert Slownie.liczba(12010) == 'dwanaście tysięcy dziesięć'
        assert Slownie.liczba(112033) == 'sto dwanaście tysięcy trzydzieści trzy'

    def test_ujemne(self):
        assert Slownie.liczba(-1) == "minus jeden"
        assert Slownie.liczba(-2) == "minus dwa"
        assert Slownie.liczba(-10) == "minus dziesięć"
        assert Slownie.liczba(-100) == "minus sto"
        assert Slownie.liczba(-1000) == "minus tysiąc"

    def test_wartosci_innych_typow(self):
        from decimal import Decimal as D
        from fractions import Fraction as F

        with pytest.raises(TypeError):
            Slownie.liczba(1234.5)
        with pytest.raises(TypeError):
            Slownie.liczba([1234])
        with pytest.raises(TypeError):
            Slownie.liczba("1234")
        with pytest.raises(TypeError):
            Slownie.liczba("qwe")
        with pytest.raises(TypeError):
            Slownie.liczba(D(10) / D(3))
        with pytest.raises(TypeError):
            Slownie.liczba(F(10) / F(3))
        with pytest.raises(TypeError):
            Slownie.liczba(D(0.8) + D(0.2))

        assert Slownie.liczba(4.0)
        assert Slownie.liczba(4.5 * 2)
        assert Slownie.liczba(D(10))
        assert Slownie.liczba(D(10.0))
        assert Slownie.liczba(D(10.25) * D(100)) 
        assert Slownie.liczba(D('10.40') * D(10)) 
        assert Slownie.liczba(F(100, 4))
        assert Slownie.liczba(F(100) / F(5)) 

