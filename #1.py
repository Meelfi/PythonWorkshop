class Human:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        print("Human With name {} {} born. Let's celebrate!".format(self.firstname, self.lastname))

    def __del__(self):
        print("Human with name {} {} RIP.".format(self.firstname, self.lastname))
        self.firstname = ""
        self.lastname = ""


igor = Human("Igor", "Kk")


class Programmer(Human):
    def __init__(self, firstname, lastname, programming_language):
        super(Programmer, self).__init__(firstname, lastname)
        print("There is nothink to celebrate. It's just programmer.")
        self.programming_language = programming_language

    def __del__(self):
        print("How sad. This guy just create Facebook")
        self.programming_language = ""


class Singer(Human):
    def __init__(self, firstname, lastname, song_type):
        super(Singer, self).__init__(firstname, lastname)
        print("This guy like music")
        self.song_type = song_type

    def __del__(self):
        print("He just sleep")
        self.song_type = ""


mark = Programmer("Mark", "Zuckerberg", "PHP")
alec = Singer("Alec", "Benjamin", "POP")
