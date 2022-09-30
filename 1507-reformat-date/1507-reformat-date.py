class Solution:
    def reformatDate(self, date: str) -> str:
        MONTH_MAP = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        day, month, year = date.split(' ')
        
        def convertMonth(month):
            month_int = MONTH_MAP.index(month) + 1
            return '0' + str(month_int) if month_int < 10 else str(month_int)
        
        def convertDay(day):
            return day[:-2] if len(day[:-2]) == 2 else '0' + day[:-2]
        
        return (str(year) + '-' + convertMonth(month) + '-' + convertDay(day))