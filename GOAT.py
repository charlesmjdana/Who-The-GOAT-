SAT = [[-6, 7, 8, 9, 10, 11, -12, 13, -14, 15, 16, -17, 18, -19, 20, 100], 
       [1, 2, 3, 4, -5, -6, 7, 8, 9, 10, 11, -12, -13, -14, -15, -16, -100], 
       [1, 2, 3, -4, 5, -6, 7, 8, 9, 10, 11, -12, -13, -14, 15, -16, -17, -18, 19, -20, -100], 
       [-1, 2, 3, 4, -5, -6, 7, 8, 9, 10, 11, 12, 13, -14, -15, -16, 17, 18, -100], 
       [2, -3, -4, 5, -6, 7, 8, 9, 10, 11, -12, -13, 14, -15, -16, -17, -18, 19, -20, -21, 22, 23, -24, -25, -26, -27, -28, -29, -30, -31, 32, -33, -34, -35, -36, -37, -38, -39, -40, -41, -42, -43, -44, -45, 46, -47, 48, -49, -50, -51, -52, -53, -54, -55, -56, -57, -58, -59, -60, -61, -62, -63, -64, -65, -66, -67, -68, -69, -70, -71, 100], 
       [-2, 3, -4, 5, -6, 7, 8, 9, 10, 11, 12, -13, 14, -15, -16, -100], [2, 3, 4, 5, -6, 7, 8, 9, 10, 11, 12, 13, 14, 15, -16, -17, -18, -19, -100], 
       [2, -3, 4, -5, -6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, -17, 18, 19, 20, 21, 22, -100], 
       [-3, -4, 5, -6, 7, 8, 9, 10, 11, -12, 13, -14, -15, -16, -17, -18, -19, 20, 21, -22, -23, 24, -25, -26, -27, -28, -29, -30, -31, -32, 33, -34, -35, -36, -37, -38, -39, -40, -41, -42, -43, -44, 45, 46, 47, 48, -49, -50, -51, -52, -53, -54, -55, -56, -57, -58, -59, -60, -61, -62, -63, -64, -65, -66, -67, -68, -69, -70, -71, 100], 
       [5, -6, 7, 8, 9, 10, 11, 12, 13, 14, 15, -16, -17, -18, -19, -20, 100], 
       [-4, -5, -6, 7, 8, 9, 10, 11, -12, 13, -14, 15, 16, -17, 18, -19, 20, -100], 
       [2, -3, 4, 5, -6, 7, 8, 9, 10, 11, 12, 13, -14, 15, -16, -17, -18, -19, 100], 
       [-22, 23, -24, -25, -26, -27, -28, -29, -30, 100], [-5, 6, 7, 8, 9, 10, 11, 12, -13, -14, -15, 16, -17, 100], 
       [-6, 7, 8, 9, 10, 11, 12, -13, 14, -15, 16, -17, -100], [-4, -5, 6, 7, 8, 9, 10, 11, 12, -13, -14, -15, 16, -100], 
       [-3, 5, 7, 8, 9, 10, 11, -100], 
       [5, -6, 7, 8, 9, 10, 11, -12, -13, 14, -15, -16, -17, -18, 19, -20, -21, 22, 23, -24, -25, -26, -27, -28, -29, -30, -31, -32, -33, 34, -35, -36, -37, -38, -39, -40, -41, -42, -43, -44, -45, 46, -47, -48, 49, -50, -51, -52, -53, -54, -55, -56, -57, -58, -59, -60, -61, -62, -63, -64, -65, -66, -67, -68, -69, -70, -71, 100], 
       [5, -6, 7, 8, 9, 10, 11, -12, -13, -14, 15, -16, -17, -18, 19, -20, 21, 22, 23, -24, -25, -26, -27, -28, -29, -30, -31, -32, 33, 34, -35, -36, -37, -38, -39, -40, -41, -42, -43, -44, 45, 46, -47, -48, 49, -50, -51, -52, -53, -54, -55, -56, -57, -58, -59, -60, -61, -62, -63, -64, -65, -66, -67, -68, -69, -70, -71, 100], 
       [4, -5, -6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, -17, 18, 19, 20, 21, 100]]
# algorithmes.org 🏗
from random import choice
from pysat.solvers import Solver

def solve(problem):
    if problem == []:
        return False
    s = Solver(name='g4')
    for clause in problem:
        s.add_clause(clause)
    is_SAT = s.solve()
    s.delete()
    return is_SAT

def run():
    anchor = str(input("Season considered <YYYY-YY>: "))
    while (int(anchor.split("-")[0]) % 100) != (int(anchor.split("-")[1]) - 1) % 100:
        anchor = str(input("Season considered <YYYY-YY>: "))
    datebinary = [(int(anchor.split("-")[0]) // (2**k)) % 2 for k in range(11)] + [(int(anchor.split("-")[1]) // (2**k)) % 2 for k in range(7)]
    player = str(input("Player considered [🐍, 👑, 🌬]: "))
    while player != "🐍" and player != "👑" and player != "🌬":
        player = str(input("Player considered [🐍, 👑, 🌬]: "))
    if player == "🐍":
        # Kobe
        player = 2
    if player == "👑":
        # LeBron
        player = 0
    if player == "🌬":
        # Jordan
        player = 1
    playerbinary = [(player // (2**k)) % 2 for k in range(13)]
    age = str(input("Age during the season <YY>: "))
    while len(age) != 2 and not age[0] in "123456789" and not age[1] in "0123456789":
        age = str(input("Age during the season <YY>: "))
    agebinary = [(int(age) // (2**k)) % 2 for k in range(13)]
    stat = str(input("Stat considered [Age, Tm, Lg, Pos, G, MP, PER, TS%, 3PAr, FTr, ORB%, DRB%, TRB%, AST%, STL%, BLK%, TOV%, USG%, OWS, DWS, WS, WS/48, OBPM, DBPM, BPM, VORP]: "))
    while not stat in ['Pos', 'G', 'MP', 'PER', 'TS%', '3PAr', 'FTr', 'ORB%', 'DRB%', 'TRB%', 'AST%', 'STL%', 'BLK%', 'TOV%', 'USG%', 'OWS', 'DWS', 'WS', 'WS/48', 'OBPM', 'DBPM', 'BPM', 'VORP']:
        stat = str(input("Stat considered [Age, Tm, Lg, Pos, G, MP, PER, TS%, 3PAr, FTr, ORB%, DRB%, TRB%, AST%, STL%, BLK%, TOV%, USG%, OWS, DWS, WS, WS/48, OBPM, DBPM, BPM, VORP]: "))
    VALUES = ['Age', 'Tm', 'Lg', 'Pos', 'G', 'MP', 'PER', 'TS%', '3PAr', 'FTr', 'ORB%', 'DRB%', 'TRB%', 'AST%', 'STL%', 'BLK%', 'TOV%', 'USG%', 'OWS', 'DWS', 'WS', 'WS/48', 'OBPM', 'DBPM', 'BPM', 'VORP']
    v = 0
    while v < len(VALUES) and VALUES[v] != stat:
        v += 1
    xtra = [(v // (2**k)) % 2 for k in range(len(VALUES) + 1)]
    dpoint = datebinary + agebinary + playerbinary + xtra
    instance = [[int(((-1)**(dpoint[k])) * int(k + 1))] for k in range(len(dpoint))]
    result = solve(instance + SAT)
    if result == False:
        print("Result: not the 🐐")
    else:
        print("Result: might be the 🐐")

run()
