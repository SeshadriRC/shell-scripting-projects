```bash
$, $?, awk, head, IFS
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
