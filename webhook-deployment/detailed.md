# Configuration Options Documentation for Eka Webhook Deployment

## Overview

This documentation covers all configuration options used in the Eka webhook deployment process as defined in `config.env`. These settings are used by the deployment script and CloudFormation template to provision and configure required AWS resources.

## Stack Configuration

| Parameter | Description | Service |
|-----------|-------------|---------|
| `STACK_NAME` | Name of the CloudFormation stack to be created or updated | AWS CloudFormation |
| `TEMPLATE_FILE` | Path to the CloudFormation template file | AWS CloudFormation |
| `REGION` | AWS region where resources will be deployed | All AWS services |

## Docker Image Configuration

| Parameter | Description | Service |
|-----------|-------------|---------|
| `DOCKER_IMAGE_VERSION` | Version tag of the Docker image to pull from DockerHub | Docker, ECR | You can get the latest version at https://github.com/eka-care/ekapython-webhook-sdk/releases
| `AWS_ACCOUNT_ID` | AWS account ID for constructing ECR repository URL | ECR |
| `ECR_REPO_NAME` | Name of the ECR repository to store Lambda container image | ECR |

## API Gateway Configuration

| Parameter | Description | Service |
|-----------|-------------|---------|
| `API_GW_NAME` | Name for the API Gateway instance | API Gateway |
| `STAGE_NAME` | Deployment stage name for API Gateway (e.g., prod, dev) | API Gateway |

## Custom Domain Configuration

| Parameter | Description | Service |
|-----------|-------------|---------|
| `EXTERNAL_URL` | External URL that will be used as the custom domain | API Gateway, Route 53 |
| `HOSTED_ZONE_ID` | ID of the Route 53 hosted zone for DNS configuration | Route 53 |
| `CERTIFICATE_ARN` | ARN of the ACM certificate for HTTPS on the custom domain | ACM, API Gateway |

## Lambda Configuration

| Parameter | Description | Service |
|-----------|-------------|---------|
| `LAMBDA_NAME` | Name for the Lambda function that will process webhook requests | Lambda |

## AWS Services Used

- **AWS CloudFormation**: Infrastructure as code service for stack management
- **Amazon ECR**: Container registry for storing webhook Lambda container images
- **AWS Lambda**: Serverless compute service for webhook request processing
- **Amazon API Gateway**: API management service for creating REST endpoints
- **Amazon Route 53**: DNS service for custom domain configuration
- **AWS Certificate Manager (ACM)**: Certificate service for HTTPS configuration

The deployment workflow pulls a Docker image from DockerHub, pushes it to ECR, then uses CloudFormation to provision and configure all the required AWS resources according to these configuration parameters.