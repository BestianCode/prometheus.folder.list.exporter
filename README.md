# Prometheus File List Exporter

This Python-based exporter is designed to expose file sizes in a directory as Prometheus metrics. It's particularly useful for monitoring the size of files in a specific directory, such as backup files on a filesystem.

## Features

- **Update Frequency**: Monthly.
- **Operating System**: Debian Bookworm (12) Slim.
- **Timezone**: Europe/Berlin.

- **File Pattern Matching**: The exporter can filter files based on a pattern, such as `*.gz` or `*.*`.
- **File Size Metrics**: The exporter exposes the size of each file in bytes as a Prometheus gauge metric.
- **File Age Metrics**: The exporter also provides the age of each file in seconds.

## Configuration

The exporter can be configured using the following environment variables:

- `EXPORT_PORT`: The port on which the exporter listens (default: 8080).
- `EXPORT_DIR`: The directory to monitor (default: "/var/www/html").
- `EXPORT_FILE_PATTERN`: The pattern to match files (default: "*").

## Metrics

The exporter exposes the following metrics:

- `file_size`: This gauge metric represents the size of each file in bytes. It includes the following labels:
  - `name`: The name of the file.
  - `date`: The last modification date of the file.
  - `age`: The age of the file in seconds.
  - `period`: The period when the file was last modified ("today", "yesterday", or "previous_days").

Here's an example of the metrics:

```plaintext
file_size{age="47878.657218933105", cluster="k8s-test", date="2024-04-16 00:00:10.560550", kubernetes_node_name="k8s-worker01", name="test-file-2024-04-16-00-00.gz", namespace="namespace-test", period="today" } 27012456
file_size{age="134278.59226727486", cluster="k8s-test", date="2024-04-15 00:00:10.625646", kubernetes_node_name="k8s-worker01", name="test-file-2024-04-15-00-00.gz", namespace="namespace-test", period="yesterday" } 26091123
file_size{age="1084674.0214140415", cluster="k8s-test", date="2024-04-04 00:00:15.196284", kubernetes_node_name="k8s-worker01", name="test-file-2024-04-04-00-00.gz", namespace="namespace-test", period="previous_days" } 14123654
```

## Usage

This exporter is designed to be used as a base image in Helm charts or other Kubernetes deployments to expose Prometheus metrics for files in a directory.

## Kubernetes Deployment annotations

```yaml
    annotations:
        prometheus.io/path: /metrics
        prometheus.io/port: 8080
        prometheus.io/scrape: "true"
```

## URLs

- **GitHub**: https://github.com/BestianCode/prometheus.folder.list.exporter
- **DockerHub**: https://hub.docker.com/r/bestian/prometheus.folder.list.exporter
