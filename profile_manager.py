import json
import os


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
