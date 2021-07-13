#!/usr/bin/python3
import json
import os
from glob import glob

key_versions = {}

def walk(keys, node):
    version = int(node["minimumLauncherVersion"])
    _walk(keys, node, "", version)

def _walk(keys, node, cur, version):
    if isinstance(node, dict):
        for k, v in node.items():
            next = "{}/{}".format(cur, k)
            _walk(keys, v, next, version)
    elif isinstance(node, list):
        next = cur + "/*"
        for v in node:
            _walk(keys, v, next, version)
    else:
        cur = "{}({})".format(cur, type(node).__name__)
        if cur not in keys:
            keys[cur] = set()
        keys[cur].add(version)

files = glob("json/*.json")
for filename in files:
    with open(filename, 'r') as fd:
        launch_info = json.load(fd)
        walk(key_versions, launch_info)

print("SUMMARY:")
for k in sorted(key_versions.keys()):
    print(k)

print("\nDIFFERENCES:")

version_keys = {}

for k, v in key_versions.items():
    for version in v:
        if version not in version_keys:
            version_keys[version] = set()
        version_keys[version].add(k)

prev_keys = set()
for version in sorted(version_keys.keys()):
    print("launcher version:", version)

    cur_keys = version_keys[version]
    added = cur_keys - prev_keys
    missing = prev_keys - cur_keys

    for k in sorted(added):
        print("+", k)

    for k in sorted(missing):
        print("-", k)

    print()

    prev_keys = cur_keys
