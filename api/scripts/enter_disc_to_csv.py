import csv
import pandas as pd

filename = "files/discs.csv"

headers = ["manifacturer", "name", "type", "speed", "glide", "turn", "fade"]


try:
    with open(filename, "x", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
except FileExistsError:
    pass

while 1:

    print("==== Options ====")
    print("Enter new disc: 1")
    print("     Exit: 2     ")
    
    option = input()
    if option == "1":
        while 1:
            manifacturer = input("Enter manifacturer: ")
            disc_name = input("Enter name: ")
            disc_type = input("Enter disc type: ")
            speed = input("Enter speed: ")
            glide = input("Enter glide: ")
            turn = input("Enter turn: ")
            fade = input("Enter fade: ")

            print(f"""Is the following info correct?\n\n
                Manifacturer: {manifacturer}\n
                Name: {disc_name}\n
                Type: {disc_type}\n
                Speed: {speed}\n
                Glide: {glide}\n
                Turn: {turn}\n
                Fade: {fade}""")

            answ = input("y/n?")
            if answ == "y" or answ == "Y":                
                
                df = pd.read_csv("files/discs.csv")
                
                if not ((df["manifacturer"] == manifacturer) & (df["name"] == disc_name)).any():
                      
                    with open(filename, "a", newline="", encoding="utf-8") as f:
                        writer = csv.writer(f)
                        writer.writerow([manifacturer, disc_name, disc_type, speed, glide, turn, fade])

                    # SORT CSV
                    df = df.sort_values(by=["manifacturer", "name"], ignore_index=True)
                    df.to_csv("files/discs.csv", index=False)

                    break
                else:
                    print("Disc already exists!!")
    elif option == "2":
        exit()
    else:
        print("Invalid option!")
