# Untitled object in buildtest configuration schema Schema

```txt
https://buildtesters.github.io/schemas/schemas/settings.schema.json#/definitions/local
```




| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                   |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | ---------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [settings.schema.json\*](../out/settings.schema.json "open original schema") |

## local Type

`object` ([Details](settings-definitions-local.md))

# undefined Properties

| Property                    | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                  |
| :-------------------------- | --------- | -------- | -------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [description](#description) | `string`  | Optional | cannot be null | [buildtest configuration schema](settings-definitions-local-properties-description.md "https&#x3A;//buildtesters.github.io/schemas/schemas/settings.schema.json#/definitions/local/properties/description") |
| [shell](#shell)             | `string`  | Required | cannot be null | [buildtest configuration schema](settings-definitions-local-properties-shell.md "https&#x3A;//buildtesters.github.io/schemas/schemas/settings.schema.json#/definitions/local/properties/shell")             |
| [environment](#environment) | `object`  | Optional | cannot be null | [buildtest configuration schema](global-definitions-env.md "https&#x3A;//buildtesters.github.io/schemas/schemas/settings.schema.json#/definitions/local/properties/environment")                            |
| [variables](#variables)     | `object`  | Optional | cannot be null | [buildtest configuration schema](global-definitions-env.md "https&#x3A;//buildtesters.github.io/schemas/schemas/settings.schema.json#/definitions/local/properties/variables")                              |
| [retry](#retry)             | `integer` | Optional | cannot be null | [buildtest configuration schema](settings-definitions-local-properties-retry.md "https&#x3A;//buildtesters.github.io/schemas/schemas/settings.schema.json#/definitions/local/properties/retry")             |
| [modules](#modules)         | `object`  | Optional | cannot be null | [buildtest configuration schema](settings-definitions-modules.md "https&#x3A;//buildtesters.github.io/schemas/schemas/settings.schema.json#/definitions/local/properties/modules")                          |

## description




`description`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [buildtest configuration schema](settings-definitions-local-properties-description.md "https&#x3A;//buildtesters.github.io/schemas/schemas/settings.schema.json#/definitions/local/properties/description")

### description Type

`string`

## shell




`shell`

-   is required
-   Type: `string`
-   cannot be null
-   defined in: [buildtest configuration schema](settings-definitions-local-properties-shell.md "https&#x3A;//buildtesters.github.io/schemas/schemas/settings.schema.json#/definitions/local/properties/shell")

### shell Type

`string`

### shell Constraints

**pattern**: the string must match the following regular expression: 

```regexp
^(/bin/bash|/bin/sh|sh|bash|python).*
```

[try pattern](https://regexr.com/?expression=%5E(%2Fbin%2Fbash%7C%2Fbin%2Fsh%7Csh%7Cbash%7Cpython).* "try regular expression with regexr.com")

## environment

One or more key value pairs for an environment (key=value)


`environment`

-   is optional
-   Type: `object` ([Details](global-definitions-env.md))
-   cannot be null
-   defined in: [buildtest configuration schema](global-definitions-env.md "https&#x3A;//buildtesters.github.io/schemas/schemas/settings.schema.json#/definitions/local/properties/environment")

### environment Type

`object` ([Details](global-definitions-env.md))

### environment Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

## variables

One or more key value pairs for an environment (key=value)


`variables`

-   is optional
-   Type: `object` ([Details](global-definitions-env.md))
-   cannot be null
-   defined in: [buildtest configuration schema](global-definitions-env.md "https&#x3A;//buildtesters.github.io/schemas/schemas/settings.schema.json#/definitions/local/properties/variables")

### variables Type

`object` ([Details](global-definitions-env.md))

### variables Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

## retry




`retry`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [buildtest configuration schema](settings-definitions-local-properties-retry.md "https&#x3A;//buildtesters.github.io/schemas/schemas/settings.schema.json#/definitions/local/properties/retry")

### retry Type

`integer`

### retry Constraints

**maximum**: the value of this number must smaller than or equal to: `5`

**minimum**: the value of this number must greater than or equal to: `1`

## modules




`modules`

-   is optional
-   Type: `object` ([Details](settings-definitions-modules.md))
-   cannot be null
-   defined in: [buildtest configuration schema](settings-definitions-modules.md "https&#x3A;//buildtesters.github.io/schemas/schemas/settings.schema.json#/definitions/local/properties/modules")

### modules Type

`object` ([Details](settings-definitions-modules.md))
