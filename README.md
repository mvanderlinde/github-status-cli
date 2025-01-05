# GitHub Status CLI
[![PyPI Downloads](https://static.pepy.tech/badge/github-status-cli)](https://pepy.tech/projects/github-status-cli)

A small command-line utility that returns current status and incident information from the GitHub API.

Helpful to quickly check for service disruptions without switching apps when experiencing issues with git commands.

## Usage
```bash
$ github-status

----------------------------------------------------------------------------------------
|                        GitHub Status: All Systems Operational                        |
----------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------
|                     COMPONENT                      |             STATUS              |
----------------------------------------------------------------------------------------
| Git Operations                                     |           operational           |
| API Requests                                       |           operational           |
| Webhooks                                           |           operational           |
| Issues                                             |           operational           |
| Pull Requests                                      |           operational           |
| Actions                                            |           operational           |
| Packages                                           |           operational           |
| Pages                                              |           operational           |
| Codespaces                                         |           operational           |
| Copilot                                            |           operational           |
----------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------
|                      INCIDENT                      |  IMPACT  |        STATUS        |
----------------------------------------------------------------------------------------
|                       There are currently no active incidents.                       |
----------------------------------------------------------------------------------------
```



## Installation

### Using `pip`
```bash
$ pip install github-status-cli
```

### Manually
```bash
$ git clone https://github.com/mvanderlinde/github-status-cli.git
$ cd github-status-cli
$ python -m build
$ pip install dist/github_status_cli-1.0.0-py3-none-any.whl
```
