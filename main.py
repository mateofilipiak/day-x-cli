from storage import load_data, save_data
from menu import menu
from day_manager import handle_new_day, start_day, end_day
from onboarding import onboarding
from profile_manager import show_profile, edit_profile
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
    show_journal,
    end_day
)