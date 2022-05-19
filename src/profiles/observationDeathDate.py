from fhirgenerator.resources.r4.observation import generateObservation, generateObservationComponent
from fhir.resources.observation import Observation
from src.cannonicalUrls import observation_DeathDate as cannonical_profile_url
from src.fixedCodes import code_DeathDate as fixed_code
from src.fixedCodes import code_PronouncedDeadComponent
from src.extensions.observationLocation import generateObservationLocationExtension


def generateObservationDeathDate(config: dict, location_id: str, patient_id: str, performer_id: str, start_date: str, days: int) -> dict:
    resource_detail = {}
    resource_detail["codes"] = [fixed_code]
    resource_detail["profile"] = [cannonical_profile_url]
    resource_detail["dateRange"] = config['deathDateRange']
    resource = generateObservation(resource_detail, patient_id, start_date, days)
    resource["performer"] = [ {"reference": f'Practitioner/{performer_id}'} ]

    resource["extension"] = [generateObservationLocationExtension(location_id)]

    component_detail = {}
    component_detail["codes"] = [code_PronouncedDeadComponent]
    component_detail["dateRange"] = config['deathDateRange']
    resource["component"] = [generateObservationComponent(component_detail, resource["effectiveDateTime"])]

    resource = Observation(**resource).dict()
    return resource