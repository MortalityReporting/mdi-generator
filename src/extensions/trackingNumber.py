from fhir.resources.extension import Extension
import uuid

def generateTrackingNumberExtension() -> dict:
    extension = {
      "url" : "http://hl7.org/fhir/us/mdi/StructureDefinition/Extension-tracking-number",
      "valueIdentifier" : {
        "type" : {
          "coding" : [
            {
              "system" : "http://hl7.org/fhir/us/mdi/CodeSystem/CodeSystem-mdi-codes",
              "code" : "mdi-case-number"
            }
          ]
        },
        "value" : str(uuid.uuid4())
      }
    }

    extension = Extension(**extension).dict()
    return extension