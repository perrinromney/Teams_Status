def fetch_presence():
    from pprint import pprint
    from configparser import ConfigParser
    from client import MicrosoftGraphClient
    from pprint import pprint

    scopes = [
        'User.Read',
        'Presence.Read',
        'Presence.Read.All'
    ]

    # Initialize the Parser.
    config = ConfigParser()

    # Read the file.
    print(config.read('config.ini'))
    

    # Get the specified credentials.
    client_id = config.get('graph_api', 'client_id')
    client_secret = config.get('graph_api', 'client_secret')
    redirect_uri = config.get('graph_api', 'redirect_uri')

    # Initialize the Client.
    graph_client = MicrosoftGraphClient(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri,
        scope=scopes,
        credentials='ms_graph_state.jsonc'
    )

    # Login to the Client.
    graph_client.login()

    # Grab the User Services.
    # users = graph_client.users()
    presence = graph_client.presence()
    import json
    printPresence = presence.list_presence()

    # List the Users.
    pprint(printPresence)
    return printPresence
