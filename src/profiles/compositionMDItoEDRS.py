from src.cannonicalUrls import composition_MDItoEDRS, loinc
from src.helpers.unique_identifier import generateUniqueIdentifier
from fhir.resources.composition import Composition
from fhirgenerator.helpers.helpers import makeRandomDate
import uuid

def generateCompositionMDItoEDRS(subject_id: str, practitioner_id: str, start_date: str) -> dict:
    composition = {}
    composition["resourceType"] = "Composition"
    
    composition["id"] = str(uuid.uuid4())
    composition["meta"] = {}
    composition["meta"]["profile"] = [ composition_MDItoEDRS ]
    composition["status"] = "final"
    
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

def generateTrackingNumberExtension() -> dict:
    return {}

def addSection(composition, section) -> dict:
    if not "section" in composition.keys():
        composition["section"] = []
    composition["section"].append(section)
    return composition