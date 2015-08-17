from elasticsearch import Elasticsearch
from time import strftime
import argparse
import json
import sys

def timestamp():
    return strftime('%Y%m%d-%H%M%S')

def write_json(es_diags):
    es = Elasticsearch(hosts=['localhost'])

    for diag in es_diags:
        print 'Collecting %s...' % es_diags[diag]['status']
        filename = diag + '.json'
        f = open(filename, mode='w')
        result = eval(es_diags[diag]['method'])
        json.dump(result, f, indent=2)

    return

def main():
    #Connection tests?
    #Sanity check against the node?
    #_licenses API? It does not appear to be valid when Shield is not installed.

    targetNode = '_local'

    diags = {'alias': {'status': 'Index Aliases', 'method': 'es.indices.get_aliases()'},
             'cluster_state': {'status': 'Cluster State', 'method': 'es.cluster.state()'},
             'cluster_stats': {'status': 'Cluster Stats', 'method': 'es.cluster.stats()'},
             'cluster_health': {'status': 'Cluster Health', 'method': 'es.cluster.health()'},
             'cluster_pending_tasks': {'status': 'Pending Cluster Tasks', 'method': 'es.cluster.pending_tasks()'},
             'count': {'status': 'ES Count', 'method': 'es.count()'},
             'nodes': {'status': 'ES Nodes', 'method': 'es.nodes.info()'},
             'mapping': {'status': 'Index Mappings', 'method': "es.indices.get_mapping(index='_all')"},
             'settings': {'status': 'Index Settings', 'method': "es.indices.get_settings(index='_all')"},
             'cluster_settings': {'status': 'Cluster Settings', 'method': 'es.cluster.get_settings()'},
             'segments': {'status': 'Index Segments', 'method': "es.indices.segments(index='_all')"},
             'version': {'status': 'Version', 'method': 'es.info()'}
            }

    #write diags
    write_json(diags)

if __name__ == "__main__":
    script_description = 'This script is used to gather diagnostics information for Elasticsearch support. \
                          In order to gather the Elasticsearch config and logs you must run this on a node within your \
                          Elasticsearch cluster.'
    parser = argparse.ArgumentParser(description=script_description)
    parser.add_argument('-H', '--host', metavar='HOST:PORT', default='localhost:9200', help='Elasticsearch \
                        hostname:port. Default: localhost:9200')
    parser.add_argument('-n', '--node', default='_local', help='On a host with multiple nodes, specify the node name \
                        to gather data for. Value should match node.name as defined in elasticsearch.yml')
    parser.add_argument('-d', '--destination', metavar='PATH', help='Destination root path. Support diagnostics will \
                        be written to [PATH]/support-diagnostics.[host].[node].[timestamp]. Defaults to script \
                        location.')
    parser.add_argument('-nc', '--no-compression', metavar='', default=False, help='Skip tarball creation.')
    parser.add_argument('-u', '--username', help='Basic authentication username. Prompt for password unless -p is \
                        specified.')
    parser.add_argument('-p', '--password', help='Password for authentication when -u is used.')
    stats_group = parser.add_argument_group(title='Periodic Stats Collection', description='Parameters for repeating \
                                            calls to the _stats API.')
    stats_group.add_argument('-r', '--repeat', metavar="N", default=10, help='Repeat stats collection N times. Use \
                             with -i. Default: 1')
    stats_group.add_argument('-i', '--interval', type=int, default=60, metavar='N', help='Interval in seconds between \
                             stat collections (optional, in conjunction with -r. Default: 60)')

    args = parser.parse_args()
    host = args.host.split(':')
    targetNode = '_local'
    diag_directory = 'support-diagnostics.' + host[0] + '.' + targetNode + '.' + timestamp()

    main()