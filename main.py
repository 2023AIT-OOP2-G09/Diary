from diaries.DiarySample import DiarySample
from diaries.GotoDiary import GotoDiary
from diaries.ShibataToa import ShibataToaDiary
from diaries.ReoDiary import ReoDiary
from diaries.FujitaDiary import FujitaDiary
from diaries.TakemotoDiary import TakemotoDiary
from diaries.shibataDiary import shibataDiary
from diaries.MurayamaDiary import MurayamaDiary

diaries = [
    DiarySample(),
    TakemotoDiary(),
    FujitaDiary(),
    ReoDiary(),
    shibataDiary(),
    MurayamaDiary(),
    ShibataToaDiary(),
    GotoDiary(),
]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
