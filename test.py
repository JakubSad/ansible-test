#!/usr/bin/env python3

import json
import platform

os_version = {
	"System": [
	platform.system(),
    platform.release(),
    platform.version()
	]
}

print(json.dumps(os_version, indent=4))
