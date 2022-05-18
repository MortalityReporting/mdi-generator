from fhirgenerator.resources.r4.observation import generateObservation
from fhir.resources.observation import Observation
from src.cannonicalUrls import observation_CauseOfDeathCondition as cannonical_profile_url
from src.cannonicalUrls import system_ucum, system_null_flavor
from src.fixedCodes import code_CauseOfDeathCondition as fixed_code
from src.fixedCodes import code_IntervalComponent
import random

def generateObservationCauseOfDeathCondition(causeOfDeathList: list, patient_id: str, performer_id: str, start_date: str, days: int) -> dict:
    resource_detail = {}
    resource_detail["codes"] = [fixed_code]
    resource_detail["enumSetList"] = causeOfDeathList
    resource = generateObservation(resource_detail, patient_id, start_date, days)

    resource["meta"] = { "profile": [ cannonical_profile_url ] }
    resource["performer"] = [ {"reference": f'Practitioner/{performer_id}'} ]
    interval_component = generateIntervalComponent()
    resource["component"] = [interval_component]
    resource["valueCodeableConcept"] = { "text": resource["valueString"]}
    resource.pop("valueString")

    resource = Observation(**resource).dict()
    return resource

def generateIntervalComponent() -> dict:
  interval = {
    "code" : {
      "coding" : [ code_IntervalComponent ]
    },
    "valueQuantity" : generateIntervalQuantity()
  }
  return interval

def generateIntervalQuantity() -> dict:
  # https://build.fhir.org/ig/HL7/fhir-mdi-ig/ValueSet-ValueSet-units-of-age.html
  ValueSet_units_of_age = ["min", "d", "h", "mo", "a", "UNK"]
  interval = {
    "code": random.choice(ValueSet_units_of_age)
  }
  if interval["code"] == "UNK":
    interval["system"] = system_null_flavor
  else:
    interval["system"] = system_ucum
    interval["value"] = int(round(random.uniform(1, 10)))
  return interval