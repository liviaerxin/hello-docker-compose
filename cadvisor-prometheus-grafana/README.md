# Monitor Docker Containers with cAdvisor + Prometheus + Grafana

The project is automated **provisioning** with `datasources` & `dashboards`:

- Facilitate DevOps, reducing chores that you have to visit  **Grafana** Web UI to configure `datasource` and import `dashboard` every time setting up a new infrastructure.
- The default `datasource` and `dashboard` can be restored after restarting, if you delete them accidentally.
- Provisioning one `datasource` in `./datasources/datasource.yaml` file
- Provisioning two `dashboard` with two `./dashboards/*.json` files that I use from others but do a little tweak. These awesome creations are:
  - `893_rev5.json`: Docker and system monitoring
    - ID: 893
    - URL: https://grafana.com/grafana/dashboards/179-docker-prometheus-monitoring
  - `193_rev1.json`: Docker and system monitoring
    - ID: 193
    - URL: https://grafana.com/grafana/dashboards/193-docker-monitoring/

However, I do some modification on `"datasource"` in these `dashboard.json` files for my `Prometheus` datsource.

## Set `datasource` in `dashboard.json` when provisioning

If you want to use an existed `dashboard.json` which is downloaded from grafana dashboard center, it maybe show `{..., "datasource": {"uid": ${DS_PROMETHEUS}}}`. We need to provide a right `datasource` by doing either of the following:

- Set `{"datasource":null}`: means dashboard will use the default datasource.
- Set `{"datasource":"Prometheus"}`: means dashboard will use the datasource of name `Prometheus`.
- Set `{"datasource": {"type": "prometheus", "uid": "c1d0d42c"}}`: means dashboard will use the datasource of uid `c1d0d42c`.

## Example

cAdvisor:   http://localhost:8080
Prometheus: http://localhost:9090
Grafana:    http://localhost:3000

## References

[Provision Grafana | Grafana documentation](https://grafana.com/docs/grafana/latest/administration/provisioning)

[Monitoring Docker Containers with cAdvisor, Prometheus, and Grafana Using Docker Compose | by Varun Jain | Medium](https://medium.com/@varunjain2108/monitoring-docker-containers-with-cadvisor-prometheus-and-grafana-d101b4dbbc84)

[GitHub - vegasbrianc/prometheus: A docker-compose stack for Prometheus monitoring](https://github.com/vegasbrianc/prometheus)