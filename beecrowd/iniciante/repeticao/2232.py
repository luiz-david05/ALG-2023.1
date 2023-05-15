def main():
    t = int(input())

    while t > 0:
        n = int(input())
        print(2**n - 1)
        t -= 1
    
    
if __name__ == '__main__': 
    main()