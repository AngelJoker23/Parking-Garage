class ParkingGarage:
    def __init__(self, total_tickets, total_parking_spaces):
        self.tickets = list(range(1, total_tickets + 1))
        self.parkingSpaces = list(range(1, total_parking_spaces + 1))
        self.currentTicket = {}

    def takeTicket(self):
        if self.tickets:
            ticket_number = self.tickets.pop(0)
            parking_space = self.parkingSpaces.pop(0)
            self.currentTicket = {
                'ticket_number': ticket_number,
                'parking_space': parking_space,
                'paid': False
            }
            print(f"Ticket {ticket_number} has been issued. Parking space {parking_space} is assigned.")

    def payForParking(self):
        if not self.currentTicket:
            print("No active ticket. Please take a ticket first.")
            return

        if self.currentTicket['paid']:
            print("Your ticket has already been paid. You have 15 minutes to leave.")
            return

        payment = input("Please enter the payment amount: ")
        if payment:
            self.currentTicket['paid'] = True
            print("Payment received. Your ticket has been paid. You have 15 minutes to leave.")

    def leaveGarage(self):
        if not self.currentTicket:
            print("No active ticket. Please take a ticket first.")
            return

        if self.currentTicket['paid']:
            print("Thank you! Have a nice day!")
            self.parkingSpaces.append(self.currentTicket['parking_space'])
            self.tickets.append(self.currentTicket['ticket_number'])
            self.currentTicket = {}
        else:
            payment = input("Please pay for your ticket: ")
            if payment:
                print("Thank you! Have a nice day!")
                self.parkingSpaces.append(self.currentTicket['parking_space'])
                self.tickets.append(self.currentTicket['ticket_number'])
                self.currentTicket = {}


# Create an instance of the ParkingGarage class
my_garage = ParkingGarage(total_tickets=10, total_parking_spaces=10)

# Example usage:
my_garage.takeTicket()

# Simulate paying for parking
my_garage.payForParking()

# Simulate leaving the garage
my_garage.leaveGarage()
