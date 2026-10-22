**Concepts**

- Operators
- IFS


**In this document**
```bash
$, $?, awk, head, grep
```


---

## 1. $ use cases 

```bash
# $ means "get the value of a variable"
NAME="Seshadri"
echo $NAME

# $?	Previous command's exit status
sesha@Sesha-PC:/mnt/c/Myfolder/MyProjects/shell-scripting-projects$ ps -ef | awk '{print $1,$2}' | head -2
UID PID
root 1
sesha@Sesha-PC:/mnt/c/Myfolder/MyProjects/shell-scripting-projects$ echo $?
0

sesha@Sesha-PC:/mnt/c/Myfolder/MyProjects/shell-scripting-projects$ ps -ef | awk '{print $1,$2}' | headd
Command 'headd' not found, did you mean:
  command 'head' from deb coreutils (9.4-3ubuntu6.2)
Try: sudo apt install <deb name>
sesha@Sesha-PC:/mnt/c/Myfolder/MyProjects/shell-scripting-projects$ echo $?
127  --> meaning is command not found

# show the current process id
echo $$
1169


```

## 2. AWK use cases

```bash
# Print the first two columns from the output
ps -ef | awk '{print $1,$2}'

sesha@Sesha-PC:/mnt/c/Myfolder/MyProjects/shell-scripting-projects$ ps -ef | awk '{print $1,$2}' | head -2
UID PID
root 1

# Print the first column from the output
ps -ef | awk '{print $1}'
```

---

## 3. grep

```bash
# command safely counts the number of matching lines in a single file without printing the matching lines themselves?
grep -c "ERROR" app.log
49

# command safely counts the number of matching lines in multiple files
grep -c "ERROR" *.log
access.log:0
api-service.json.log:99
app.log:49
auth.log:0
database.log:8

# only print the matched part
grep -o "ERROR" app.log | head -2
ERROR
ERROR
```
