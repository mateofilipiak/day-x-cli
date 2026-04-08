import json
import os

from storage import save_data


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