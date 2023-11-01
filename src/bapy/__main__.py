from bapy import puhoo, fooloo, fuh

def main():
    # PRINT
    puhoo("Hi")
    
    # FOR
    fooloo(5, 1, lambda x: print(x))
    
    # IF
    fuh(1 > 2, lambda: print("Condition is true :)"), lambda: print("Condition is false :("))
    fuh(2 > 1, lambda: print("Condition is true :)"), lambda: print("Condition is false :("))
    
    # WHILE

if __name__ == '__main__':
    main()