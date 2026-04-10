import json
import os
from storage import save_data
from datetime import datetime


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

    while True:
        birthdate = input(f"Birthdate YYYY-MM-DD [{old_birthdate}]: ").strip()

        if not birthdate:
            birthdate = old_birthdate
            break

        try:
            birthdate_obj = datetime.strptime(birthdate, "%Y-%m-%d")

            if birthdate_obj > datetime.now():
                print("Birthdate cannot be in the future.")
                continue

            break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

        break

    while True:
        height = input(f"Height in cm [{old_height}]: ").strip()
        
        if not height:
            height = old_height
            break

        if height.isdigit() and 100 <= int(height) <= 250:
            height = int(height)
            break

        print("Please enter a valid height between 100 and 250 cm.")

    while True:
        weight = input(f"Weight in kg [{old_weight}]: ").strip()
        
        if not weight:
            weight = old_weight
            break

        try:
            w = float(weight)
            if 30 <= w <= 300:
                weight = w
                break
            else:
                print("Please enter a valid weight between 30 and 300 kg.")
        except ValueError:
            print("Please enter a valid number for weight.")
          
    reason = input(f"Why do you want to improve yourself? 💭 [{old_reason}]: ")

    data["profile"] = {
        "birthdate": birthdate,
        "height": height,
        "weight": weight,
    }

    if reason:
        data["reason"] = reason

    save_data(data)
    print("Profile updated! ✔")