# Settings schema

The settings schema is used for configuring buildtest. The schema defines the 
structure of how to write your `settings.yml` 

This schema can be found at https://buildtesters.github.io/schemas/settings/settings.schema.json


## Main Keys

| Name | Type | Supported in buildtest | Description | 
| ---- | ---- | -----------------------| ----------- | 
| executors | object | YES | Specify an executor type used for running tests. One can specify multiple executors, currently schema supports `local`, `ssh`, and `slurm` executor. Multiple executors can be defined in each executor type |
| config | object | YES | Specify configuration to tweak buildtest behavior |

Required Keys: [`executors`,`config`]


## executors Key

| Name | Type | Supported in buildtest | Description | 
| ---- | ---- | -----------------------| ----------- | 
| local | object | YES | Define a list of local executors. These executors can be used in Buildspec to run jobs locally. |
| ssh | object | NO | Define a list of ssh executors. These executors can be used in Buildspec to run jobs via ssh on remote nodes. |
| slurm | object | NO | Define a list of slurm executors. These executors can be used in Buildspec to run jobs via Slurm scheduler | 

## executors[local] Key

| Name | Type | Supported in buildtest | Description | 
| ---- | ---- | -----------------------| ----------- | 
| description | string | YES | Specify description field for executor |
| shell | string | NO | Specify shell command to use when running all jobs with the local executor. |
| environment | array | NO | Specify a list of environment variables for all Buildspec using the local executor |
| variables | array | NO | Specify a list of variables for all Buildspec using the local executor. |
| retry | integer | NO | Number of times to retry test in the event of a failure. The values can be in range of `1-5` |
| modules | array | NO | Specify a list of modules to load for all Buildspec associated to local executor |

# executors[slurm] Key

| Name | Type | Supported in buildtest | Description | 
| ---- | ---- | -----------------------| ----------- | 
| description | string | YES | Specify description field for executor |
| launcher | string | NO | Specify slurm launcher to use when submitting job. Currently we support `sbatch`. |
| environment | array | NO | specify a list of environment variables for all Buildspec using the slurm executor |
| variables | array | NO | Specify a list of variables for all Buildspec using the slurm executor. |
| modules | array | NO | Specify a list of modules to load for all Buildspec associated to slurm executor |
| options | array | NO | Specify a list of options to pass to the `launcher` key |

Required Keys: [`launcher`]

# executors[ssh] Key

| Name | Type | Supported in buildtest | Description | 
| ---- | ---- | -----------------------| ----------- | 
| description | string | YES | Specify description field for executor |
| host | string | NO | Specify remote hostname where jobs will be run via `ssh`. |
| user | string | NO | Specify user when connecting to remote host, the user must have access to test in order to run it remotely. |
| identity_file | string | NO | Specify user identity file when connecting to remote host via ssh. This is the `ssh -i` option where one must specify the private key to. This could be one of the files:  `~/.ssh/id_rsa`, `~/.ssh/id_rsa` or you can specify an alternate file.  |
| environment | array | NO | specify a list of environment variables for all Buildspec using the slurm executor |
| variables | array | NO | Specify a list of variables for all Buildspec using the slurm executor. |
| modules | array | NO | Specify a list of modules to load for all Buildspec associated to slurm executor |
| options | array | NO | Specify a list of options to pass to the `launcher` key |
 
required: [`host`,`user`,`identity_file`]

# config Key

| Name | Type | Supported in buildtest | Description | 
| ---- | ---- | -----------------------| ----------- | 
| editor | string | YES | Specify editor to use when opening files. Valid values are `vi`,`vim`,`nano`,`emacs`. Defaults to `vim` if none specified|
| paths | string | YES | Specify path configuration for buildtest settings  |

# config[paths] Key

| Name | Type | Supported in buildtest | Description | 
| ---- | ---- | -----------------------| ----------- | 
| prefix | string | NO | Specify prefix path where buildtest will write all path settings. If keys `clonepath`, `logdir`, `testdir` are not specified, then `prefix` will be used to build the path. |
| clonepath | string | YES | Specify path where `buildtest repo` will clone repositories. |
| logdir | string | NO | Specify path where buildtest logs will be written. |
| testdir | string | YES | Specify location of test directory where tests will be written. This value can be overriden by command line option `buildtest build --testdir`. |


