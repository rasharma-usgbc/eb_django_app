import os
import sys
import neo4j

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "neo4j.settings")

    from django.core.management import execute_from_command_line
    print sys.argv
    execute_from_command_line(sys.argv)
