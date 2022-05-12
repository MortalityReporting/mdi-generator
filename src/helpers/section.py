from fhir.resources.composition import CompositionSection
from fhir.resources.coding import Coding

def generateCompositionSection(coding: Coding, resources: list):
    section = {}
    section["code"] = { "coding": [coding] }
    if resources:
        section["entry"] = []
        for resource in resources:
            section["entry"].append({ "reference": f"{resource['resourceType']}/{resource['id']}"})
    else:
        section["text"] = { "status": "empty", "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\">Records Unavailable</div>" }
        section["emptyReason"] = {
            "coding": [
                {
                    "system" : "http://terminology.hl7.org/CodeSystem/list-empty-reason",
                    "code" : "unavailable",
                    "display" : "Unavailable"
                }
            ]
        }

    section = CompositionSection(**section).dict()
    return section