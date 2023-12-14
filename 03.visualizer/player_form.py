class PlayerForm:
    def __init__(self, list_form):
        self.__form = { \
            "부상":list_form[0],
            "체력":list_form[1],
            "경기력":list_form[2],
        }


    def getForm(self):
        return self.__form
