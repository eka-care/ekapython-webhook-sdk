FROM public.ecr.aws/lambda/python:3.10


COPY app.py ${LAMBDA_TASK_ROOT}
COPY ./requirements.txt ${LAMBDA_TASK_ROOT}
COPY ./webhook_consumer.py ${LAMBDA_TASK_ROOT}


CMD ["app.lambda_handler"]