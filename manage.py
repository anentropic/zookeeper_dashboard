#!/usr/bin/env python
import os
import sys
#try:
#import settings # Assumed to be in the same directory.
#except ImportError:
#    import sys
#    sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r.")
#    sys.exit(1)

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "zookeeper_dashboard.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
