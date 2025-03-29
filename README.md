Geth
=========

Ethereum execution layer client ansible role.

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
  - [geth_dir_base](#geth_dir_base)
  - [geth_dir_binary](#geth_dir_binary)
  - [geth_dir_config](#geth_dir_config)
  - [geth_dir_data](#geth_dir_data)
  - [geth_dir_log](#geth_dir_log)
  - [geth_dir_systemd](#geth_dir_systemd)
  - [geth_general_owner](#geth_general_owner)
  - [geth_group](#geth_group)
  - [geth_http_host](#geth_http_host)
  - [geth_http_modules](#geth_http_modules)
  - [geth_http_port](#geth_http_port)
  - [geth_jwt_secret_path](#geth_jwt_secret_path)
  - [geth_log_level](#geth_log_level)
  - [geth_network_id](#geth_network_id)
  - [geth_reinstall](#geth_reinstall)
  - [geth_sync_mode](#geth_sync_mode)
  - [geth_systemd_service_name](#geth_systemd_service_name)
  - [geth_user](#geth_user)
  - [geth_ws_enabled](#geth_ws_enabled)
  - [geth_ws_host](#geth_ws_host)
  - [geth_ws_modules](#geth_ws_modules)
  - [geth_ws_port](#geth_ws_port)
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

### geth_general_owner

General owner for Geth system files.

#### Defaults

```YAML
geth_general_owner: root
```

### geth_group

Group for running the Geth node.

#### Defaults

```YAML
geth_group: geth
```

### geth_http_host

HTTP-RPC server host address.

#### Defaults

```YAML
geth_http_host: 0.0.0.0
```

### geth_http_modules

Enabled HTTP-RPC modules.

#### Defaults

```YAML
geth_http_modules:
  - eth
  - net
  - web3
```

### geth_http_port

HTTP-RPC server port.

#### Defaults

```YAML
geth_http_port: 8545
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

### geth_network_id

Ethereum network ID (1 - Mainnet, 5 - Goerli, etc).

#### Defaults

```YAML
geth_network_id: 5
```

### geth_reinstall

#### Defaults

```YAML
geth_reinstall: false
```

### geth_sync_mode

Sync mode for Geth (fast, full, snap, light).

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

### geth_user

Username for the Geth node.

#### Defaults

```YAML
geth_user: geth
```

### geth_ws_enabled

Enable WebSocket RPC server.

#### Defaults

```YAML
geth_ws_enabled: false
```

### geth_ws_host

WebSocket RPC server host address.

#### Defaults

```YAML
geth_ws_host: 0.0.0.0
```

### geth_ws_modules

Enabled WebSocket RPC modules.

#### Defaults

```YAML
geth_ws_modules:
  - eth
  - net
  - web3
```

### geth_ws_port

WebSocket RPC server port.

#### Defaults

```YAML
geth_ws_port: 8546
```

## Tags

**_geth-config_**

**_geth-install_**

**_geth-prepare_**

## Dependencies

None.
