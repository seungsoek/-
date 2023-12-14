class PlayerAbility:
    def __init__(self, list_ability):
        self.__ability = { \
            "테크닉":{\
                "개인기":list_ability[0][0],
                "드리블":list_ability[0][1],
                "골결정력":list_ability[0][2],
                "일대일마크":list_ability[0][3],
                "던지기":list_ability[0][4],
                "중장거리슛":list_ability[0][5],
                "코너킥":list_ability[0][6],
                "크로스":list_ability[0][7],
                "태클":list_ability[0][8],
                "패스":list_ability[0][9],
                "퍼스트터치":list_ability[0][10],
                "페널티킥":list_ability[0][11],
                "프리킥":list_ability[0][12],
                "헤더":list_ability[0][13],
                },
            "멘탈":{ \
                "오프더볼":list_ability[1][0],
                "대담성":list_ability[1][1],
                "리더십":list_ability[1][2],
                "승부욕":list_ability[1][3],
                "시야":list_ability[1][4],
                "예측력":list_ability[1][5],
                "적극성":list_ability[1][6],
                "집중력":list_ability[1][7],
                "천재성":list_ability[1][8],
                "침착성":list_ability[1][9],
                "팀워크":list_ability[1][10],
                "판단력":list_ability[1][11],
                "활동량":list_ability[1][12],
                "위치선정":list_ability[1][13],
                },
            "피지컬":{ \
                "밸런스":list_ability[2][0],
                "몸싸움":list_ability[2][1],
                "민첩성":list_ability[2][2],
                "순간속도":list_ability[2][3],
                "스피드":list_ability[2][4],
                "지구력":list_ability[2][5],
                "신체강건성":list_ability[2][6],
                "점프력":list_ability[2][7],
            },
            "골키퍼능력":{ \
                "골킥":list_ability[3][0],
                "공중장악력":list_ability[3][1],
                "기행":list_ability[3][2],
                "돌진":list_ability[3][3],
                "반사신경":list_ability[3][4],
                "볼핸들링":list_ability[3][5],
                "펀칭":list_ability[3][6],
                "페널티박스장악력":list_ability[3][7],
                "수비조율":list_ability[3][8],
                },
            "잠재력":list_ability[4],
        }

    def getAbility(self):
        return self.__abiliity
    def getTechnical(self):
        return self.__ability["테크닉"]
    def getMental(self):
        return self.__ability["멘탈"]
    def getPhysical(self):
        return self.__ability["피지컬"]
    def getGoalkeeping(self):
        return self.__ability["골키퍼능력"]
    def getPotential(self):
        return self.__ability["잠재력"]

    def setTechnical(self, key, val):
        if key in self.__ability["테크닉"]:
            if val >= 0 and val <= 99:
                self.__ability["테크닉"][key] = val
    def setMental(self, key, val):
        if key in self.__ability["멘탈"]:
            if val >= 0 and val <= 99:
                self.__ability["멘탈"][key] = val
    def setPhysical(self, key, val):
        if key in self.__ability["피지컬"]:
            if val >= 0 and val <= 99:
                self.__ability["피지컬"][key] = val
    def setGoalKeeping(self, key, val):
        if key in self.__ability["골키퍼능력"]:
            if val >= 0 and val <= 99:
                self.__ability["골키퍼능력"][key] = val
    def setPotential(self, val):
        if val >= 0 and val <= 99:
            self.__ability["잠재력"] = val
