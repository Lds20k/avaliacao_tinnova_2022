from voter import Voter

if __name__ == "__main__":
    voters = Voter(800, 150, 50)
    print(voters.valid_percentual())
    print(voters.white_percentual())
    print(voters.null_percentual())