from diaries.AbstractDiary import AbstractDiary

class FujitaDiary (AbstractDiary):
    def get_date (self):
        return "2020-12-14"
    
    def get_summary (self):
        return "頑張った"
    
    def get_author (self):
        return "Fujita"