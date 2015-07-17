from django.shortcuts import render
from django.http import HttpResponse
from neo4jrestclient.client import GraphDatabase
from django.core import serializers
import json
from json import dumps

from neo4j.neo4j.settings import NEO4J_HOST, NEO4J_USERNAME, NEO4J_PASSWORD

def buildings(request):
    status={}
    if request.method == 'GET':
        gdb = GraphDatabase(NEO4J_HOST,NEO4J_USERNAME,NEO4J_PASSWORD)
        #gdb = GraphDatabase("http://localhost:7474", username="neo4j", password="papageno1")
        #building = gdb.labels.get('Building')
        #building.all()
        q = """MATCH (n:Building) return n.name, n.address, n.certification, n.leed_id"""
        results = gdb.query(q=q)
    
        buildings = []
        for building in results:
            building_info = {}
            building_info['name'] = building[0]
            building_info['address'] = building[1]
            building_info['certification'] = building[2]
            building_info['leed_id'] = building[3]
            buildings.append(building_info)
        
        status.update({'buildings': buildings})
        status.update({'status': 'Success'})
        return HttpResponse(json.dumps(status),content_type="application/json")
    else:
        status.update({'buildings': ''})
        status.update({'status': 'Invalid Request'})
        
    return HttpResponse(json.dumps(status))
