# Untitled object in Buildtest Settings Schema Schema

```txt
https://buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/slurm
```




| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                      |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | ------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [settings.schema.json\*](../../out/settings.schema.json "open original schema") |

## slurm Type

`object` ([Details](settings-definitions-slurm.md))

# undefined Properties

| Property                    | Type          | Required | Nullable       | Defined by                                                                                                                                                                                              |
| :-------------------------- | ------------- | -------- | -------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [description](#description) | `string`      | Optional | cannot be null | [Buildtest Settings Schema](settings-definitions-slurm-properties-description.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/slurm/properties/description") |
| [launcher](#launcher)       | `string`      | Optional | cannot be null | [Buildtest Settings Schema](settings-definitions-slurm-properties-launcher.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/slurm/properties/launcher")       |
| [options](#options)         | `array`       | Optional | cannot be null | [Buildtest Settings Schema](settings-definitions-slurm-properties-options.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/slurm/properties/options")         |
| [environment](#environment) | Not specified | Optional | cannot be null | [Buildtest Settings Schema](settings-definitions-slurm-properties-environment.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/slurm/properties/environment") |
| [variables](#variables)     | Not specified | Optional | cannot be null | [Buildtest Settings Schema](settings-definitions-slurm-properties-variables.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/slurm/properties/variables")     |
| [cluster](#cluster)         | `string`      | Optional | cannot be null | [Buildtest Settings Schema](settings-definitions-slurm-properties-cluster.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/slurm/properties/cluster")         |
| [partition](#partition)     | `string`      | Optional | cannot be null | [Buildtest Settings Schema](settings-definitions-slurm-properties-partition.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/slurm/properties/partition")     |
| [qos](#qos)                 | `string`      | Optional | cannot be null | [Buildtest Settings Schema](settings-definitions-slurm-properties-qos.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/slurm/properties/qos")                 |
| [modules](#modules)         | `object`      | Optional | cannot be null | [Buildtest Settings Schema](settings-definitions-modules.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/slurm/properties/modules")                          |

## description




`description`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Buildtest Settings Schema](settings-definitions-slurm-properties-description.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/slurm/properties/description")

### description Type

`string`

## launcher




`launcher`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Buildtest Settings Schema](settings-definitions-slurm-properties-launcher.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/slurm/properties/launcher")

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
-   defined in: [Buildtest Settings Schema](settings-definitions-slurm-properties-options.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/slurm/properties/options")

### options Type

`string[]`

## environment




`environment`

-   is optional
-   Type: unknown
-   cannot be null
-   defined in: [Buildtest Settings Schema](settings-definitions-slurm-properties-environment.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/slurm/properties/environment")

### environment Type

unknown

## variables




`variables`

-   is optional
-   Type: unknown
-   cannot be null
-   defined in: [Buildtest Settings Schema](settings-definitions-slurm-properties-variables.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/slurm/properties/variables")

### variables Type

unknown

## cluster




`cluster`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Buildtest Settings Schema](settings-definitions-slurm-properties-cluster.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/slurm/properties/cluster")

### cluster Type

`string`

## partition




`partition`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Buildtest Settings Schema](settings-definitions-slurm-properties-partition.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/slurm/properties/partition")

### partition Type

`string`

## qos




`qos`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Buildtest Settings Schema](settings-definitions-slurm-properties-qos.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/slurm/properties/qos")

### qos Type

`string`

## modules




`modules`

-   is optional
-   Type: `object` ([Details](settings-definitions-modules.md))
-   cannot be null
-   defined in: [Buildtest Settings Schema](settings-definitions-modules.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/slurm/properties/modules")

### modules Type

`object` ([Details](settings-definitions-modules.md))
