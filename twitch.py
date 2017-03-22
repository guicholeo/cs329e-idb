import requests

def main():

	#r = requests.get('https://api.twitch.tv/kraken/users/Heinz?client_id=e6xu67x7c493rmp1osdcrnivd3j8g3')
	#print(r.json())

	
	streams = requests.get('https://api.twitch.tv/kraken/streams/?game=The Long Dark&client_id=e6xu67x7c493rmp1osdcrnivd3j8g3')
	stream_json = streams.json()


	stream_data = stream_json["streams"]
	
	print(stream_data[0])

main()