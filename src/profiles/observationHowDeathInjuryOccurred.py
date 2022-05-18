from fhirgenerator.resources.r4.observation import generateObservation
from fhir.resources.observation import Observation
from src.cannonicalUrls import observation_HowDeathInjuryOccurred


def generateObservationHowDeathInjuryOccurred(howDeathInjuryOccurredList, patient_id: str, performer_id: str, start_date: str, days: int) -> dict:
    fixed_code = { "system": "http://loinc.org", "code": "11374-6", "display": "Injury incident description Narrative" }

    resource_detail = {}
    resource_detail["codes"] = [fixed_code]
    resource_detail["profile"] = [observation_HowDeathInjuryOccurred]
    resource_detail["enumSetList"] = howDeathInjuryOccurredList
    resource = generateObservation(resource_detail, patient_id, start_date, days)
    resource["performer"] = [ {"reference": f'Practitioner/{performer_id}'} ]

    
    resource = Observation(**resource).dict()
    return resource