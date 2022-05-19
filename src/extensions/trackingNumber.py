from fhir.resources.extension import Extension
import uuid
from src.cannonicalUrls import extension_TrackingNumber as cannonical_url

def generateTrackingNumberExtension() -> dict:
    extension = {
      "url" : cannonical_url,
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