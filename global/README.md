# Buildtest Global Schema

The `global` schema specifies key/values that are shared across all Buildspec 
schemas. The global schema is validated with all Buildspec recipes, these keys are
defined at top most level.

## State: In Development

# Keys

| Name | Type | Supported in buildtest | Description | 
| ---- | ---- | -----------------------| ----------- | 
| version | string | YES | Select the version of schema to use with the key `type`. Currently `version: 1.0` is supported so if `type : script` then `script-v1.0.schema.json` will be used for validating buildspec | 
| maintainers | array | YES | A list of maintainers to specify for a Buildspec. This is an array of `string` items where one can specify their name, email, or github handle. | 

Required Keys: [`version`]