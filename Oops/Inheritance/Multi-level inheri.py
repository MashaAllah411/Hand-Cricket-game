class Vehicle:
    def __init__(self,manufactured_date,manufactured_place):
        self.manufactured_date=manufactured_date
        self.manufactured_place=manufactured_place
        
    def access(self):
        print(f"Manufactured Date :{self.manufactured_date}")
        print(f"Manufactured Place :{self.manufactured_place}")
        
class Car(Vehicle):
    def __init__(self,engine,eng_mileage,varient,manufactured_date,manufactured_place):
        super().__init__(manufactured_date,manufactured_place)
        self.engine=engine
        self.eng_mileage=eng_mileage
        self.varient=varient
        
    def access2(self):
        super().access()
        print(f"Engine Name :{self.engine}")
        print(f"Mileage :{self.eng_mileage}")
        print(f"Varient :{self.varient}")
        
class Maruthi(Car):
    def __init__(self,name,model,speed,mileage,engine,eng_mileage,varient,manufactured_date,manufactured_place):
        super().__init__(engine,eng_mileage,varient,manufactured_date,manufactured_place)
        self.name=name
        self.model=model
        self.speed=speed
        self.mileage=mileage
        
    def access3(self):
        super().access2()
        print(f"Car Name :{self.name}")
        print(f"Car Model:{self.model}")
        print(f"Speed :{self.speed}")
        print(f"Mileage :{self.mileage}")
        
m=Maruthi("Maruthi",2018,110,45,'v8',"normal car",2018,"18/8/2018","paris")
m.access3()

        
        
        
        
        
        
        
        
        
        
        