from datetime import date, datetime
from storage import save_data
from achievements import check_achievements


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