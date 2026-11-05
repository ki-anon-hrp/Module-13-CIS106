# Kirill M13P3 11/05/2026

# Creating empty list 
players_dic = {}

# Opening txt file
with open("M13P3.txt", "r") as f:
    for line in f:
# Separate names and numbers
        name, avg = line.strip().split(",")
        players_dic[name.strip()] = avg.strip()

# Define a function
def display(players):
    print()
# Printing header
    print(f"{'Players:':<15}{'Batting Average:':<15}")
# Using loop for using each value in the list
    for name, avg in players.items():
        print(f"{name:<15} | {avg:<15}")

# Calling function
display(players_dic)