# Question 1
class Car:
    def __init__(self, car_model, number_plate, rental_price):
        self.car_model = car_model
        self.number_plate = number_plate
        self.rental_price = rental_price

# Question 2
ford_list = [
    Car("Ford_Focus", "123AB", 300),
    Car("Ford_Focus", "1241253", 400),
    Car("Ford_Focus", "1414", 500)
]

bmw_list = [
    Car("BMW_X1", "345CD", 700),
    Car("BMW_X1", "543633CD", 600),
    Car("BMW_X1", "345CDEFG", 500)
]

mercedes_list = [
    Car("Mercedes-Benz_Maybach", "678abcEF", 1000),
    Car("Mercedes-Benz_Maybach", "678324EF", 1200),
    Car("Mercedes-Benz_Maybach", "67ddef8EF", 3000)
]

car_list = [ford_list, bmw_list, mercedes_list]

# Question 3
def modify_price(car_list, new_price):
    for car in car_list:
        car.rental_price = new_price

modify_price(ford_list, 300)
print(ford_list[0].rental_price)

# Question 4
def compute_rent(num_plate, dist, discount_flag):
    for sublist in car_list:
        for car in sublist:
            if car.number_plate == num_plate:
                base_cost = dist * 0.7 + car.rental_price
                return base_cost * 0.8 if discount_flag else base_cost
    
    return "Car not found"

print(compute_rent("67ddef8EF", 3000, True))