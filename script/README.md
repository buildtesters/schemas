# Script

This is the `script` schema used for `type: script` in Buildspec. This schema
is used for writing shell script like content in a Buildspec.

The schema can be found at https://buildtesters.github.io/schemas/script/script-v1.0.schema.json

# Keys

| Name | Type | Supported in buildtest | Description | 
| ---- | ---- | -----------------------| ----------- | 
| type | string | YES | The type must be  `script`. This is used to validate Buildspec with script schema | 
| description | string | YES | a description field to summarize the test | 
| env | object | YES | an object (dict) of custom environment variables | 
| shell | string | YES | shell interpreter to use for run section | 
| run | string | YES | main script to run |
| shebang | string | YES | specify shebang line for test script. This could be any value you like such as `#!/bin/bash`, `#!/bin/sh`, etc... |
| executor | string | NO | name of executor to dispatch job defined in buildtest configuration |
| status | object | YES | specify behavior of how test state will be determined, this could be checked via returncode or regular expression |  

Required Keys: [ `type`, `run` ]

# status key
| Name | Type | Supported in buildtest | Description |
| ---- | ---- | ---------------------- | ----------- |
| returncode  | integer | YES | specify desired returncode for test to succeed. The returncode will be matched with returncode from test |
| regex | object | YES | specify regular expression to check with output or error stream |

# status[regex] key
| Name | Type | Supported in buildtest | Description |
| ---- | ---- | ---------------------- | ----------- |
| stream  | string | YES | Select stream to run regular expression check. Stream can be one of the two: [`stdout`, `stderr`] for test to succeed. |
| exp | string | YES | Specify regular expression to run with the specified stream. The expression is run internally via `re.search` and if there is a match test will pass. |
 