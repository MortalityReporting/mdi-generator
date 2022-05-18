from fhirgenerator.resources.r4.observation import generateObservation
from fhir.resources.observation import Observation
from src.cannonicalUrls import observation_HowDeathInjuryOccurred as cannonical_profile_url
from src.fixedCodes import code_HowDeathInjuryOccurred as fixed_code

def generateObservationHowDeathInjuryOccurred(howDeathInjuryOccurredList, patient_id: str, performer_id: str, start_date: str, days: int) -> dict:
    resource_detail = {}
    resource_detail["codes"] = [fixed_code]
    resource_detail["profile"] = [cannonical_profile_url]
    resource_detail["enumSetList"] = howDeathInjuryOccurredList
    resource = generateObservation(resource_detail, patient_id, start_date, days)
    resource["performer"] = [ {"reference": f'Practitioner/{performer_id}'} ]

    
    resource = Observation(**resource).dict()
    return resource