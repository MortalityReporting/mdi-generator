import orjson
from src.profiles.bundleDocumentMDItoEDRS import generateBundleDocumentMDItoEDRS
import uuid
from fhirgenerator.helpers.helpers import default


def testBundleDocumentMDItoEDRS():

    resource = generateBundleDocumentMDItoEDRS()

    with open(f'tests/output/test_bundle_document_mdi_to_edrs.json', 'wb') as outfile:
        outfile.write(orjson.dumps(resource, default=default, option=orjson.OPT_NAIVE_UTC))
