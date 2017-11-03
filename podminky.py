
def trojuhelnik(a, b, c):
    if a + b < c:
        print("Toto není trojúhelník.")
    elif b + c < a:
        print("Toto není trojúhelník.")
    elif a + c < b:
        print("Toto není trojúhelník.")
    else:
        print("Toto jsou strany trojúhelníku")

