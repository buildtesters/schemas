# Buildtest Global Schema

The `global` schema specifies key/values that are shared across all Buildspec 
schemas. The global schema is validated with all Buildspec recipes, these keys are
defined at top most level. The schema documentation is based on [global.schema.json](https://buildtesters.github.io/schemas/global/global.schema.json).

# Keys

| Name | Type | Supported in buildtest | Required | Description | 
| ---- | ---- | -----------------------| ---------| ----------- | 
| version | string | YES | YES | Select the version of sub-schema to use with the `type` field when validating test. Currently `version` only supports `1.0` so if `type : script` then `script-v1.0.schema.json` will be used for validating test | 
| buildspecs | object | YES | YES | buildspecs is an object used to define one or more tests. Every test name follows the pattern `"^[A-Za-z_][A-Za-z0-9_]*$"`. You may define as many tests as you desire but each name must be unique. |  
| maintainers | array | YES | NO | A list of maintainers to specify for a Buildspec. This is an array of `string` items where one can specify their name, email, or github handle. | 



# Global definitions

Below are keys that are defined in global.schema.json but are inherited
by other schemas.

| Name | Type | Supported in buildtest | Description | 
| ---- | ---- | -----------------------| ----------- | 
| env | object | YES | an object (dict) of custom environment variables | 
| executor | string | YES | name of executor to dispatch job defined in buildtest configuration |
| status | object | YES | specify behavior of how test state will be determined, this could be checked via returncode or regular expression |  
| sbatch | object | YES | specify sbatch options (#SBATCH) in test script.  For example if you specify ``sbatch: ["-t 10:00"]`` this will generate ``#SBATCH -t 10:00`` in test script. Do not pass the directive #SBATCH when using ``sbatch`` key because buildtest will automatically insert this for every key.
| skip | boolean | YES | To skip a test set `skip: True` otherwise buildtest will build all tests. |
| tags | array | NO | Add tags to classify test, each tag must be of `string` type. |

## status key

| Name | Type | Supported in buildtest | Description |
| ---- | ---- | ---------------------- | ----------- |
| returncode  | integer | YES | specify desired returncode for test to succeed. The returncode will be matched with returncode from test |
| regex | object | YES | specify regular expression to check with output or error stream |

## regex object

| Name | Type | Supported in buildtest | Required | Description |
| ---- | ---- | ---------------------- | ---------| ----------- |
| stream  | string | YES | YES | Select stream to run regular expression check. Stream can be one of the two: [`stdout`, `stderr`] for test to succeed. |
| exp | string | YES | YES | Specify regular expression to run with the specified stream. The expression is run internally via `re.search` and if there is a match test will pass. |
 
## Example

```yaml
version: "1.0"
buildspecs:
  hello_world:
    executor: local.bash
    type: script
    description: "hello world example"
    run: "echo hello"
maintainers: 
   - "@shahzebsiddiqui"
```

Note that the outer structure contains the `version` and `maintainers` field, these
are validated by the [global](global) schema. The contents of the section `hello_world`
are of type `script`, and thus are tested by the [script](script) schema.
The above would say to use version 1.0 of the script schema to run the test.

