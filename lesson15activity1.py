import os

print("=== Science Notes ===")
with open("C:\\Users\\NICE COMPUTERS\\Desktop\\Devansh Coding HW\\Python\\sciencenotes.txt","r") as f:
    for line in f:
        print(line.strip())
print()

print("=== Word Count ===")
with open("maths.txt","r") as f:
    for line in f:
        words = line.split()
        print(len(words),"words ->",line.strip())
print()

print("=== Merging Notes ===")
if os.path.exists("allnotes.txt"):
    print("'allnotes.txt' file already exists - overwriting it")
else:
    print("'allnotes.txt' file does not exist - creating it")

content = ""
with open("C:\\Users\\NICE COMPUTERS\\Desktop\\Devansh Coding HW\\Python\\sciencenotes.txt","r") as f:
    content += "--- sciencenotes.txt ---\n"
    content += f.read() + "\n"
with open("maths.txt","r") as f:
    content += "--- maths.txt ---\n"
    content += f.read() + "\n"
with open("allnotes.txt","w") as out:
    out.write(content)
print("Everything saved to file 'allnotes.txt'")
print()

if os.path.exists("allnotes.txt"):
    os.remove("allnotes.txt")
    print("File 'allnotes.txt' has been successfully deleted.")
else:
    print("The file with name 'allnotes.txt' does not exist")
