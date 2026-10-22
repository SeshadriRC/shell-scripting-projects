In shell scripting, **operators are symbols/keywords used to perform operations or comparisons**.

For DevOps shell scripting, learn these main types:

### 1. Arithmetic operators

Used for calculations:

```bash
+    # addition
-    # subtraction
*    # multiplication
/    # division
%    # remainder
```

Example:

```bash
a=10
b=3

echo $((a + b))
```

Output:

```text
13
```

---

### 2. Comparison operators

Used to compare numbers:

```bash
-eq    # equal
-ne    # not equal
-gt    # greater than
-lt    # less than
-ge    # greater than or equal
-le    # less than or equal
```

Example:

```bash
CPU=80

if [[ $CPU -gt 70 ]]; then
    echo "High CPU usage"
fi
```

Here:

```bash
-gt
```

means **greater than**.

---

### 3. String operators

Used to check strings:

```bash
==       # equal
!=       # not equal
-z       # string is empty
-n       # string is NOT empty
```

Example:

```bash
STATUS="running"

if [[ "$STATUS" == "running" ]]; then
    echo "Application is running"
fi
```

And the one you asked about earlier:

```bash
if [[ -n "$IMAGES" ]]; then
```

`-n` means **the string is not empty**.

---

### 4. Logical operators

Used to combine conditions:

```bash
&&    # AND
||    # OR
!     # NOT
```

Example:

```bash
if [[ $CPU -gt 80 && $MEMORY -gt 80 ]]; then
    echo "High CPU and memory"
fi
```

Both conditions must be true.

---

### 5. File operators

Very important in DevOps scripts:

```bash
-f file    # regular file exists
-d dir     # directory exists
-e path    # path exists
-r file    # readable
-w file    # writable
-x file    # executable
```

Example:

```bash
if [[ -f "/etc/nginx/nginx.conf" ]]; then
    echo "Nginx config exists"
fi
```

### Quick interview table

| Operator | Meaning |
|---|---|
| `-eq` | Number equal |
| `-ne` | Number not equal |
| `-gt` | Greater than |
| `-lt` | Less than |
| `-n` | String not empty |
| `-z` | String empty |
| `==` | Strings equal |
| `!=` | Strings not equal |
| `&&` | AND |
| `\|\|` | OR |
| `!` | NOT |
| `-f` | File exists |
| `-d` | Directory exists |

For DevOps interviews, **`-eq`, `-gt`, `-lt`, `-n`, `-z`, `-f`, `-d`, `&&`, and `||`** are especially useful to know.
