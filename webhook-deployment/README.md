# How to Deploy `eka-webhook` Python Lambda in an AWS Environment

## Prerequisites

- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
- `curl` and `unzip` installed on your system
- `Docker` installed and running
- `AWS Credentials` to deploy the required Resources. (API GW, Cloudformation, Lambda, ECR)


## Step-by-Step Setup

1. **Configure AWS Credentials**

   ```bash
   aws configure
   ```
   or export your AWS credentials if you are using IAM Identity Center
2. **Download and Extract the Project**

   ```bash
   curl -OL https://sdk-archives.eka.care/ekapython-webhook-sdk/v1/eka-webhook-deployment.zip
   unzip eka-webhook-deployment.zip && cd eka-webhook-deployment
   ```

3. **Configure Environment Variables**

   Edit the `config.env` file with the necessary configuration values. For more detailed configuration setup, refer to [detailed.md](./detailed.md).

   ```bash
   vim config.env
   ```

4. **Make the Deployment Script Executable**

   ```bash
   chmod +x deploy.sh
   ```

## Deployment Commands

- **To Deploy:**

  ```bash
  ./deploy.sh deploy
  ```

- **To Delete:**

  ```bash
  ./deploy.sh delete
  ```