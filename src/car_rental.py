from datetime import datetime

class CarRental:
  def __init__(self, inventory):
    self.inventory = inventory  # Dictionary {car_model: quantity}

  def display_cars(self):
    print("Available Cars:")
    for car, quantity in self.inventory.items():
      print(f"{car}: {quantity}")

  def rent_car_hourly(self, car_model, quantity, duration):
    if quantity <= 0 or duration <= 0:
      print("Invalid input. Please enter positive values.")
      return
    if self.inventory[car_model] < quantity:
      print(f"Sorry, only {self.inventory[car_model]} {car_model} cars available.")
      return
    self.inventory[car_model] -= quantity
    self.rental_time = datetime.now()  # Store rental time
    print(f"Successfully rented {quantity} {car_model} cars for {duration} hours.")

  def rent_car_daily(self, car_model, quantity, days):
    # Similar logic as rent_car_hourly with daily duration
    pass

  def rent_car_weekly(self, car_model, quantity, weeks):
    # Similar logic as rent_car_hourly with weekly duration
    pass

  def return_car(self, car_model, quantity, rental_mode, rental_duration):
    if quantity <= 0:
      print("Invalid input. Please enter a positive value.")
      return
    self.inventory[car_model] += quantity
    rental_end = datetime.now()
    rental_period = rental_end - self.rental_time  # Calculate rental period

    # Calculate bill based on rental mode and duration (implementation omitted for brevity)
    print(f"Successfully returned {quantity} {car_model} cars.")
    print(f"Rental details: Car Model - {car_model}, Quantity - {quantity}, Mode - {rental_mode}, Duration - {rental_period}")
    # Print the generated bill here

class Customer:
  def __init__(self, name):
    self.name = name

  def request_car(self, car_rental, choice):
    if choice == 1:
      car_rental.display_cars()
    elif choice == 2:
      # Choose rental mode and car details
      pass
    elif choice == 3:
      # Return car details
      pass
    else:
      print("Invalid choice.")