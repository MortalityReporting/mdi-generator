from fhirgenerator.resources.r4.observation import generateObservation
from fhir.resources.observation import Observation
from src.cannonicalUrls import observation_CauseOfDeathCondition


def generateObservationProfile(config: dict, patient_id: str, performer_id: str, start_date: str, days: int) -> dict:
    resource = {}


    


    resource = Observation(**resource).dict()
    return resource