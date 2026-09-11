members = {}

while True:
    print("\n--- GYM MANAGEMENT SYSTEM ---")
    print("1. Add Member")
    print("2. View Members")
    print("3. Remove Member")
    print("4. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        member_id = input("Enter Member ID: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        plan = input("Enter Plan (Monthly/Yearly): ")

        members[member_id] = {
            "name": name,
            "age": age,
            "plan": plan
        }

        print("Member added successfully!")

    elif choice == "2":
        if not members:
            print("No members found.")
        else:
            print("\n--- MEMBER LIST ---")
            for member_id, details in members.items():
                print("ID:", member_id)
                print("Name:", details["name"])
                print("Age:", details["age"])
                print("Plan:", details["plan"])
                print("------------------")

    elif choice == "3":
        member_id = input("Enter Member ID to remove: ")

        if member_id in members:
            del members[member_id]
            print("Member removed successfully!")
        else:
            print("Member not found.")

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")
        fee = {"Monthly": 1000, "Yearly": 10000}
print("Membership Fee:", fee.get(plan, "Invalid Plan"))

search = input("Enter Member ID: ")
print(members.get(search, "Member not found"))

