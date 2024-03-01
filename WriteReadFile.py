# Samuel Parente - Python programming exercises

# Create a new file and add text to it
try:
    file = open("myFile.txt", "x")
    try:
        file.write("Samuel Parente")
    except:
        print("Something went wrong when writing to the file.")
    finally:
        file.close()
except:
    print("Something went wrong when opening the file.")


# Open the file, read contents and output text
try:
    file = open("myFile.txt")
    try:
        text = file.read()
        print(text)
    except:
        print("Something went wrong when opening the file.")
    finally:
        file.close()
except:
    print("Something went wrong when opening the file.")
