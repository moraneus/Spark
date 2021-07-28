from tests.test_monitor import *
from frontend.parser import parse


class TestTranslation:
    def test1(self):
        specification = parse("""!exist B1, B2, D . B1("BOOT") & B2("BOOT") & D("DL_IMAGE") & B1 < B2 & (B1 i D | B2 i D | (B1 < D & D < B2) | (B1 o D & !D i B2) | (D o B2 & !D i B1))""")
        dejavu = specification.translate()
        print(dejavu)

    def test2(self):
        specification = parse("""!exist D, F . (D("DL_MOBPRM") | D("DL_ARMPRM")) & F("DL_FAIL") & D i F""")
        dejavu = specification.translate()
        print(dejavu)

    def test3(self):
        specification = parse("""!exist O, F, R . O("INS_ON") & F("INS_FAIL") & R("INS_RECOVER") & O < F & F < R & !exist X . (X("INS_ON") | X("INS_RECOVER")) & O < X & X < R""")
        dejavu = specification.translate()
        print(dejavu)

    def test4(self):
        specification = parse("""!exist D, G, S . D("DL_IMAGE") & G("GET_CAMDATA") & S("STARVE") & D i S & G i S""")
        dejavu = specification.translate()
        print(dejavu)


test = TestTranslation()

test.test1()
test.test2()
test.test3()
test.test4()



