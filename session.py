import json as json_lib
import requests
import logging
import pathlib

from typing import Dict


class GraphSession():

    """Serves as the Session for the Current Microsoft
    Graph API."""

    def __init__(self, client: object) -> None:
        """Initializes the `GraphSession` client.

        ### Overview:
        ----
        The GraphSession object handles all the requests made
        for the different endpoints on the Microsoft Graph API.

        ### Arguments:
        ----
        client (str): The Microsoft Graph API Python Client.

        ### Usage:
        ----
            >>> graph_session = GraphSession()
        """

        from client import MicrosoftGraphClient

        # We can also add custom formatting to our log messages.
        log_format = '%(asctime)-15s|%(filename)s|%(message)s'

        if not pathlib.Path('logs').exists():
            pathlib.Path('logs').mkdir()
            pathlib.Path('logs/log_file_custom.log').touch()

        self.client: MicrosoftGraphClient = client
        logging.basicConfig(
            filename="logs/log_file_custom.log",
            level=logging.INFO,
            encoding="utf-8",
            format=log_format
        )

    def build_headers(self, mode: str = 'json') -> Dict:
        """Used to build the headers needed to make the request.

        ### Parameters
        ----
        mode: str, optional
            The content mode the headers is being built for, by default `json`.

        ### Returns
        ----
        Dict:
            A dictionary containing all the components.
        """

        # Fake the headers.
        headers = {
            "Authorization": "Bearer {access_token}".format(access_token=self.client.access_token)
        }

        return headers

    def build_url(self, endpoint: str) -> str:
        """Build the URL used the make string.

        ### Parameters
        ----
        endpoint : str
            The endpoint used to make the full URL.

        ### Returns
        ----
        str:
            The full URL with the endpoint needed.
        """

        url = self.client.RESOURCE + self.client.api_version + "/" + endpoint

        return url

    def make_request(self, method: str, endpoint: str, mode: str = None, params: dict = None,
                     data: dict = None, json: dict = None, order_details: bool = False) -> Dict:
        """Handles all the requests in the library.

        ### Overview:
        ---
        A central function used to handle all the requests made in the library,
        this function handles building the URL, defining Content-Type, passing
        through payloads, and handling any errors that may arise during the request.

        ### Arguments:
        ----
        method: The Request method, can be one of the
            following: ['get','post','put','delete','patch']

        endpoint: The API URL endpoint, example is 'quotes'

        mode: The content-type mode, can be one of the
            following: ['form','json']

        params: The URL params for the request.

        data: A data payload for a request.

        json: A json data payload for a request

        ### Returns:
        ----
        A Dictionary object containing the JSON values.
        """

        # Build the URL.
        url = self.build_url(endpoint=endpoint)

        # Define the headers.
        headers = self.build_headers(mode='json')

        logging.info(
            "URL: {url}".format(url=url)
        )

        # Define a new session.
        request_session = requests.Session()
        request_session.verify = True

        # Define a new request.
        request_request = requests.Request(
            method=method.upper(),
            headers=headers,
            url=url,
            params=params,
            data=data,
            json=json
        ).prepare()

        # Send the request.
        response: requests.Response = request_session.send(
            request=request_request
        )

        # Close the session.
        request_session.close()

        # If it's okay and no details.
        if response.ok and len(response.content) > 0:
            return response.json()
        elif len(response.content) > 0 and response.ok:
            return {
                'message': 'response successful',
                'status_code': response.status_code
            }
        elif not response.ok:

            # Define the error dict.
            error_dict = {
                'error_code': response.status_code,
                'response_url': response.url,
                'response_body': json_lib.loads(response.content.decode('ascii')),
                'response_request': dict(response.request.headers),
                'response_method': response.request.method,
            }

            # Log the error.
            logging.error(
                msg=json_lib.dumps(obj=error_dict, indent=4)
            )

            raise requests.HTTPError()
