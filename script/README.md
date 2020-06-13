# Script

This is the `script` schema used for `type: script` in Buildspec. This schema
is used for writing shell script like content in a Buildspec.

The schema can be found at https://buildtesters.github.io/schemas/script/script-v1.0.schema.json

## Keys

| Name | Type | Supported in buildtest | Description | 
| ---- | ---- | -----------------------| ----------- | 
| type | string | YES | The type must be  `script`. This is used to validate Buildspec with script schema | 
| description | string | YES | a description field to summarize the test | 
| shell | string | YES | shell interpreter to use for run section | 
| run | string | YES | main script to run |
| shebang | string | YES | specify shebang line for test script. This could be any value you like such as `#!/bin/bash`, `#!/bin/sh`, etc... |

Required Keys: [ `type`, `run`, `executor`]

## Keys inherited from global.schema.json

- status
- env
- executor

