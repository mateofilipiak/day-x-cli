from datetime import date, datetime
from storage import save_data
from achievements import check_achievements


def start_day(data):
    print(f"\n🔥 Day {data['day_count']} in progress! Keep going {data['name']}! ✨")

    while True:
        rating_input = input("How was your day? Rate 1-5 ⭐: ").strip()
        
        if rating_input.isdigit() and 1 <= int(rating_input) <= 5:
            rating = int(rating_input)
            break
        else:
            print("Please enter a number between 1 and 5.")

    reflect = input("Short note about today? ✍️ ")

    if "daily_journal" not in data:
        data["daily_journal"] = []

    data["daily_journal"].append({
        "date": str(date.today()),
        "rating": rating,
        "note": reflect
    })

    save_data(data)
    print("Day saved with reflection! 🧠✨")


def handle_new_day(data):
    last_date = datetime.fromisoformat(data["last_active"]).date()
    today = date.today()

    if today > last_date:
        day_gap = (today - last_date).days

        if day_gap == 1:
            data["day_count"] += 1
            print(f"🔥 New day! Day {data['day_count']} activated! 💪")
        else:
            data["day_count"] = 1
            print("⏱ Long break detected - restarting from Day 1!🔄")

        data["last_active"] = str(today)
        save_data(data)
        check_achievements(data)

    elif today == last_date:
        print("You've already activated today! 👍")

    return data