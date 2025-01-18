import requests

file_source = "https://theweekinchess.com/zips/twic{}g.zip"
destination_folder = "/Users/aya/Desktop/chess_pgns/"
destination = destination_folder + "{}.zip"


for i in range(920,1574):
    url = file_source.format(i)
    file_name = destination.format(i)
    print(file_name)

    response = requests.get(url)

    with open(file_name, 'wb') as f:
        f.write(response.content)

