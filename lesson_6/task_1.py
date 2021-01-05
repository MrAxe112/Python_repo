import time


class TrafficLight:
    def __init__(self, colour):
        self.__colour = colour

    def running(self):
        while True:
            if self.__colour == "Green":
                print("\033[92mСейчас зеленый сигнал светофора\033[0m")
                time.sleep(5)
                self.__colour = "Red"
            elif self.__colour == "Yellow":
                print("\033[93mСейчас желтый сигнал светофора\033[0m")
                time.sleep(2)
                self.__colour = "Green"
            elif self.__colour == "Red":
                print("\033[91mСейчас красный сигнал светофора\033[0m")
                time.sleep(7)
                self.__colour = "Yellow"


obj = TrafficLight("Green")
obj.running()
