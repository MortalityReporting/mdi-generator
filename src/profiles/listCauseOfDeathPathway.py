from fhir.resources.list import List
from src.cannonicalUrls import list_CauseOfDeathPathway
import uuid
import random

def generateListCauseOfDeathPathway(observationCauseOfDeathConditionList: list, subject_id: str, practitioner_id: str) -> dict:
    list = {}
    
    list["id"] = str(uuid.uuid4())
    list["meta"] = { "profile": [list_CauseOfDeathPathway] }
    list["status"] = "current"
    list["mode"] = "snapshot"
    list["entry"] = []

    list["subject"] = { "reference": f"Patient/{subject_id}"}
    list["source"] = { "reference": f"Practitioner/{practitioner_id}"}

    for resource in observationCauseOfDeathConditionList:
        list["entry"].append({ "item": { "reference": f"Observation/{resource['id']}" }})

    list = List(**list).dict()

    return list