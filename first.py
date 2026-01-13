class HotelService:
    def book_room(self, *args, **kwargs):
        if len(args) == 1:
            # print
            return f"Room booked for {args[0]}"
        elif len(args) == 2:
            return f"{args[0]} booked {args[1]} room"
        elif len(args) ==3:
            result = f"{args[0]} - {args[1]} room for {args[2]} days"
            if kwargs.get('breakfast'):
                result += " with breakfast"
            if kwargs.get('airport_pickup'):
                result += " + airport pickup"
            return result
        return "Booking failed"
    
class BillingSystem(HotelService):
    def calculate_bill(self, *args):
        if len(args) == 1:
            return args[0]
        elif len(args) == 2:
            return args[0] * args[1]
        elif len(args) == 3:
            return (args[0] * args[1]) - args[2]
        elif len(args) == 4:
            return (args[0] * args[1]) - args[2] + args[3]
        return 0
    

class Customer:
    def show_summary(self):
        return "Customer summary"

class Individual_customer(Customer):
    def show_summary(self):
        return "Individual Customer"
    
class Corporate_customer(Customer):
    def show_summary(self):
        return "Corporate Customer - 10% discount"
    
class Foreign_customer(Customer):
    def show_summary(self):
        return "Foreign customer + 5% tax rate"
    
service = HotelService()
billing = BillingSystem()

print(service.book_room("Arushi"))
print(service.book_room("Arushi", "Suite"))
print(service.book_room("Arushi", "Deluxe", 5, breakfast = True, airport_pickup =True))

print(f"Bill: ₹{billing.calculate_bill(100): .2f}")
print(f"Bill: ₹{billing.calculate_bill(100, 3): .2f}")
print(f"Bill: ₹{billing.calculate_bill(100, 3, 50): .2f}")

customers = [Individual_customer(), Corporate_customer(), Foreign_customer()]
for customer in customers:
    print(customer.show_summary())

with open("report.txt", "w") as f:
    f.write("Hotel Report\n")
    for customer in customers:
        f.write(customer.show_summary() + "\n")

print("Saved!")
