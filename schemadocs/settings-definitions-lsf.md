# Untitled object in buildtest configuration schema Schema

```txt
https://buildtesters.github.io/schemas/schemas/settings.schema.json#/definitions/lsf
```




| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                   |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | ---------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [settings.schema.json\*](../out/settings.schema.json "open original schema") |

## lsf Type

`object` ([Details](settings-definitions-lsf.md))

# undefined Properties

| Property                    | Type     | Required | Nullable       | Defined by                                                                                                                                                                                              |
| :-------------------------- | -------- | -------- | -------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [description](#description) | `string` | Optional | cannot be null | [buildtest configuration schema](settings-definitions-lsf-properties-description.md "https&#x3A;//buildtesters.github.io/schemas/schemas/settings.schema.json#/definitions/lsf/properties/description") |
| [launcher](#launcher)       | `string` | Optional | cannot be null | [buildtest configuration schema](settings-definitions-lsf-properties-launcher.md "https&#x3A;//buildtesters.github.io/schemas/schemas/settings.schema.json#/definitions/lsf/properties/launcher")       |
| [options](#options)         | `array`  | Optional | cannot be null | [buildtest configuration schema](settings-definitions-lsf-properties-options.md "https&#x3A;//buildtesters.github.io/schemas/schemas/settings.schema.json#/definitions/lsf/properties/options")         |
| [environment](#environment) | `object` | Optional | cannot be null | [buildtest configuration schema](global-definitions-env.md "https&#x3A;//buildtesters.github.io/schemas/schemas/settings.schema.json#/definitions/lsf/properties/environment")                          |
| [variables](#variables)     | `object` | Optional | cannot be null | [buildtest configuration schema](global-definitions-env.md "https&#x3A;//buildtesters.github.io/schemas/schemas/settings.schema.json#/definitions/lsf/properties/variables")                            |
| [queue](#queue)             | `string` | Optional | cannot be null | [buildtest configuration schema](settings-definitions-lsf-properties-queue.md "https&#x3A;//buildtesters.github.io/schemas/schemas/settings.schema.json#/definitions/lsf/properties/queue")             |
| [modules](#modules)         | `object` | Optional | cannot be null | [buildtest configuration schema](settings-definitions-modules.md "https&#x3A;//buildtesters.github.io/schemas/schemas/settings.schema.json#/definitions/lsf/properties/modules")                        |

## description




`description`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [buildtest configuration schema](settings-definitions-lsf-properties-description.md "https&#x3A;//buildtesters.github.io/schemas/schemas/settings.schema.json#/definitions/lsf/properties/description")

### description Type

`string`

## launcher




`launcher`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [buildtest configuration schema](settings-definitions-lsf-properties-launcher.md "https&#x3A;//buildtesters.github.io/schemas/schemas/settings.schema.json#/definitions/lsf/properties/launcher")

### launcher Type

`string`

### launcher Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value    | Explanation |
| :------- | ----------- |
| `"bsub"` |             |

## options




`options`

-   is optional
-   Type: `string[]`
-   cannot be null
-   defined in: [buildtest configuration schema](settings-definitions-lsf-properties-options.md "https&#x3A;//buildtesters.github.io/schemas/schemas/settings.schema.json#/definitions/lsf/properties/options")

### options Type

`string[]`

## environment

One or more key value pairs for an environment (key=value)


`environment`

-   is optional
-   Type: `object` ([Details](global-definitions-env.md))
-   cannot be null
-   defined in: [buildtest configuration schema](global-definitions-env.md "https&#x3A;//buildtesters.github.io/schemas/schemas/settings.schema.json#/definitions/lsf/properties/environment")

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
-   defined in: [buildtest configuration schema](global-definitions-env.md "https&#x3A;//buildtesters.github.io/schemas/schemas/settings.schema.json#/definitions/lsf/properties/variables")

### variables Type

`object` ([Details](global-definitions-env.md))

### variables Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

## queue




`queue`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [buildtest configuration schema](settings-definitions-lsf-properties-queue.md "https&#x3A;//buildtesters.github.io/schemas/schemas/settings.schema.json#/definitions/lsf/properties/queue")

### queue Type

`string`

## modules




`modules`

-   is optional
-   Type: `object` ([Details](settings-definitions-modules.md))
-   cannot be null
-   defined in: [buildtest configuration schema](settings-definitions-modules.md "https&#x3A;//buildtesters.github.io/schemas/schemas/settings.schema.json#/definitions/lsf/properties/modules")

### modules Type

`object` ([Details](settings-definitions-modules.md))
