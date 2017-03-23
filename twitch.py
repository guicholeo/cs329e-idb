import requests

def main():

	#r = requests.get('https://api.twitch.tv/kraken/users/Heinz?client_id=e6xu67x7c493rmp1osdcrnivd3j8g3')
	#print(r.json())

	
	streams = requests.get('https://api.twitch.tv/kraken/channels/pokimane?client_id=e6xu67x7c493rmp1osdcrnivd3j8g3')
	stream_json = streams.json()


	print(stream_json)
main()