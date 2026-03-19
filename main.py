from storage import load_data, save_data
from menu import menu
from day_manager import handle_new_day, start_day
from onboarding import onboarding
from profile_manager import show_profile
from reflections import show_journal


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
    edit_profile,
    show_profile,
    show_journal
)