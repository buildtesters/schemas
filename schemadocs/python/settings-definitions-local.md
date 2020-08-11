# Untitled object in Buildtest Settings Schema Schema

```txt
https://buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/local
```




| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                      |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | ------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [settings.schema.json\*](../../out/settings.schema.json "open original schema") |

## local Type

`object` ([Details](settings-definitions-local.md))

# undefined Properties

| Property                    | Type          | Required | Nullable       | Defined by                                                                                                                                                                                              |
| :-------------------------- | ------------- | -------- | -------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [description](#description) | `string`      | Optional | cannot be null | [Buildtest Settings Schema](settings-definitions-local-properties-description.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/local/properties/description") |
| [shell](#shell)             | `string`      | Required | cannot be null | [Buildtest Settings Schema](settings-definitions-local-properties-shell.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/local/properties/shell")             |
| [environment](#environment) | Not specified | Optional | cannot be null | [Buildtest Settings Schema](settings-definitions-local-properties-environment.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/local/properties/environment") |
| [variables](#variables)     | Not specified | Optional | cannot be null | [Buildtest Settings Schema](settings-definitions-local-properties-variables.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/local/properties/variables")     |
| [retry](#retry)             | `integer`     | Optional | cannot be null | [Buildtest Settings Schema](settings-definitions-local-properties-retry.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/local/properties/retry")             |
| [modules](#modules)         | `object`      | Optional | cannot be null | [Buildtest Settings Schema](settings-definitions-modules.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/local/properties/modules")                          |

## description




`description`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Buildtest Settings Schema](settings-definitions-local-properties-description.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/local/properties/description")

### description Type

`string`

## shell




`shell`

-   is required
-   Type: `string`
-   cannot be null
-   defined in: [Buildtest Settings Schema](settings-definitions-local-properties-shell.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/local/properties/shell")

### shell Type

`string`

### shell Constraints

**pattern**: the string must match the following regular expression: 

```regexp
^(/bin/bash|/bin/sh|sh|bash|python).*
```

[try pattern](https://regexr.com/?expression=%5E(%2Fbin%2Fbash%7C%2Fbin%2Fsh%7Csh%7Cbash%7Cpython).* "try regular expression with regexr.com")

## environment




`environment`

-   is optional
-   Type: unknown
-   cannot be null
-   defined in: [Buildtest Settings Schema](settings-definitions-local-properties-environment.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/local/properties/environment")

### environment Type

unknown

## variables




`variables`

-   is optional
-   Type: unknown
-   cannot be null
-   defined in: [Buildtest Settings Schema](settings-definitions-local-properties-variables.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/local/properties/variables")

### variables Type

unknown

## retry




`retry`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [Buildtest Settings Schema](settings-definitions-local-properties-retry.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/local/properties/retry")

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
-   defined in: [Buildtest Settings Schema](settings-definitions-modules.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/local/properties/modules")

### modules Type

`object` ([Details](settings-definitions-modules.md))
