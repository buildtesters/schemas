# Untitled object in buildtest Global Schema Schema

```txt
https://buildtesters.github.io/schemas/global/global.schema.json#/definitions/status
```




| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                  |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | --------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [global.schema.json\*](../../out/global.schema.json "open original schema") |

## status Type

`object` ([Details](global-definitions-status.md))

# undefined Properties

| Property                                        | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                            |
| :---------------------------------------------- | --------- | -------- | -------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [slurm_job_state_codes](#slurm_job_state_codes) | `string`  | Optional | cannot be null | [buildtest Global Schema](global-definitions-status-properties-slurm_job_state_codes.md "https&#x3A;//buildtesters.github.io/schemas/global/global.schema.json#/definitions/status/properties/slurm_job_state_codes") |
| [returncode](#returncode)                       | `integer` | Optional | cannot be null | [buildtest Global Schema](global-definitions-status-properties-returncode.md "https&#x3A;//buildtesters.github.io/schemas/global/global.schema.json#/definitions/status/properties/returncode")                       |
| [regex](#regex)                                 | `object`  | Optional | cannot be null | [buildtest Global Schema](global-definitions-status-properties-regex.md "https&#x3A;//buildtesters.github.io/schemas/global/global.schema.json#/definitions/status/properties/regex")                                 |

## slurm_job_state_codes




`slurm_job_state_codes`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [buildtest Global Schema](global-definitions-status-properties-slurm_job_state_codes.md "https&#x3A;//buildtesters.github.io/schemas/global/global.schema.json#/definitions/status/properties/slurm_job_state_codes")

### slurm_job_state_codes Type

`string`

### slurm_job_state_codes Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value             | Explanation |
| :---------------- | ----------- |
| `"COMPLETED"`     |             |
| `"FAILED"`        |             |
| `"OUT_OF_MEMORY"` |             |
| `"TIMEOUT"`       |             |

## returncode




`returncode`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [buildtest Global Schema](global-definitions-status-properties-returncode.md "https&#x3A;//buildtesters.github.io/schemas/global/global.schema.json#/definitions/status/properties/returncode")

### returncode Type

`integer`

## regex




`regex`

-   is optional
-   Type: `object` ([Details](global-definitions-status-properties-regex.md))
-   cannot be null
-   defined in: [buildtest Global Schema](global-definitions-status-properties-regex.md "https&#x3A;//buildtesters.github.io/schemas/global/global.schema.json#/definitions/status/properties/regex")

### regex Type

`object` ([Details](global-definitions-status-properties-regex.md))
