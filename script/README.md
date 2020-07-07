# Script

This is the `script` schema used for `type: script` in Buildspec. This schema
is used for writing shell script like content in a Buildspec. The schema documentation 
is based on [script-v1.0.schema.json](https://buildtesters.github.io/schemas/script/script-v1.0.schema.json).

## Script Schema Fields 

| Name | Type | Supported in buildtest | Required | Description | Valid Options | 
| ---- | ---- | -----------------------| --------- | ----------- | ------------- | 
| type | string | YES | YES | The schema type used to validate test . | `script` | 
| executor | string | YES | YES | inherited from global definition | |
| description | string | YES | NO |  a description field to summarize the test | | 
| shell | string | YES | NO | shell interpreter to use for run section | `"^(/bin/bash|/bin/sh|sh|bash|python).*"` |
| run | string | YES | YES | main script to run | |
| shebang | string | YES | NO | specify shebang line for test script. This could be any value you like such as `#!/bin/bash`, `#!/bin/sh`, etc... | |
| status | object | YES | NO | inherited from global definition | |
| vars | object | YES | NO | inherited from global definition  | |
| env | object | YES | NO | inherited from global definition | |
| sbatch | object | YES | NO | inherited from global definition | |
