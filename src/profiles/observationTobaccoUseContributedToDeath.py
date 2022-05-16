from fhirgenerator.resources.r4.observation import generateObservation
from fhir.resources.observation import Observation
from src.cannonicalUrls import observation_TobaccoUseContributedToDeath


def generateObservationTobaccoUseContributedToDeath(patient_id: str, performer_id: str, start_date: str, days: int) -> dict:
    fixed_code = { "system": "http://loinc.org", "code": "69443-0", "display": "Did tobacco use contribute to death" }

    resource_detail = {}
    resource_detail["codes"] = [fixed_code]
    resource_detail["profile"] = [observation_TobaccoUseContributedToDeath]
    resource_detail["enumSetList"] = [
        { "coding": [ { "system": "http://snomed.info/sct", "code": "373066001", "display": "Yes" } ]},
        { "coding": [ { "system": "http://snomed.info/sct", "code": "373067005", "display": "No" } ]},
        { "coding": [ { "system": "http://snomed.info/sct", "code": "2931005", "display": "Probably" } ]},
        { "coding": [ { "system": "http://terminology.hl7.org/CodeSystem/v3-NullFlavor", "code": "UNK", "display": "Unknown" } ]},
        { "coding": [ { "system": "http://terminology.hl7.org/CodeSystem/v3-NullFlavor", "code": "NASK", "display": "not asked" } ]}
    ]
    resource = generateObservation(resource_detail, patient_id, start_date, days)
    resource["performer"] = [ {"reference": f'Practitioner/{performer_id}'} ]

    resource = Observation(**resource).dict()
    return resource