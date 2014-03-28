#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
# Changed to add ".local" to D_D_M
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "JOSFound.settings.local")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
