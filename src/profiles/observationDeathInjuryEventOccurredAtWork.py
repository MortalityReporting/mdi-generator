from fhirgenerator.resources.r4.observation import generateObservation
from fhir.resources.observation import Observation
from src.cannonicalUrls import observation_DeathInjuryEventOccurredAtWork as cannonical_profile_url
from src.fixedCodes import code_DeathInjuryEventOccurredAtWork as fixed_code


def generateObservationDeathInjuryEventOccurredAtWork(patient_id: str, performer_id: str, start_date: str, days: int) -> dict:
    resource_detail = {}
    resource_detail["codes"] = [fixed_code]
    resource_detail["profile"] = [cannonical_profile_url]
    resource_detail["enumSetList"] = [
        { "coding": [ { "system": "http://terminology.hl7.org/CodeSystem/v2-0136", "code": "Y", "display": "Yes" } ]},
        { "coding": [ { "system": "http://terminology.hl7.org/CodeSystem/v2-0136", "code": "N", "display": "No" } ]},
        { "coding": [ { "system": "http://terminology.hl7.org/CodeSystem/v3-NullFlavor", "code": "NA", "display": "not applicable" } ]}
    ]
    resource = generateObservation(resource_detail, patient_id, start_date, days)
    resource["performer"] = [ {"reference": f'Practitioner/{performer_id}'} ]

    resource = Observation(**resource).dict()
    return resource