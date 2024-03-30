import boto3
import json
from src.core.util.logger_custom import Logger
from src.core.domain.enum.constants import Contants
from src.core.util.json_util import JsonUtil

class SqsProducer:
    def __init__(self) -> None:
        Logger.info(method=Logger.getMethodCurrent(), message="Start config to SQS producer")
        self.__sqsClient = boto3.client(
            service_name="sqs",
            region_name=Contants.AWS_REGION.value,
            endpoint_url=Contants.SQS_HOST.value
        ) 

        # session = boto3.Session(profile_name='default')
        # self.__sqsClient = session.client(
        #     service_name='sqs',
        #     region_name=Contants.AWS_REGION.value,
        #     endpoint_url=Contants.SQS_HOST.value,
        #     use_ssl=False
        # ) 

        # self.__sqsClient = boto3.client(
        #     'sqs',            
        #     region_name=Contants.AWS_REGION.value,
        #     endpoint_url=Contants.SQS_HOST.value,
        #     aws_access_key_id="jvds",
        #     aws_secret_access_key="jvds"
        # )    


    def send_message(self, queue_name: str, payload) -> bool:
        try:        
            # Logger.info(method=Logger.getMethodCurrent(), message=f"Start sending message to SQS queue: {queue_name}", data=payload)
            
            Logger.info(method=Logger.getMethodCurrent(), message=f"Start sending message to SQS queue: {queue_name}")            
            print("===========================================")            
            print(json.dumps(payload.toDict()))
            print("{}/{}".format(Contants.SQS_HOST_QUEUE.value, queue_name))
            response = self.__sqsClient.send_message(                
                # QueueUrl="{}/000000000000/{}".format(Contants.SQS_HOST_QUEUE.value, queue_name),                
                # MessageBody=JsonUtil.parseObjectToJson(payload.toDict())
                QueueUrl=queue_name,
                MessageBody=JsonUtil.parseObjectToJson(payload.toDict())
            )
            Logger.info(method=Logger.getMethodCurrent(), message=f"Done sending message to SQS queue: {queue_name}", data=response)
        except Exception as ex:
            Logger.error(method=Logger.getClassMethodCurrent(), message=f"Error sending message to sqs queue {queue_name} exception: {str(ex)}")
            return False;
        return True;
