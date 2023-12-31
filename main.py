import time
import cProfile
from io import StringIO
import pstats



class Node:
    def __init__(self, chessboard, order, row, column):
        self.chessboard = [row[:] for row in chessboard]
        self.order = order
        self.row = row
        self.column = column

def findSolution(startingRow, startingColumn, chessBoardSize, maxTime):
    # Vytvorenie sachovnice naplnenej nulami
    chessboard = createChessboard(chessBoardSize)
    # Vyplnenie zaciatocnej pozicie
    chessboard[startingRow][startingColumn] = 1
    order = 1
    # Vytvorenie prveho uzla na zaklade vstupu
    firstNode = Node(chessboard, order, startingRow, startingColumn)
    operands = [[1, 2], [1, -2], [2, 1], [2, -1], [-1, 2], [-1, -2], [-2, 1], [-2, -1]]
    # Vytvorenie zasobnika a vlozenie prveho uzla do zasobnika
    allNodes = []
    allNodes.append(firstNode)

    # Stav==1 prve riesenie sa naslo, start_time = spustenie casovaca
    # numberOfGeneratedNodes nepotrebna premenna urcena iba na testovanie, predstavuje pocet
    # vygenerovanych uzlov v ramci behu programu
    stav = 0
    start_time = time.time()
    numberOfGeneratedNodes = 0
    target_size = chessBoardSize * chessBoardSize;

    while True:
        curent_time = time.time()
        # Max time je urceny ako 15 sekund
        if curent_time - start_time > maxTime:
            print("Velkost:", chessBoardSize, "Zaciatocny riadok:", startingRow + 1, "Zaciatocny stlpec:",
                  startingColumn + 1)
            print("Nenaslo sa riesenie v stanovenom case", "Pocet vygenerovanych uzlov:", numberOfGeneratedNodes)
            break

        # najdenie prveho riesenia
        if stav == 1:
            break

        # preskumanie vsetkych moznych uzlov
        if len(allNodes) == 0:
            print("Velkost:", chessBoardSize, "Zaciatocny riadok:", startingRow + 1, "Zaciatocny stlpec:",
                  startingColumn + 1)
            print("Neexistuje riesenie", "Pocet vygenerovanych uzlov:", numberOfGeneratedNodes)
            break

        # pop vrchneho uzla zo zasobnika a prehladanie
        lastNode = allNodes.pop()
        for i, (operand_row, operand_col) in enumerate(operands):
            posRow = operand_row + lastNode.row
            posCol = operand_col + lastNode.column

            # Ak sa po posune nachadzame stale v sachovnici
            if 0 <= posRow <= chessBoardSize - 1 and 0 <= posCol <= chessBoardSize - 1:
                posValue = lastNode.chessboard[posRow][posCol]
                # Ak na danom mieste este jazdec nebol
                if posValue == 0:
                    # Vytvorime novy uzol s novou sachovnicou
                    newNode = Node(lastNode.chessboard, lastNode.order, posRow, posCol)
                    newNode.order = lastNode.order + 1
                    newNode.chessboard[posRow][posCol] = newNode.order
                    numberOfGeneratedNodes += 1
                    # Ak uz v danom uzle bolo vykonanych n*n (n je velkost sachovnice)
                    # tahov, tak jazdec presiel celu sachovnicu
                    if newNode.order >= target_size:
                        print("Velkost:", chessBoardSize, "Zaciatocny riadok:", startingRow + 1, "Zaciatocny stlpec:",
                              startingColumn + 1)
                        for j in range(chessBoardSize):
                            print(newNode.chessboard[j])
                        print("Prve riesenie sa naslo za:", time.time() - start_time, "Pocet vygenerovanych uzlov:",
                              numberOfGeneratedNodes)
                        stav = 1
                        break
                    allNodes.append(newNode)


def createChessboard(chessboardSize):
    chessboard = [[0] * chessboardSize for _ in range(chessboardSize)]
    return chessboard

def profile_code():
    findSolution(4, 0, 5, 15)
    findSolution(2, 2, 5, 15)
    findSolution(3, 2, 5, 15)
    findSolution(4, 4, 5, 15)
    findSolution(0, 0, 5, 15)
    findSolution(5, 0, 6, 15)
    findSolution(3, 5, 6, 15)
    findSolution(5, 1, 6, 15)
    findSolution(1, 5, 6, 15)
    findSolution(2, 1, 6, 15)


def main():
    profiler = cProfile.Profile()
    profiler.enable()
    profile_code()
    profiler.disable()
    output_stream = StringIO()
    stats = pstats.Stats(profiler, stream=output_stream).sort_stats('cumulative')
    stats.print_stats()

    with open('profile_results.txt', 'w') as f:
        f.write(output_stream.getvalue())


if __name__ == "__main__":
    main()
