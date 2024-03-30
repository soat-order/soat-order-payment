from enum import Enum

class Contants(Enum):
    # http://sqs.sa-east-1.localhost.localstack.cloud:4566/000000000000
    SQS_HOST = "http://localhost:4566"
    # SQS_HOST = "http://sqs.sa-east-1.localhost.localstack.cloud:4566"
    SQS_HOST_QUEUE = "{}/000000000000".format(SQS_HOST)
    AWS_REGION = "sa-east-1"
    AWS_ACCESS_KEY = ""
    AWS_SECRET_KEY = ""
