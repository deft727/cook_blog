# # # version 1:

# # class Container:
# #     def __init__(self,name:str,volume:int,current_volume:int,pour_out:int = 100) -> None:
# #         self.__name = name
# #         self.__volume = volume
# #         self.current_volume = current_volume
# #         self.pour_out = pour_out

# #     def pour_out_liquid(self) -> int:
# #         if self.current_volume > 0:
# #             self.current_volume -= self.pour_out
# #             return self.pour_out
# #         else:
# #             print(f"{self.__name} пуст")
# #             return 0
    
# #     def pour_liquid(self,volume:int) -> None:
# #         if self.current_volume + volume <= self.__volume:
# #             self.current_volume += volume
# #         else:
# #             print(f"{self.__name} полон")

# #     def info(self):
# #         print(f"{self.__name} = {self.current_volume}")


# # def main() -> None:
# #     jug = Container(name = 'Jug',volume=1000,current_volume=1000)
# #     glass = Container(name = 'Glass',volume=200,current_volume=0,pour_out=50)
# #     i=0
# #     while i < 15:
# #         jug.info()
# #         glass.info()
# #         glass.pour_liquid(jug.pour_out_liquid())
# #         i+=1
        
# # main()


# # # version 2:

# class Container:
#     name: str = ""
#     _volume: int = 0
#     _current_volume: int = 0
#     pour_out: int = 0

#     def pour_out_liquid(self) -> int:
#         if self._current_volume > 0:
#             self._current_volume -= self.pour_out
#             return self.pour_out
#         else:
#             print(f"{self.name} пуст")
#             return 0
    
#     def pour_liquid(self,volume:int) -> None:
#         if self._current_volume + volume <= self._volume:
#             self._current_volume += volume
#         else:
#             print(f"{self.name} полон")

#     def info(self):
#         print(f"{self.name} = {self._current_volume}")


# class Jug(Container):
#     name: str = "Jug"
#     _volume: int = 1000
#     _current_volume: int = 600
#     pour_out: int = 100


# class Glass(Container):
#     name: str = "Glass"
#     _volume: int = 300
#     _current_volume: int = 0
#     pour_out: int = 50


# def main() -> None:
#     jug = Jug()
#     glass = Glass()
#     i=0
#     while jug._current_volume>0 and glass._current_volume<=glass._volume:
#         jug.info()
#         glass.info()
#         glass.pour_liquid(jug.pour_out_liquid())
#         i+=1
        
# main()


# def main():
#     cars = ["BMW","AUDI","Honda","Mazda"]
#     men = ["John","Bob","Mike","Noah","Jacob"]
#     cars_of_men = dict(zip(cars,men))
#     # for c,m in zip(cars,men):    
#     #     print(c,m)
#     #     cars_of_men[c]=m
#     print(cars_of_men)

# main()