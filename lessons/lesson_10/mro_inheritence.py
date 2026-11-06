class Artist(object):
    def perform(self):
        print("Going a stage...")


class Singer(Artist):
    def perform(self):
        super().perform()
        print("Singing...")



class Guitarist(Artist):
    def perform(self):
        super().perform()
        print("Playing a guitar...")


class RockStar(Singer, Guitarist):
    def perform(self):
        super().perform()
        print("Drinking....")


# singer = Singer()
#
# singer.perform()


rock_star = RockStar()
rock_star.perform()

print(RockStar.mro())