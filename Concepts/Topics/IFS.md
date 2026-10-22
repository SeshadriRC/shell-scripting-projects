`IFS` in shell scripting means **Internal Field Separator**.

It tells the shell **how to split a string into separate fields/words**.

### Default IFS

By default, IFS contains:

```text
space
tab
newline
```

For example:

```bash
NAME="John DevOps Engineer"

for word in $NAME; do
    echo "$word"
done
```

Output:

```text
John
DevOps
Engineer
```

The spaces are used as separators because of the default `IFS`.

---

### Common DevOps example: comma-separated values

Suppose:

```bash
SERVERS="server1,server2,server3"
```

By default, Bash doesn't split on commas.

You can set:

```bash
IFS=","

for server in $SERVERS; do
    echo "$server"
done
```

Output:

```text
server1
server2
server3
```

Here:

```bash
IFS=","
```

means:

> **Use comma as the separator.**

---

### Very common pattern

You'll often see:

```bash
IFS=',' read -ra SERVERS <<< "$SERVER_LIST"
```

For example:

```bash
# Store comma-separated server names
SERVER_LIST="web01,web02,web03"

# IFS=',' sets comma as the field separator for this read command
# read reads the input string
# -r prevents backslashes from being treated as escape characters
# -a stores the split fields in an array named SERVERS
# <<< passes SERVER_LIST as input to the read command (here-string)
IFS=',' read -ra SERVERS <<< "$SERVER_LIST"

# Loop through all elements in the SERVERS array
# ${SERVERS[@]} expands to all array elements individually
for server in "${SERVERS[@]}"; do
    # Print the current server name
    echo "$server"
done
```

Output:

```text
web01
web02
web03
```

Quick interview notes:

- read -r — reads input without interpreting backslashes as escape characters.
- -a SERVERS — stores the input fields in the SERVERS array.
- <<< "$SERVER_LIST" — passes the variable's value as input to read.
- "${SERVERS[@]}" — expands all array elements separately, preserving each element as an individual word when quoted.

### Interview answer

> **IFS stands for Internal Field Separator. It defines the characters Bash uses to split input into fields, with space, tab, and newline being the default separators.**

One important best practice: **avoid changing `IFS` globally unless you need to**. Prefer limiting it to the command/loop where it's required.
