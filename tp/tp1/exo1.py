import sys
# exercice 1 : 
# le premier element de sys.argv est le nom du fichier 
if len( sys.argv ) == 1:
    print( "auteur viny presty nakavoua" )
    print( "\tusage: python3 triangle.py intValue..." )
    exit()

# on doit convertir les strparam en int,  
# car parametres entrés en console sont mis en string par defaut

res = 0
li_value = []
for strParam in sys.argv[1:]:
    try:
        param = int( strParam )
        li_value.append(param)
        res += param
    except ValueError: 
        print( "Bad parameter value: %s" % strParam, file=sys.stderr )

max_value = max(li_value)
sum_cotes_except_max = res - max_value

if max_value <= sum_cotes_except_max:
    print("c'est un triangle")
else:
    print("ce n'est pas un triangle")






