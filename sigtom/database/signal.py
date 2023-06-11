from influxdb_client import Point
import datetime


class SignalPoint:

    def __init__(self, _frequency: int, sdr: str) -> None:
        self.frequency = _frequency
        self.measurement = "signal"
        self.sdr = sdr # 
        self.start_time = datetime.datetime.now()
        self.payload = "test"


    def convert(self):
        base = Point("signal")
        base.tag("from", self.sdr)
        base.tag("frequency", self.frequency)
        base.field("payload", self.payload)
        base.time(str(self.start_time))
        return base