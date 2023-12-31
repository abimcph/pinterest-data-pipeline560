# Pinterest Data Pipeline

## Table of Contents
- [Project Description](#project-description)
- [Installation Instructions](#installation-instructions)
- [Usage Instructions](#usage-instructions)
- [File Structure](#file-structure)
- [License](#license)

## Project Description
### What the Project Does
The Pinterest Data Pipeline project simulates a complex data ingestion, processing, and analysis system using AWS and Databricks, akin to the massive data operations at Pinterest. It integrates services like Amazon MSK (Managed Streaming for Apache Kafka), EC2, S3, and AWS Kinesis for stream and batch data handling, coupled with Databricks for powerful data processing and analytics.

### Aim of the Project
The aim is to understand and construct a scalable, distributed data pipeline that reflects real-world big data use cases. By building this project, one learns to handle vast amounts of data in various formats, process it in real-time and batch modes, and perform complex analytical queries to derive insights.

### What I Learned
- Setting up and configuring AWS services for data handling.
- Integrating Amazon MSK with EC2 and S3 for data streaming and storage.
- Constructing and deploying data pipelines using AWS MWAA (Amazon Managed Workflows for Apache Airflow).
- Implementing real-time and batch data processing with AWS Kinesis and Databricks.
- Best practices for data security, efficiency, and scalability in cloud-based data solutions.

## Installation Instructions
1. **AWS Setup**: Create an AWS account and set up the necessary services: MSK, EC2, S3, MWAA, and Kinesis as per the AWS Management Console's guidelines.
2. **Databricks Setup**: Create a Databricks workspace and configure it to interact with your AWS environment.
3. **Local Environment**: For simulation scripts, ensure Python and necessary libraries are installed.
   - More detailed steps and specific commands for each setup can be found in the respective sections below.

## Usage Instructions
### Kafka and EC2 Setup
- Follow the steps detailed in the sections below to create an Amazon MSK cluster, set up an EC2 client, install Java and Apache Kafka, and configure the client.
- Refer to the provided client properties configurations to properly set up the connection to the MSK cluster.

### Connecting MSK to S3
- Utilize the MSK Connect service to set up a custom plugin for the S3 sink connector.
- Configure the MSK Connector with the appropriate S3 bucket, ensuring the right permissions and settings are applied.

### Data Streaming and Batch Processing
- Run the user posting emulation scripts to generate and send data to the configured streams.
- Use the Databricks notebooks to ingest, clean, and analyze the batch and streaming data.

### Monitoring and Validation
- Ensure proper setup in AWS CloudWatch and Databricks monitoring tools to keep track of the pipelines' health and performance.
- Validate the successful data flow from the streaming services to S3 and then to Databricks for processing.

For more comprehensive steps and commands for using each component, refer to the detailed sections below.

## File Structure
- `README.md`: This file with project documentation.
- `user_posting_emulation.py`: User posting emulation scripts.
- `user_posting_emulation_streaming.py`: Similar to above, for streaming purposes.
- `setup.sh`: Directory containing some setup scripts and configuration files for AWS services.

## License
[MIT License](LICENSE)

This project is made available under the MIT License. See the LICENSE file for full details.

---

**Contributor(s)**: Abigail McPherson

**Acknowledgements**: Thank you to AICore for supporting me and guiding me throughout this project.

