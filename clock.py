from datetime import datetime

class PartOfDay(Enum):
    MORNING = 'morning'
    AFTERNOON = 'afternoon'
    EVENING = 'evening'

class Clock:
    def __init__(self):
        return
    
    @staticmethod
    def get_hour():
        return datetime.now().hour
    
    @staticmethod
    def what_part_of_day(hour):
        if 6 <= hour < 12:
            return PartOfDay.MORNING
        elif 12 <= hour < 18:
            return PartOfDay.AFTERNOON
        else:
            return PartOfDay.EVENING