import time
import random
from datetime import datetime, timedelta

# -----------------------------
# Motivational Quotes List
# -----------------------------
quotes = [
    "Believe in yourself! You’ve got this! 💪",
    "Stay consistent. Small steps lead to big results. 🚀",
    "You’re one study session away from progress. 📚",
    "Don’t give up. Great things take time. 🌱",
    "Focus today for a better tomorrow. 🎯"
]

# -----------------------------
# Functions
# -----------------------------

def greet_user():
    print("👋 Hello! I’m your AI Study Buddy.")
    name = input("What's your name? ")
    print(f"\nNice to meet you, {name}! Let's plan your study session today!\n")
    return name

def get_study_time():
    try:
        available_time = float(input("⏰ How many hours can you study today? "))
        return available_time
    except ValueError:
        print("Please enter a valid number.")
        return get_study_time()

def generate_schedule(hours):
    subjects = []
    print("\n📘 Enter the subjects you want to study today (type 'done' when finished):")
    while True:
        subject = input("- ")
        if subject.lower() == 'done':
            break
        subjects.append(subject)

    if not subjects:
        print("You must enter at least one subject.")
        return generate_schedule(hours)

    time_per_subject = round(hours / len(subjects), 2)
    print("\n📅 Your Personalized Study Plan:")
    for i, subject in enumerate(subjects, start=1):
        print(f"{i}. {subject} – {time_per_subject} hours")

def set_goals():
    goal = input("\n✅ What's your main study goal for today? ")
    print(f"Awesome! Your goal is: {goal}")
    return goal

def send_motivation():
    print("\n💡 Here's your motivation for today:")
    print(random.choice(quotes))

def set_reminder(minutes=1):
    print(f"\n⏳ A reminder will be sent in {minutes} minute(s)...")
    time.sleep(minutes * 60)
    print("\n🔔 Reminder: Time to study! Stay focused! 💡")

# -----------------------------
# Main Chatbot Flow
# -----------------------------

def study_buddy():
    name = greet_user()
    available_time = get_study_time()
    generate_schedule(available_time)
    set_goals()
    send_motivation()
    
    try:
        reminder_choice = input("\nWould you like a reminder in 1 minute? (yes/no): ").strip().lower()
        if reminder_choice == 'yes':
            set_reminder(minutes=1)
        else:
            print("\n👍 No problem! Stay productive, and good luck with your studies!")
    except:
        print("Reminder skipped.")

    print("\n✅ Study Buddy Session Complete. Have a productive day! 🎓")

# -----------------------------
# Run the Chatbot
# -----------------------------
if __name__ == "__main__":
    study_buddy()
