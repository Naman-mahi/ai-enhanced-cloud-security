# Cloud Provider Settings
CLOUD_PROVIDER = 'aws'
AWS_REGION = 'us-west-2'
AWS_ACCESS_KEY = 'your-access-key'
AWS_SECRET_KEY = 'your-secret-key'

# Blockchain Settings
BLOCKCHAIN_URL = 'http://localhost:8545'
CONTRACT_ADDRESS = '0x...'
ABI_PATH = 'contracts/SecurityLog.abi'

# ML Model Settings
MODEL_PATH = 'models/threat_detection_model.h5'
THRESHOLD = 0.75

# Automation Settings
RULES_PATH = 'config/automation_rules.yaml'

# Monitoring Settings
METRICS_INTERVAL = 300  # 5 minutes
ALERT_THRESHOLD = 0.9 