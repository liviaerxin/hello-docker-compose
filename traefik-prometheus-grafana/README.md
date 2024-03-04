# Monitoring Traefik metrics with Prometheus + Grafana

A docker compose example, which extends from [Monitor Docker Containers with cAdvisor + Prometheus + Grafana](../cadvisor-prometheus-grafana/README.md), has been designed specifically to monitor Traefik **metrics**.

```mermaid 
graph LR;
    A[Traefik] -->|pull metrics| B[Prometheus]
    B -->|pull data| C[Grafana]
```

The project is automated **provisioning** with `datasources` & `dashboards`:

- Facilitate DevOps, reducing chores that you have to visit  **Grafana** Web UI to configure `datasource` and import `dashboard` every time setting up a new infrastructure.
- The default `datasource` and `dashboard` can be restored after restarting, if you delete them accidentally.
- Provisioning one `datasource` in `./datasources/datasource.yaml` file
- Provisioning two `dashboard` with two `./dashboards/*.json` files that I use from others but do a little **tweak**. These awesome creations are:
  - `17346_rev7.json`: Traefik Official Standalone Dashboard
    - ID: `17346`
    - URL: https://grafana.com/grafana/dashboards/17346-traefik-official-standalone-dashboard/
  - `12250_rev1.json`: Traefik 2.2
    - ID: `12250`
    - URL: https://grafana.com/grafana/dashboards/12250-traefik-2-2/

However, I do some modification on `"datasource"` in these `dashboard.json` files for my `Prometheus` datasource.

## Set `datasource` in `dashboard.json` when provisioning

If you are using an existed `dashboard.json` which is downloaded from grafana dashboard center, it maybe show `{..., "datasource": {"uid": ${DS_PROMETHEUS}}}`. We need to replace it with a right `datasource` by doing either of the following:

- Set `{"datasource":null}`: means dashboard will use the `default` datasource.
- Set `{"datasource":"Prometheus"}`: means dashboard will use the datasource of **name**: `Prometheus`.
- Set `{"datasource": {"type": "prometheus", "uid": "c1d0d42c"}}`: means dashboard will use the datasource of **uid**: `c1d0d42c`.

## Example

Traefik     :   http://localhost:8082/metrics
Prometheus  :   http://localhost:9090
Grafana     :   http://localhost:3000
Web         :   http://localhost/foo


## References

