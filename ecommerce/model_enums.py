from enum import Enum


class DepartmentEnum(Enum):
    COMPS = 0
    IT = 1
    ELEX = 2
    EXTC = 3
    MECH = 4
    PROD = 5
    BIO = 6
    CIV = 7
    INST = 8
    CHEM = 9
    AGRI = 10

    @staticmethod
    def get_choices():
        return [m for m in DepartmentEnum]
