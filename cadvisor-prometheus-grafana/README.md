# Monitor Docker Containers with cAdvisor + Prometheus + Grafana

Feature:

- Provision the **Grafana** with default `datasource` and `dashboard`,
  - Facilitate DevOps, reducing chores that you have to visit  **Grafana** Web UI to configure `datasource` and import `dashboard` every time setting up a new infrastructure.
  - The default `datasource` and `dashboard` can be restored after restarting, if you delete them accidentally.
  - In provision, `datasource` uses `/etc/grafana/provisioning/datasources/prometheus.yaml` file and `dashboard` uses `/etc/grafana/provisioning/dashboards/docker-container.json` file.

[Monitoring Docker Containers with cAdvisor, Prometheus, and Grafana Using Docker Compose | by Varun Jain | Medium](https://medium.com/@varunjain2108/monitoring-docker-containers-with-cadvisor-prometheus-and-grafana-d101b4dbbc84)