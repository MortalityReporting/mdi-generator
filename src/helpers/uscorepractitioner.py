from fhir.resources.practitioner import Practitioner

def getUsCorePractitioner() -> dict:
    practitioner = {
        "resourceType" : "Practitioner",
        "id" : "static-practitioner",
        "meta" : {
            "profile" : [
            "http://hl7.org/fhir/us/core/StructureDefinition/us-core-practitioner"
            ]
        },
        "identifier" : [
            {
            "system" : "http://hl7.org.fhir/sid/us-npi",
            "value" : "9912345678"
            },
            {
            "system" : "http://www.acme.org/practitioners",
            "value" : "25456"
            }
        ],
        "name" : [
            {
            "family" : "Generator",
            "given" : [
                "MDI"
            ],
            "prefix" : [
                "Dr"
            ]
            }
        ],
        "address" : [
            {
            "use" : "home",
            "line" : [
                "1555 MDI Drive"
            ],
            "city" : "Atlanta",
            "state" : "GA",
            "postalCode" : "33333"
            }
        ]
        }
    
    practitioner = Practitioner(**practitioner).dict()
    return practitioner
