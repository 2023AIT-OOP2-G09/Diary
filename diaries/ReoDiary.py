from diaries.AbstractDiary import AbstractDiary
class ReoDiary(AbstractDiary):
    def get_date(self):
        return "2023-12-13"
    def get_summary(self):
        return """今日は寒かった。バイトもないから、はやく家に帰りたい。"""
    def get_author(self):
        return "Reo"