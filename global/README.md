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


# Global definitions

Below are keys that are defined in global.schema.json but are inherited
by other schemas.

| Name | Type | Supported in buildtest | Description | 
| ---- | ---- | -----------------------| ----------- | 
| env | object | YES | an object (dict) of custom environment variables | 
| executor | string | YES | name of executor to dispatch job defined in buildtest configuration |
| status | object | YES | specify behavior of how test state will be determined, this could be checked via returncode or regular expression |  
| sbatch | object | NO | specify sbatch options (#SBATCH) in test script.  For example if you specify ``sbatch: ["-t 10:00"]`` this will generate ``#SBATCH -t 10:00`` in test script. Do not pass the directive #SBATCH when using ``sbatch`` key because buildtest will automatically insert this for every key.

## status key

| Name | Type | Supported in buildtest | Description |
| ---- | ---- | ---------------------- | ----------- |
| returncode  | integer | YES | specify desired returncode for test to succeed. The returncode will be matched with returncode from test |
| regex | object | YES | specify regular expression to check with output or error stream |

## status[regex] key

| Name | Type | Supported in buildtest | Description |
| ---- | ---- | ---------------------- | ----------- |
| stream  | string | YES | Select stream to run regular expression check. Stream can be one of the two: [`stdout`, `stderr`] for test to succeed. |
| exp | string | YES | Specify regular expression to run with the specified stream. The expression is run internally via `re.search` and if there is a match test will pass. |
 
## Example

```yaml
version: "1.0"
hello_ex1:
  executor: local.bash
  type: script
  description: "hello world example"
  shell: "echo hello"
maintainers: 
   - "@vsoch"
```

Note that the outer structure contains the `version` and `maintainers` field, these
are validated by the [global](global) schema. The contents of the section `hello_ex1`
are of type `script`, and thus are tested by the [script](script) schema.
The above would say to use version 1.0 of the script schema to run the test.

