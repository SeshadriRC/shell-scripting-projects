```bash
$, awk, IFS
```


---

## 1. $ use cases 

```bash
# $ means "get the value of a variable"
NAME="Seshadri"
echo $NAME
```

## 2. AWK use cases

```bash
# Print the first two columns from the output
ps -ef | awk '{print $1,$2}'

# Print the first column from the output
ps -ef | awk '{print $1}'
```
