# python schema Schema

```txt
https://buildtesters.github.io/schemas/schemas/python-v1.0.schema.json
```




| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                       |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | -------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [python-v1.0.schema.json](../out/python-v1.0.schema.json "open original schema") |

## python schema Type

`object` ([python schema](python-v1.md))

# python schema Properties

| Property                    | Type          | Required | Nullable       | Defined by                                                                                                                                                 |
| :-------------------------- | ------------- | -------- | -------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [type](#type)               | `string`      | Required | cannot be null | [python schema](python-v1-properties-type.md "https&#x3A;//buildtesters.github.io/schemas/schemas/python-v1.0.schema.json#/properties/type")               |
| [description](#description) | `string`      | Optional | cannot be null | [python schema](python-v1-properties-description.md "https&#x3A;//buildtesters.github.io/schemas/schemas/python-v1.0.schema.json#/properties/description") |
| [executor](#executor)       | Not specified | Required | cannot be null | [python schema](python-v1-properties-executor.md "https&#x3A;//buildtesters.github.io/schemas/schemas/python-v1.0.schema.json#/properties/executor")       |
| [pyver](#pyver)             | `array`       | Required | cannot be null | [python schema](python-v1-properties-pyver.md "https&#x3A;//buildtesters.github.io/schemas/schemas/python-v1.0.schema.json#/properties/pyver")             |
| [package](#package)         | `object`      | Optional | cannot be null | [python schema](python-v1-properties-package.md "https&#x3A;//buildtesters.github.io/schemas/schemas/python-v1.0.schema.json#/properties/package")         |
| [module](#module)           | `array`       | Optional | cannot be null | [python schema](python-v1-properties-module.md "https&#x3A;//buildtesters.github.io/schemas/schemas/python-v1.0.schema.json#/properties/module")           |
| [sbatch](#sbatch)           | `array`       | Optional | cannot be null | [python schema](python-v1-properties-sbatch.md "https&#x3A;//buildtesters.github.io/schemas/schemas/python-v1.0.schema.json#/properties/sbatch")           |
| [python](#python)           | `string`      | Required | cannot be null | [python schema](python-v1-properties-python.md "https&#x3A;//buildtesters.github.io/schemas/schemas/python-v1.0.schema.json#/properties/python")           |
| [script](#script)           | `string`      | Optional | cannot be null | [python schema](python-v1-properties-script.md "https&#x3A;//buildtesters.github.io/schemas/schemas/python-v1.0.schema.json#/properties/script")           |
| [status](#status)           | `object`      | Optional | cannot be null | [python schema](global-definitions-status.md "https&#x3A;//buildtesters.github.io/schemas/schemas/python-v1.0.schema.json#/properties/status")             |
| [skip](#skip)               | `boolean`     | Optional | cannot be null | [python schema](global-definitions-skip.md "https&#x3A;//buildtesters.github.io/schemas/schemas/python-v1.0.schema.json#/properties/skip")                 |
| [tags](#tags)               | `array`       | Optional | cannot be null | [python schema](global-definitions-tags.md "https&#x3A;//buildtesters.github.io/schemas/schemas/python-v1.0.schema.json#/properties/tags")                 |

## type




`type`

-   is required
-   Type: `string`
-   cannot be null
-   defined in: [python schema](python-v1-properties-type.md "https&#x3A;//buildtesters.github.io/schemas/schemas/python-v1.0.schema.json#/properties/type")

### type Type

`string`

### type Constraints

**pattern**: the string must match the following regular expression: 

```regexp
^python$
```

[try pattern](https://regexr.com/?expression=%5Epython%24 "try regular expression with regexr.com")

## description




`description`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [python schema](python-v1-properties-description.md "https&#x3A;//buildtesters.github.io/schemas/schemas/python-v1.0.schema.json#/properties/description")

### description Type

`string`

## executor




`executor`

-   is required
-   Type: unknown
-   cannot be null
-   defined in: [python schema](python-v1-properties-executor.md "https&#x3A;//buildtesters.github.io/schemas/schemas/python-v1.0.schema.json#/properties/executor")

### executor Type

unknown

## pyver




`pyver`

-   is required
-   Type: `number[]`
-   cannot be null
-   defined in: [python schema](python-v1-properties-pyver.md "https&#x3A;//buildtesters.github.io/schemas/schemas/python-v1.0.schema.json#/properties/pyver")

### pyver Type

`number[]`

## package




`package`

-   is optional
-   Type: `object` ([Details](python-v1-properties-package.md))
-   cannot be null
-   defined in: [python schema](python-v1-properties-package.md "https&#x3A;//buildtesters.github.io/schemas/schemas/python-v1.0.schema.json#/properties/package")

### package Type

`object` ([Details](python-v1-properties-package.md))

## module




`module`

-   is optional
-   Type: `string[]`
-   cannot be null
-   defined in: [python schema](python-v1-properties-module.md "https&#x3A;//buildtesters.github.io/schemas/schemas/python-v1.0.schema.json#/properties/module")

### module Type

`string[]`

## sbatch




`sbatch`

-   is optional
-   Type: `string[]`
-   cannot be null
-   defined in: [python schema](python-v1-properties-sbatch.md "https&#x3A;//buildtesters.github.io/schemas/schemas/python-v1.0.schema.json#/properties/sbatch")

### sbatch Type

`string[]`

## python

A python script to run


`python`

-   is required
-   Type: `string`
-   cannot be null
-   defined in: [python schema](python-v1-properties-python.md "https&#x3A;//buildtesters.github.io/schemas/schemas/python-v1.0.schema.json#/properties/python")

### python Type

`string`

## script




`script`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [python schema](python-v1-properties-script.md "https&#x3A;//buildtesters.github.io/schemas/schemas/python-v1.0.schema.json#/properties/script")

### script Type

`string`

## status

The status section describes how buildtest detects PASS/FAIL on test. By default returncode 0 is a PASS and anything else is a FAIL, however buildtest can support other types of PASS/FAIL conditions.


`status`

-   is optional
-   Type: `object` ([Details](global-definitions-status.md))
-   cannot be null
-   defined in: [python schema](global-definitions-status.md "https&#x3A;//buildtesters.github.io/schemas/schemas/python-v1.0.schema.json#/properties/status")

### status Type

`object` ([Details](global-definitions-status.md))

## skip

The `skip` is a boolean field that can be used to skip tests during builds. By default buildtest will build and run all tests in your buildspec file, if `skip: True` is set it will skip the buildspec.


`skip`

-   is optional
-   Type: `boolean`
-   cannot be null
-   defined in: [python schema](global-definitions-skip.md "https&#x3A;//buildtesters.github.io/schemas/schemas/python-v1.0.schema.json#/properties/skip")

### skip Type

`boolean`

## tags

Classify tests using a tag name, this can be used for categorizing test and building tests using `--tags` option


`tags`

-   is optional
-   Type: `string[]`
-   cannot be null
-   defined in: [python schema](global-definitions-tags.md "https&#x3A;//buildtesters.github.io/schemas/schemas/python-v1.0.schema.json#/properties/tags")

### tags Type

`string[]`

### tags Constraints

**minimum number of items**: the minimum number of items for this array is: `1`
