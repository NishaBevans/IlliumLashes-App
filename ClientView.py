class EyelashSalon:
    def __init__(self):
        self.services = {
            "1": "Full Set of Eyelashes",
            "2": "1 Week Refill",
            "3": "2 Week Refill",
            "4": "3 Week Refill"
        }
        self.appointments = []

    def display_services(self):
        print("\nAvailable Services:")
        for key, service in self.services.items():
            print(f"{key}. {service}")

    def schedule_appointment(self):
        self.display_services()
        choice = input("Please enter the number of the service you want to schedule: ")
        
        if choice in self.services:
            name = input("Please enter your name: ")
            phone = input("Please enter your phone number: ")
            date = input("Please enter the date for your appointment (YYYY-MM-DD): ")
            time = input("Please enter the time for your appointment (HH:MM): ")
            appointment = {
                "name": name,
                "phone": phone,
                "service": self.services[choice],
                "date": date,
                "time": time
            }
            self.appointments.append(appointment)
            print(f"Appointment scheduled for {name} ({phone}) for a {self.services[choice]} on {date} at {time}.")
        else:
            print("Invalid choice. Please try again.")

    def view_appointments(self):
        if not self.appointments:
            print("No appointments scheduled.")
        else:
            print("\nScheduled Appointments:")
            for appointment in self.appointments:
                print(f"{appointment['name']} ({appointment['phone']}) - {appointment['service']} on {appointment['date']} at {appointment['time']}")

def main():
    salon = EyelashSalon()
    while True:
        print("\nWelcome to Lilium Lashes!")
        print("1. View Services")
        print("2. Schedule Appointment")
        print("3. View Appointments")
        print("4. Exit")

        choice = input("Please choose an option: ")

        if choice == '1':
            salon.display_services()
        elif choice == '2':
            salon.schedule_appointment()
        elif choice == '3':
            salon.view_appointments()
        elif choice == '4':
            print("Thank you for using the Eyelash Salon system. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()