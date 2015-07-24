#!/usr/bin/env python
import os
import sys

from py2neo import neo4j
#graph_db = neo4j.GraphDatabaseService("http://arcdb.sb05.stations.graphenedb.com:24789/db/data/")

#from py2neo import neo4j
#from neo4jrestclient.client import GraphDatabase

#from urlparse import urlparse, urlunparse
#url = urlparse("http://arcdb.sb05.stations.graphenedb.com:24789/db/data/")
#url_without_auth = urlunparse((url.scheme, "{0}:{1}".format(url.hostname, url.port), url.path, None, None, None))

#gdb = GraphDatabase(url_without_auth, username = 'arc_db', password = 'EOrf19W9V1DpiNZEwyli')

#graph_db = neo4j.GraphDatabaseService("http://localhost:7474/db/data/")

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "neo4j.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
