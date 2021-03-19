import requests

f = open("map_list", "r")

index = "https://imkservers.com/stats/index.php?"
style = "style="
#style_name = "0"
style_name = str(input("style_name: "))
map = "&map="
map_name = ""
track = "&track="
#track_name = "0"
track_name = str(input("track_name: "))


#url = "https://imkservers.com/stats/index.php?style=0&map=bhop_anotherboostermap&track=0"

for line in f:
	map_name = line.rstrip()
	url = index + style + style_name + map + map_name + track + track_name
	print(url)
	response = requests.get(url, allow_redirects=True)
	open(style_name + "_" + map_name + "_" + track_name + ".html", "wb").write(response.content)


#response = requests.get(url, allow_redirects=True)

#open("tst.html", "wb").write(response.content)
