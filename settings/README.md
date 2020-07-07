# Settings schema

The settings schema is used for configuring buildtest. The schema defines the 
structure of how to write your `settings.yml` 

The schema documentation is based on [settings.schema.json](https://buildtesters.github.io/schemas/settings/settings.schema.json).


## Main Keys

| Name | Type | Supported in buildtest | Required | Description | 
| ---- | ---- | -----------------------| --------- | ----------- | 
| executors | object | YES | YES | Specify an executor type used for running tests. One can specify multiple executors, currently schema supports `local`, `ssh`, and `slurm` executor. Multiple executors can be defined in each executor type |
| config | object | YES | YES | Specify configuration to tweak buildtest behavior |

## executors object

| Name | Type | Supported in buildtest | Required |  Description | 
| ---- | ---- | -----------------------| --------- | ----------- | 
| local | object | YES | YES | Define a list of local executors. These executors can be used in Buildspec to run jobs locally. |
| ssh | object | NO | NO | Define a list of ssh executors. These executors can be used in Buildspec to run jobs via ssh on remote nodes. |
| slurm | object | YES | NO | Define a list of slurm executors. These executors can be used in Buildspec to run jobs via Slurm scheduler | 

## local executor object

| Name | Type | Supported in buildtest | Required | Description | Valid Options |
| ---- | ---- | -----------------------| --------- |----------- | ------------- | 
| description | string | YES | NO | Specify description field for executor | | 
| shell | string | YES | YES | Specify shell command to use when running all jobs with the local executor. | `"^(/bin/bash|/bin/sh|sh|bash|python).*"`  | 
| environment | array | NO | NO | Specify a list of environment variables for all Buildspec using the local executor | |
| variables | array | NO | NO | Specify a list of variables for all Buildspec using the local executor. | | 
| retry | integer | NO | NO | Number of times to retry test in the event of a failure. The values can be in range of `1-5` | `[1-5]` |
| modules | array | NO | NO | Specify a list of modules to load for all Buildspec associated to executor | |

Required Fields for local executor: [`shell`]

# slurm executor object

| Name | Type | Supported in buildtest | Required | Description | Valid Options | 
| ---- | ---- | -----------------------| -------- | ----------- | -------------- |
| description | string | YES | NO |  Specify description field for executor |
| launcher | string | YES | YES | Specify slurm launcher to use when submitting job. Currently we support `sbatch`. | `sbatch` | 
| environment | array | NO | Specify a list of environment variables for all Buildspec using the slurm executor | | 
| variables | array | NO | Specify a list of variables for all Buildspec using the slurm executor. | | 
| pollinterval | number | YES | NO | Specify poll interval between range ``[10-300]`` seconds when buildtest will initiate query for slurm job. Default interval is 30 seconds. | `[10-300]` seconds, defaults to 30 secs | 
| cluster | string | YES | NO | Specify slurm cluster to use when submitting jobs. This is ``sbatch -M`` option. Use this option if you have a multi slurm cluster. | |
| partition | string | YES | NO | Specify slurm partition (``sbatch -p <partition>``) when submitting job. | |
| qos | string | YES | NO | specify slurm Quality of Service (QOS) to use when submitting job. This is the ``sbatch -q <qos>`` option. | |
| modules | array | NO | NO | Specify a list of modules to load for all Buildspec associated to executor | | 
| options | array | YES | NO | Specify a list of options to pass to the `launcher` key | |

Required Fields for slurm executor: [`launcher`]

# ssh executor object

| Name | Type | Supported in buildtest | Required | Description | 
| ---- | ---- | -----------------------| ----------- | -------- |  
| description | string | NO | NO |  Specify description field for executor |
| host | string | NO | YES | Specify remote hostname where jobs will be run via `ssh`. |
| user | string | NO | YES | Specify user when connecting to remote host, the user must have access to test in order to run it remotely. |
| identity_file | string | NO | YES | Specify user identity file when connecting to remote host via ssh. This is the `ssh -i` option where one must specify the private key to. This could be one of the files:  `~/.ssh/id_rsa`, `~/.ssh/id_rsa` or you can specify an alternate file.  |
| environment | array | NO | NO | specify a list of environment variables for all Buildspec using the slurm executor |
| variables | array | NO | NO | Specify a list of variables for all Buildspec using the slurm executor. |
| modules | array | NO | NO | Specify a list of modules to load for all Buildspec associated to executor |
 
 Required Fields for ssh executor: [`host`, `user`, `identity_file`]

# config object

| Name | Type | Supported in buildtest | Required | Description | Valid Options | 
| ---- | ---- | -----------------------| --------- | ----------- | ------------- |
| editor | string | YES | YES | Specify editor to use when opening files. | [`vi`,`vim`,`nano`,`emacs`]. Defaults to `vim` if none specified|
| paths | object | YES | YES | Specify path configuration for buildtest settings  | |

# path object

| Name | Type | Supported in buildtest |  Description | 
| ---- | ---- | -----------------------| ----------- | 
| prefix | string | YES | Specify prefix path where buildtest will write all path settings. If keys `clonepath`, `logdir`, `testdir` are not specified, then `prefix` will be used to build the path. |
| clonepath | string | YES | Specify path where `buildtest repo` will clone repositories. |
| logdir | string | NO | Specify path where buildtest logs will be written. |
| testdir | string | YES | Specify location of test directory where tests will be written. This value can be overriden by command line option `buildtest build --testdir`. |


