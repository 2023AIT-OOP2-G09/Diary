from diaries.AbstractDiary import AbstractDiary

class TakemotoDiary(AbstractDiary):
    def get_date(self):
        return "2023-12-28"
    def get_summary(self):
        return """もう冬だなと思いました。"""
    def get_author(self):
        return "Takemoto"