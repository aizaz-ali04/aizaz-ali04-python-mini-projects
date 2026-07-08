candidates = {
    "ali": 0,
    "ahmed": 0,
    "sara": 0
}

voted_users = []

while True:
    print("\n--- Voting System ---")
    print("1. Vote")
    print("2. Show Result")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter your name: ").lower()

        if name in voted_users:
            print("You have already voted!")
        else:
            print("Candidates: Ali, Ahmed, Sara")
            vote = input("Enter candidate name: ").lower()

            if vote in candidates:
                candidates[vote] += 1
                voted_users.append(name)
                print("Vote recorded successfully!")
            else:
                print("Invalid candidate!")

    elif choice == "2":
        print("\n--- Results ---")
        for person, votes in candidates.items():
            print(person.capitalize(), ":", votes)

        winner = max(candidates, key=candidates.get)
        print("Winner is:", winner.capitalize())

    elif choice == "3":
        print("Exiting system...")
        break

    else:
        print("Invalid choice!")