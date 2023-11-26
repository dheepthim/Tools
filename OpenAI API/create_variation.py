from openai import OpenAI
import requests

client = OpenAI()

response = client.images.create_variation(
  image = open("OpenAI API/PNGs/image4.png", "rb"),
  model = "dall-e-2",
  n = 1,
  response_format = "url",
  size = "1024x1024"
)

data = requests.get(response.data[0].url).content
with open('OpenAI API/Variations/variations4-1.png', 'wb') as fh:
  fh.write(data)