from fhir.resources.coding import Coding
import random

allowedValueTypeList = ["Quantity", "CodeableConcept", "String", "Boolean", "Integer", "Range", "Ratio", "SampledData", "Time", "DateTime", "Period"]

def generateComponent(coding: list[Coding], valueType: str, values: list = None):
    # TODO: Handle SampledData and DateTime due to capitalization differently
    valueType = (valueType.lower()).capitalize()
    if valueType not in allowedValueTypeList:
        raise TypeError(f"ValueType must be one of following: {allowedValueTypeList}")

    if valueType == "String":
        generatedValue = random.choice(values)


    component = {
      "code" : {
        "coding" : coding
      },
      f"value{valueType}" : generatedValue
    }

    return component
