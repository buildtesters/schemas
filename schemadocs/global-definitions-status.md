# Untitled object in BuildTest Test Configuration for Script Schema

```txt
https://buildtesters.github.io/schemas/schemas/script-v1.0.schema.json#/properties/status
```

The status section describes how buildtest detects PASS/FAIL on test. By default returncode 0 is a PASS and anything else is a FAIL, however buildtest can support other types of PASS/FAIL conditions.


| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                         |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | ---------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [script-v1.0.schema.json\*](../out/script-v1.0.schema.json "open original schema") |

## status Type

`object` ([Details](global-definitions-status.md))

# undefined Properties

| Property                                        | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                             |
| :---------------------------------------------- | --------- | -------- | -------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [slurm_job_state_codes](#slurm_job_state_codes) | `string`  | Optional | cannot be null | [buildtest global schema](global-definitions-status-properties-slurm_job_state_codes.md "https&#x3A;//buildtesters.github.io/schemas/schemas/global.schema.json#/definitions/status/properties/slurm_job_state_codes") |
| [returncode](#returncode)                       | `integer` | Optional | cannot be null | [buildtest global schema](global-definitions-status-properties-returncode.md "https&#x3A;//buildtesters.github.io/schemas/schemas/global.schema.json#/definitions/status/properties/returncode")                       |
| [regex](#regex)                                 | `object`  | Optional | cannot be null | [buildtest global schema](global-definitions-status-properties-regex.md "https&#x3A;//buildtesters.github.io/schemas/schemas/global.schema.json#/definitions/status/properties/regex")                                 |

## slurm_job_state_codes

This field can be used for checking Slurm Job State, if there is a match buildtest will report as `PASS` 


`slurm_job_state_codes`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [buildtest global schema](global-definitions-status-properties-slurm_job_state_codes.md "https&#x3A;//buildtesters.github.io/schemas/schemas/global.schema.json#/definitions/status/properties/slurm_job_state_codes")

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

By default, returncode 0 is PASS, if you want to emulate a non-zero returncode to pass then specify an expected return code. buildtest will match actual returncode with one defined in this field, if there is a match buildtest will report as `PASS`


`returncode`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [buildtest global schema](global-definitions-status-properties-returncode.md "https&#x3A;//buildtesters.github.io/schemas/schemas/global.schema.json#/definitions/status/properties/returncode")

### returncode Type

`integer`

## regex

Perform regular expression search using `re.search` python module on stdout/stderr stream for reporting if test `PASS`. 


`regex`

-   is optional
-   Type: `object` ([Details](global-definitions-status-properties-regex.md))
-   cannot be null
-   defined in: [buildtest global schema](global-definitions-status-properties-regex.md "https&#x3A;//buildtesters.github.io/schemas/schemas/global.schema.json#/definitions/status/properties/regex")

### regex Type

`object` ([Details](global-definitions-status-properties-regex.md))
