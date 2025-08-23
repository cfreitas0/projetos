import time

doc = open("#", "r")

while True:
    for i in range(50):
        time.sleep(0.2)
        print(f"{i+1}: ", doc.readline(), "\n\n")
        if i == 49:
            print("\n\n" "   ####### GRUPO COM 50 #######  ""\n\n\n")