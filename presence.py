from typing import Dict
from session import GraphSession


class Presence():

    """
    ## Overview:
    ----
    You can use Microsoft Graph to build compelling app experiences
    based on users, their relationships with other users and groups,
    and their mail, calendar, and files.
    """

    def __init__(self, session: object) -> None:
        """Initializes the `Users` object.

        ### Parameters
        ----
        session : object
            An authenticated session for our Microsoft Graph Client.
        """

        # Set the session.
        self.graph_session: GraphSession = session

        # Set the endpoint.
        self.endpoint = 'me/presence'

    def list_presence(self) -> Dict:
        """Retrieve a list of user objects.

        ### Returns
        ----
        Dict :
            If successful, this method returns a 200 OK response code
            and collection of user objects in the response body. If a
            large user collection is returned, you can use paging in your
            app.
        """

        content = self.graph_session.make_request(
            method='get',
            endpoint=self.endpoint
        )

        return content
