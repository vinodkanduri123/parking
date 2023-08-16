import datetime

class Parking:
    def __init__(self, num_floors, max_capacity_per_floor):
        self.num_floors = num_floors
        self.max_capacity_per_floor = max_capacity_per_floor
        self.floors = []  
    
    def add_floor(self, floor):
        if len(self.floors) < self.num_floors:
            self.floors.append(floor)
        else:
            print("Cannot add more floors, parking lot is full.")
    
    def is_full(self):
        return all(floor.is_full() for floor in self.floors)

class Floor:
    def __init__(self, floor_number, num_spots_per_type):
        self.floor_number = floor_number
        self.num_spots_per_type = num_spots_per_type
        self.spots = {} 
    
    def add_spot(self, spot):
        if spot.spot_type not in self.spots:
            self.spots[spot.spot_type] = []
        if len(self.spots[spot.spot_type]) < self.num_spots_per_type:
            self.spots[spot.spot_type].append(spot)
        else:
            print(f"No more {spot.spot_type} spots available on floor {self.floor_number}.")
    
    def is_full(self):
        return all(len(spots) >= self.num_spots_per_type for spots in self.spots.values())

class Spot:
    def __init__(self, spot_number, spot_type):
        self.spot_number = spot_number
        self.spot_type = spot_type
        self.is_empty = True

class Ticket:
    def __init__(self, spot, entry_time):
        self.spot = spot
        self.entry_time = entry_time
    
    def calculate_fee(self, exit_time):
     
        time_difference = exit_time - self.entry_time
        hours_parked = time_difference.total_seconds() / 3600

        first_hour_fee = 4
        second_third_hour_fee = 3.5
        remaining_hour_fee = 2.5

        if hours_parked <= 1:
            fee = first_hour_fee
        elif 1 < hours_parked <= 3:
            fee = first_hour_fee + (hours_parked - 1) * second_third_hour_fee
        else:
            fee = first_hour_fee + 2 * second_third_hour_fee + (hours_parked - 3) * remaining_hour_fee

        return fee

class Payment:
    def process_payment(self, amount, payment_method):
        if payment_method == "cash":
            print(f"Received ${amount} in cash. Payment successful.")
            return True
        elif payment_method == "credit_card":
            print(f"Charged ${amount} to the credit card. Payment successful.")
            return True
        else:
            print("Invalid payment method.")
            return False

class ElectricPanel:
    def process_payment_and_charge(self, ticket, exit_time):
        fee = ticket.calculate_fee(exit_time)
        
        payment = Payment()
        payment_successful = payment.process_payment(fee, "credit_card")
        
        if payment_successful:
            print("Electric car charged successfully.")
        else:
            print("Payment or charging failed.")

parking_lot = Parking(num_floors=3, max_capacity_per_floor=50)
floor1 = Floor(floor_number=1, num_spots_per_type=20)
floor2 = Floor(floor_number=2, num_spots_per_type=30)
parking_lot.add_floor(floor1)
parking_lot.add_floor(floor2)

spot1 = Spot(spot_number=1, spot_type="Compact")
spot2 = Spot(spot_number=2, spot_type="Large")
entry_time = datetime.datetime(2023, 8, 10, 10, 0, 0)
exit_time = datetime.datetime(2023, 8, 10, 12, 30, 0)
ticket = Ticket(spot=spot1, entry_time=entry_time)
fee = ticket.calculate_fee(exit_time)
print(f"Total fee: ${fee:.2f}")

payment = Payment()
payment.process_payment(fee, "cash")

electric_panel = ElectricPanel()
electric_panel.process_payment_and_charge(ticket, exit_time)

