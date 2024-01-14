from datetime import datetime, timedelta
    
class date:
    def __init__(self, date_str,format_date):
        self.date = datetime.strptime(date_str,format_date)
    #下一天的日期
    def get_next_day(self,output_format):
        next_day = self.date + timedelta(days=1)
        self.date=next_day
        return next_day.strftime(output_format)