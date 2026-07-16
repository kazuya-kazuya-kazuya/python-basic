class Vehicle: # 親クラス
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def get_information(self):
        return f"{self.name}はスピード{self.speed}km/hです。"

class Bycycle(Vehicle): # 子クラス
    pass

class Car(Vehicle): # 子クラス
    def get_information(self):
        return f"{self.name}の車のスピードは{self.speed}km/hです。"
    
    def original(self):
        return "子のメソッド"
    
vehicle = Vehicle("テスラ", 30) # 親クラス
print(vehicle.get_information())

bicycle = Bycycle("自転車", 10)
print(bicycle.get_information())

car = Car("ステップワゴン", 50)
print(car.get_information())
print(car.original())