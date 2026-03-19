def show_journal(data):
    journal = data.get("daily_journal", [])
    if not journal:
        print("No journal entries yet. ")
        return

    print("\n📓 Journal entries:")

    for entry in journal:
        print(f"{entry['date']} ⭐{entry['rating']} - {entry['note']}")
