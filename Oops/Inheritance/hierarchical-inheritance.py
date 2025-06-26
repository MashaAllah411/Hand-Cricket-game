class Vehicle:
    def __init__(self, manufacture_date, manufactured_country, vehicle_type):
        self.manufacture_date = manufacture_date
        self.manufactured_country = manufactured_country
        self.vehicle_type = vehicle_type

    def accessobj(self):
        print(f"Manufacture Date     : {self.manufacture_date}")
        print(f"Manufactured Country : {self.manufactured_country}")
        print(f"Vehicle Type         : {self.vehicle_type}")

class Car(Vehicle):
    def __init__(self, brand_name, on_road_price, mileage, manufacture_date, manufactured_country, vehicle_type):
        super().__init__(manufacture_date, manufactured_country, vehicle_type)
        self.brand_name = brand_name
        self.on_road_price = on_road_price
        self.mileage = mileage

    def accessobj2(self):
        super().accessobj()
        print(f"Brand Name           : {self.brand_name}")
        print(f"On Road Price        : {self.on_road_price}")
        print(f"Mileage              : {self.mileage}")

class Bike(Vehicle):
    def __init__(self, brand_name, on_road_price, mileage, variant, manufacture_date, manufactured_country, vehicle_type):
        super().__init__(manufacture_date, manufactured_country, vehicle_type)
        self.brand_name = brand_name
        self.on_road_price = on_road_price
        self.mileage = mileage
        self.variant = variant

    def accessobj3(self):
        super().accessobj()
        print(f"Brand Name           : {self.brand_name}")
        print(f"On Road Price        : {self.on_road_price}")
        print(f"Mileage              : {self.mileage}")
        print(f"Variant              : {self.variant}")


vehicle_choice = input("Is it a Car or Bike? ").strip().lower()

manufacture_date = input("Enter Manufacture Date (YYYY-MM-DD): ")
manufactured_country = input("Enter Manufactured Country: ")
vehicle_type = input("Enter Vehicle Type: ")

if vehicle_choice == "car":
    brand_name = input("Enter Car Brand Name: ")
    on_road_price = float(input("Enter On Road Price: "))
    mileage = float(input("Enter Mileage: "))
    print("-----------------------------------------")
    print("--------------Entered Data---------------")
    car_obj = Car(brand_name, on_road_price, mileage, manufacture_date, manufactured_country, vehicle_type)
    car_obj.accessobj2()

elif vehicle_choice == "bike":
    brand_name = input("Enter Bike Brand Name: ")
    on_road_price = float(input("Enter On Road Price: "))
    mileage = float(input("Enter Mileage: "))
    variant = input("Enter Variant: ")
    print("-----------------------------------------")
    print("--------------Entered Data---------------")
    bike_obj = Bike(brand_name, on_road_price, mileage, variant, manufacture_date, manufactured_country, vehicle_type)
    bike_obj.accessobj3()

else:
    print("Invalid input. Please enter either 'Car' or 'Bike'.")
