# test.py
# written for python 3

from patentlyclear import PatentlyClear

p = PatentlyClear("f9058429-fc9c-43da-9742-a7d0da16b2bd")
#print(p.get_by_id("US8851389"))

print(p.search({"assignee": "google"}))
#print(p.analyze("state", {"assignee": "google"}))
#print(p.backward_citation("US8851389"))
#print(p.forward_citation("US8851389", {"terms": "device"}))
