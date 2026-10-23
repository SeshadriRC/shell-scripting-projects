# DevOps Shell Scripting (Bash) Study Notes

A quick reference guide covering core Bash scripting patterns for DevOps automation.

---

## 📌 Topic 1: Variables, Arguments & Quotes

### 1. Variables Definition & Calling
* **No spaces around `=`**:
  ```bash
  # Correct:
  SERVICE_NAME="payment-api"
  PORT=8080

  # WRONG (Bash will try to run SERVICE_NAME as a command):
  SERVICE_NAME = "payment-api"
  ```
* **Referencing variables**: Use `$VARIABLE` or preferably `"${VARIABLE}"`:
  ```bash
  echo "Service: ${SERVICE_NAME} on port: ${PORT}"
  ```

---

### 2. Double Quotes (`"..."`) vs Single Quotes (`'...'`)
* **Double Quotes (`"..."`)**: Expands variables and escape characters:
  ```bash
  ENV="production"
  echo "Current env is: $ENV"  # Output: Current env is: production
  ```
* **Single Quotes (`'...'`)**: Literal text (does NOT expand variables):
  ```bash
  echo 'Current env is: $ENV'  # Output: Current env is: $ENV
  ```

> 💡 **DevOps Rule**: Always double-quote variables (`"${VAR}"`) to prevent word-splitting and whitespace bugs.

---

### 3. Special Parameters (Arguments passed to scripts)

When you run `./script.sh arg1 arg2`:

| Parameter | What it represents | Example |
| :--- | :--- | :--- |
| `$0` | Name of the script itself | `./script.sh` |
| `$1`, `$2`... | The 1st and 2nd positional arguments | `arg1`, `arg2` |
| `$#` | Total number of arguments passed | `2` |
| `$@` | All arguments as a list | `"arg1" "arg2"` |
| `$$` | Process ID (PID) of the current script | `14298` |
| `$?` | **Exit status** of the last command (0 = success, non-zero = fail) | `0` |

---

### 4. Safe Default Values (`${VAR:-default}`)
If a variable might not be passed or set in the environment:
```bash
# If $ENVIRONMENT is unset or empty, use 'development':
TARGET_ENV="${ENVIRONMENT:-development}"

# If $1 (first argument) is not provided, default to 'nginx':
SERVICE="${1:-nginx}"
```

---

### 5. Exit Codes (`$?` & `exit`)
Every Linux command returns an exit code between `0` and `255`:
* `0`: Success (All good)
* `1` to `255`: Error or threshold violation

```bash
# Exit with failure if required argument is missing:
if [ -z "$1" ]; then
    echo "ERROR: Please provide a service name."
    exit 1
fi
```
