from flask import Flask
import ibm_boto3
from ibm_botocore.client import Config, ClientError

COS_ENDPOINT="https://s3.jp-tok.cloud-object-storage.appdomain.cloud"
COS_API_KEY_ID="eMcex_1Ai5Ee0zdY02faN3xOI11a0n00ousBac2XmyeT"
COS_INSTANCE_CRN="crn:v1:bluemix:public:cloud-object-storage:global:a/fd8584e5ab4b4110b3cdf639fd12266c:43ac326a-7436-4af1-ab27-4359450ec159::"

cos = ibm_boto3.resource("s3",
    ibm_api_key_id=COS_API_KEY_ID,
    ibm_service_instance_id=COS_INSTANCE_CRN,
    config=Config(signature_version="oauth"),
    endpoint_url=COS_ENDPOINT
)

def get_item(jeevika, nutri3.jpg):
    print("Retrieving item from bucket: {0}, key: {1}".format(jeevika, nutri3.jpg))
    try:
        file = cos.Object(jeevika, nutri3.jpg).get()

        print("File Contents: {0}".format(file["Body"].read()))
    except ClientError as be:
        print("CLIENT ERROR: {0}\n".format(be))
    except Exception as e:
        print("Unable to retrieve file contents: {0}".format(e))

if __name__=='__main__':
    app.run(host='0.0.0.0',port=8080,debug=True)

