from fhirgenerator.resources.r4.observation import generateObservation
from fhir.resources.observation import Observation
from src.cannonicalUrls import observation_ConditionContributingToDeath as cannonical_profile_url
from src.fixedCodes import code_ConditionContributingToDeath as fixed_code

def generateObservationConditionContributingToDeath(contributingCauseList: dict, patient_id: str, performer_id: str, start_date: str, days: int) -> dict:
    resource_detail = {}
    resource_detail["codes"] = [fixed_code]
    resource_detail["enumSetList"] = contributingCauseList
    resource_detail["profile"] = [cannonical_profile_url]
    resource = generateObservation(resource_detail, patient_id, start_date, days)

    #resource["meta"] = { "profile": [ observation_ConditionContributingToDeath ] }
    resource["performer"] = [ {"reference": f'Practitioner/{performer_id}'} ]
    resource["valueCodeableConcept"] = { "text": resource["valueString"]}
    resource.pop("valueString")
    
    resource = Observation(**resource).dict()
    return resource