from datetime import datetime, timezone, timedelta

class DateTimeUtil:

    @staticmethod
    def getTimeZoneSaoPaulo() -> timezone:
        return DateTimeUtil.getTimeZoneBrazil(nameTimeZone="America/Sao_Paulo")

    @staticmethod
    def getTimeZoneBrazil(gmt: int = -3, nameTimeZone: str = None) -> timezone:
        return timezone(offset=timedelta(hours=gmt), name=nameTimeZone)

    """
    Conversor DataHota: https://www.strerr.com/pt/timestamp.html
    DateTimeUtil.parseToDateTime(mseconds=1693827585000, tz=DateTimeUtil.getTimeZoneSaoPaulo())
    """
    @staticmethod
    def parseToDateTime(mseconds: int, tz: timezone = None) -> datetime:
        tz = DateTimeUtil.getTimeZoneSaoPaulo() if tz is None else tz
        return datetime.fromtimestamp(mseconds/1000, tz=tz)
