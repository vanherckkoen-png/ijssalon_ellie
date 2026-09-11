def decoreer(tekst=""):
    lengte=len(tekst)+4
    print()
    print (lengte*"*")
    print(f"* {tekst} *")
    print (lengte*"*")
    print()
def fooi_pp(bedrag, personen):
    try:
        bedrag_pp = bedrag/personen
    except:
        bedrag_pp = "??"
    return(f"bedrag per persoon is {bedrag_pp} €")
bedrag = int(input("bedrag fooienpot ? "))
personen = int(input("aantal personen ? "))
print(fooi_pp(bedrag, personen))