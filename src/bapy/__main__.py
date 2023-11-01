from bapy import puhoo, fooloo, fuh, wuhoo

def main():
    # PRINT
    puhoo("Print Statement:\nHi :D")
    
    # FOR
    puhoo("\nFor Loop:")
    fooloo(5, 1, lambda x: puhoo(x))
    
    # IF
    puhoo("\nIf Statement:")
    fuh(1 > 2, lambda: puhoo("1 > 2 is true :)"), lambda: puhoo("1 > 2 is false :("))
    fuh(2 > 1, lambda: puhoo("2 > 1 is true :)"), lambda: puhoo("2 > 1 is false :("))
    
    # WHILE
    puhoo("\nWhile Loop:")
    counter = [0]
    wuhoo(lambda: counter[0] < 5, lambda: (puhoo(counter[0]), counter.__setitem__(0, counter[0] + 1))[0])

if __name__ == '__main__':
    main()