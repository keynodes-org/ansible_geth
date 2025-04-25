Geth
=========

Geth execution layer

**Tests:**
* Ubuntu 22.04 (jammy)

How to run molecule tests
----------------------

```shell
python3 -m venv venv
pip install -r requirements.txt
source venv/bin/activate
make init
make test
```

Make
----

`make init` - Prepare environment
`make test` - Run molecule tests (`molecule -v test`)
`make docs` - Auto-generate `README` (`ansible-doctor`)

Role install
--------------

You can install role by using `ansible-galaxy`:

```shell
ansible-galaxy role install git+git@github.com:keynodes-org/ansible_geth.git
```

For particular version of this role:
```shell
ansible-galaxy role install git+git@github.com:keynodes-org/ansible_geth.git,main
```

Update to latest version:
```shell
ansible-galaxy role install git+git@github.com:keynodes-org/ansible_geth.git --upgrade
```

Example of using in `requirements.yml`:
```yaml
---
roles:
  - name: geth
    src: git+git@github.com:keynodes-org/ansible_geth.git
    version: main
```

How to use in playbook:
-------------------------

```yaml
- hosts: ansible_hostname
  roles:
    - role: ansible_geth
```

Variables
===============

Ansible role for deploying Geth Ethereum Execution layer node

## Auto-generated

- [Defaults](#default-vars)
  - [geth_binary_download_url](#geth_binary_download_url)
  - [geth_binary_path](#geth_binary_path)
  - [geth_blobpool_datacap](#geth_blobpool_datacap)
  - [geth_blobpool_datadir](#geth_blobpool_datadir)
  - [geth_blobpool_price_bump](#geth_blobpool_price_bump)
  - [geth_database_cache](#geth_database_cache)
  - [geth_database_freezer](#geth_database_freezer)
  - [geth_dir_base](#geth_dir_base)
  - [geth_dir_binary](#geth_dir_binary)
  - [geth_dir_config](#geth_dir_config)
  - [geth_dir_data](#geth_dir_data)
  - [geth_dir_log](#geth_dir_log)
  - [geth_dir_systemd](#geth_dir_systemd)
  - [geth_enable_preimage_recording](#geth_enable_preimage_recording)
  - [geth_eth_discovery_urls](#geth_eth_discovery_urls)
  - [geth_filter_log_cache_size](#geth_filter_log_cache_size)
  - [geth_general_owner](#geth_general_owner)
  - [geth_gpo_blocks](#geth_gpo_blocks)
  - [geth_gpo_ignore_price](#geth_gpo_ignore_price)
  - [geth_gpo_max_block_history](#geth_gpo_max_block_history)
  - [geth_gpo_max_header_history](#geth_gpo_max_header_history)
  - [geth_gpo_max_price](#geth_gpo_max_price)
  - [geth_gpo_percentile](#geth_gpo_percentile)
  - [geth_group](#geth_group)
  - [geth_history_mode](#geth_history_mode)
  - [geth_http_idle_timeout](#geth_http_idle_timeout)
  - [geth_http_read_header_timeout](#geth_http_read_header_timeout)
  - [geth_http_read_timeout](#geth_http_read_timeout)
  - [geth_http_write_timeout](#geth_http_write_timeout)
  - [geth_jwt_secret_path](#geth_jwt_secret_path)
  - [geth_log_level](#geth_log_level)
  - [geth_metrics_http](#geth_metrics_http)
  - [geth_metrics_influxdb_bucket](#geth_metrics_influxdb_bucket)
  - [geth_metrics_influxdb_database](#geth_metrics_influxdb_database)
  - [geth_metrics_influxdb_endpoint](#geth_metrics_influxdb_endpoint)
  - [geth_metrics_influxdb_organization](#geth_metrics_influxdb_organization)
  - [geth_metrics_influxdb_password](#geth_metrics_influxdb_password)
  - [geth_metrics_influxdb_tags](#geth_metrics_influxdb_tags)
  - [geth_metrics_influxdb_token](#geth_metrics_influxdb_token)
  - [geth_metrics_influxdb_username](#geth_metrics_influxdb_username)
  - [geth_metrics_port](#geth_metrics_port)
  - [geth_miner_gas_ceil](#geth_miner_gas_ceil)
  - [geth_miner_gas_price](#geth_miner_gas_price)
  - [geth_miner_recommit](#geth_miner_recommit)
  - [geth_network_id](#geth_network_id)
  - [geth_network_name](#geth_network_name)
  - [geth_no_prefetch](#geth_no_prefetch)
  - [geth_no_pruning](#geth_no_pruning)
  - [geth_node_auth_addr](#geth_node_auth_addr)
  - [geth_node_auth_port](#geth_node_auth_port)
  - [geth_node_auth_virtual_hosts](#geth_node_auth_virtual_hosts)
  - [geth_node_batch_request_limit](#geth_node_batch_request_limit)
  - [geth_node_batch_response_max_size](#geth_node_batch_response_max_size)
  - [geth_node_datadir](#geth_node_datadir)
  - [geth_node_graphql_virtual_hosts](#geth_node_graphql_virtual_hosts)
  - [geth_node_http_host](#geth_node_http_host)
  - [geth_node_http_modules](#geth_node_http_modules)
  - [geth_node_http_port](#geth_node_http_port)
  - [geth_node_http_virtual_hosts](#geth_node_http_virtual_hosts)
  - [geth_node_ipc_path](#geth_node_ipc_path)
  - [geth_node_ws_host](#geth_node_ws_host)
  - [geth_node_ws_modules](#geth_node_ws_modules)
  - [geth_node_ws_port](#geth_node_ws_port)
  - [geth_p2p_bootstrap_nodes](#geth_p2p_bootstrap_nodes)
  - [geth_p2p_bootstrap_nodes_v5](#geth_p2p_bootstrap_nodes_v5)
  - [geth_p2p_disc_addr](#geth_p2p_disc_addr)
  - [geth_p2p_discovery_v4](#geth_p2p_discovery_v4)
  - [geth_p2p_discovery_v5](#geth_p2p_discovery_v5)
  - [geth_p2p_enable_msg_events](#geth_p2p_enable_msg_events)
  - [geth_p2p_listen_addr](#geth_p2p_listen_addr)
  - [geth_p2p_max_peers](#geth_p2p_max_peers)
  - [geth_p2p_nat](#geth_p2p_nat)
  - [geth_p2p_no_discovery](#geth_p2p_no_discovery)
  - [geth_p2p_static_nodes](#geth_p2p_static_nodes)
  - [geth_p2p_trusted_nodes](#geth_p2p_trusted_nodes)
  - [geth_preimages](#geth_preimages)
  - [geth_reinstall](#geth_reinstall)
  - [geth_rpc_evm_timeout](#geth_rpc_evm_timeout)
  - [geth_rpc_gas_cap](#geth_rpc_gas_cap)
  - [geth_rpc_tx_fee_cap](#geth_rpc_tx_fee_cap)
  - [geth_snap_discovery_urls](#geth_snap_discovery_urls)
  - [geth_snapshot_cache](#geth_snapshot_cache)
  - [geth_state_history](#geth_state_history)
  - [geth_sync_mode](#geth_sync_mode)
  - [geth_systemd_service_name](#geth_systemd_service_name)
  - [geth_transaction_history](#geth_transaction_history)
  - [geth_trie_clean_cache](#geth_trie_clean_cache)
  - [geth_trie_dirty_cache](#geth_trie_dirty_cache)
  - [geth_trie_timeout](#geth_trie_timeout)
  - [geth_tx_lookup_limit](#geth_tx_lookup_limit)
  - [geth_txpool_account_queue](#geth_txpool_account_queue)
  - [geth_txpool_account_slots](#geth_txpool_account_slots)
  - [geth_txpool_global_queue](#geth_txpool_global_queue)
  - [geth_txpool_global_slots](#geth_txpool_global_slots)
  - [geth_txpool_journal](#geth_txpool_journal)
  - [geth_txpool_lifetime](#geth_txpool_lifetime)
  - [geth_txpool_locals](#geth_txpool_locals)
  - [geth_txpool_no_locals](#geth_txpool_no_locals)
  - [geth_txpool_price_bump](#geth_txpool_price_bump)
  - [geth_txpool_price_limit](#geth_txpool_price_limit)
  - [geth_txpool_rejournal](#geth_txpool_rejournal)
  - [geth_user](#geth_user)
  - [geth_vm_trace](#geth_vm_trace)
  - [geth_vm_trace_json_config](#geth_vm_trace_json_config)
- [Tags](#tags)

- [Dependencies](#dependencies)

---

## Defaults

### geth_binary_download_url

URL to download the Geth binary.

#### Defaults

```YAML
geth_binary_download_url: https://gethstore.blob.core.windows.net/builds/geth-linux-amd64-1.15.6-19d2b4c8.tar.gz
```

### geth_binary_path

Path the Geth binary.

#### Defaults

```YAML
geth_binary_path: '{{ geth_dir_binary }}/geth'
```

### geth_blobpool_datacap

Maximum storage capacity of the blob pool in bytes.

#### Defaults

```YAML
geth_blobpool_datacap: 2684354560
```

### geth_blobpool_datadir

Directory for the blob pool.

#### Defaults

```YAML
geth_blobpool_datadir: blobpool
```

### geth_blobpool_price_bump

Price bump percentage to replace an already existing blob transaction.

#### Defaults

```YAML
geth_blobpool_price_bump: 100
```

### geth_database_cache

Memory allocated to the database cache (MB).

#### Defaults

```YAML
geth_database_cache: 512
```

### geth_database_freezer

Ancient database to freeze chain data in (directory).

#### Defaults

```YAML
geth_database_freezer: ''
```

### geth_dir_base

Base directory for Geth installation.

#### Defaults

```YAML
geth_dir_base: /opt/geth
```

### geth_dir_binary

#### Defaults

```YAML
geth_dir_binary: /usr/local/bin
```

### geth_dir_config

Directory for Geth configuration files.

#### Defaults

```YAML
geth_dir_config: '{{ geth_dir_base }}/config'
```

### geth_dir_data

Directory for Geth data storage.

#### Defaults

```YAML
geth_dir_data: '{{ geth_dir_base }}/data'
```

### geth_dir_log

Directory for Geth log files.

#### Defaults

```YAML
geth_dir_log: '{{ geth_dir_base }}/logs'
```

### geth_dir_systemd

Systemd service directory for Geth.

#### Defaults

```YAML
geth_dir_systemd: /lib/systemd/system
```

### geth_enable_preimage_recording

Enable recording the SHA3/keccak preimages of trie keys.

#### Defaults

```YAML
geth_enable_preimage_recording: false
```

### geth_eth_discovery_urls

List of Ethereum discovery URLs.

#### Defaults

```YAML
geth_eth_discovery_urls: []
```

### geth_filter_log_cache_size

Size of the filter cache for logs.

#### Defaults

```YAML
geth_filter_log_cache_size: 32
```

### geth_general_owner

General owner for Geth system files.

#### Defaults

```YAML
geth_general_owner: root
```

### geth_gpo_blocks

Number of blocks to track for gas price oracle.

#### Defaults

```YAML
geth_gpo_blocks: 20
```

### geth_gpo_ignore_price

Gas price below which geth will ignore transactions when calculating percentiles.

#### Defaults

```YAML
geth_gpo_ignore_price: 2
```

### geth_gpo_max_block_history

Maximum number of blocks to keep for gas price calculations.

#### Defaults

```YAML
geth_gpo_max_block_history: 1024
```

### geth_gpo_max_header_history

Maximum number of headers to keep for gas price calculations.

#### Defaults

```YAML
geth_gpo_max_header_history: 1024
```

### geth_gpo_max_price

Maximum transaction priority fee (or gas price before London fork) to be recommended by the oracle.

#### Defaults

```YAML
geth_gpo_max_price: 500000000000
```

### geth_gpo_percentile

Percentile value for gas price oracle.

#### Defaults

```YAML
geth_gpo_percentile: 60
```

### geth_group

Group for running the Geth node.

#### Defaults

```YAML
geth_group: geth
```

### geth_history_mode

History mode: "archive", "prune", "all".

#### Defaults

```YAML
geth_history_mode: all
```

### geth_http_idle_timeout

Maximum duration for idle connections (nanoseconds).

#### Defaults

```YAML
geth_http_idle_timeout: 120000000000
```

### geth_http_read_header_timeout

Maximum duration for reading request headers (nanoseconds).

#### Defaults

```YAML
geth_http_read_header_timeout: 30000000000
```

### geth_http_read_timeout

Maximum duration for reading the entire request (nanoseconds).

#### Defaults

```YAML
geth_http_read_timeout: 30000000000
```

### geth_http_write_timeout

Maximum duration for writing the response (nanoseconds).

#### Defaults

```YAML
geth_http_write_timeout: 30000000000
```

### geth_jwt_secret_path

jwt token path for Geth.

#### Defaults

```YAML
geth_jwt_secret_path: '{{ geth_dir_config }}/jwt.hex'
```

### geth_log_level

Force reinstall Geth binary.

#### Defaults

```YAML
geth_log_level: info
```

### geth_metrics_http

Metrics HTTP server listening interface.

#### Defaults

```YAML
geth_metrics_http: 127.0.0.1
```

### geth_metrics_influxdb_bucket

InfluxDB bucket name for metrics.

#### Defaults

```YAML
geth_metrics_influxdb_bucket: geth
```

### geth_metrics_influxdb_database

InfluxDB database name for metrics (deprecated).

#### Defaults

```YAML
geth_metrics_influxdb_database: geth
```

### geth_metrics_influxdb_endpoint

InfluxDB API endpoint for metrics.

#### Defaults

```YAML
geth_metrics_influxdb_endpoint: http://localhost:8086
```

### geth_metrics_influxdb_organization

InfluxDB organization name for metrics.

#### Defaults

```YAML
geth_metrics_influxdb_organization: geth
```

### geth_metrics_influxdb_password

InfluxDB password for metrics (deprecated).

#### Defaults

```YAML
geth_metrics_influxdb_password: test
```

### geth_metrics_influxdb_tags

Comma-separated InfluxDB tags for metrics (deprecated).

#### Defaults

```YAML
geth_metrics_influxdb_tags: host=localhost
```

### geth_metrics_influxdb_token

InfluxDB authentication token for metrics.

#### Defaults

```YAML
geth_metrics_influxdb_token: test
```

### geth_metrics_influxdb_username

InfluxDB username for metrics (deprecated).

#### Defaults

```YAML
geth_metrics_influxdb_username: test
```

### geth_metrics_port

Metrics HTTP server listening port.

#### Defaults

```YAML
geth_metrics_port: 6060
```

### geth_miner_gas_ceil

Target gas ceiling for mined blocks.

#### Defaults

```YAML
geth_miner_gas_ceil: 30000000
```

### geth_miner_gas_price

Minimum gas price for mining a transaction.

#### Defaults

```YAML
geth_miner_gas_price: 1000000
```

### geth_miner_recommit

Time interval to recreate the block being mined (nanoseconds).

#### Defaults

```YAML
geth_miner_recommit: 2000000000
```

### geth_network_id

The network ID of the Ethereum network to connect to.

#### Defaults

```YAML
geth_network_id: 560048
```

### geth_network_name

The network name of the Ethereum network ("mainnet, sepolia, hoodi, etc")

#### Defaults

```YAML
geth_network_name: hoodi
```

### geth_no_prefetch

Disable prefetching and only load state on demand.

#### Defaults

```YAML
geth_no_prefetch: false
```

### geth_no_pruning

Disable pruning and flush everything to disk.

#### Defaults

```YAML
geth_no_pruning: false
```

### geth_node_auth_addr

Listening address for authenticated APIs.

#### Defaults

```YAML
geth_node_auth_addr: localhost
```

### geth_node_auth_port

Listening port for authenticated APIs.

#### Defaults

```YAML
geth_node_auth_port: 8551
```

### geth_node_auth_virtual_hosts

List of virtual hostnames from which to accept requests for authenticated APIs.

#### Defaults

```YAML
geth_node_auth_virtual_hosts:
  - localhost
```

### geth_node_batch_request_limit

Maximum number of requests in a batch.

#### Defaults

```YAML
geth_node_batch_request_limit: 1000
```

### geth_node_batch_response_max_size

Maximum size of a batch response in bytes.

#### Defaults

```YAML
geth_node_batch_response_max_size: 25000000
```

### geth_node_datadir

Data directory for the Ethereum node.

#### Defaults

```YAML
geth_node_datadir: '{{ geth_dir_data }}/.ethereum'
```

### geth_node_graphql_virtual_hosts

List of virtual hostnames from which to accept GraphQL requests.

#### Defaults

```YAML
geth_node_graphql_virtual_hosts:
  - localhost
```

### geth_node_http_host

HTTP-RPC server listening interface.

#### Defaults

```YAML
geth_node_http_host: 127.0.0.1
```

### geth_node_http_modules

API modules to enable via HTTP-RPC interface.

#### Defaults

```YAML
geth_node_http_modules:
  - net
  - web3
  - eth
  - engine
```

### geth_node_http_port

HTTP-RPC server listening port.

#### Defaults

```YAML
geth_node_http_port: 8545
```

### geth_node_http_virtual_hosts

List of virtual hostnames from which to accept requests.

#### Defaults

```YAML
geth_node_http_virtual_hosts:
  - localhost
```

### geth_node_ipc_path

Filename for IPC socket/pipe within the datadir.

#### Defaults

```YAML
geth_node_ipc_path: geth.ipc
```

### geth_node_ws_host

WS-RPC server listening interface.

#### Defaults

```YAML
geth_node_ws_host: 127.0.0.1
```

### geth_node_ws_modules

API modules to enable via WS-RPC interface.

#### Defaults

```YAML
geth_node_ws_modules:
  - net
  - web3
  - eth
  - engine
```

### geth_node_ws_port

WS-RPC server listening port.

#### Defaults

```YAML
geth_node_ws_port: 8546
```

### geth_p2p_bootstrap_nodes

List of bootstrap nodes for P2P discovery.

#### Defaults

```YAML
geth_p2p_bootstrap_nodes:
  - enode://d860a01f9722d78051619d1e2351aba3f43f943f6f00718d1b9baa4101932a1f5011f16bb2b1bb35db20d6fe28fa0bf09636d26a87d31de9ec6203eeedb1f666@18.138.108.67:30303
  - enode://22a8232c3abc76a16ae9d6c3b164f98775fe226f0917b0ca871128a74a8e9630b458460865bab457221f1d448dd9791d24c4e5d88786180ac185df813a68d4de@3.209.45.79:30303
  - enode://2b252ab6a1d0f971d9722cb839a42cb81db019ba44c08754628ab4a823487071b5695317c8ccd085219c3a03af063495b2f1da8d18218da2d6a82981b45e6ffc@65.108.70.101:30303
  - enode://4aeb4ab6c14b23e2c4cfdce879c04b0748a20d8e9b59e25ded2a08143e265c6c25936e74cbc8e641e3312ca288673d91f2f93f8e277de3cfa444ecdaaf982052@157.90.35.166:30303
```

### geth_p2p_bootstrap_nodes_v5

List of bootstrap nodes for V5 discovery protocol.

#### Defaults

```YAML
geth_p2p_bootstrap_nodes_v5:
  - enr:-KG4QMOEswP62yzDjSwWS4YEjtTZ5PO6r65CPqYBkgTTkrpaedQ8uEUo1uMALtJIvb2w_WWEVmg5yt1UAuK1ftxUU7QDhGV0aDKQu6TalgMAAAD__________4JpZIJ2NIJpcIQEnfA2iXNlY3AyNTZrMaEDfol8oLr6XJ7FsdAYE7lpJhKMls4G_v6qQOGKJUWGb_uDdGNwgiMog3VkcIIjKA
  - enr:-KG4QF4B5WrlFcRhUU6dZETwY5ZzAXnA0vGC__L1Kdw602nDZwXSTs5RFXFIFUnbQJmhNGVU6OIX7KVrCSTODsz1tK4DhGV0aDKQu6TalgMAAAD__________4JpZIJ2NIJpcIQExNYEiXNlY3AyNTZrMaECQmM9vp7KhaXhI-nqL_R0ovULLCFSFTa9CPPSdb1zPX6DdGNwgiMog3VkcIIjKA
  - enr:-Ku4QImhMc1z8yCiNJ1TyUxdcfNucje3BGwEHzodEZUan8PherEo4sF7pPHPSIB1NNuSg5fZy7qFsjmUKs2ea1Whi0EBh2F0dG5ldHOIAAAAAAAAAACEZXRoMpD1pf1CAAAAAP__________gmlkgnY0gmlwhBLf22SJc2VjcDI1NmsxoQOVphkDqal4QzPMksc5wnpuC3gvSC8AfbFOnZY_On34wIN1ZHCCIyg
  - enr:-Ku4QP2xDnEtUXIjzJ_DhlCRN9SN99RYQPJL92TMlSv7U5C1YnYLjwOQHgZIUXw6c-BvRg2Yc2QsZxxoS_pPRVe0yK8Bh2F0dG5ldHOIAAAAAAAAAACEZXRoMpD1pf1CAAAAAP__________gmlkgnY0gmlwhBLf22SJc2VjcDI1NmsxoQMeFF5GrS7UZpAH2Ly84aLK-TyvH-dRo0JM1i8yygH50YN1ZHCCJxA
  - enr:-Ku4QPp9z1W4tAO8Ber_NQierYaOStqhDqQdOPY3bB3jDgkjcbk6YrEnVYIiCBbTxuar3CzS528d2iE7TdJsrL-dEKoBh2F0dG5ldHOIAAAAAAAAAACEZXRoMpD1pf1CAAAAAP__________gmlkgnY0gmlwhBLf22SJc2VjcDI1NmsxoQMw5fqqkw2hHC4F5HZZDPsNmPdB1Gi8JPQK7pRc9XHh-oN1ZHCCKvg
  - enr:-Le4QPUXJS2BTORXxyx2Ia-9ae4YqA_JWX3ssj4E_J-3z1A-HmFGrU8BpvpqhNabayXeOZ2Nq_sbeDgtzMJpLLnXFgAChGV0aDKQtTA_KgEAAAAAIgEAAAAAAIJpZIJ2NIJpcISsaa0Zg2lwNpAkAIkHAAAAAPA8kv_-awoTiXNlY3AyNTZrMaEDHAD2JKYevx89W0CcFJFiskdcEzkH_Wdv9iW42qLK79ODdWRwgiMohHVkcDaCI4I
  - enr:-Le4QLHZDSvkLfqgEo8IWGG96h6mxwe_PsggC20CL3neLBjfXLGAQFOPSltZ7oP6ol54OvaNqO02Rnvb8YmDR274uq8ChGV0aDKQtTA_KgEAAAAAIgEAAAAAAIJpZIJ2NIJpcISLosQxg2lwNpAqAX4AAAAAAPA8kv_-ax65iXNlY3AyNTZrMaEDBJj7_dLFACaxBfaI8KZTh_SSJUjhyAyfshimvSqo22WDdWRwgiMohHVkcDaCI4I
  - enr:-Le4QH6LQrusDbAHPjU_HcKOuMeXfdEB5NJyXgHWFadfHgiySqeDyusQMvfphdYWOzuSZO9Uq2AMRJR5O4ip7OvVma8BhGV0aDKQtTA_KgEAAAAAIgEAAAAAAIJpZIJ2NIJpcISLY9ncg2lwNpAkAh8AgQIBAAAAAAAAAAmXiXNlY3AyNTZrMaECDYCZTZEksF-kmgPholqgVt8IXr-8L7Nu7YrZ7HUpgxmDdWRwgiMohHVkcDaCI4I
  - enr:-Le4QIqLuWybHNONr933Lk0dcMmAB5WgvGKRyDihy1wHDIVlNuuztX62W51voT4I8qD34GcTEOTmag1bcdZ_8aaT4NUBhGV0aDKQtTA_KgEAAAAAIgEAAAAAAIJpZIJ2NIJpcISLY04ng2lwNpAkAh8AgAIBAAAAAAAAAA-fiXNlY3AyNTZrMaEDscnRV6n1m-D9ID5UsURk0jsoKNXt1TIrj8uKOGW6iluDdWRwgiMohHVkcDaCI4I
  - enr:-Ku4QHqVeJ8PPICcWk1vSn_XcSkjOkNiTg6Fmii5j6vUQgvzMc9L1goFnLKgXqBJspJjIsB91LTOleFmyWWrFVATGngBh2F0dG5ldHOIAAAAAAAAAACEZXRoMpC1MD8qAAAAAP__________gmlkgnY0gmlwhAMRHkWJc2VjcDI1NmsxoQKLVXFOhp2uX6jeT0DvvDpPcU8FWMjQdR4wMuORMhpX24N1ZHCCIyg
  - enr:-Ku4QG-2_Md3sZIAUebGYT6g0SMskIml77l6yR-M_JXc-UdNHCmHQeOiMLbylPejyJsdAPsTHJyjJB2sYGDLe0dn8uYBh2F0dG5ldHOIAAAAAAAAAACEZXRoMpC1MD8qAAAAAP__________gmlkgnY0gmlwhBLY-NyJc2VjcDI1NmsxoQORcM6e19T1T9gi7jxEZjk_sjVLGFscUNqAY9obgZaxbIN1ZHCCIyg
  - enr:-Ku4QPn5eVhcoF1opaFEvg1b6JNFD2rqVkHQ8HApOKK61OIcIXD127bKWgAtbwI7pnxx6cDyk_nI88TrZKQaGMZj0q0Bh2F0dG5ldHOIAAAAAAAAAACEZXRoMpC1MD8qAAAAAP__________gmlkgnY0gmlwhDayLMaJc2VjcDI1NmsxoQK2sBOLGcUb4AwuYzFuAVCaNHA-dy24UuEKkeFNgCVCsIN1ZHCCIyg
  - enr:-Ku4QEWzdnVtXc2Q0ZVigfCGggOVB2Vc1ZCPEc6j21NIFLODSJbvNaef1g4PxhPwl_3kax86YPheFUSLXPRs98vvYsoBh2F0dG5ldHOIAAAAAAAAAACEZXRoMpC1MD8qAAAAAP__________gmlkgnY0gmlwhDZBrP2Jc2VjcDI1NmsxoQM6jr8Rb1ktLEsVcKAPa08wCsKUmvoQ8khiOl_SLozf9IN1ZHCCIyg
  - enr:-LK4QA8FfhaAjlb_BXsXxSfiysR7R52Nhi9JBt4F8SPssu8hdE1BXQQEtVDC3qStCW60LSO7hEsVHv5zm8_6Vnjhcn0Bh2F0dG5ldHOIAAAAAAAAAACEZXRoMpC1MD8qAAAAAP__________gmlkgnY0gmlwhAN4aBKJc2VjcDI1NmsxoQJerDhsJ-KxZ8sHySMOCmTO6sHM3iCFQ6VMvLTe948MyYN0Y3CCI4yDdWRwgiOM
  - enr:-LK4QKWrXTpV9T78hNG6s8AM6IO4XH9kFT91uZtFg1GcsJ6dKovDOr1jtAAFPnS2lvNltkOGA9k29BUN7lFh_sjuc9QBh2F0dG5ldHOIAAAAAAAAAACEZXRoMpC1MD8qAAAAAP__________gmlkgnY0gmlwhANAdd-Jc2VjcDI1NmsxoQLQa6ai7y9PMN5hpLe5HmiJSlYzMuzP7ZhwRiwHvqNXdoN0Y3CCI4yDdWRwgiOM
```

### geth_p2p_disc_addr

Custom discovery address (different from listening address).

#### Defaults

```YAML
geth_p2p_disc_addr: ''
```

### geth_p2p_discovery_v4

Enable V4 discovery protocol.

#### Defaults

```YAML
geth_p2p_discovery_v4: true
```

### geth_p2p_discovery_v5

Enable V5 discovery protocol.

#### Defaults

```YAML
geth_p2p_discovery_v5: true
```

### geth_p2p_enable_msg_events

Enable message events in the P2P network.

#### Defaults

```YAML
geth_p2p_enable_msg_events: false
```

### geth_p2p_listen_addr

Network listening address.

#### Defaults

```YAML
geth_p2p_listen_addr: :30303
```

### geth_p2p_max_peers

Maximum number of network peers (network disabled if set to 0).

#### Defaults

```YAML
geth_p2p_max_peers: 50
```

### geth_p2p_nat

NAT port mapping mechanism (any|none|upnp|pmp|extip:<IP>).

#### Defaults

```YAML
geth_p2p_nat: any
```

### geth_p2p_no_discovery

Disable peer discovery mechanism (manual peer addition).

#### Defaults

```YAML
geth_p2p_no_discovery: false
```

### geth_p2p_static_nodes

List of static nodes to maintain persistent connections to.

#### Defaults

```YAML
geth_p2p_static_nodes: []
```

### geth_p2p_trusted_nodes

List of trusted nodes to maintain persistent connections to.

#### Defaults

```YAML
geth_p2p_trusted_nodes: []
```

### geth_preimages

Enable recording the SHA3/keccak preimages of trie keys.

#### Defaults

```YAML
geth_preimages: false
```

### geth_reinstall

#### Defaults

```YAML
geth_reinstall: false
```

### geth_rpc_evm_timeout

Sets a timeout used for eth_call (0=infinite).

#### Defaults

```YAML
geth_rpc_evm_timeout: 5000000000
```

### geth_rpc_gas_cap

Sets a cap on gas that can be used in eth_call/estimateGas (0=infinite).

#### Defaults

```YAML
geth_rpc_gas_cap: 50000000
```

### geth_rpc_tx_fee_cap

Sets a cap on transaction fee (in ether) that can be sent via the RPC APIs (0 = no cap).

#### Defaults

```YAML
geth_rpc_tx_fee_cap: 1.0
```

### geth_snap_discovery_urls

List of snap discovery URLs.

#### Defaults

```YAML
geth_snap_discovery_urls: []
```

### geth_snapshot_cache

Memory allowance (MB) for snapshot caching.

#### Defaults

```YAML
geth_snapshot_cache: 102
```

### geth_state_history

Number of blocks from head whose state databases should be maintained.

#### Defaults

```YAML
geth_state_history: 90000
```

### geth_sync_mode

Blockchain sync mode ("fast", "full", "snap" or "light").

#### Defaults

```YAML
geth_sync_mode: snap
```

### geth_systemd_service_name

Systemd service name for Geth.

#### Defaults

```YAML
geth_systemd_service_name: geth
```

### geth_transaction_history

Number of blocks from head whose transaction indexes should be maintained.

#### Defaults

```YAML
geth_transaction_history: 2350000
```

### geth_trie_clean_cache

Memory allowance (MB) for clean trie nodes cache.

#### Defaults

```YAML
geth_trie_clean_cache: 154
```

### geth_trie_dirty_cache

Memory allowance (MB) for dirty trie nodes cache.

#### Defaults

```YAML
geth_trie_dirty_cache: 256
```

### geth_trie_timeout

Time limit for unloading trie nodes from memory (nanoseconds).

#### Defaults

```YAML
geth_trie_timeout: 3600000000000
```

### geth_tx_lookup_limit

Number of recent blocks to maintain transactions index for.

#### Defaults

```YAML
geth_tx_lookup_limit: 2350000
```

### geth_txpool_account_queue

Maximum number of non-executable transaction slots permitted per account.

#### Defaults

```YAML
geth_txpool_account_queue: 64
```

### geth_txpool_account_slots

Number of executable transaction slots guaranteed per account.

#### Defaults

```YAML
geth_txpool_account_slots: 16
```

### geth_txpool_global_queue

Maximum number of non-executable transaction slots for all accounts.

#### Defaults

```YAML
geth_txpool_global_queue: 1024
```

### geth_txpool_global_slots

Maximum number of executable transaction slots for all accounts.

#### Defaults

```YAML
geth_txpool_global_slots: 5120
```

### geth_txpool_journal

Disk journal for local transaction to survive node restarts.

#### Defaults

```YAML
geth_txpool_journal: transactions.rlp
```

### geth_txpool_lifetime

Maximum amount of time non-executable transactions are queued (nanoseconds).

#### Defaults

```YAML
geth_txpool_lifetime: 10800000000000
```

### geth_txpool_locals

List of local accounts whose transactions are included with higher priority.

#### Defaults

```YAML
geth_txpool_locals: []
```

### geth_txpool_no_locals

Disables price exemptions for locally submitted transactions.

#### Defaults

```YAML
geth_txpool_no_locals: false
```

### geth_txpool_price_bump

Price bump percentage to replace an already existing transaction.

#### Defaults

```YAML
geth_txpool_price_bump: 10
```

### geth_txpool_price_limit

Minimum gas price limit to enforce for acceptance into the pool.

#### Defaults

```YAML
geth_txpool_price_limit: 1
```

### geth_txpool_rejournal

Time interval to regenerate the local transaction journal (nanoseconds).

#### Defaults

```YAML
geth_txpool_rejournal: 3600000000000
```

### geth_user

Username for the Geth node.

#### Defaults

```YAML
geth_user: geth
```

### geth_vm_trace

Single transaction trace file.

#### Defaults

```YAML
geth_vm_trace: ''
```

### geth_vm_trace_json_config

VM trace configuration file as JSON.

#### Defaults

```YAML
geth_vm_trace_json_config: ''
```

## Tags

**_geth-config_**

**_geth-install_**

**_geth-prepare_**

## Dependencies

None.
