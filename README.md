# elasticsearch-support-diagnostics-py

elasticsearch-support-diagnostics-py is a diagnostics support tool for Elasticsearch written in Python. It is based off the elasticsearch-support-diagnostics Elasticsearch plugin found here https://github.com/elastic/elasticsearch-support-diagnostics. The goal of the Python tool is to make full use of elasticsearch-py, the official low-level client for Elasticsearch. See https://www.elastic.co/guide/en/elasticsearch/client/python-api/current/index.html.

##Installation
elasticsearch-support-diagnostics-py requires elasticsearch-py for Elasticsearch API calls and Python 2.7+. 
```
pip install elasticsearch
git clone https://github.com/inqueue/elasticsearch-support-diagnostics-py.git
```

## Usage
All features are not yet fully implemented.
```
usage: esdiagnostics.py [-h] [-H HOST:PORT] [-n NODE] [-d PATH] [-nc]
                        [-u USERNAME] [-p PASSWORD] [-r N] [-i N]

This script is used to gather diagnostics information for Elasticsearch
support. In order to gather the Elasticsearch config and logs you must run
this on a node within your Elasticsearch cluster.

optional arguments:
  -h, --help            show this help message and exit
  -H HOST:PORT, --host HOST:PORT
                        Elasticsearch hostname:port. Default: localhost:9200
  -n NODE, --node NODE  On a host with multiple nodes, specify the node name
                        to gather data for. Value should match node.name as
                        defined in elasticsearch.yml
  -d PATH, --destination PATH
                        Destination root path. Support diagnostics will be
                        written to [PATH]/support-
                        diagnostics.[host].[node].[timestamp]. Defaults to
                        script location.
  -nc , --no-compression
                        Skip tarball creation.
  -u USERNAME, --username USERNAME
                        Basic authentication username. Prompt for password
                        unless -p is specified.
  -p PASSWORD, --password PASSWORD
                        Password for authentication when -u is used.

Periodic Stats Collection:
  Parameters for repeating calls to the _stats API.

  -r N, --repeat N      Repeat stats collection N times. Use with -i. Default:
                        1
  -i N, --interval N    Interval in seconds between stat collections
                        (optional, in conjunction with -r. Default: 60)
```

## Running On Windows
Running on Windows has not been tested and is not yet supported. Hopefully it'll just run like any other Python program.
