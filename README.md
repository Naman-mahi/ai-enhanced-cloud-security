# AI-Enhanced Cloud Security Platform 🛡️

## Project Overview

The AI-Enhanced Cloud Security Platform is an advanced security monitoring and threat detection system that leverages artificial intelligence, blockchain technology, and cloud computing to provide comprehensive security protection for cloud infrastructure.

### Key Features

- **Real-time Threat Detection**: AI-powered analysis of network traffic and system behavior
- **Multi-Cloud Monitoring**: Support for AWS, Azure, and GCP
- **Blockchain Logging**: Immutable security event logging using blockchain
- **Automated Response**: Configurable automated responses to security threats
- **Interactive Dashboard**: Real-time visualization of security metrics
- **Mitigation Center**: Automated threat mitigation recommendations
- **Security Logs**: Comprehensive logging and audit trails

## Technology Stack

- **Frontend**: Streamlit
- **Backend**: Python 3.8+
- **AI/ML**: TensorFlow, Scikit-learn
- **Data Processing**: Pandas, NumPy
- **Visualization**: Plotly
- **Cloud Integration**: AWS SDK, Azure SDK, Google Cloud SDK
- **Blockchain**: Web3.py
- **Security**: Python-cryptography

## Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Git
- Access to cloud platforms (AWS/Azure/GCP)
- Local blockchain network (optional, for development)

### Step 1: Clone the Repository 

```bash
git clone https://github.com/namanmahi/ai-enhanced-cloud-security.git
```
cd ai-enhanced-cloud-security
```
### Step 2: Create Virtual Environment

```bash
python -m venv venv
```

### Step 3: Activate Virtual Environment

```bash
source venv/bin/activate or .\venv\Scripts\activate
```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables

#Create a `.env` file in the root directory:

```bash
AWS_ACCESS_KEY_ID=your_aws_access_key_id
AWS_SECRET_ACCESS_KEY=your_aws_secret_access_key
AWS_REGION=your_aws_region
AWS_REGION=your_aws_region
AZURE_TENANT_ID=your_azure_tenant_id
AZURE_CLIENT_ID=your_azure_client_id
AZURE_CLIENT_SECRET=your_azure_client_secret
GCP_PROJECT_ID=your_gcp_project_id
GOOGLE_APPLICATION_CREDENTIALS=path/to/credentials.json
```

### Blockchain Configuration

```bash
BLOCKCHAIN_URL=http://localhost:8545
CONTRACT_ADDRESS=your_contract_address
```


### Step 5: Run the Application

```bash
streamlit run app.py
```


The application will be available at `http://localhost:8501`

## Project Structure

```bash
.
├── app.py
├── requirements.txt
├── .env
├── .streamlit
├── models
├── utils
├── data
├── contracts
├── README.md
├── auth_log.py
├── config.py
├── dashboard.py
├── mitigation_center.py
├── real_time_monitoring.py
├── security_logs.py
```



## Usage

1. **Dashboard**: View overall security status and metrics
2. **Threat Detection**: Upload and analyze network data
3. **Security Logs**: Review detailed security events
4. **Mitigation Center**: View and apply security recommendations
5. **Settings**: Configure cloud providers and alert thresholds

## Development

### Setting Up Development Environment

1. Follow installation steps above
2. Install development dependencies:

```bash
pip install -r requirements-dev.txt
```
### Running Tests

```bash
pytest
```

### Code Style

- Follow PEP 8 guidelines
- Use type hints
- Maximum line length: 88 characters

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## Security

- Never commit sensitive credentials
- Use environment variables for secrets
- Regularly update dependencies
- Follow security best practices

## Troubleshooting

### Common Issues

1. **Cloud Connection Issues**
   - Verify credentials in `.env`
   - Check network connectivity
   - Ensure proper IAM permissions

2. **ML Model Loading Errors**
   - Verify model file exists
   - Check TensorFlow version compatibility
   - Ensure correct model format

3. **Blockchain Connection Issues**
   - Verify network connectivity
   - Check contract deployment status
   - Confirm Web3 configuration

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Cloud security community
- Open source contributors
- Streamlit team

## Contact

- Created by Namanmahi
- Email: your.email@example.com
- GitHub: [Your GitHub Profile](https://github.com/yourusername)

---
Developed with ❤️ by Namanmahi