def add_habit(data):
    habits = data.setdefault("habits", [])

    if len(habits) >= 3:
        print("❌ You can only have up to 3 habits.")
        return
    
    name = input("Enter the name of the habit: ").strip()

    if not name:
        print("Habit name cannot be empty.")
        return
    
    habits.append({"name": name, "done": False})

    print("✅ Habit added!")


def show_habits(data):
    habits = data.get("habits", [])

    if not habits:
        print("📭 No habits yet.")
        return
    
    print("\n📌 Your habits:")

    for i, habit in enumerate(habits, 1):
        status = "✅" if habit["done"] else "❌"
        print(f"{i}. {habit['name']} {status}")

    choice = input("Mark habit as done (number of ENTER to skip): ").strip()

    if choice.isdigit():
        index = int(choice) -1
        if 0 <= index < len(habits):
            habits[index]["done"] = True
            print("🔥 Habit completed!")