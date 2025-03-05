Voters_Name = []
Voters_Gender = []
Voters_Age = []
Voting_IDs = []
Votes = []
Parties_Name = ["B.J.P","I.N.C","A.A.P","C.I.P"]
Parties_Vote = [0,0,0,0]

while True:
    Name = input("Enter your Name: ")
    Gender = input("Enter your Gender: ")
    while True:
        Age = int(input("Enter Your Age: "))
        if Age<18:
            print("You are not eligible to cast a vote")
        else:
            break
    while True:
        Voting_ID = (input("Enter your 12 digit voting ID: "))
        if len(Voting_ID) != 12:
            print("Invalid ID")
        else:
            break
    if Voting_ID in Voting_IDs:
            print("This ID has already been used and can not be used to vote again")
            continue 

    print("Parties participating in elsections are:")
    for i,Parties in enumerate(Parties_Name):
        print(f"{i+1}.{Parties}")
    while True:
        Vote = int(input("Select your desired party: "))
        if 1<= Vote <= len(Parties_Name):
            break
        else:
            print("Invalid input.")
    Voters_Name.append(Name)
    Voters_Gender.append(Gender)
    Voters_Age.append(Age)
    Voting_IDs.append(Voting_ID)
    Votes.append(Vote)
    Another_Voter = input("Do want to continue? (yes/no: )")
    if Another_Voter.upper() != "YES":
        break
    
print("Results")
Total_Votes = len(Votes)
print("Total votes cast: ",Total_Votes)
Winner = max(Votes)
print("Winner of this election is: ",Winner)
# print("\n--- Voting Results ---")
# total_votes = len(Votes)
# print(f"Total votes cast: {total_votes}")

# for i, candidate in enumerate(Parties_Name):
#     percentage = (Parties_Vote[i] / total_votes) * 100 if total_votes > 0 else 0
#     print(f"{candidate}: {Parties_Vote[i]} Votes ({percentage:.2f}%)")

# # Determine the winner
# winning_votes = max(Parties_Vote)
# winner_index = Parties_Vote.index(winning_votes)
# winner = Parties_Name[winner_index]

# print(f"\n--- The winner is {winner} with {winning_votes} votes! ---")