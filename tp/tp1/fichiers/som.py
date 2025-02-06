import sys

if len( sys.argv ) == 1:
    print( "auteur viny presty nakavoua" )
    print( "\tusage: fonction qui fait une somme des paramètres..." )
    exit()


params = sys.argv[1:]
res = 0
for i in range(len(params)):
    res += int(params[i])

print(res)


