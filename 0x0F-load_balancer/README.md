# 0x0F-load_balancer

## Background Context
You have been given 2 additional servers:

* gc-[STUDENT_ID]-web-02-XXXXXXXXXX
* gc-[STUDENT_ID]-lb-01-XXXXXXXXXX
Let’s improve our web stack so that there is redundancy for our web servers. This will allow us to be able to accept more traffic by doubling the number of web servers, and to make our infrastructure more reliable. If one web server fails, we will still have a second one to handle requests.

For this project, you will need to write Bash scripts to automate your work. All scripts must be designed to configure a brand new Ubuntu server to match the task requirements.

## Requirements
### General
* Allowed editors: `vi`, `vim`, `emacs`
* All files will be interpreted on Ubuntu 14.04 LTS
* All files should end with a new line
* A `README.md` file, at the root of the project folder, is mandatory
* All Bash script files must be executable
* Your scripts must pass `Shellcheck` (version `0.3.7`) without any error
* Your Bash scripts must run without error
* The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
* The second line of all your Bash scripts should be a comment explaining what the script does
