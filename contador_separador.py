import time

doc = open("numero.txt", "r")

while True:
    for i in range(50):
        time.sleep(0.2)

        print(f"({i+1})")
        if i == 49:
            print("\n" "GRUPO  ""\n")