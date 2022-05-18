from fhirgenerator.resources.r4.observation import generateObservation
from fhir.resources.observation import Observation
from src.cannonicalUrls import observation_DeathDate as cannonical_profile_url
from src.fixedCodes import code_DeathDate as fixed_code


def generateObservationDeathDate(config: dict, location_id: str, patient_id: str, performer_id: str, start_date: str, days: int) -> dict:
    resource_detail = {}
    resource_detail["codes"] = [fixed_code]
    resource_detail["profile"] = [cannonical_profile_url]
    resource_detail["dateRange"] = config['deathDateRange']
    resource = generateObservation(resource_detail, patient_id, start_date, days)
    resource["performer"] = [ {"reference": f'Practitioner/{performer_id}'} ]

    # TODO: Implement once valueDateTime available.

    # TODO: Set Location

    # TODO: Set Pronounced Dead Component
    
    resource = Observation(**resource).dict()
    return resource