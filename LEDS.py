N = int(input())
for I in range(1,N+1):
    led = 0
    X = input()
    for J in range(0,len(X)):
        if X[J] == "1":
            led = led + 2
        if X[J] == "2":
            led = led + 5
        if X[J] == "3":
            led = led + 5
        if X[J] == "4":
            led = led + 4
        if X[J] == "5":
            led = led + 5
        if X[J] == "6":
            led = led + 6
        if X[J] == "7":
            led = led + 3
        if X[J] == "8":
            led = led + 7
        if X[J] == "9":
            led = led + 6
        if X[J] == "0":
            led = led + 6
    print(str(led) + " leds")