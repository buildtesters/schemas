# Untitled string in buildtest Global Schema Schema

```txt
https://buildtesters.github.io/schemas/global/global.schema.json#/definitions/status/properties/slurm_job_state_codes
```

This field can be used for checking Slurm Job State, if there is a match buildtest will report as `PASS` 


| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                  |
| :------------------ | ---------- | -------------- | ----------------------- | :---------------- | --------------------- | ------------------- | --------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [global.schema.json\*](../../out/global.schema.json "open original schema") |

## slurm_job_state_codes Type

`string`

## slurm_job_state_codes Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value             | Explanation |
| :---------------- | ----------- |
| `"COMPLETED"`     |             |
| `"FAILED"`        |             |
| `"OUT_OF_MEMORY"` |             |
| `"TIMEOUT"`       |             |
