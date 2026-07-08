# Total seats (1 to 10)
seats = [1,2,3,4,5,6,7,8,9,10]

booked_seats = []

while True:
    print("\n--- Bus Reservation System ---")
    print("1. Book Seat")
    print("2. Cancel Seat")
    print("3. Show Available Seats")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # 1. Book Seat
    if choice == "1":
        seat = int(input("Enter seat number to book (1-10): "))

        if seat in seats and seat not in booked_seats:
            booked_seats.append(seat)
            print("Seat booked successfully!")
        else:
            print("Seat not available!")

    # 2. Cancel Seat
    elif choice == "2":
        seat = int(input("Enter seat number to cancel: "))

        if seat in booked_seats:
            booked_seats.remove(seat)
            print("Seat cancelled successfully!")
        else:
            print("This seat was not booked!")

    # 3. Show Available Seats
    elif choice == "3":
        print("Available seats:")

        for seat in seats:
            if seat not in booked_seats:
                print(seat, end=" ")

    # 4. Exit
    elif choice == "4":
        print("Exiting system...")
        break

    else:
        print("Invalid choice!")