
import os
if __name__ == '__main__':
    print("welcome to Robo speaker")
    while True:
            x = input("enter what you want to pronounce")
            if x=="z":
                break
            command = f"say {x}"
            os.system(command)


