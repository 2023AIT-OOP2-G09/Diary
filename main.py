from diaries.DiarySample import DiarySample
from diaries.ReoDiary import ReoDiary
from diaries.FujitaDiary import FujitaDiary
from diaries.TakemotoDiary import TakemotoDiary
from diaries.shibataDiary import shibataDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
    DiarySample(),
    TakemotoDiary(),
    FujitaDiary(),
    ReoDiary(),
    shibataDiary(),
]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()