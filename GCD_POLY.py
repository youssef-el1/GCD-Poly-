import gmpy2 as gm
# Calcule récursivement le pgcd de deux polynômes dans un corps fini donné p (pour p premier)
# Les polynômes sont donnés par une liste de coefficients du plus petit au plus grand.
# Lorsque p=0 essaie de calculer le pgcd dans R 
EPSILON = 0.0001	
#fonction qui calcule le pgcd de deux polynomes       
def gcd(f, g, p=0, verbose=False):
    if (len(f)<len(g)):
        return gcd(g,f,p, verbose)    
    r = [0]*len(f)
    r_mult = reciprocal(g[0], p)*f[0]
    for i in range(len(f)):
        if (i < len(g)):
            r[i] = f[i] - g[i]*r_mult
        else:
            r[i] = f[i]
        if (p != 0):
            r[i] %= p
    if(verbose):
        print(f,'by',g,'got',r)
    while (abs(r[0])<EPSILON):
        r.pop(0)
        if (len(r) == 0):
            return g
    return gcd(r, g, p, verbose)	
# renvoie l'inverse de n dans le corps fini de p premier, si p=0 renvoie 1/n#	
def reciprocal(n, p=0):
    if (p == 0):
        return 1/n
    for i in range(p):
        if (n*i)%p == 1:
            return i
    return None
#remplir le degre de deux polynome 
degPX = gm.mpz(input("entrer le degree du polynome P(x) : "))
degGX = gm.mpz(input("entrer le degree du polynome G(x) : "))
px = []
gx = []
#remplir les cofficents de P(x)
for i in range(degPX+1):
    px.append(gm.mpz(input("P(X) enter le coefficent x*{} ".format(i))))
#remplir les cofficients de G(x)
for i in range(degGX+1):
    gx.append(gm.mpz(input("G(X) enter le coefficent x**{} ".format(i))))
#calculer le pgcd
PGCD_Poly=gcd(px,gx,0, True)
#afficher le pgcd
print(PGCD_Poly)