import boto3
import azure.monitor
from google.cloud import monitoring_v3

class CloudMonitor:
    def __init__(self, cloud_provider):
        self.cloud_provider = cloud_provider
        self.client = self._initialize_client()

    def _initialize_client(self):
        if self.cloud_provider == 'aws':
            return boto3.client('cloudwatch')
        elif self.cloud_provider == 'azure':
            return azure.monitor.MonitorClient()
        elif self.cloud_provider == 'gcp':
            return monitoring_v3.MetricServiceClient()

    def get_metrics(self, resource_id, metric_name, time_period):
        """
        Get monitoring metrics from cloud provider
        """
        if self.cloud_provider == 'aws':
            return self._get_aws_metrics(resource_id, metric_name, time_period)
        # Add similar methods for Azure and GCP
        
    def _get_aws_metrics(self, resource_id, metric_name, time_period):
        response = self.client.get_metric_statistics(
            Namespace='AWS/EC2',
            MetricName=metric_name,
            Dimensions=[{'Name': 'InstanceId', 'Value': resource_id}],
            StartTime=time_period['start'],
            EndTime=time_period['end'],
            Period=300,
            Statistics=['Average']
        )
        return response 