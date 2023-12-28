#!/usr/bin/env python3

import json

cars = {
	"manufacturers": [
	"toyota", "BMW", "Audi",
	"Ford", "Honda", "Suzuki"
	]
}

print(json.dumps(cars, indent=4))
