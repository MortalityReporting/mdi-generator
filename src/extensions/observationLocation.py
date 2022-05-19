from fhir.resources.extension import Extension
from src.cannonicalUrls import extension_ObservationLocation as cannonical_url

def generateObservationLocationExtension(location_id):
    extension = {
      "url" : cannonical_url,
      "valueReference" : {
          "reference" : f"Location/{location_id}"
      }
    }

    extension = Extension(**extension).dict()
    return extension