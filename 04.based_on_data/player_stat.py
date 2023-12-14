class PlayerStat:
    def __init__(self, list_stat):
        self.stat = { \
            "경기수":list_stat[0],
            "골":list_stat[1],
            "도움":list_stat[2],
            "실점":list_stat[3],
            "경고":list_stat[4],
            "퇴장":list_stat[5],
            "평균평점":list_stat[6],
            "MOM":list_stat[7],
        }

    def getStat(self):
        return self.stat
