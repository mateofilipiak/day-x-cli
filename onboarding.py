from datetime import date
from storage import save_data


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