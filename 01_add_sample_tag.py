import requests

api_key = 'asdf1234asdf1234asdf1234'

sample_id = '<SAMPLE_ID>'

tag = 'MyTag'

url = 'https://panacea.threatgrid.com/api/v2/samples/{}/tag?api_key={}&tag={}'.format(sample_id, api_key, tag)

r = requests.post(url)

print(r.json())
