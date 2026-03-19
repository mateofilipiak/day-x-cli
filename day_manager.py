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


def end_day(state):
    if "current_streak" not in state:
        state["current_streak"] = 0
    if "longest_streak" not in state:
        state["longest_streak"] = 0

    state["current_streak"] += 1

    if state["current_streak"] > state["longest_streak"]:
        state["longest_streak"] = state["current_streak"]

    note = input("How was your day? Any reflections? ✍️ ")
    state["last_note"] = note
    rating = int(input("Rate your day (1-5): "))
    state["last_rating"] = rating
    try:
        rating = int(input("Rate your day (1-5): "))
    except ValueError:
        rating = 0
    print(f"🔥 Current streak: {state['current_streak']}")
    print(f"🏆 Longest streak: {state['longest_streak']}")