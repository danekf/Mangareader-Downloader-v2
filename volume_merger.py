import os
import fitz #PyMuPDF
import time

volumes = os.listdir("Incomplete Volumes")

if not os.path.exists("Completed Volumes"):
    os.mkdir("Completed Volumes")

for volume in volumes:
  print(f"Processing {volume}")
  time.sleep(1)

  chapters_list = os.listdir(f"Incomplete Volumes/{volume}")
  doc = fitz.open() #create new pdf
  
  for chapter in chapters_list:
    doc.insert_file(f"Incomplete Volumes/{volume}/{chapter}") #add chapter to volume
    
  doc.save(f"Completed Volumes/{volume}.pdf") #save volume with directory name
  doc.close()

  #rmdir seems to be having issues removig manga dir because its not empty. Commenting out for now.
  #os.rmdir(f"temp/{manga}")
    
