from fhirgenerator.resources.r4.observation import generateObservation
from fhir.resources.observation import Observation
from src.cannonicalUrls import observation_DecedentPregnancy as cannonical_profile_url
from src.fixedCodes import code_DecedentPregnancy as fixed_code

def generateObservationDecedentPregnancy(patient_id: str, performer_id: str, start_date: str, days: int) -> dict:
    resource_detail = {}
    resource_detail["codes"] = [fixed_code]
    resource_detail["profile"] = [cannonical_profile_url]
    resource_detail["enumSetList"] = [
        { "coding": [ { "system": "http://hl7.org/fhir/us/mdi/CodeSystem/CodeSystem-death-pregnancy-status", "code": "1", "display": "Not pregnant within past year" } ]},
        { "coding": [ { "system": "http://hl7.org/fhir/us/mdi/CodeSystem/CodeSystem-death-pregnancy-status", "code": "2", "display": "Pregnant at time of death" } ]},
        { "coding": [ { "system": "http://hl7.org/fhir/us/mdi/CodeSystem/CodeSystem-death-pregnancy-status", "code": "3", "display": "Not pregnant, but pregnant within 42 days of death" } ]},
        { "coding": [ { "system": "http://hl7.org/fhir/us/mdi/CodeSystem/CodeSystem-death-pregnancy-status", "code": "4", "display": "Not pregnant, but pregnant 43 days to 1 year before death" } ]},
        { "coding": [ { "system": "http://hl7.org/fhir/us/mdi/CodeSystem/CodeSystem-death-pregnancy-status", "code": "9", "display": "Unknown if pregnant within the past year" } ]},
        { "coding": [ { "system": "http://terminology.hl7.org/CodeSystem/v3-NullFlavor", "code": "NA", "display": "Not applicable" } ]}
    ]
    resource = generateObservation(resource_detail, patient_id, start_date, days)
    resource["performer"] = [ {"reference": f'Practitioner/{performer_id}'} ]

    resource = Observation(**resource).dict()
    return resource