import schedule


class ScheduleService:

    @staticmethod
    def call_by_minutes(min: int, callables: callable) -> None:
        """
            Task scheduling
            After every 10mins geeks() is called.     
        """
        schedule.every(min).minutes.do(callables)

    # After every hour geeks() is called.
    @staticmethod
    def call_by_hour(callables: callable) -> None:
        schedule.every().hour.do(callables)

    # Every day at 12am or 00:00 time bedtime() is called.
    @staticmethod
    def call_by_day_at_time(time: str, callables: callable) -> None:
        schedule.every().day.at(time).do(callables)

    @staticmethod
    def run_pending() -> None:
        schedule.run_pending()

    # After every 5 to 10mins in between run work()
    # schedule.every(5).to(10).minutes.do(work)

    # Every monday good_luck() is called
    # schedule.every().monday.do(good_luck)

    # Every tuesday at 18:00 sudo_placement() is called
    # schedule.every().tuesday.at("18:00").do(sudo_placement)
