file_path = "auth.txt"
cred = []
with open(file_path) as file:
	for line in file:
		cred.append(line)
print(cred)

