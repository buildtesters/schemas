# BuildTest Test Configuration for Script Schema

```txt
https://buildtesters.github.io/schemas/schemas/script-v1.0.schema.json
```




| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                       |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | -------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [script-v1.0.schema.json](../out/script-v1.0.schema.json "open original schema") |

## BuildTest Test Configuration for Script Type

`object` ([BuildTest Test Configuration for Script](script-v1.md))

# BuildTest Test Configuration for Script Properties

| Property                    | Type      | Required | Nullable       | Defined by                                                                                                                                                                           |
| :-------------------------- | --------- | -------- | -------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [type](#type)               | `string`  | Required | cannot be null | [BuildTest Test Configuration for Script](script-v1-properties-type.md "https&#x3A;//buildtesters.github.io/schemas/schemas/script-v1.0.schema.json#/properties/type")               |
| [description](#description) | `string`  | Optional | cannot be null | [BuildTest Test Configuration for Script](script-v1-properties-description.md "https&#x3A;//buildtesters.github.io/schemas/schemas/script-v1.0.schema.json#/properties/description") |
| [sbatch](#sbatch)           | `array`   | Optional | cannot be null | [BuildTest Test Configuration for Script](global-definitions-sbatch.md "https&#x3A;//buildtesters.github.io/schemas/schemas/script-v1.0.schema.json#/properties/sbatch")             |
| [bsub](#bsub)               | `array`   | Optional | cannot be null | [BuildTest Test Configuration for Script](global-definitions-bsub.md "https&#x3A;//buildtesters.github.io/schemas/schemas/script-v1.0.schema.json#/properties/bsub")                 |
| [env](#env)                 | `object`  | Optional | cannot be null | [BuildTest Test Configuration for Script](global-definitions-env.md "https&#x3A;//buildtesters.github.io/schemas/schemas/script-v1.0.schema.json#/properties/env")                   |
| [vars](#vars)               | `object`  | Optional | cannot be null | [BuildTest Test Configuration for Script](global-definitions-env.md "https&#x3A;//buildtesters.github.io/schemas/schemas/script-v1.0.schema.json#/properties/vars")                  |
| [executor](#executor)       | `string`  | Required | cannot be null | [BuildTest Test Configuration for Script](global-definitions-executor.md "https&#x3A;//buildtesters.github.io/schemas/schemas/script-v1.0.schema.json#/properties/executor")         |
| [shell](#shell)             | `string`  | Optional | cannot be null | [BuildTest Test Configuration for Script](script-v1-properties-shell.md "https&#x3A;//buildtesters.github.io/schemas/schemas/script-v1.0.schema.json#/properties/shell")             |
| [shebang](#shebang)         | `string`  | Optional | cannot be null | [BuildTest Test Configuration for Script](script-v1-properties-shebang.md "https&#x3A;//buildtesters.github.io/schemas/schemas/script-v1.0.schema.json#/properties/shebang")         |
| [run](#run)                 | `string`  | Required | cannot be null | [BuildTest Test Configuration for Script](script-v1-properties-run.md "https&#x3A;//buildtesters.github.io/schemas/schemas/script-v1.0.schema.json#/properties/run")                 |
| [status](#status)           | `object`  | Optional | cannot be null | [BuildTest Test Configuration for Script](global-definitions-status.md "https&#x3A;//buildtesters.github.io/schemas/schemas/script-v1.0.schema.json#/properties/status")             |
| [skip](#skip)               | `boolean` | Optional | cannot be null | [BuildTest Test Configuration for Script](global-definitions-skip.md "https&#x3A;//buildtesters.github.io/schemas/schemas/script-v1.0.schema.json#/properties/skip")                 |
| [tags](#tags)               | `array`   | Optional | cannot be null | [BuildTest Test Configuration for Script](global-definitions-tags.md "https&#x3A;//buildtesters.github.io/schemas/schemas/script-v1.0.schema.json#/properties/tags")                 |

## type

Select schema type to use when validating buildspec. This must be of set to 'script'


`type`

-   is required
-   Type: `string`
-   cannot be null
-   defined in: [BuildTest Test Configuration for Script](script-v1-properties-type.md "https&#x3A;//buildtesters.github.io/schemas/schemas/script-v1.0.schema.json#/properties/type")

### type Type

`string`

### type Constraints

**pattern**: the string must match the following regular expression: 

```regexp
^script$
```

[try pattern](https://regexr.com/?expression=%5Escript%24 "try regular expression with regexr.com")

## description

The `description` field is used to document what the test is doing


`description`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [BuildTest Test Configuration for Script](script-v1-properties-description.md "https&#x3A;//buildtesters.github.io/schemas/schemas/script-v1.0.schema.json#/properties/description")

### description Type

`string`

## sbatch

This field is used for specifying #SBATCH options in test script. buildtest will insert #SBATCH in front of each value


`sbatch`

-   is optional
-   Type: `string[]`
-   cannot be null
-   defined in: [BuildTest Test Configuration for Script](global-definitions-sbatch.md "https&#x3A;//buildtesters.github.io/schemas/schemas/script-v1.0.schema.json#/properties/sbatch")

### sbatch Type

`string[]`

## bsub

This field is used for specifying #BSUB options in test script. buildtest will insert #BSUB in front of each value


`bsub`

-   is optional
-   Type: `string[]`
-   cannot be null
-   defined in: [BuildTest Test Configuration for Script](global-definitions-bsub.md "https&#x3A;//buildtesters.github.io/schemas/schemas/script-v1.0.schema.json#/properties/bsub")

### bsub Type

`string[]`

## env

One or more key value pairs for an environment (key=value)


`env`

-   is optional
-   Type: `object` ([Details](global-definitions-env.md))
-   cannot be null
-   defined in: [BuildTest Test Configuration for Script](global-definitions-env.md "https&#x3A;//buildtesters.github.io/schemas/schemas/script-v1.0.schema.json#/properties/env")

### env Type

`object` ([Details](global-definitions-env.md))

### env Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

## vars

One or more key value pairs for an environment (key=value)


`vars`

-   is optional
-   Type: `object` ([Details](global-definitions-env.md))
-   cannot be null
-   defined in: [BuildTest Test Configuration for Script](global-definitions-env.md "https&#x3A;//buildtesters.github.io/schemas/schemas/script-v1.0.schema.json#/properties/vars")

### vars Type

`object` ([Details](global-definitions-env.md))

### vars Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

## executor

Select one of the executor name defined in your configuration file (`config.yml`). Every buildspec must have an executor which is responsible for running job. 


`executor`

-   is required
-   Type: `string`
-   cannot be null
-   defined in: [BuildTest Test Configuration for Script](global-definitions-executor.md "https&#x3A;//buildtesters.github.io/schemas/schemas/script-v1.0.schema.json#/properties/executor")

### executor Type

`string`

## shell

Specify a shell launcher to use when running jobs. This sets the shebang line in your test script. The `shell` key can be used with `run` section to describe content of script and how its executed


`shell`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [BuildTest Test Configuration for Script](script-v1-properties-shell.md "https&#x3A;//buildtesters.github.io/schemas/schemas/script-v1.0.schema.json#/properties/shell")

### shell Type

`string`

### shell Constraints

**pattern**: the string must match the following regular expression: 

```regexp
^(/bin/bash|/bin/sh|sh|bash|python).*
```

[try pattern](https://regexr.com/?expression=%5E(%2Fbin%2Fbash%7C%2Fbin%2Fsh%7Csh%7Cbash%7Cpython).* "try regular expression with regexr.com")

## shebang

Specify a custom shebang line. If not specified buildtest will automatically add it in the test script.


`shebang`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [BuildTest Test Configuration for Script](script-v1-properties-shebang.md "https&#x3A;//buildtesters.github.io/schemas/schemas/script-v1.0.schema.json#/properties/shebang")

### shebang Type

`string`

## run

A script to run using the default shell.


`run`

-   is required
-   Type: `string`
-   cannot be null
-   defined in: [BuildTest Test Configuration for Script](script-v1-properties-run.md "https&#x3A;//buildtesters.github.io/schemas/schemas/script-v1.0.schema.json#/properties/run")

### run Type

`string`

## status

The status section describes how buildtest detects PASS/FAIL on test. By default returncode 0 is a PASS and anything else is a FAIL, however buildtest can support other types of PASS/FAIL conditions.


`status`

-   is optional
-   Type: `object` ([Details](global-definitions-status.md))
-   cannot be null
-   defined in: [BuildTest Test Configuration for Script](global-definitions-status.md "https&#x3A;//buildtesters.github.io/schemas/schemas/script-v1.0.schema.json#/properties/status")

### status Type

`object` ([Details](global-definitions-status.md))

## skip

The `skip` is a boolean field that can be used to skip tests during builds. By default buildtest will build and run all tests in your buildspec file, if `skip: True` is set it will skip the buildspec.


`skip`

-   is optional
-   Type: `boolean`
-   cannot be null
-   defined in: [BuildTest Test Configuration for Script](global-definitions-skip.md "https&#x3A;//buildtesters.github.io/schemas/schemas/script-v1.0.schema.json#/properties/skip")

### skip Type

`boolean`

## tags

Classify tests using a tag name, this can be used for categorizing test and building tests using `--tags` option


`tags`

-   is optional
-   Type: `string[]`
-   cannot be null
-   defined in: [BuildTest Test Configuration for Script](global-definitions-tags.md "https&#x3A;//buildtesters.github.io/schemas/schemas/script-v1.0.schema.json#/properties/tags")

### tags Type

`string[]`

### tags Constraints

**minimum number of items**: the minimum number of items for this array is: `1`
