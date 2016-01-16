# patentlyclear.py
# python script for accessing patently clear api

import requests

class PatentlyClear:

    def __init__(self, api_token):
        self._api_token = api_token
        self._api_endpoint = "https://api.patentlyclear.com"

    def get_by_id(self, docid):
        """
        Looks up a document by its docid
        Supplying an id that points to multiple resources (such as an application number)
        will return all forms of that document.

        Application ID
        * `api.get_by_id('US20140000001') => {application: {...}}`

        Grant ID
        * `api.get_by_id('US8877876') => {grant: {...}}`

        Application Number (both string and number formats are accepted)
        * `api.get_by_id('13/538,394') => {application: {...}, grant: {...}}`
        * `api.get_by_id(13538394) => {application: {...}, grant: {...}}`
        """
        url = self._api_endpoint + "/" + docid + "?token=" + self._api_token
        response = requests.get(url)
        return response.json()

    def search(self, payload):
        """
        Search for a set of documents with a query payload.

        There are several fields that can be searched on. They are:
        * terms [string]: Perform a full text search with a set of keywords.
        * inventor [string]: Search on inventor name.
        * assignee [string]: Who owns the document.
        * filing_date {before: Date, after: Date}: When the document was filed.
        * publication_date {before: Date, after: Date}: When the document was published.
        * type: [application || grant]: What sort of document it is.
        * size int: Total number of documents to return. (Max = 100)
        """
        url = self._api_endpoint + "/search" + "?token=" + self._api_token
        response = requests.post(url, data=payload)
        return response.json()


    def analyze(self, field, payload):
        """
        Fetches the top trends in a field for a search payload.
        """
        url = self._api_endpoint + "/analyze/" + field + "?token=" + self._api_token
        response = requests.post(url, data=payload)
        return response.json()

    def backward_citation(self, docid, payload=None):
        """
        Fetches the backward citations of `docid` (eg. the documents that `docid` cites.) that match a given search query.
        Optionally provide a search payload to filter documents that are retrieved.
        """
        url = self._api_endpoint + "/backward_citation/" + docid + "?token=" + self._api_token
        response = requests.post(url, data=payload)
        return response.json()

    def forward_citation(self, docid, payload=None):
        """
        Fetches the backward citations of `docid` (eg. the documents that cite `docid`.) that match a given search query.
        Optionally provide a search payload to filter documents that are retrieved.
        """
        url = self._api_endpoint + "/forward_citation/" + docid + "?token=" + self._api_token
        response = requests.post(url, data=payload)
        return response.json()

