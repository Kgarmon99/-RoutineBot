# Daily Money Adventure with Milestones and Gamification 🚀

def beautiful_progress_bar(value, goal, length=30):
    progress = min(value, goal)
    gap = goal - progress
    fill_length = int(length * (progress / goal))
    gap_length = length - fill_length
    bar = "█" * fill_length + " " * gap_length
    return f"Progress: [{bar}] ${gap:.2f} away from your next milestone 🏁"

# Define your financial milestones (in dollars)
milestones = [1e2, 1e3, 1e4, 1e5, 1e6, 1e7, 1e8, 1e9, 1e10, 1e11, 1e12]  # $100 to 1 trillion dollars
Name = input("Good morning, I'm MoneyBot!! your finace co-pilot. What is your name? ")
print(f"Welcome {Name}! to the MoneyVerse! 🚀")
print("Let's begin your journey of riches & success. 💼💰")

# How will you make more money today?
make_more_money = input("\nYour mission: How will you INCREASE your income today? 🤑 ")

# How will you save more money today?
save_more_money = input("Your strategy: What's your PLAN for SAVING money today? 📈 ")

# Cash on Hand
cash_on_hand = float(input("Your resources: How much cash do you have on hand? 💵 $"))

# Your Current Net Worth (Assets - Debts)
current_net_worth = float(input("\nYour status: What's your current net worth? 🥇 $"))

# Calculate the next upcoming milestone
next_milestone = next((milestone for milestone in milestones if milestone > current_net_worth), None)

# Financial Milestone Map
print("\n🗺️ Financial Milestone Map 🗺️")
for i, milestone in enumerate(milestones, 1):
    progress_marker = "🚀" if milestone == next_milestone else "  "
    print(f"{progress_marker} Level {i}: ${milestone:.2f}")

# Progress Bar Visualization
if next_milestone is not None:
    print("\n🌟 Your Current Progress 🌟")
    print(beautiful_progress_bar(current_net_worth, next_milestone))
    print(f"🚀 Your next milestone: Level {milestones.index(next_milestone) + 1} 🚀")
else:
    print("\n🏆 Congratulations! You've reached your ultimate financial goal. Keep it up! 🏆")

print("\nThank you for joining the Money Adventure! 🐐")

# Today's Money-Making Quest
print(f"\n📜 Today's Money-Making Quest 📜")
print(f"Objective: {make_more_money} 📈")

# Today's Money-Saving Challenge
print(f"\n💼 Today's Money-Saving Challenge 💼")
print(f"Challenge: {save_more_money} 📈")

# Progress to Next Milestone
if next_milestone is not None:
    remaining_to_next_milestone = next_milestone - current_net_worth
    print(f"\n🎯 Your Next Milestone Quest 🎯")
    print(f"Quest: Earn ${remaining_to_next_milestone:.2f} to reach the next milestone.")
else:
    print("\n🏆 Congratulations, you've reached your ultimate financial goal! 🏆")

# Gamified Income and Expenses
daily_income = float(input("\n💰 Income Update: How much gold did you find today? 🤑 $"))
daily_expenses = float(input("💸 Expenses Update: How much treasure did you spend today? 💎 $"))
cash_on_hand += daily_income - daily_expenses

print(f"\n💰 Your Wealth Status: You now have ${cash_on_hand:.2f} in your treasure chest. 💰")

print("\n🚀 Continue your Money Adventure! 🚀")