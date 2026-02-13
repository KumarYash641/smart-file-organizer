import os

files = os.listdir("data")
print(files)

for file in files:
    
    folder = ""
    f = file.lower()

    if file.lower().endswith(".jpg"):
        folder ="Images"

    elif file.lower().endswith(".mp4"):
        folder="Videos"

    elif file.lower().endswith(".txt"):
        folder="Documents"

    elif file.lower().endswith(".pdf"):
        folder="Pdf"



    if folder!="":

            if not os.path.exists("data/"+folder):
                os.mkdir("data/"+folder)
            os.rename("data/"+file,"data/"+folder+"/"+file)

            print(file,"moved to",folder)
     