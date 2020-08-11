# Untitled object in buildtest configuration schema Schema

```txt
https://buildtesters.github.io/schemas/schemas/settings.schema.json#/definitions/slurm
```




| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                   |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | ---------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [settings.schema.json\*](../out/settings.schema.json "open original schema") |

## slurm Type

`object` ([Details](settings-definitions-slurm.md))

# undefined Properties

| Property                    | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                  |
| :-------------------------- | -------- | -------- | -------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [description](#description) | `string` | Optional | cannot be null | [buildtest configuration schema](settings-definitions-slurm-properties-description.md "https&#x3A;//buildtesters.github.io/schemas/schemas/settings.schema.json#/definitions/slurm/properties/description") |
| [launcher](#launcher)       | `string` | Optional | cannot be null | [buildtest configuration schema](settings-definitions-slurm-properties-launcher.md "https&#x3A;//buildtesters.github.io/schemas/schemas/settings.schema.json#/definitions/slurm/properties/launcher")       |
| [options](#options)         | `array`  | Optional | cannot be null | [buildtest configuration schema](settings-definitions-slurm-properties-options.md "https&#x3A;//buildtesters.github.io/schemas/schemas/settings.schema.json#/definitions/slurm/properties/options")         |
| [environment](#environment) | `object` | Optional | cannot be null | [buildtest configuration schema](global-definitions-env.md "https&#x3A;//buildtesters.github.io/schemas/schemas/settings.schema.json#/definitions/slurm/properties/environment")                            |
| [variables](#variables)     | `object` | Optional | cannot be null | [buildtest configuration schema](global-definitions-env.md "https&#x3A;//buildtesters.github.io/schemas/schemas/settings.schema.json#/definitions/slurm/properties/variables")                              |
| [cluster](#cluster)         | `string` | Optional | cannot be null | [buildtest configuration schema](settings-definitions-slurm-properties-cluster.md "https&#x3A;//buildtesters.github.io/schemas/schemas/settings.schema.json#/definitions/slurm/properties/cluster")         |
| [partition](#partition)     | `string` | Optional | cannot be null | [buildtest configuration schema](settings-definitions-slurm-properties-partition.md "https&#x3A;//buildtesters.github.io/schemas/schemas/settings.schema.json#/definitions/slurm/properties/partition")     |
| [qos](#qos)                 | `string` | Optional | cannot be null | [buildtest configuration schema](settings-definitions-slurm-properties-qos.md "https&#x3A;//buildtesters.github.io/schemas/schemas/settings.schema.json#/definitions/slurm/properties/qos")                 |
| [modules](#modules)         | `object` | Optional | cannot be null | [buildtest configuration schema](settings-definitions-modules.md "https&#x3A;//buildtesters.github.io/schemas/schemas/settings.schema.json#/definitions/slurm/properties/modules")                          |

## description




`description`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [buildtest configuration schema](settings-definitions-slurm-properties-description.md "https&#x3A;//buildtesters.github.io/schemas/schemas/settings.schema.json#/definitions/slurm/properties/description")

### description Type

`string`

## launcher




`launcher`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [buildtest configuration schema](settings-definitions-slurm-properties-launcher.md "https&#x3A;//buildtesters.github.io/schemas/schemas/settings.schema.json#/definitions/slurm/properties/launcher")

### launcher Type

`string`

### launcher Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value      | Explanation |
| :--------- | ----------- |
| `"sbatch"` |             |

## options




`options`

-   is optional
-   Type: `string[]`
-   cannot be null
-   defined in: [buildtest configuration schema](settings-definitions-slurm-properties-options.md "https&#x3A;//buildtesters.github.io/schemas/schemas/settings.schema.json#/definitions/slurm/properties/options")

### options Type

`string[]`

## environment

One or more key value pairs for an environment (key=value)


`environment`

-   is optional
-   Type: `object` ([Details](global-definitions-env.md))
-   cannot be null
-   defined in: [buildtest configuration schema](global-definitions-env.md "https&#x3A;//buildtesters.github.io/schemas/schemas/settings.schema.json#/definitions/slurm/properties/environment")

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
-   defined in: [buildtest configuration schema](global-definitions-env.md "https&#x3A;//buildtesters.github.io/schemas/schemas/settings.schema.json#/definitions/slurm/properties/variables")

### variables Type

`object` ([Details](global-definitions-env.md))

### variables Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

## cluster




`cluster`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [buildtest configuration schema](settings-definitions-slurm-properties-cluster.md "https&#x3A;//buildtesters.github.io/schemas/schemas/settings.schema.json#/definitions/slurm/properties/cluster")

### cluster Type

`string`

## partition




`partition`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [buildtest configuration schema](settings-definitions-slurm-properties-partition.md "https&#x3A;//buildtesters.github.io/schemas/schemas/settings.schema.json#/definitions/slurm/properties/partition")

### partition Type

`string`

## qos




`qos`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [buildtest configuration schema](settings-definitions-slurm-properties-qos.md "https&#x3A;//buildtesters.github.io/schemas/schemas/settings.schema.json#/definitions/slurm/properties/qos")

### qos Type

`string`

## modules




`modules`

-   is optional
-   Type: `object` ([Details](settings-definitions-modules.md))
-   cannot be null
-   defined in: [buildtest configuration schema](settings-definitions-modules.md "https&#x3A;//buildtesters.github.io/schemas/schemas/settings.schema.json#/definitions/slurm/properties/modules")

### modules Type

`object` ([Details](settings-definitions-modules.md))
