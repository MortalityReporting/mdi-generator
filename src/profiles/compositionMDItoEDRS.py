from src.cannonicalUrls import composition_MDItoEDRS, loinc
from src.extensions.trackingNumber import generateTrackingNumberExtension
from src.helpers.unique_identifier import generateUniqueIdentifier
from fhir.resources.composition import Composition, CompositionSection
from fhir.resources.coding import Coding
from fhirgenerator.helpers.helpers import makeRandomDate
import uuid

def generateCompositionMDItoEDRS(subject_id: str, practitioner_id: str, start_date: str) -> dict:
    composition = {}
    composition["resourceType"] = "Composition"
    
    composition["id"] = str(uuid.uuid4())
    composition["meta"] = {}
    composition["meta"]["profile"] = [ composition_MDItoEDRS ]
    composition["status"] = "final"

    composition["extension"] = []
    composition["extension"].append(generateTrackingNumberExtension())
    
    composition["identifier"] = generateUniqueIdentifier()
    composition["subject"] = { "reference": f"Patient/{subject_id}"}
    composition["author"] = [{ "reference": f"Practitioner/{practitioner_id}"}]
    composition["title"] = "MDI to EDRS Composition"
    
    composition["type"] = {}
    composition["type"]["coding"] = []
    composition["type"]["coding"].append({ "system": loinc, "code": "86807-5", "display": "Death administrative information Document"})

    composition["date"] = makeRandomDate(start_date, 1)

    composition = Composition(**composition).dict()
    return composition


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

def addSection(composition, section) -> dict:
    if not "section" in composition.keys():
        composition["section"] = []
    composition["section"].append(section)
    return composition