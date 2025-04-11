FROM public.ecr.aws/lambda/python:3.11

WORKDIR /app

COPY . .

CMD ["webhook_sdk.app.lambda_handler"]