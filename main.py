# Daily Money Routine with Milestones and Gamification

def beautiful_progress_bar(value, goal, length=30):
    progress = min(value, goal)
    gap = goal - progress
    fill_length = int(length * (progress / goal))
    gap_length = length - fill_length
    bar = "█" * fill_length + " " * gap_length
    return f"Progress: [{bar}] ${gap:.2f} away from your next milestone🏁"

# Define your financial milestones (in dollars)
milestones = [1e2, 1e3, 1e4, 1e5, 1e6, 1e7, 1e8, 1e9, 1e10, 1e11, 1e12]  # $100 to 1 trillion dollars

print("Hello, I'm MoneyBot, your financial motivator.")
print("Let's start your day with financial goals in mind.")

# How will you make more money?
make_more_money = input("\nHow will you MAKE more money today?🤑 ")

# How will you save more money?
save_more_money = input("How will you SAVE more money today?📈 ")

# Cash on Hand
cash_on_hand = float(input("How much cash do you have on hand? 💵$"))

# Current Net Worth (You can input your actual net worth)
current_net_worth = float(input("\nYour current net worth (assets - debts): 🥇$"))

# Calculate the next upcoming milestone
next_milestone = next((milestone for milestone in milestones if milestone > current_net_worth), None)

# Milestones List
print("\nFinancial Milestones:")
for milestone in milestones:
    print(f"${milestone:.2f}")

# Simple and Beautiful Progress Bar
if next_milestone is not None:
    print("\n" + beautiful_progress_bar(current_net_worth, next_milestone))
    print(f"Your next milestone is: ${next_milestone:.2f}")
else:
    print("\nCongratulations! You've reached your 1 Trillion dollar goal. Keep it up!")

print("\nThank you for starting your day with a financial vision.🐐")

# Money-Making Update
print(f"\nToday's Money-Making Plan: {make_more_money}📈")

# Money-Saving Update
print(f"Today's Money-Saving Strategy: {save_more_money}📈")

# Remaining to Next Milestone
if next_milestone is not None:
    remaining_to_next_milestone = next_milestone - current_net_worth
    print(f"\nYou have ${remaining_to_next_milestone:.2f} left to reach your next milestone.")
else:
    print("\nCongratulations, you've reached your ultimate financial goal!")

# Gamification: Income and Expenses
daily_income = float(input("\nHow much money did you make today? $🤑"))
daily_expenses = float(input("How much did you spend today? $👀"))
cash_on_hand += daily_income - daily_expenses

print(f"\nCash on Hand: ${cash_on_hand:.2f}")

print("\nMake it a great day!🕺🏽")