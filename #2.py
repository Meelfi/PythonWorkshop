class Games:
    def __init__(self):
        print("Creating Games")

    def install(self):
        print("Please Wait game was install")

    def succes(self):
        print("Succes")


games = Games()
games.install()
games.succes()


class PCGame(Games):
    def __init__(self):
        print("Adding PC Game")

    def install(self):
        print("Install on PC")


class AndroidGame(Games):
    def __init__(self):
        print("Adding Android Game")

    def install(self):
        print("Install on Android")

    def failed(self):
        print("Failed")


pc_game = PCGame()
android_game = AndroidGame()

pc_game.install()
android_game.install()

pc_game.succes()
android_game.failed()
