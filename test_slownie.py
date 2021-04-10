#!/usr/bin/env python3

import pytest

import slownie

class Test_Odmien():
    odmiana = ['kot', 'koty', 'kotów']

    def test_zakres_0_9(self):
        assert slownie.odmien(0, self.odmiana) == 'kotów'
        assert slownie.odmien(1, self.odmiana) == 'kot'
        assert slownie.odmien(2, self.odmiana) == 'koty'
        assert slownie.odmien(3, self.odmiana) == 'koty'
        assert slownie.odmien(4, self.odmiana) == 'koty'
        assert slownie.odmien(5, self.odmiana) == 'kotów'
        assert slownie.odmien(6, self.odmiana) == 'kotów'

    def test_zakres_10_19(self):
        assert slownie.odmien(10, self.odmiana) == 'kotów'
        assert slownie.odmien(11, self.odmiana) == 'kotów'
        assert slownie.odmien(12, self.odmiana) == 'kotów'
        assert slownie.odmien(13, self.odmiana) == 'kotów'
        assert slownie.odmien(14, self.odmiana) == 'kotów'
        assert slownie.odmien(19, self.odmiana) == 'kotów'

    def test_zakres_20_99(self):
        assert slownie.odmien(20, self.odmiana) == 'kotów'
        assert slownie.odmien(21, self.odmiana) == 'kotów'
        assert slownie.odmien(22, self.odmiana) == 'koty'
        assert slownie.odmien(23, self.odmiana) == 'koty'
        assert slownie.odmien(24, self.odmiana) == 'koty'
        assert slownie.odmien(25, self.odmiana) == 'kotów'
        assert slownie.odmien(29, self.odmiana) == 'kotów'
        assert slownie.odmien(30, self.odmiana) == 'kotów'
        assert slownie.odmien(31, self.odmiana) == 'kotów'
        assert slownie.odmien(32, self.odmiana) == 'koty'
        assert slownie.odmien(33, self.odmiana) == 'koty'
        assert slownie.odmien(34, self.odmiana) == 'koty'
        assert slownie.odmien(35, self.odmiana) == 'kotów'
        assert slownie.odmien(39, self.odmiana) == 'kotów'
        assert slownie.odmien(40, self.odmiana) == 'kotów'
        assert slownie.odmien(41, self.odmiana) == 'kotów'
        assert slownie.odmien(42, self.odmiana) == 'koty'
        assert slownie.odmien(43, self.odmiana) == 'koty'
        assert slownie.odmien(44, self.odmiana) == 'koty'
        assert slownie.odmien(45, self.odmiana) == 'kotów'
        assert slownie.odmien(49, self.odmiana) == 'kotów'
        assert slownie.odmien(99, self.odmiana) == 'kotów'

    def test_zakres_100_199(self):
        assert slownie.odmien(100, self.odmiana) == 'kotów'
        assert slownie.odmien(101, self.odmiana) == 'kotów'
        assert slownie.odmien(102, self.odmiana) == 'koty'
        assert slownie.odmien(103, self.odmiana) == 'koty'
        assert slownie.odmien(105, self.odmiana) == 'kotów'
        assert slownie.odmien(112, self.odmiana) == 'kotów'
        assert slownie.odmien(115, self.odmiana) == 'kotów'
        assert slownie.odmien(122, self.odmiana) == 'koty'
        assert slownie.odmien(125, self.odmiana) == 'kotów'

    def test_zakres_od_200(self):
        assert slownie.odmien(200, self.odmiana) == 'kotów'
        assert slownie.odmien(201, self.odmiana) == 'kotów'
        assert slownie.odmien(202, self.odmiana) == 'koty'
        assert slownie.odmien(203, self.odmiana) == 'koty'
        assert slownie.odmien(205, self.odmiana) == 'kotów'
        assert slownie.odmien(215, self.odmiana) == 'kotów'
        assert slownie.odmien(222, self.odmiana) == 'koty'
        assert slownie.odmien(905, self.odmiana) == 'kotów'

    def test_str_zamiast_zestawu_slow(self):
        with pytest.raises(TypeError):
            assert slownie.odmien(1, 'abc')
        with pytest.raises(TypeError):
            assert slownie.odmien(1, 'abcdef')

    def test_inny_typ_zamiast_zestawu_slow(self):
        assert slownie.odmien(7, ('mysz', 'myszy', 'myszy'))
        assert slownie.odmien(9, 'dom domy domów'.split())

        with pytest.raises(TypeError):
            assert slownie.odmien(1, 1234)
        with pytest.raises(TypeError):
            assert slownie.odmien(1, bool)

    def test_za_krotki_zestaw_slow(self):

        with pytest.raises(ValueError):
            assert slownie.odmien(1, [])
        with pytest.raises(ValueError):
            assert slownie.odmien(1, ['pies'])
        with pytest.raises(ValueError):
            assert slownie.odmien(1, ['pies', 'psy'])

    def test_za_dlugi_zestaw_slow(self):
        with pytest.raises(ValueError):
            assert slownie.odmien(1, ['pies', 'psy', 'psów', 'psami'])
        with pytest.raises(ValueError):
            assert slownie.odmien(1, range(1,10))

class Test_Grupa():
    def test_jednostki(self):
        assert slownie.grupa(0) == 'zero'
        assert slownie.grupa(1) == 'jeden'
        assert slownie.grupa(2) == 'dwa'
        assert slownie.grupa(3) == 'trzy'
        assert slownie.grupa(4) == 'cztery'
        assert slownie.grupa(5) == 'pięć'
        assert slownie.grupa(9) == 'dziewięć'

    def test_jednostki_z_pominietym_zerem(self):
        assert slownie.grupa(0, False) == ''
        assert slownie.grupa(1, False) == 'jeden'
        assert slownie.grupa(2, False) == 'dwa'
        assert slownie.grupa(8, False) == 'osiem'

    def test_jednostki_z_pominietym_zerem_i_jedynka(self):
        assert slownie.grupa(0, False, True) == ''
        assert slownie.grupa(1, False, True) == ''
        assert slownie.grupa(2, False, True) == 'dwa'

    def test_zakres_10_20(self):
        assert slownie.grupa(10) == 'dziesięć'
        assert slownie.grupa(11) == 'jedenaście'
        assert slownie.grupa(12) == 'dwanaście'
        assert slownie.grupa(13) == 'trzynaście'
        assert slownie.grupa(19) == 'dziewiętnaście'
        assert slownie.grupa(20) != 'dziesiętnaście'

    def test_zakres_20_99(self):
        assert slownie.grupa(20) == 'dwadzieścia'
        assert slownie.grupa(21) == 'dwadzieścia jeden'
        assert slownie.grupa(22) == 'dwadzieścia dwa'
        assert slownie.grupa(32) == 'trzydzieści dwa'
        assert slownie.grupa(33) == 'trzydzieści trzy'
        assert slownie.grupa(43) == 'czterdzieści trzy'
        assert slownie.grupa(53) == 'pięćdziesiąt trzy'
        assert slownie.grupa(99) == 'dziewięćdziesiąt dziewięć'

    def test_setki(self):
        assert slownie.grupa(100) == 'sto'
        assert slownie.grupa(200) == 'dwieście'
        assert slownie.grupa(300) == 'trzysta'
        assert slownie.grupa(400) == 'czterysta'

    def test_wartosci_spoza_zakresu(self):
        assert slownie.grupa(0)
        assert slownie.grupa(1)
        assert slownie.grupa(999)

        with pytest.raises(ValueError):
            slownie.grupa(-1)
        with pytest.raises(ValueError):
            slownie.grupa(-2)
        with pytest.raises(ValueError):
            slownie.grupa(-100)
        with pytest.raises(ValueError):
            slownie.grupa(1000)
        with pytest.raises(ValueError):
            slownie.grupa(1002)
        with pytest.raises(ValueError):
            slownie.grupa(1000000)

    def test_wartosci_innych_typow(self):
        with pytest.raises(TypeError):
            slownie.grupa(-2.5)
        with pytest.raises(TypeError):
            slownie.grupa("123")
        with pytest.raises(TypeError):
            slownie.grupa("qwe")
        with pytest.raises(TypeError):
            slownie.grupa([100])

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

