from configparser import ConfigParser

# Initialize the Parser.
config = ConfigParser()

# Add the Section.
config.add_section('graph_api')

# Set the Values.
config.set('graph_api', 'client_id', '_______')
print('set client ID')
config.set('graph_api', 'client_secret', '_______')
print('set client secret')
config.set('graph_api', 'redirect_uri', '_______')
print('set redirect url')

# Write the file.
with open(file='config.ini', mode='w+') as f:
    config.write(f)
    print('config written')
    print(config)
