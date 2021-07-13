#!/usr/bin/python3
import requests

VERSION_MANIFEST_URL = "https://launchermeta.mojang.com/mc/game/version_manifest.json"

req = requests.get(VERSION_MANIFEST_URL)
manifest = req.json()

for version_info in manifest["versions"]:
    version_req = requests.get(version_info["url"])
    version = version_req.json()

    filename = "json/{}-mojang-{}-{}.json".format(
        version["minimumLauncherVersion"],
        version_info["type"],
        version_info["id"]
    )

    print("Writing to", filename)

    with open(filename, 'wb') as fd:
        for chunk in version_req.iter_content(chunk_size=128):
            fd.write(chunk)
