"""
support_utils.py - misc utilities: dirs, date parsing.
"""
import os
import datetime

def ensure_dirs():
    """Create data/ and output/ if missing."""
    os.makedirs('data', exist_ok=True)
    os.makedirs('output', exist_ok=True)

def parse_date(s):
    """Try common formats, return ISO string or original."""
    for fmt in ("%Y-%m-%d","%m/%d/%Y","%Y/%m/%d","%m-%d-%Y"):
        try:
            return datetime.datetime.strptime(s,fmt).date().isoformat()
        except:
            pass
    return s
