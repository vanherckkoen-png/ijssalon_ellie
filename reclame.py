# huiswerk les  8.4 - deze file aangemaakt
# huiswerk les 8.12 - functie_2 importeren
from algemene_functies import mijn_functie_2
# huiswerk les 8.5 - functie aanbieding_1()
def aanbieding_1(smaak, prijs, korting):
    korting = 1-korting
    print("Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak", smaak, "van", prijs, "euro voor", prijs*korting, "euro" )
print()
aanbieding_1("Aardbei", 4, 0.1)
print()

# huiswerk les 8.6" & 8.7 - functie inkomsten_totaal()
def inkomsten_totaal(inkomsten,btw):
    print("weektotaal is €",sum(inkomsten), "waarvan €",sum(inkomsten)*btw, "BTW" )
inkomsten = [220, 430, 125, 160, 205, 90, 345]
btw=0.09
inkomsten_totaal(inkomsten,btw)
print()

# huiswerk les 8.8 - functie laag_en_hoog()
def laag_en_hoog(mijn_lijst):
    laag = min(mijn_lijst)
    hoog = max(mijn_lijst)
    return [laag, hoog]
mijn_lijst = inkomsten # gebruik de reeds bestaande lijst inkomsten voor mijn_lijst
minmax = laag_en_hoog(mijn_lijst)
print("minimum daginkomsten =", minmax[0],"  Maximum daginkomsten =", minmax[1])
print(minmax)
print()

# huiswerk les 8.9 en 8.10 - functie gemiddelde()
def gemiddelde(mijn_lijst):
    global bedrag
    bedrag =  sum(mijn_lijst)/len(mijn_lijst)
    return bedrag
mijn_lijst=inkomsten
print(f"Gemiddelde inkomsten deze week", gemiddelde(mijn_lijst), "€." )
print()

# huiswerk les 8.11 - meervoudige functie meervoudig()
def meervoudig(invoer_lijst):
    return laag_en_hoog(invoer_lijst)
invoer_lijst = [10, 5, 3, 2, 1, 7, 7]
print(f"Laagste en hoogste waarde [laagste, hoogste]=>",meervoudig(invoer_lijst))
print()

# huiswerk les 8.12 - functie importeren op eerste regel
# huiswerk les 8.12 - functie combinatie()
def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    return mijn_functie_2(korte_lijst[0], korte_lijst[1])
invoer_lijst_2 = [23, 45,  1, 45, 80]
print(combinatie(invoer_lijst_2))   
