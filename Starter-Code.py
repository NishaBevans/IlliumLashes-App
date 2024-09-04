name = input("Please enter your name: ")

print(f"Hello, {name}.")

service = input("Which service are you looking to schedule today? (extensions/touch up/full set)")

if service == "extensions":
    print("Wonderful! Lets get you scheduled!")
elif service == "touch up":
       print("Please call the salon to schedule a touch up based on necessity.")
elif service == "full set":
    print("Awesome! Let's get you scheduled!")
else:
     print("Please call the salon and we will happily walk you through our available services!")