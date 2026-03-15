from storage import load_data, save_data
from datetime import date, datetime
from menu import menu


def onboarding():
    print("\n👋 Welcome to Day X Coding!")
    
    name = input("How should I call you? ")
    goal = input("What's your main goal? 🎯 ")
    
    data = {
        "name": name,
        "goal": goal,
        "day_count": 1,
        "last_active": str(date.today()),
        "profile": {
            "birthdate": None,
            "height": None,
            "weight": None
        },
        "reflections": []
    }
    
    save_data(data)
    print(f"Nice to meet you, {name}! 🚀 Day X begins now!")
    return data


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


def show_progress(data):
    print("\n📊 Progress:")
    print(f"Name: {data['name']}")
    print(f"Day count: {data['day_count']}")
    print(f"Last active: {data['last_active']}")
    print(f"Goal: {data['goal']} 🎯")
    print(f"Reason: {data.get('reason', 'Not set yet')}")
    ach = data.get("achievements", [])
    if ach:
        print("Achievements:")
        for a in ach:
            print(" -", a)


def show_profile(data):
    profile = data.get("profile", {})
    print("\n👤 Profile:")
    print(f"Name: {data['name']}")

    if profile:
        print(f"Birthdate: {profile.get('birthdate', '-')}")
        print(f"Height: {profile.get('height', '-')} cm")
        print(f"Weight: {profile.get('weight', '-')} kg")
    else:
        print("No profile data yet.")


def edit_profile(data):
    print("\n📝 Edit Profile")

    profile = data.get("profile", {})

    old_birthdate = profile.get("birthdate", "")
    old_height = profile.get("height", "")
    old_weight = profile.get("weight", "")
    old_reason = data.get("reason", "")

    birthdate = input(f"Birthdate (YYYY-MM-DD) [{old_birthdate}]: ")
    height = input(f"Height in cm [{old_height}]: ")
    weight = input(f"Weight in kg [{old_weight}]: ")
    reason = input(f"Why do you want to improve yourself? 💭 [{old_reason}]: ")

    data["profile"] = {
        "birthdate": birthdate if birthdate else old_birthdate,
        "height": int(height) if height.isdigit() else old_height,
        "weight": int(weight) if weight.isdigit() else old_weight,
    }

    if reason:
        data["reason"] = reason

    save_data(data)
    print("Profile updated! ✔")


def check_achievements(data):
    day_count = data.get("day_count", 0)
    achievements = data.get("achievements", [])

    achievement_rules = [
        (1, "Day One Warrior"),
        (7, "Warrior Novice"),
        (14, "Consistency Knight"),
        (30, "One-Month Champion"),
        (100, "Unbreakable Legend")
    ]

    for required_days, title in achievement_rules:
        if day_count >= required_days and title not in achievements:
            achievements.append(title)
            print(f"🏆 New Achievement: {title}! ⚔️")

    data["achievements"] = achievements
    save_data(data)


def show_journal(data):
    journal = data.get("daily_journal", [])
    if not journal:
        print("No journal entries yet. ")
        return

    print("\n📓 Journal entries:")

    for entry in journal:
        print(f"{entry['date']} ⭐{entry['rating']} - {entry['note']}")


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


data = load_data()

if data is None:
    data = onboarding()
else:
    if "achievements" not in data:
        data["achievements"] = []
    print(f"Welcome back {data['name']}! 👋")
    data = handle_new_day(data)

menu(
    data,
    start_day,
    show_progress,
    show_profile,
    edit_profile,
    show_journal
)