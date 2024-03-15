import requests

url = 'https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.worldwildlife.org%2Fspecies%2Ftiger&psig=AOvVaw3eCVGOMSq6KnwaGlq0MZgO&ust=1709331164854000&source=images&cd=vfe&opi=89978449&ved=0CBMQjRxqFwoTCJjh1vrI0YQDFQAAAAAdAAAAABAJ'
filename = url.split('/')[-1]
r = requests.get(url, allow_redirects=True)
open(filename, 'wb').write(r.content)

# vars needed
bucket_name = str
object_name = str
expires_in = int

response = s3.generate_presigned_url(
    'get_object',
    Params={'Bucket': bucket_name, 'Key': object_name},
    ExpiresIn=expires_in
    )