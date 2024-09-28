class Customer:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.visits = []

    def add_visit(self, date, service):
        self.visits.append({'date': date, 'service': service})

    def get_recent_visit(self):
        if self.visits:
            return self.visits[-1]
        else:
            return None


class Salon:
    def __init__(self):
        self.customers = {}

    def add_customer(self, name, phone):
        if phone not in self.customers:
            self.customers[phone] = Customer(name, phone)
            print(f"Customer {name} added successfully.")
        else:
            print("Customer already exists.")

    def view_customer(self, phone):
        if phone in self.customers:
            customer = self.customers[phone]
            recent_visit = customer.get_recent_visit()
            if recent_visit:
                print(f"Recent visit for {customer.name}: {recent_visit}")
            else:
                print(f"No visits recorded for {customer.name}.")
        else:
            print("Customer not found.")

    def schedule_appointment(self, phone, date, service):
        if phone in self.customers:
            customer = self.customers[phone]
            customer.add_visit(date, service)
            print(f"Appointment scheduled for {customer.name} on {date} for {service}.")
        else:
            print("Customer not found.")

    def view_all_customers(self):
        if self.customers:
            print("Customer List:")
            for customer in self.customers.values():
                print(f"- {customer.name} (Phone: {customer.phone})")
        else:
            print("No customers found.")


def main():
    salon = Salon()

    while True:
        print("\nEyelash Salon Management")
        print("1. Add Customer")
        print("2. View Customer Recent Visit")
        print("3. Schedule Appointment")
        print("4. View All Customers")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter customer name: ")
            phone = input("Enter customer phone number: ")
            salon.add_customer(name, phone)

        elif choice == '2':
            phone = input("Enter customer phone number: ")
            salon.view_customer(phone)

        elif choice == '3':
            phone = input("Enter customer phone number: ")
            date = input("Enter appointment date (YYYY-MM-DD): ")
            service = input("Enter service: ")
            salon.schedule_appointment(phone, date, service)

        elif choice == '4':
            salon.view_all_customers()

        elif choice == '5':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()