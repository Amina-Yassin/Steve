secret = "Orang"
pw = ''
 
auth = False
count = 0
max_attempt = 5
 
while pw != secret:
	count += 1
	if count > max_attempt: break
	if pw == "conspiracy": continue #Exits loop
	pw = input(f"Attempt {count}: What's the secret word? ")
else:
	auth = True
print ("Authorized" if auth else "Calling the cops...")