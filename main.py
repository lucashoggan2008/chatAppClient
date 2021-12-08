import requests
import hashlib

BASEURL = "https://flaskChatappApi.lucashoggan.repl.co/"
def getApiResponce(HTMLTYPE, ENDPOINT, PERS):
	if HTMLTYPE == "POST":
		return requests.post(f"{BASEURL}{ENDPOINT}", json=PERS)
	elif HTMLTYPE == "GET":
		return requests.get(f"{BASEURL}{ENDPOINT}", json=PERS)

	return False

authid = False
email = False
passhash = False
username=False
userid = False
run = False


if __name__ == "__main__":
	loginChoice = input("Login(L) or sign-up(S) |>").lower()
	username = input("Username |>")
	email = input("Email |>")
	password = input("Password |>")
	userid = username + "|" + email
	passHash = hashlib.sha512(bytes(password, 'utf-8')).hexdigest()
	if loginChoice == "l":
		responce = getApiResponce("POST", "acc/login", {"username":username, "email":email,"passHash":passHash})
		authid = responce.json()['authid']
	else:
		responce = getApiResponce("POST", "acc/add", {"username":username, "email":email,"passHash":passHash})
		authid = responce.json()["response"]['authid']

	if authid != False:
		run = True

while run:
	action = input("|>")
	if action == "get posts":
		pers = {
			"authid":authid,
			"userid":userid
		}
		responce = getApiResponce("GET", "posts/getall", PERS=pers)
		responce = responce.json().values()
		
		for post in responce:
			print("_"*20)
			print()
			print(f'{post["title"]} | by {post["author"]}')	
			print()
			print(f"{post['content']}")

		for x in range(4):
			print()
	if action == "add post":
		title = input("title |>")
		content = input("content |>")
		pers = {
			"authid":authid,
			"userid":userid,
			"post":{
				"title":title,
				"content":content
			}
		}
		responce = getApiResponce("POST", "posts/add", pers)
		if responce.json() == {"responce": "sucsess"}:
			print("Uploaded post ")
		else:
			print("Something happened with your post ")





