def show_journal(data):
    journal = data.get("daily_journal", [])

    if not journal:
        print("📭 No journal entries yet.")
        return

    print("\n📘 Your Journal:\n")

    for entry in journal:
        print(f"📅 {entry['date']}")
        print(f"⭐ Rating: {entry['rating']}")
        
        if entry.get("note"):
            print(f"📝 Note: {entry['note']}")
        
        print("-" * 30)
