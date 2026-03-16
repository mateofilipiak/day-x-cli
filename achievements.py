from storage import save_data


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
