# Evaluation Data
Assorted evaluation data from Polus, ElasticWISP-NG, ElasticRoute, and PURPLE.

This repository contains links to evaluation data for various research projects focused on improving Wireless Internet Service Provider (WISP) networks and related technologies. Due to file size constraints, the some data is hosted in an S3 bucket rather than directly in this repository.

> **Note:** Our S3 bucket does not support directory listing. All files must be accessed using their direct download links.

## Data Files

| Project   | File | Description | Link |
|-----------|------|-------------|------|
| **ElasticRoute** | xdp_unloaded.csv | Performance measurements without network load | [Download](https://data.wine.ac.nz/elasticroute/xdp_unloaded.csv) |
| | xdp_loaded.csv | Performance measurements under network load | [Download](https://data.wine.ac.nz/elasticroute/xdp_loaded.csv) |
| **ElasticWISP-NG** | influx_cleaned.data.csv | Cleaned network traffic data used for evaluating energy-proportional operation | [Download](https://data.wine.ac.nz/elasticwisp-ng/influx_cleaned.data.csv) |
| **POLUS** | influxdb_data_delta_drops.csv | Packet drop measurements for bufferbloat analysis | [Download](https://data.wine.ac.nz/polus/influxdb_data_delta_drops.csv) |
| | structure.txt | Data structure information for SQL databases | [Download](https://data.wine.ac.nz/polus/structure.txt) |
| | influxdb_data_backlog_p.csv | Packet backlog measurements for latency analysis | [Download](https://data.wine.ac.nz/polus/influxdb_data_backlog_p.csv) |
| | log_pi.csv | ICMP ping RTT measurement logs from central office to client | [Download](https://data.wine.ac.nz/polus/log_pi.csv) |
| | log_data.csv | General performance measurement logs | [Download](https://data.wine.ac.nz/polus/log_data.csv) |
| **PURPLE Testbed** | site_usbimager-20250502T1749.dd.zst | Compressed disk image for site deployment | [Download](https://data.wine.ac.nz/purple-testbed/site_usbimager-20250502T1749.dd.zst) |
| | client_usbimager-20250503T1944.dd.zst | Compressed disk image for client deployment | [Download](https://data.wine.ac.nz/purple-testbed/client_usbimager-20250503T1944.dd.zst) |
| **Turbine** | turbine_power_data.zip | Power generation measurements from Heights Road wind turbine | [Download](https://data.wine.ac.nz/turbine/turbine_power_data.zip) |
| | turbine_image_data.zip | Image dataset of Heights Road turbine for visual analysis | [Download](https://data.wine.ac.nz/turbine/turbine_image_data.zip) |

## Project Descriptions

### ElasticRoute
Framework that complements the ElasticWISP architecture by providing energy-aware flow-routing capabilities.

### ElasticWISP-NG
Next-generation framework for dynamic resource provisioning in WISP access networks, building on the original ElasticWISP model. Focuses on energy-proportional operation to reduce power consumption in off-grid WISP deployments.

### POLUS
Framework for detecting and characterising latency under load in multi-bottleneck WISP networks. POLUS helps identify bufferbloat issues that can significantly degrade user experience, particularly for real-time applications. POLUS uses PURPLE to control CAKE's bandwidth parameter, helping beat bufferbloat.

### PURPLE Testbed
Test environment for bufferbloat-related research, providing reproducible deployment configurations for experimental validation.

### Turbine
Dataset related to wind turbine operation for research on renewable energy sources for powering off-grid WISP sites.

## Citation
If you use this data in your research, please cite the relevant papers associated with each project.
