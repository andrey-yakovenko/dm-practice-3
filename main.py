from additional import *

# Loading data form the "data.csv" file
preferences = list(pd.read_csv('data.csv', index_col=0).preferences)

# Calculating all results for respective voting rules
plurality_result, plurality_winner = plurality(preferences)
plurality_runoff_first_round, plurality_runoff_second_round, plurality_runoff_winner = plurality_runoff(preferences)
condorcet_voting_relation, condorcet_voting_winner = condorcet_voting(preferences)
borda_voting_result, borda_voting_winner = borda_voting(preferences)

# Printing all the results
print("Student: Andrii Yakovenko (M2 BDMA)")
print("Course: Decision Modelling (2020-2021)")
print("Assignment: Voting Rules (Practical Work 3)\n\n")
print("PLURALITY VOTING:\n")
for outcome in plurality_result: print("   candidate " + outcome[0] + "  - ", outcome[1], "votes")
print("\nPLURALITY RUNOFF VOTING:\n")
if plurality_runoff_winner is not None:
    print("   ROUND 1:")
    for outcome in plurality_runoff_first_round: print("   candidate " + outcome[0] + "  - ", outcome[1], "votes")
    print("\n   ROUND 2:")
    for outcome in plurality_runoff_second_round: print("   candidate " + outcome[0] + "  - ", outcome[1], "votes")
else: print("   draw in first round detected")
print("\nCONDORCET VOTING:\n")
if condorcet_voting_winner is not None: print("   candidate " + condorcet_voting_winner + "  -  winner\n")
else: print("condorcet winner was not found\n")
print(condorcet_voting_relation)
print("\nBORDA VOTING:\n")
for outcome in borda_voting_result: print("   candidate " + outcome[0] + "  - ", outcome[1], "points")
