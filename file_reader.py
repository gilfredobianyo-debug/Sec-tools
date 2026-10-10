## File ##
import json
import csv

def read_file():
  while True:
    try:
      file = str(input("Enter a file that you will like to read(q to cancel): "))
      file_split = []

      if file.lower() == "q":
        print("You canceled the program")
        break
      else:
        pass
      if "." in file:
        pass
      else:
        raise ValueError("file Name must contain a '.'")
      
      if file.endswith(".json") == True:
        with open(file,"r") as f:
          data = json.load(f)
          print(data)
      elif file.endswith(".txt") == True:
        with open(file,"r") as f:
          data = f.read()
          print(data)
      elif file.endswith(".csv") == True:
        with open(file,"r",) as f:
          reader = csv.reader(f)
          for line in reader:
            print(line)
      else:
        raise ValueError("file must either be a txt,json or csv")
      
    except FileNotFoundError:
      print(f"{file} was not found, creating an empty file")
      if file.endswith(".json") == True:
        json_file = [{"File-create": True}]
        with open(file,"w") as f:
          json.dump(json_file,f,indent=4)
      elif file.endswith(".csv") == True:
        with open(file,"w") as f:
          writer = csv.writer(f)
          writer.writerow(["Name","Class","Score"])
      elif file.endswith(".txt") == True:
        with open(file,"w") as f:
          f.write("")
      else:
        raise ValueError
      print("File created")
    except PermissionError:
      print(f"Sorry you do not have the permission to read this file")
    except ValueError as e:
      print(e)
    else:
      print("Program completed")
      print(file.endswith(".json"))
      break
      
read_file()
