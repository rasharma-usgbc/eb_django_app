#!/usr/bin/env python
import os
import sys
from py2neo import neo4j
graph_db = neo4j.GraphDatabaseService("http://localhost:7474/db/data/")

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "neo4j.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
