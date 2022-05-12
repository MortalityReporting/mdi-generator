from fhirgenerator.resources.r4.observation import generateObservation
from fhir.resources.observation import Observation
from src.cannonicalUrls import observation_CauseOfDeathCondition
import random
from src.helpers.component import generateComponent

# https://build.fhir.org/ig/HL7/fhir-mdi-ig/ValueSet-ValueSet-units-of-age.html
ValueSet_units_of_age = ["min", "d", "h", "mo", "a", "UNK"]
system_ucum = "http://unitsofmeasure.org"
system_null_flavor = "http://terminology.hl7.org/CodeSystem/v3-NullFlavor"

def generateObservationCauseOfDeathCondition(causeOfDeathList: list, patient_id: str, performer_id: str, start_date: str, days: int) -> dict:
    fixed_profile = observation_CauseOfDeathCondition
    fixed_code = { "system": "http://loinc.org", "code": "69453-9" }

    resource_detail = {}
    resource_detail["codes"] = [fixed_code]
    resource_detail["enumSetList"] = causeOfDeathList
    resource = generateObservation(resource_detail, patient_id, start_date, days)

    resource["meta"] = { "profile": [ fixed_profile ] }
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
      "coding" : [
        {
          "system" : "http://loinc.org",
          "code" : "69440-6",
          "display" : "Disease onset to death interval"
        }
      ]
    },
    "valueQuantity" : generateIntervalQuantity()
  }
  return interval

def generateIntervalQuantity() -> dict:
  interval = {
    "code": random.choice(ValueSet_units_of_age)
  }
  if interval["code"] == "UNK":
    interval["system"] = system_null_flavor
  else:
    interval["system"] = system_ucum
    interval["value"] = int(round(random.uniform(1, 10)))
  return interval