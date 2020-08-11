# Buildtest Settings Schema Schema

```txt
https://buildtesters.github.io/schemas/settings/settings.schema.json
```




| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                    |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | ----------------------------------------------------------------------------- |
| Can be instantiated | Yes        | Unknown status | No           | Forbidden         | Forbidden             | none                | [settings.schema.json](../../out/settings.schema.json "open original schema") |

## Buildtest Settings Schema Type

`object` ([Buildtest Settings Schema](settings.md))

# Buildtest Settings Schema Properties

| Property                                      | Type          | Required | Nullable       | Defined by                                                                                                                                                      |
| :-------------------------------------------- | ------------- | -------- | -------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [executors](#executors)                       | `object`      | Required | cannot be null | [Buildtest Settings Schema](settings-properties-executors.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/properties/executors") |
| [config](#config)                             | `object`      | Required | cannot be null | [Buildtest Settings Schema](settings-properties-config.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/properties/config")       |
| [additionalProperties](#additionalProperties) | Not specified | Optional | cannot be null | [Untitled schema](undefined.md "undefined#undefined")                                                                                                           |

## executors




`executors`

-   is required
-   Type: `object` ([Details](settings-properties-executors.md))
-   cannot be null
-   defined in: [Buildtest Settings Schema](settings-properties-executors.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/properties/executors")

### executors Type

`object` ([Details](settings-properties-executors.md))

## config




`config`

-   is required
-   Type: `object` ([Details](settings-properties-config.md))
-   cannot be null
-   defined in: [Buildtest Settings Schema](settings-properties-config.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/properties/config")

### config Type

`object` ([Details](settings-properties-config.md))

## additionalProperties

no description

`additionalProperties`

-   is optional
-   Type: unknown
-   cannot be null
-   defined in: [Untitled schema](undefined.md "undefined#undefined")

### Untitled schema Type

unknown

# Buildtest Settings Schema Definitions

## Definitions group modules

Reference this group by using

```json
{"$ref":"https://buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/modules"}
```

| Property        | Type      | Required | Nullable       | Defined by                                                                                                                                                                                      |
| :-------------- | --------- | -------- | -------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [purge](#purge) | `boolean` | Optional | cannot be null | [Buildtest Settings Schema](settings-definitions-modules-properties-purge.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/modules/properties/purge") |
| [load](#load)   | `array`   | Optional | cannot be null | [Buildtest Settings Schema](settings-definitions-modules-properties-load.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/modules/properties/load")   |

### purge




`purge`

-   is optional
-   Type: `boolean`
-   cannot be null
-   defined in: [Buildtest Settings Schema](settings-definitions-modules-properties-purge.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/modules/properties/purge")

#### purge Type

`boolean`

### load




`load`

-   is optional
-   Type: `string[]`
-   cannot be null
-   defined in: [Buildtest Settings Schema](settings-definitions-modules-properties-load.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/modules/properties/load")

#### load Type

`string[]`

## Definitions group local

Reference this group by using

```json
{"$ref":"https://buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/local"}
```

| Property                    | Type          | Required | Nullable       | Defined by                                                                                                                                                                                              |
| :-------------------------- | ------------- | -------- | -------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [description](#description) | `string`      | Optional | cannot be null | [Buildtest Settings Schema](settings-definitions-local-properties-description.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/local/properties/description") |
| [shell](#shell)             | `string`      | Required | cannot be null | [Buildtest Settings Schema](settings-definitions-local-properties-shell.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/local/properties/shell")             |
| [environment](#environment) | Not specified | Optional | cannot be null | [Buildtest Settings Schema](settings-definitions-local-properties-environment.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/local/properties/environment") |
| [variables](#variables)     | Not specified | Optional | cannot be null | [Buildtest Settings Schema](settings-definitions-local-properties-variables.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/local/properties/variables")     |
| [retry](#retry)             | `integer`     | Optional | cannot be null | [Buildtest Settings Schema](settings-definitions-local-properties-retry.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/local/properties/retry")             |
| [modules](#modules)         | `object`      | Optional | cannot be null | [Buildtest Settings Schema](settings-definitions-modules.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/local/properties/modules")                          |

### description




`description`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Buildtest Settings Schema](settings-definitions-local-properties-description.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/local/properties/description")

#### description Type

`string`

### shell




`shell`

-   is required
-   Type: `string`
-   cannot be null
-   defined in: [Buildtest Settings Schema](settings-definitions-local-properties-shell.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/local/properties/shell")

#### shell Type

`string`

#### shell Constraints

**pattern**: the string must match the following regular expression: 

```regexp
^(/bin/bash|/bin/sh|sh|bash|python).*
```

[try pattern](https://regexr.com/?expression=%5E(%2Fbin%2Fbash%7C%2Fbin%2Fsh%7Csh%7Cbash%7Cpython).* "try regular expression with regexr.com")

### environment




`environment`

-   is optional
-   Type: unknown
-   cannot be null
-   defined in: [Buildtest Settings Schema](settings-definitions-local-properties-environment.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/local/properties/environment")

#### environment Type

unknown

### variables




`variables`

-   is optional
-   Type: unknown
-   cannot be null
-   defined in: [Buildtest Settings Schema](settings-definitions-local-properties-variables.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/local/properties/variables")

#### variables Type

unknown

### retry




`retry`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [Buildtest Settings Schema](settings-definitions-local-properties-retry.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/local/properties/retry")

#### retry Type

`integer`

#### retry Constraints

**maximum**: the value of this number must smaller than or equal to: `5`

**minimum**: the value of this number must greater than or equal to: `1`

### modules




`modules`

-   is optional
-   Type: `object` ([Details](settings-definitions-modules.md))
-   cannot be null
-   defined in: [Buildtest Settings Schema](settings-definitions-modules.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/local/properties/modules")

#### modules Type

`object` ([Details](settings-definitions-modules.md))

## Definitions group slurm

Reference this group by using

```json
{"$ref":"https://buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/slurm"}
```

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

### description




`description`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Buildtest Settings Schema](settings-definitions-slurm-properties-description.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/slurm/properties/description")

#### description Type

`string`

### launcher




`launcher`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Buildtest Settings Schema](settings-definitions-slurm-properties-launcher.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/slurm/properties/launcher")

#### launcher Type

`string`

#### launcher Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value      | Explanation |
| :--------- | ----------- |
| `"sbatch"` |             |

### options




`options`

-   is optional
-   Type: `string[]`
-   cannot be null
-   defined in: [Buildtest Settings Schema](settings-definitions-slurm-properties-options.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/slurm/properties/options")

#### options Type

`string[]`

### environment




`environment`

-   is optional
-   Type: unknown
-   cannot be null
-   defined in: [Buildtest Settings Schema](settings-definitions-slurm-properties-environment.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/slurm/properties/environment")

#### environment Type

unknown

### variables




`variables`

-   is optional
-   Type: unknown
-   cannot be null
-   defined in: [Buildtest Settings Schema](settings-definitions-slurm-properties-variables.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/slurm/properties/variables")

#### variables Type

unknown

### cluster




`cluster`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Buildtest Settings Schema](settings-definitions-slurm-properties-cluster.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/slurm/properties/cluster")

#### cluster Type

`string`

### partition




`partition`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Buildtest Settings Schema](settings-definitions-slurm-properties-partition.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/slurm/properties/partition")

#### partition Type

`string`

### qos




`qos`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Buildtest Settings Schema](settings-definitions-slurm-properties-qos.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/slurm/properties/qos")

#### qos Type

`string`

### modules




`modules`

-   is optional
-   Type: `object` ([Details](settings-definitions-modules.md))
-   cannot be null
-   defined in: [Buildtest Settings Schema](settings-definitions-modules.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/slurm/properties/modules")

#### modules Type

`object` ([Details](settings-definitions-modules.md))

## Definitions group lsf

Reference this group by using

```json
{"$ref":"https://buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/lsf"}
```

| Property                    | Type          | Required | Nullable       | Defined by                                                                                                                                                                                          |
| :-------------------------- | ------------- | -------- | -------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [description](#description) | `string`      | Optional | cannot be null | [Buildtest Settings Schema](settings-definitions-lsf-properties-description.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/lsf/properties/description") |
| [launcher](#launcher)       | `string`      | Optional | cannot be null | [Buildtest Settings Schema](settings-definitions-lsf-properties-launcher.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/lsf/properties/launcher")       |
| [options](#options)         | `array`       | Optional | cannot be null | [Buildtest Settings Schema](settings-definitions-lsf-properties-options.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/lsf/properties/options")         |
| [environment](#environment) | Not specified | Optional | cannot be null | [Buildtest Settings Schema](settings-definitions-lsf-properties-environment.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/lsf/properties/environment") |
| [variables](#variables)     | Not specified | Optional | cannot be null | [Buildtest Settings Schema](settings-definitions-lsf-properties-variables.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/lsf/properties/variables")     |
| [queue](#queue)             | `string`      | Optional | cannot be null | [Buildtest Settings Schema](settings-definitions-lsf-properties-queue.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/lsf/properties/queue")             |
| [modules](#modules)         | `object`      | Optional | cannot be null | [Buildtest Settings Schema](settings-definitions-modules.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/lsf/properties/modules")                        |

### description




`description`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Buildtest Settings Schema](settings-definitions-lsf-properties-description.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/lsf/properties/description")

#### description Type

`string`

### launcher




`launcher`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Buildtest Settings Schema](settings-definitions-lsf-properties-launcher.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/lsf/properties/launcher")

#### launcher Type

`string`

#### launcher Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value    | Explanation |
| :------- | ----------- |
| `"bsub"` |             |

### options




`options`

-   is optional
-   Type: `string[]`
-   cannot be null
-   defined in: [Buildtest Settings Schema](settings-definitions-lsf-properties-options.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/lsf/properties/options")

#### options Type

`string[]`

### environment




`environment`

-   is optional
-   Type: unknown
-   cannot be null
-   defined in: [Buildtest Settings Schema](settings-definitions-lsf-properties-environment.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/lsf/properties/environment")

#### environment Type

unknown

### variables




`variables`

-   is optional
-   Type: unknown
-   cannot be null
-   defined in: [Buildtest Settings Schema](settings-definitions-lsf-properties-variables.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/lsf/properties/variables")

#### variables Type

unknown

### queue




`queue`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Buildtest Settings Schema](settings-definitions-lsf-properties-queue.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/lsf/properties/queue")

#### queue Type

`string`

### modules




`modules`

-   is optional
-   Type: `object` ([Details](settings-definitions-modules.md))
-   cannot be null
-   defined in: [Buildtest Settings Schema](settings-definitions-modules.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/lsf/properties/modules")

#### modules Type

`object` ([Details](settings-definitions-modules.md))

## Definitions group ssh

Reference this group by using

```json
{"$ref":"https://buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/ssh"}
```

| Property                        | Type          | Required | Nullable       | Defined by                                                                                                                                                                                              |
| :------------------------------ | ------------- | -------- | -------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [description](#description)     | `string`      | Optional | cannot be null | [Buildtest Settings Schema](settings-definitions-ssh-properties-description.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/ssh/properties/description")     |
| [host](#host)                   | `string`      | Required | cannot be null | [Buildtest Settings Schema](settings-definitions-ssh-properties-host.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/ssh/properties/host")                   |
| [user](#user)                   | `string`      | Required | cannot be null | [Buildtest Settings Schema](settings-definitions-ssh-properties-user.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/ssh/properties/user")                   |
| [identity_file](#identity_file) | `string`      | Required | cannot be null | [Buildtest Settings Schema](settings-definitions-ssh-properties-identity_file.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/ssh/properties/identity_file") |
| [environment](#environment)     | Not specified | Optional | cannot be null | [Buildtest Settings Schema](settings-definitions-ssh-properties-environment.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/ssh/properties/environment")     |
| [variables](#variables)         | Not specified | Optional | cannot be null | [Buildtest Settings Schema](settings-definitions-ssh-properties-variables.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/ssh/properties/variables")         |
| [modules](#modules)             | `object`      | Optional | cannot be null | [Buildtest Settings Schema](settings-definitions-modules.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/ssh/properties/modules")                            |

### description




`description`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Buildtest Settings Schema](settings-definitions-ssh-properties-description.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/ssh/properties/description")

#### description Type

`string`

### host




`host`

-   is required
-   Type: `string`
-   cannot be null
-   defined in: [Buildtest Settings Schema](settings-definitions-ssh-properties-host.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/ssh/properties/host")

#### host Type

`string`

### user




`user`

-   is required
-   Type: `string`
-   cannot be null
-   defined in: [Buildtest Settings Schema](settings-definitions-ssh-properties-user.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/ssh/properties/user")

#### user Type

`string`

### identity_file




`identity_file`

-   is required
-   Type: `string`
-   cannot be null
-   defined in: [Buildtest Settings Schema](settings-definitions-ssh-properties-identity_file.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/ssh/properties/identity_file")

#### identity_file Type

`string`

### environment




`environment`

-   is optional
-   Type: unknown
-   cannot be null
-   defined in: [Buildtest Settings Schema](settings-definitions-ssh-properties-environment.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/ssh/properties/environment")

#### environment Type

unknown

### variables




`variables`

-   is optional
-   Type: unknown
-   cannot be null
-   defined in: [Buildtest Settings Schema](settings-definitions-ssh-properties-variables.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/ssh/properties/variables")

#### variables Type

unknown

### modules




`modules`

-   is optional
-   Type: `object` ([Details](settings-definitions-modules.md))
-   cannot be null
-   defined in: [Buildtest Settings Schema](settings-definitions-modules.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/ssh/properties/modules")

#### modules Type

`object` ([Details](settings-definitions-modules.md))
