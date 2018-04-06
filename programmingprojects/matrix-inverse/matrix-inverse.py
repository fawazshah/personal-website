import sys
import fractions
mat = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

print("""Matrix must be entered in the form:
[A B C]
[D E F]
[G H I]
""")
mat_value_names = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']]
for i in range(0, 3):
    for j in range(0, 3):
        var = int(input("Enter number " + mat_value_names[i][j] + ": "))
        mat[i][j] = var

cf1 = mat[1][1] * mat[2][2] - mat[1][2] * mat[2][1]
cf2 = -(mat[1][0] * mat[2][2] - mat[1][2] * mat[2][0])
cf3 = mat[1][0] * mat[2][1] - mat[1][1] * mat[2][0]
cf4 = -(mat[0][1] * mat[2][2] - mat[0][2] * mat[2][1])
cf5 = mat[0][0] * mat[2][2] - mat[0][2] * mat[2][0]
cf6 = -(mat[0][0] * mat[2][1] - mat[0][1] * mat[2][0])
cf7 = mat[0][1] * mat[1][2] - mat[0][2] * mat[1][1]
cf8 = -(mat[0][0] * mat[1][2] - mat[0][2] * mat[1][0])
cf9 = mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]

adj = [[cf1, cf4, cf7], [cf2, cf5, cf8], [cf3, cf6, cf9]]

det = mat[0][0] * cf1 + mat[0][1] * cf2 + mat[0][2] * cf3
print("\nDeterminant: " + str(det))

if det == 0:
    print("Sorry, the inverse does not exist")
    sys.exit()

print("\nCofactor matrix: ")
print("[" + str(cf1) + "    " + str(cf2) + "    " + str(cf3) + "]")
print("[" + str(cf4) + "    " + str(cf5) + "    " + str(cf6) + "]")
print("[" + str(cf7) + "    " + str(cf8) + "    " + str(cf9) + "]")

print("\nTranspose matrix: ")
print("[" + str(adj[0][0]) + "    " + str(adj[0][1]) + "    " + str(adj[0][2]) + "]")
print("[" + str(adj[1][0]) + "    " + str(adj[1][1]) + "    " + str(adj[1][2]) + "]")
print("[" + str(adj[2][0]) + "    " + str(adj[2][1]) + "    " + str(adj[2][2]) + "]")

inv = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(0, 3):
    for j in range(0, 3):
        inv[i][j] = 1/det * adj[i][j]

print("\nInverse matrix: ")
print("[" + str(fractions.Fraction(inv[0][0]).limit_denominator()) + "    " + str(fractions.Fraction(inv[0][1]).limit_denominator()) + "    " + str(fractions.Fraction(inv[0][2]).limit_denominator()) + "]")
print("[" + str(fractions.Fraction(inv[1][0]).limit_denominator()) + "    " + str(fractions.Fraction(inv[1][1]).limit_denominator()) + "    " + str(fractions.Fraction(inv[1][2]).limit_denominator()) + "]")
print("[" + str(fractions.Fraction(inv[2][0]).limit_denominator()) + "    " + str(fractions.Fraction(inv[2][1]).limit_denominator()) + "    " + str(fractions.Fraction(inv[2][2]).limit_denominator()) + "]")
