class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self):
        if not self.__status:
            self.__status = True
        else:
            self.__status = False

    def mute(self):
        if self.__status:
            self.__muted = not self.__muted
            if self.__muted:
                self.__volume = Television.MIN_VOLUME


    def channel_up(self):
        if self.__status:
            self.__channel = (self.__channel + 1) % (Television.MAX_CHANNEL + 1)

    def channel_down(self):
        if self.__status:
            self.__channel = (self.__channel - 1) % (Television.MAX_CHANNEL + 1)

    def volume_up(self):
        if self.__status:
            if self.__muted:
                self.__volume = Television.MAX_VOLUME
                self.__muted = False
            elif self.__volume < Television.MAX_VOLUME:
                self.__volume += 1


    def volume_down(self):
        if self.__status:
            if self.__muted:
                self.__volume = 1
                self.__muted = False
            elif self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        if self.__status:
            if self.__muted:
                return f'Power = True, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}'
            else:
                return f'Power = True, Channel = {self.__channel}, Volume = {self.__volume}'
        else:
            return f'Power = False, Channel = {self.__channel}, Volume = {self.__volume}'



# Channel Logic
#####################################################
# Default - NFL - Cartoon Network - Discovery Channel
#    0       1           2                  3

# Volume Logic
######################
#    0       1       2
