myList = ["Ahmed", "Mohammed", "Mona", "Khareem", "Moayed", "Khadeeja", "Salim"]
specialList = list(filter(lambda ele: ele.startswith("Kh") or ele.startswith("Mo"),myList))
print(specialList)