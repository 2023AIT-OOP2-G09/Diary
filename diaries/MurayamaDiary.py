from diaries.AbstractDiary import AbstractDiary

class MurayamaDiary (AbstractDiary):
    def get_date (self):
        return "2023-12-14"
    
    def get_summary (self):
        return "GitHubの使い方は簡単だと思ったけど大人数での作業が苦手だから徐々に慣れていける様頑張りたい"
    
    def get_author (self):
        return "Murayama"