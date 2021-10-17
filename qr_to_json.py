import re
import base64
import json
import zlib
from pprint import pprint

rawSHC = "shc:/12345............" # REPLACE with value from your QR scan

rawSHC = rawSHC.split('/')[1];
jwt = "".join([chr(int(element, 10)+45) for element in re.findall(r"(..?)", rawSHC)])
splitJwt = jwt.split(".")
#print(splitJwt)

'''
padded = splitJwt[0] + "="*divmod(len(splitJwt[0]),4)[1]
jsondata = base64.urlsafe_b64decode(padded)
header = json.loads(jsondata)
pprint(header)
'''

decompressor = zlib.decompressobj(wbits=-15)
padded = splitJwt[1] + "="*divmod(len(splitJwt[1]),4)[1]
payload = json.loads(decompressor.decompress(base64.urlsafe_b64decode(padded)))
pprint(payload.get("vc").get("credentialSubject").get("fhirBundle").get("entry"))
