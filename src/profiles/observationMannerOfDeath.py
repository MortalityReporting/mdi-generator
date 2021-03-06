from fhirgenerator.resources.r4.observation import generateObservation
from fhir.resources.observation import Observation
from src.cannonicalUrls import observation_MannerOfDeath as cannonical_profile_url
from src.fixedCodes import code_MannerOfDeath as fixed_code


def generateObservationMannerOfDeath(patient_id: str, performer_id: str, start_date: str, days: int) -> dict:
    resource_detail = {}
    resource_detail["codes"] = [fixed_code]
    resource_detail["profile"] = [cannonical_profile_url]
    resource_detail["enumSetList"] = [
        { "coding": [ { "system": "http://snomed.info/sct", "code": "38605008", "display": "Nautral death (event)" } ]},
        { "coding": [ { "system": "http://snomed.info/sct", "code": "7878000", "display": "Accidental death (event)" } ]},
        { "coding": [ { "system": "http://snomed.info/sct", "code": "44301001", "display": "Suicide (event)" } ]},
        { "coding": [ { "system": "http://snomed.info/sct", "code": "27935005", "display": "Homicide (event)" } ]},
        { "coding": [ { "system": "http://snomed.info/sct", "code": "185973002", "display": "Patient awaiting investigation (finding)" } ]},
        { "coding": [ { "system": "http://snomed.info/sct", "code": "65037004", "display": "Death, manner undetermined (event)" } ]}
    ]
    resource = generateObservation(resource_detail, patient_id, start_date, days)
    resource["performer"] = [ {"reference": f'Practitioner/{performer_id}'} ]


    resource = Observation(**resource).dict()
    return resource