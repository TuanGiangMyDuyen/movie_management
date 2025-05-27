from datetime import datetime, timedelta

class CalculateEndTime:

    @staticmethod
    def calculate_end_time(start_time, duration_minutes):
        start_hour, start_minute = map(int, start_time.split(":"))
        start_dt = datetime.strptime(f"{start_hour:02d}:{start_minute:02d}", "%H:%M")
        end_dt = start_dt + timedelta(minutes=duration_minutes)
        return {'start_time': start_time,"end_time": end_dt.strftime("%H:%M")}