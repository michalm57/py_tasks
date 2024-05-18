# Example post
# user_id = 209
# message = "Test message example"
# language = "English"
# datetime = "20230215T124231Z"
# location = (44.590533, -104.715556)

post = {"user_id":209, "message":"Test message example", "language": "English", "datetime": "20230215T124231Z", "location": "(44.590533, -104.715556)"}

type(post)
# <class 'dict'>

# Another way to create dictionary
post2 = dict(message="SS Cotopaxi", language="English")

# Accessing Data in Dictionaries
post['message']

# Handle possibility of the key error
if 'location' in post:
    print(post['location'])
else:
    print("The post does not contain a location value.")
    
try:
    print(post['location'])
except KeyError:
    print("The post does not contain a location value.")
    
# Another way to access the data, get method
post.get('location', None)

for key in post.keys():
    value = post[key]
    print(key, "=", value)
    
for key, value in post.items():
    print(key, "=", value)