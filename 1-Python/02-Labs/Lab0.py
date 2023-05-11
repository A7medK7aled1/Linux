import facebook

# Set up your access token and Facebook Graph API object
access_token = 'YOUR_ACCESS_TOKEN'
graph = facebook.GraphAPI(access_token)

# Post a message on your Facebook page
message = 'Hello, world!'
graph.put_object(parent_object='me', connection_name='feed', message=message)
