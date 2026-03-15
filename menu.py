def menu(data, start_day, show_progress, show_profile, edit_profile, show_journal):
    while True:
        print("\n1. Start day")
        print("2. Show progress")
        print("3. Show profile")
        print("4. Edit profile")
        print("5. Show journal")
        print("6. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            start_day(data)
        elif choice == "2":
            show_progress(data)
        elif choice == "3":
            show_profile(data)
        elif choice == "4":
            edit_profile(data)
        elif choice == "5":
            show_journal(data)
        elif choice == "6":
            print("See you tomorrow! 🚀")
            break
        else:
            print("Invalid choice, please try again.")