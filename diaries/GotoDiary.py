from diaries.AbstractDiary import AbstractDiary

class GotoDiary(AbstractDiary):
    def get_date (self):
        return "2023-12-14"
    
    def get_summary (self):
        return "グループ活動が始まった、頑張っていきたい"
    
    def get_author (self):
        return "後藤啓輔"