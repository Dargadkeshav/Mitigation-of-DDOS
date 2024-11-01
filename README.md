Mitigation of DDoS Attacks Using Support Vector Machine (SVM)
This project focuses on developing a proactive DDoS mitigation system that uses machine learning, specifically the Support Vector Machine (SVM) algorithm, to detect and neutralize Distributed Denial of Service (DDoS) attacks. This system offers a dynamic approach to identifying malicious network traffic patterns, ensuring the continuous availability and resilience of network infrastructure during such cyber threats.

Project Overview
In today's digital landscape, DDoS attacks pose a significant threat, leading to network disruptions and potential financial losses. Traditional rule-based mitigation techniques struggle to adapt to evolving attack methods. Our project addresses this issue by integrating SVM-based anomaly detection with robust traffic filtering and rerouting mechanisms to promptly detect and mitigate DDoS attacks.

Key Components
Data Collection Module: Aggregates real-time and historical network traffic data for SVM training and monitoring.
SVM Model Training: Trains the SVM model with extracted features, optimizing parameters for high accuracy in classifying legitimate vs. malicious traffic.
Real-Time Anomaly Detection: Utilizes the trained SVM model to classify incoming network traffic and identify potential DDoS threats.
Mitigation and Response: Automatically applies filtering and redirection to isolate malicious traffic, maintaining service continuity.
Monitoring and Reporting: Provides ongoing performance metrics and real-time reports to aid in identifying vulnerabilities.
System Architecture
The architecture combines hardware (firewalls, intrusion prevention systems) and software solutions, creating a layered defense mechanism that ensures resilience and effective DDoS mitigation.

Results
Experimental evaluations show that the SVM-based system effectively distinguishes between normal and malicious traffic, even under complex, high-dimensional conditions, achieving high accuracy in DDoS detection.

Requirements
Software
Python (Jupyter Notebook)
Anaconda
Slowloris or hping for DDoS simulation
Apache Server
Linux OS
Hardware
Minimum 4GB RAM, 100GB Storage, Quad-core Processor
