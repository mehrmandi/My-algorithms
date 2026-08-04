#  number of questions
n = int(input())

#  define a function that get the last element as winner
def winnerTeam(n):
    for i in range(n):
        scores = int(input())
        order = input()
        winner = order[-1:]
        if winner == "Q":
            print("Quera")
        else:
            print("CodeCup")


winnerTeam(n)