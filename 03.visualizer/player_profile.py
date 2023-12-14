class PlayerProfile:
    def __init__(self, list_profile):
        self.__profile = { \
            "이름":list_profile[0],
            "포지션":list_profile[1],
            "국적":list_profile[2],
            "신장":list_profile[3],
            "체중":list_profile[4],
            "나이":list_profile[5],
        }

    def getProfile(self):
        return self.__profile
