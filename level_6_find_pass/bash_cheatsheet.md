# Bash Commands and Options Reference

Created with chatgpt, to help me understand all the bash command we will need in order
to create a bash script that will run our docker container inside our GCE VM (google coud env) virtual machine.

## Common Commands

### `curl`
- **Usage**: `curl [options] [URL...]`
- **Purpose**: Downloads files from the Internet.
- **Common Options**:
    - `-f`: Fails silently on server errors without showing an HTTP error.
        - Example: `curl -f https://example.com`
    - `-s`: Operates in silent or quiet mode.
        - Example: `curl -s https://example.com`
    - `-S`: Shows an error message when used with `-s`.
        - Example: `curl -sS https://example.com`
    - `-L`: Follows redirects.
        - Example: `curl -L https://example.com`
    - `-o`: Writes output to a file instead of stdout.
        - Example: `curl -o output.txt https://example.com`

The `curl` command is used to download files from the Internet. It supports various options to customize the behavior of the download. Here are some common options:

- `-f`: This option makes `curl` fail silently on server errors without showing an HTTP error. It is useful when you want to handle errors programmatically.

- `-s`: This option makes `curl` operate in silent or quiet mode. It suppresses the progress meter and most error messages. It is commonly used in scripts or when you don't want any output.

- `-S`: When used with the `-s` option, this option shows an error message if an error occurs during the download. It is helpful to be notified of any errors while still keeping the output silent.

- `-L`: This option tells `curl` to follow redirects. If the requested URL returns a redirect response, `curl` will automatically follow the redirect and download the content from the new location.

- `-o`: By default, `curl` writes the downloaded content to stdout. However, with the `-o` option, you can specify a file name to write the output to a file instead. This is useful when you want to save the downloaded content for later use.

These options can be combined to achieve the desired behavior when using the `curl` command.

Remember to replace `https://example.com` with the actual URL you want to download from.


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

## Script Control Structures

### Conditional Execution
- **Usage**: `if [ condition ]; then ... fi`
- **Purpose**: Executes commands based on the conditional result.

### Here Document (HereDoc)
- **Usage**: `[command] <<EOF ... EOF`
- **Purpose**: Passes a block of text (multiple lines of input) to a command.

## Special Variables
### `$?`
- **Purpose**: Holds the exit status of the last command executed. An exit status of `0` indicates success, while a non-zero status indicates failure.

The `$?` special variable in bash holds the exit status of the last command that was executed. It is commonly used in scripts to check the success or failure of a command. 

For example, let's say you have a script that runs a command and you want to perform different actions based on whether the command was successful or not. You can use the `$?` variable to check the exit status and make decisions accordingly.

```bash
command
if [ $? -eq 0 ]; then
    echo "Command executed successfully"
else
    echo "Command failed"
fi
```

In this example, if the command succeeds (exit status of 0), the script will print "Command executed successfully". If the command fails (non-zero exit status), the script will print "Command failed".

### `$(command)`
- **Purpose**: Command substitution. It allows the output of a shell command to replace the command name.

The `$(command)` syntax in bash is used for command substitution. It allows you to capture the output of a shell command and use it as part of another command or assign it to a variable.

For example, let's say you want to store the current date and time in a variable. You can use the `$(date)` command substitution to achieve this:

```bash
current_date=$(date)
echo "The current date is: $current_date"
```

In this example, the `$(date)` command is executed and its output (the current date and time) is captured and assigned to the `current_date` variable. The variable is then used in the `echo` command to display the current date.

Command substitution is a powerful feature in bash that allows you to combine the output of commands with other commands or perform complex operations.

## SSH Commands

### `ssh`
- **Usage**: `ssh [options] user@host`
- **Purpose**: Logs into the remote host as the user and executes commands.

### `scp`
- **Usage**: `scp [options] file1 user@host:directory`
- **Purpose**: Securely copies files from one host to another.

These commands form the basis of many scripts used for automation, deployment, and system administration in Unix-like operating systems.
