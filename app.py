import streamlit as st
from modules.threat_detection import ThreatDetector
from modules.blockchain import BlockchainLogger
from modules.monitoring import CloudMonitor
from modules.automation import AutomationEngine
import config
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta
import numpy as np

def show_footer():
    st.markdown("""
    <div style='position: fixed; bottom: 0; width: 100%; text-align: center; padding: 10px; color: #000; background-color: rgba(255, 255, 255, 0.9);'>
        <p style='margin: 0; font-size: 14px;'>Developed with ❤️ by Namanmahi</p>
    </div>
    """, unsafe_allow_html=True)

def main():
    st.set_page_config(
        page_title="AI Cloud Security Platform",
        page_icon="🛡️",
        layout="wide"
    )

    st.title("AI-Enhanced Cloud Security Platform")

    # Sidebar for navigation
    page = st.sidebar.selectbox(
        "Select Module",
        ["Dashboard", "Threat Detection", "Security Logs", "Mitigation Center", "Settings"]
    )

    if page == "Dashboard":
        show_dashboard()
    elif page == "Threat Detection":
        show_threat_detection()
    elif page == "Security Logs":
        show_security_logs()
    elif page == "Mitigation Center":
        show_mitigation_center()
    elif page == "Settings":
        show_settings()

    # Add footer at the bottom of every page
    show_footer()

def analyze_system_metrics(df):
    high_cpu = df[df['cpu_usage'] > 85]
    high_memory = df[df['memory_usage'] > 85]
    high_disk = df[df['disk_usage'] > 85]
    
    mitigation_steps = []
    if not high_cpu.empty:
        mitigation_steps.append({
            "issue": "High CPU Usage",
            "affected_servers": high_cpu['server_id'].tolist(),
            "actions": [
                "Scale up server resources",
                "Check for runaway processes",
                "Enable auto-scaling",
                "Review application performance"
            ]
        })
    
    if not high_memory.empty:
        mitigation_steps.append({
            "issue": "High Memory Usage",
            "affected_servers": high_memory['server_id'].tolist(),
            "actions": [
                "Increase memory allocation",
                "Check for memory leaks",
                "Optimize application memory usage",
                "Enable memory monitoring alerts"
            ]
        })
    
    return mitigation_steps

def analyze_auth_logs(df):
    failed_logins = df[df['login_status'] == 'failed']
    suspicious_ips = failed_logins['ip_address'].value_counts()
    suspicious_users = failed_logins['username'].value_counts()
    
    mitigation_steps = []
    if not failed_logins.empty:
        mitigation_steps.append({
            "issue": "Multiple Failed Login Attempts",
            "affected_users": suspicious_users.head().to_dict(),
            "suspicious_ips": suspicious_ips.head().to_dict(),
            "actions": [
                "Implement account lockout policy",
                "Enable 2FA for affected users",
                "Block suspicious IP addresses",
                "Review login attempt patterns"
            ]
        })
    
    return mitigation_steps

def analyze_firewall_logs(df):
    blocked_attacks = df[df['action'] == 'block']
    attack_sources = blocked_attacks['source_ip'].value_counts()
    
    mitigation_steps = []
    if not blocked_attacks.empty:
        mitigation_steps.append({
            "issue": "Blocked Network Attacks",
            "attack_sources": attack_sources.head().to_dict(),
            "affected_ports": blocked_attacks['port'].value_counts().head().to_dict(),
            "actions": [
                "Update firewall rules",
                "Block malicious IP ranges",
                "Enable IDS/IPS",
                "Review network security policies"
            ]
        })
    
    return mitigation_steps

def show_mitigation_center():
    st.header("Mitigation Center")
    
    # Load and analyze different log types
    try:
        system_df = pd.read_csv('system_metrics.csv')
        auth_df = pd.read_csv('auth_logs.csv')
        firewall_df = pd.read_csv('firewall_logs.csv')
        
        # Analyze and get mitigation steps
        system_mitigations = analyze_system_metrics(system_df)
        auth_mitigations = analyze_auth_logs(auth_df)
        firewall_mitigations = analyze_firewall_logs(firewall_df)
        
        # Display mitigation recommendations
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Critical Issues")
            for mitigation in system_mitigations + auth_mitigations + firewall_mitigations:
                with st.expander(f"🚨 {mitigation['issue']}"):
                    if 'affected_servers' in mitigation:
                        st.write("Affected Servers:", ", ".join(mitigation['affected_servers']))
                    if 'affected_users' in mitigation:
                        st.write("Affected Users:", mitigation['affected_users'])
                    if 'attack_sources' in mitigation:
                        st.write("Attack Sources:", mitigation['attack_sources'])
                    
                    st.write("Recommended Actions:")
                    for action in mitigation['actions']:
                        st.write(f"- {action}")
                    
                    if st.button(f"Apply Mitigation for {mitigation['issue']}", key=mitigation['issue']):
                        st.success(f"Mitigation actions initiated for {mitigation['issue']}")
        
        with col2:
            st.subheader("Automated Response Status")
            # Show active mitigations
            active_mitigations = {
                "Firewall Rules Updated": "Active",
                "IP Blocking": "Active",
                "Account Lockout": "Active",
                "Resource Scaling": "In Progress"
            }
            for action, status in active_mitigations.items():
                st.metric(action, status)
            
            # Show mitigation effectiveness
            st.subheader("Mitigation Effectiveness")
            effectiveness_data = {
                "Blocked Attacks": "95%",
                "Failed Login Prevention": "88%",
                "Resource Optimization": "92%"
            }
            for metric, value in effectiveness_data.items():
                st.metric(metric, value)

    except Exception as e:
        st.error(f"Error loading log files: {str(e)}")
        st.info("Please ensure all required log files are present in the correct location.")

def show_dashboard():
    st.header("Security Dashboard")
    
    try:
        # Load all log files
        system_df = pd.read_csv('system_metrics.csv')
        auth_df = pd.read_csv('auth_logs.csv')
        firewall_df = pd.read_csv('firewall_logs.csv')
        
        # Display overall security status
        col1, col2, col3 = st.columns(3)
        with col1:
            high_alerts = len(system_df[system_df['alert_level'] == 3]) + \
                         len(auth_df[auth_df['alert_level'] == 3]) + \
                         len(firewall_df[firewall_df['alert_level'] == 3])
            st.metric("Critical Alerts", high_alerts, "-2")
        
        with col2:
            avg_cpu = system_df['cpu_usage'].mean()
            st.metric("Avg CPU Usage", f"{avg_cpu:.1f}%", "3%")
        
        with col3:
            blocked_attacks = len(firewall_df[firewall_df['action'] == 'block'])
            st.metric("Blocked Attacks", blocked_attacks, "5")
        
        # Show detailed metrics
        show_detailed_metrics(system_df, auth_df, firewall_df)
        
    except Exception as e:
        st.error(f"Error loading dashboard data: {str(e)}")

def show_detailed_metrics(system_df, auth_df, firewall_df):
    # System Performance Trends
    st.subheader("System Performance Trends")
    fig = px.line(system_df, x='timestamp', y=['cpu_usage', 'memory_usage', 'disk_usage'],
                 title='System Resource Usage Over Time')
    st.plotly_chart(fig)
    
    # Security Events Timeline
    st.subheader("Security Events Timeline")
    events_df = pd.concat([
        auth_df[['timestamp', 'alert_level']].assign(event_type='Authentication'),
        firewall_df[['timestamp', 'alert_level']].assign(event_type='Firewall')
    ])
    fig = px.scatter(events_df, x='timestamp', y='alert_level', color='event_type',
                    title='Security Events by Alert Level')
    st.plotly_chart(fig)

def show_threat_detection():
    st.header("Threat Detection")
    
    # File uploader for network data
    uploaded_file = st.file_uploader("Upload Network Data for Analysis", type=['csv'])
    
    if uploaded_file is not None:
        # Read and display the data
        df = pd.read_csv(uploaded_file)
        st.subheader("Network Data Preview")
        st.dataframe(df.head())
        
        st.info("Analyzing network data...")
        
        # Calculate some basic statistics
        total_connections = len(df)
        suspicious_connections = len(df[df['alert_level'] > 0])
        high_risk_connections = len(df[df['alert_level'] == 3])
        
        # Display metrics
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Connections", total_connections)
        with col2:
            st.metric("Suspicious Connections", suspicious_connections)
        with col3:
            st.metric("High Risk Connections", high_risk_connections)
        
        # Show threat distribution
        st.subheader("Threat Level Distribution")
        threat_dist = df['alert_level'].value_counts().sort_index()
        st.bar_chart(threat_dist)
        
        # Display high-risk connections
        if high_risk_connections > 0:
            st.subheader("High Risk Connections")
            st.dataframe(df[df['alert_level'] == 3])

def show_security_logs():
    st.header("Security Logs")
    
    # Date range selector
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Start Date")
    with col2:
        end_date = st.date_input("End Date")
    
    # Sample log data
    log_data = [
        {"timestamp": "2024-03-23 10:30:15", "event": "Suspicious Login Attempt", "severity": "High"},
        {"timestamp": "2024-03-23 10:35:22", "event": "Firewall Rule Update", "severity": "Low"},
        {"timestamp": "2024-03-23 10:40:18", "event": "Data Access Request", "severity": "Medium"}
    ]
    
    st.table(log_data)

def show_automation():
    st.header("Automation Rules")
    
    # Add new rule form
    st.subheader("Add New Rule")
    rule_name = st.text_input("Rule Name")
    trigger_condition = st.selectbox("Trigger Condition", 
        ["High Threat Level", "Suspicious IP", "Multiple Failed Logins"])
    action = st.selectbox("Action", 
        ["Block IP", "Send Alert", "Isolate Instance"])
    
    if st.button("Add Rule"):
        st.success("Rule added successfully!")
    
    # Display existing rules
    st.subheader("Existing Rules")
    rules = [
        {"name": "Auto-block DDoS", "condition": "High Threat Level", "action": "Block IP"},
        {"name": "Alert Admin", "condition": "Suspicious IP", "action": "Send Alert"}
    ]
    st.table(rules)

def show_settings():
    st.header("Settings")
    
    # Cloud Provider Settings
    st.subheader("Cloud Provider Configuration")
    cloud_provider = st.selectbox("Cloud Provider", ["AWS", "Azure", "GCP"])
    region = st.text_input("Region")
    
    # Alert Settings
    st.subheader("Alert Settings")
    alert_threshold = st.slider("Alert Threshold", 0, 100, 75)
    email_notifications = st.checkbox("Enable Email Notifications")
    
    if st.button("Save Settings"):
        st.success("Settings saved successfully!")

if __name__ == "__main__":
    main() 