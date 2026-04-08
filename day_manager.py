from datetime import date, datetime
from storage import save_data
from achievements import check_achievements


def start_day(data):
    print(f"\n🔥 Day {data['day_count']} in progress! Keep going {data['name']}! ✨")
    data["day_started"] = True


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


def end_day(data):
    if not data.get("day_started"):
        print("⚠️ You need to start your day first.")
        return
    
    if "current_streak" not in data:
        data["current_streak"] = 0
    if "longest_streak" not in data:
        data["longest_streak"] = 0

    data["current_streak"] += 1

    if data["current_streak"] > data["longest_streak"]:
        data["longest_streak"] = data["current_streak"]

    while True:
        rating_input = input("Rate your day (1-5): ").strip()
        if rating_input.isdigit() and 1 <= int(rating_input) <= 5:
            rating = int(rating_input)
            break
        else:
            print("Please enter a number between 1 and 5.")

        note = input("How was your day? Any reflectionS? ✍️ (optional): ").strip()

        if "daily_journal" not in data:
            data["daily_journal"] = []

        data["daily_journal"].append({
            "date": str(date.today()),
            "rating": rating,
            "note": note
        })

        save_data(data)

        data["day_started"] = False

        print("🔥 Current streak: {data['current_streak']}")
        print("🏆 Longest streak: {data['longest_streak']}")
        print("✅ Day saved! See you tomorrow! 👋")

