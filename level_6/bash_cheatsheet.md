# Bash Commands and Options Reference

Created with chatgpt, to help me understand all the bash command we will need in order
to create a bash script that will run our docker container inside our GCE VM (google coud env) virtual machine.

## Common Commands

### `curl`
- **Usage**: `curl [options] [URL...]`
- **Purpose**: Downloads files from the Internet.
- **Common Options**:
  - `-f`: Fails silently on server errors without showing an HTTP error.
  - `-s`: Operates in silent or quiet mode.
  - `-S`: Shows an error message when used with `-s`.
  - `-L`: Follows redirects.
  - `-o`: Writes output to a file instead of stdout.

### `echo`
- **Usage**: `echo [string]`
- **Purpose**: Displays a line of text/string that is passed as an argument.

### `docker`
- **Subcommands**:
  - `build`: Builds Docker images from a Dockerfile.
  - `tag`: Tags an image for upload to a registry.
  - `push`: Pushes an image or a repository to a registry.
  - `login`: Logs into a Docker registry.

### `docker compose`
- **Subcommands**:
  - `up`: Starts up services defined in a `docker-compose.yml`.
  - `pull`: Pulls service images.
  - `down`: Stops services and removes containers, networks, volumes, and images created by `up`.

### `chmod`
- **Usage**: `chmod [options] mode file`
- **Purpose**: Changes the file mode (permissions).
- **Common Options**:
  - `+x`: Adds executable permission.

### `sudo`
- **Usage**: `sudo [command]`
- **Purpose**: Executes a command with root (administrator) permissions.

### `usermod`
- **Usage**: `usermod [options] LOGIN`
- **Purpose**: Modifies the user account.
- **Common Options**:
  - `-aG`: Adds the user to the supplemental groups. Use this option with the `-G` option.

### `newgrp`
- **Usage**: `newgrp [-] [group]`
- **Purpose**: Logs in to a new group to change the current group ID during a login session.

## Special Variables

### `$?`
- **Purpose**: Holds the exit status of the last command executed. An exit status of `0` indicates success, while a non-zero status indicates failure.

### `$(command)`
- **Purpose**: Command substitution. It allows the output of a shell command to replace the command name.

## Script Control Structures

### Conditional Execution
- **Usage**: `if [ condition ]; then ... fi`
- **Purpose**: Executes commands based on the conditional result.

### Here Document (HereDoc)
- **Usage**: `[command] <<EOF ... EOF`
- **Purpose**: Passes a block of text (multiple lines of input) to a command.

## SSH Commands

### `ssh`
- **Usage**: `ssh [options] user@host`
- **Purpose**: Logs into the remote host as the user and executes commands.

### `scp`
- **Usage**: `scp [options] file1 user@host:directory`
- **Purpose**: Securely copies files from one host to another.

These commands form the basis of many scripts used for automation, deployment, and system administration in Unix-like operating systems.
