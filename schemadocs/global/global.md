# buildtest Global Schema Schema

```txt
https://buildtesters.github.io/schemas/global/global.schema.json
```




| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | ------------------------------------------------------------------------- |
| Can be instantiated | Yes        | Unknown status | No           | Forbidden         | Forbidden             | none                | [global.schema.json](../../out/global.schema.json "open original schema") |

## buildtest Global Schema Type

`object` ([buildtest Global Schema](global.md))

# buildtest Global Schema Properties

| Property                    | Type     | Required | Nullable       | Defined by                                                                                                                                                  |
| :-------------------------- | -------- | -------- | -------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [version](#version)         | `string` | Required | cannot be null | [buildtest Global Schema](global-properties-version.md "https&#x3A;//buildtesters.github.io/schemas/global/global.schema.json#/properties/version")         |
| [maintainers](#maintainers) | `array`  | Optional | cannot be null | [buildtest Global Schema](global-properties-maintainers.md "https&#x3A;//buildtesters.github.io/schemas/global/global.schema.json#/properties/maintainers") |
| [buildspecs](#buildspecs)   | `object` | Required | cannot be null | [buildtest Global Schema](global-properties-buildspecs.md "https&#x3A;//buildtesters.github.io/schemas/global/global.schema.json#/properties/buildspecs")   |

## version

The semver version of the schema to use (x.x).


`version`

-   is required
-   Type: `string`
-   cannot be null
-   defined in: [buildtest Global Schema](global-properties-version.md "https&#x3A;//buildtesters.github.io/schemas/global/global.schema.json#/properties/version")

### version Type

`string`

## maintainers

One or more maintainers or aliases


`maintainers`

-   is optional
-   Type: `string[]`
-   cannot be null
-   defined in: [buildtest Global Schema](global-properties-maintainers.md "https&#x3A;//buildtesters.github.io/schemas/global/global.schema.json#/properties/maintainers")

### maintainers Type

`string[]`

### maintainers Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

## buildspecs




`buildspecs`

-   is required
-   Type: `object` ([Details](global-properties-buildspecs.md))
-   cannot be null
-   defined in: [buildtest Global Schema](global-properties-buildspecs.md "https&#x3A;//buildtesters.github.io/schemas/global/global.schema.json#/properties/buildspecs")

### buildspecs Type

`object` ([Details](global-properties-buildspecs.md))

# buildtest Global Schema Definitions

## Definitions group env

Reference this group by using

```json
{"$ref":"https://buildtesters.github.io/schemas/global/global.schema.json#/definitions/env"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | ---- | -------- | -------- | :--------- |

## Definitions group tags

Reference this group by using

```json
{"$ref":"https://buildtesters.github.io/schemas/global/global.schema.json#/definitions/tags"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | ---- | -------- | -------- | :--------- |

## Definitions group skip

Reference this group by using

```json
{"$ref":"https://buildtesters.github.io/schemas/global/global.schema.json#/definitions/skip"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | ---- | -------- | -------- | :--------- |

## Definitions group executor

Reference this group by using

```json
{"$ref":"https://buildtesters.github.io/schemas/global/global.schema.json#/definitions/executor"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | ---- | -------- | -------- | :--------- |

## Definitions group sbatch

Reference this group by using

```json
{"$ref":"https://buildtesters.github.io/schemas/global/global.schema.json#/definitions/sbatch"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | ---- | -------- | -------- | :--------- |

## Definitions group bsub

Reference this group by using

```json
{"$ref":"https://buildtesters.github.io/schemas/global/global.schema.json#/definitions/bsub"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | ---- | -------- | -------- | :--------- |

## Definitions group status

Reference this group by using

```json
{"$ref":"https://buildtesters.github.io/schemas/global/global.schema.json#/definitions/status"}
```

| Property                                        | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                            |
| :---------------------------------------------- | --------- | -------- | -------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [slurm_job_state_codes](#slurm_job_state_codes) | `string`  | Optional | cannot be null | [buildtest Global Schema](global-definitions-status-properties-slurm_job_state_codes.md "https&#x3A;//buildtesters.github.io/schemas/global/global.schema.json#/definitions/status/properties/slurm_job_state_codes") |
| [returncode](#returncode)                       | `integer` | Optional | cannot be null | [buildtest Global Schema](global-definitions-status-properties-returncode.md "https&#x3A;//buildtesters.github.io/schemas/global/global.schema.json#/definitions/status/properties/returncode")                       |
| [regex](#regex)                                 | `object`  | Optional | cannot be null | [buildtest Global Schema](global-definitions-status-properties-regex.md "https&#x3A;//buildtesters.github.io/schemas/global/global.schema.json#/definitions/status/properties/regex")                                 |

### slurm_job_state_codes




`slurm_job_state_codes`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [buildtest Global Schema](global-definitions-status-properties-slurm_job_state_codes.md "https&#x3A;//buildtesters.github.io/schemas/global/global.schema.json#/definitions/status/properties/slurm_job_state_codes")

#### slurm_job_state_codes Type

`string`

#### slurm_job_state_codes Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value             | Explanation |
| :---------------- | ----------- |
| `"COMPLETED"`     |             |
| `"FAILED"`        |             |
| `"OUT_OF_MEMORY"` |             |
| `"TIMEOUT"`       |             |

### returncode




`returncode`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [buildtest Global Schema](global-definitions-status-properties-returncode.md "https&#x3A;//buildtesters.github.io/schemas/global/global.schema.json#/definitions/status/properties/returncode")

#### returncode Type

`integer`

### regex




`regex`

-   is optional
-   Type: `object` ([Details](global-definitions-status-properties-regex.md))
-   cannot be null
-   defined in: [buildtest Global Schema](global-definitions-status-properties-regex.md "https&#x3A;//buildtesters.github.io/schemas/global/global.schema.json#/definitions/status/properties/regex")

#### regex Type

`object` ([Details](global-definitions-status-properties-regex.md))
