from mycroft import MycroftSkill, intent_file_handler


class Relationshiptoplessey(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('relationshiptoplessey.intent')
    def handle_relationshiptoplessey(self, message):
        self.speak_dialog('relationshiptoplessey')


def create_skill():
    return Relationshiptoplessey()

