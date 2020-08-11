# Untitled object in Buildtest Settings Schema Schema

```txt
https://buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/lsf
```




| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                      |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | ------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [settings.schema.json\*](../../out/settings.schema.json "open original schema") |

## lsf Type

`object` ([Details](settings-definitions-lsf.md))

# undefined Properties

| Property                    | Type          | Required | Nullable       | Defined by                                                                                                                                                                                          |
| :-------------------------- | ------------- | -------- | -------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [description](#description) | `string`      | Optional | cannot be null | [Buildtest Settings Schema](settings-definitions-lsf-properties-description.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/lsf/properties/description") |
| [launcher](#launcher)       | `string`      | Optional | cannot be null | [Buildtest Settings Schema](settings-definitions-lsf-properties-launcher.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/lsf/properties/launcher")       |
| [options](#options)         | `array`       | Optional | cannot be null | [Buildtest Settings Schema](settings-definitions-lsf-properties-options.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/lsf/properties/options")         |
| [environment](#environment) | Not specified | Optional | cannot be null | [Buildtest Settings Schema](settings-definitions-lsf-properties-environment.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/lsf/properties/environment") |
| [variables](#variables)     | Not specified | Optional | cannot be null | [Buildtest Settings Schema](settings-definitions-lsf-properties-variables.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/lsf/properties/variables")     |
| [queue](#queue)             | `string`      | Optional | cannot be null | [Buildtest Settings Schema](settings-definitions-lsf-properties-queue.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/lsf/properties/queue")             |
| [modules](#modules)         | `object`      | Optional | cannot be null | [Buildtest Settings Schema](settings-definitions-modules.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/lsf/properties/modules")                        |

## description




`description`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Buildtest Settings Schema](settings-definitions-lsf-properties-description.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/lsf/properties/description")

### description Type

`string`

## launcher




`launcher`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Buildtest Settings Schema](settings-definitions-lsf-properties-launcher.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/lsf/properties/launcher")

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
-   defined in: [Buildtest Settings Schema](settings-definitions-lsf-properties-options.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/lsf/properties/options")

### options Type

`string[]`

## environment




`environment`

-   is optional
-   Type: unknown
-   cannot be null
-   defined in: [Buildtest Settings Schema](settings-definitions-lsf-properties-environment.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/lsf/properties/environment")

### environment Type

unknown

## variables




`variables`

-   is optional
-   Type: unknown
-   cannot be null
-   defined in: [Buildtest Settings Schema](settings-definitions-lsf-properties-variables.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/lsf/properties/variables")

### variables Type

unknown

## queue




`queue`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Buildtest Settings Schema](settings-definitions-lsf-properties-queue.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/lsf/properties/queue")

### queue Type

`string`

## modules




`modules`

-   is optional
-   Type: `object` ([Details](settings-definitions-modules.md))
-   cannot be null
-   defined in: [Buildtest Settings Schema](settings-definitions-modules.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/lsf/properties/modules")

### modules Type

`object` ([Details](settings-definitions-modules.md))
