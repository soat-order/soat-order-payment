#!/usr/bin/env bash
 
set -euo pipefail
 
# enable debug
# set -x
 

echo "#########################" 
echo "# Start configuration sqs"
echo "#########################"

AWS_REGION=sa-east-1
#export AWS_PROFILE=soat-order

 
 
# https://docs.aws.amazon.com/cli/latest/reference/sqs/create-queue.html
create_queue() {
    local QUEUE_NAME_TO_CREATE=$1
    # aws --endpoint-url=http://localhost:4566 sqs create-queue --queue-name ${QUEUE_NAME_TO_CREATE} --profile soat-order
    aws --endpoint-url=http://localhost:4566 sqs create-queue --queue-name ${QUEUE_NAME_TO_CREATE} --region $AWS_REGION
}
 
create_queue "sqs-payment-order"
create_queue "sqs-payment-received"
create_queue "sqs-payment-error"
