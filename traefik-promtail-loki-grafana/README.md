# Monitoring Traefik HTTP Logs with Promtail + Grafana Loki + Grafana

A docker compose example, which extends from [Monitoring Traefik metrics with Prometheus + Grafana](../traefik-prometheus-grafana/README.md) and [](../traefik-promtail-loki-grafana/README.md), has been designed specifically to monitor Traefik **Logs**.

```mermaid 
graph LR;
    A[Traefik] -->|tail log file| B[Promtail]
    B -->|push data| C[Grafana Loki]
    C -->|pull data| D[Grafana]
```

The project is automated **provisioning** with `datasources` & `dashboards`:

- Facilitate DevOps, reducing chores that you have to visit  **Grafana** Web UI to configure `datasource` and import `dashboard` every time setting up a new infrastructure.
- The default `datasource` and `dashboard` can be restored after restarting, if you delete them accidentally.
- Provisioning one `datasource` in `./datasources/datasource.yaml` file
- Provisioning two `dashboard` with two `./dashboards/*.json` files that I use from others but do a little **tweak**. These awesome creations are:
  - `loki-traefik-log.json`: Traefik Access Logs

However, I do some modification on `"datasource"` in these `dashboard.json` files for my `Loki` datasource.

## Set `datasource` in `dashboard.json` when provisioning

If you are using an existed `dashboard.json` which is downloaded from grafana dashboard center, it maybe show `{..., "datasource": {"uid": ${DS_PROMETHEUS}}}`. We need to replace it with a right `datasource` by doing either of the following:

- Set `{"datasource":null}`: means dashboard will use the `default` datasource.
- Set `{"datasource":"Loki"}`: means dashboard will use the datasource of **name**: `Loki`.
- Set `{"datasource": {"type": "loki", "uid": "53e1735a"}}`: means dashboard will use the datasource of **uid**: `53e1735a`.

## Example

Loki        :   http://localhost:3100  and [Grafana Loki HTTP API](https://grafana.com/docs/loki/latest/reference/api/)
Grafana     :   http://localhost:3000
Web         :   http://localhost/foo

## References

[Grafana Loki HTTP API](https://grafana.com/docs/loki/latest/reference/api/)

[Visualizing Traefik Metrics and HTTP Logs in Grafana](https://blog.lrvt.de/traefik-metrics-and-http-logs-in-grafana/)