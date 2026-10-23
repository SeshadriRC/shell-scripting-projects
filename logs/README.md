# Sample Application Logs for Shell Scripting Tasks

This folder contains realistic, production-like application log files specifically designed for practicing and mastering Bash & Linux shell scripting.

---

## 📁 Directory Structure & Log Files

| File | Type & Format | Description & Use Case |
|---|---|---|
| [`access.log`](file:///mnt/c/Myfolder/MyProjects/shell-scripting-projects/logs/access.log) | Nginx/Apache Combined Log | ~1,600+ web requests with client IPs, HTTP methods, status codes (200, 401, 403, 404, 500), user agents, and response sizes. |
| [`app.log`](file:///mnt/c/Myfolder/MyProjects/shell-scripting-projects/logs/app.log) | Java / Spring Boot Microservice Log | Application events with timestamps, log levels (`INFO`, `DEBUG`, `WARN`, `ERROR`), thread IDs, and **multi-line stack traces** (`NullPointerException`, `TimeoutException`, `HikariPool`). |
| [`api-service.json.log`](file:///mnt/c/Myfolder/MyProjects/shell-scripting-projects/logs/api-service.json.log) | JSON Structured Log | Modern cloud microservice JSON log entries containing `timestamp`, `level`, `service`, `trace_id`, `http` metadata, and `latency_ms`. |
| [`auth.log`](file:///mnt/c/Myfolder/MyProjects/shell-scripting-projects/logs/auth.log) | Linux Authentication / Syslog | SSH connections, failed password attempts (brute-force simulation), accepted public keys, `sudo` commands, and cron triggers. |
| [`database.log`](file:///mnt/c/Myfolder/MyProjects/shell-scripting-projects/logs/database.log) | PostgreSQL / MySQL Query Log | Query execution times (`duration: X.XX ms`), slow query warnings (>1000ms), and database deadlock errors. |
| [`archive/`](file:///mnt/c/Myfolder/MyProjects/shell-scripting-projects/logs/archive) | Historical Rotated Logs | Contains dated and `.gz` compressed log files with older timestamps (3 to 10 days ago) for testing retention and cleanup scripts. |

---

## 🛠️ Included Helper Scripts

### 1. Run Log Analysis Demo
Run the ready-to-use analysis script to see example shell one-liners in action:
```bash
./analyze-logs.sh
```

### 2. Regenerate Fresh Logs
Regenerate fresh sample logs with updated random distributions:
```bash
./generate-logs.sh
```

### 3. Stream Live Logs (Real-time monitoring test)
Continuously appends new entries to `app.log` and `access.log` to test `tail -f` and streaming watcher scripts:
```bash
./generate-logs.sh --stream
```

---

## 🎯 10 Shell Scripting Practice Challenges

Try solving these common DevOps / SysAdmin shell scripting interview and real-world tasks using these files:

### Challenge 1: Find Top 10 IP Addresses by Request Count
* **Log**: `access.log`
* **Skills**: `awk`, `sort`, `uniq -c`, `head`
* **One-liner**:
  ```bash
  awk '{print $1}' access.log | sort | uniq -c | sort -nr | head -n 10
  ```

### Challenge 2: Calculate HTTP Error Rate (4xx and 5xx)
* **Log**: `access.log`
* **Skills**: `awk`, arithmetic calculation
* **Example Script**:
  ```bash
  awk '{
    total++;
    if ($9 ~ /^[45]/) errors++;
  } END {
    printf "Total: %d, Errors: %d (%.2f%%)\n", total, errors, (errors/total)*100
  }' access.log
  ```

### Challenge 3: Extract Java Multi-line Exceptions
* **Log**: `app.log`
* **Skills**: `sed`, `awk`, `grep -A`
* **Task**: Extract all occurrences of `NullPointerException` including the 5 lines of stack trace following it:
  ```bash
  grep -A 5 "NullPointerException" app.log
  ```

### Challenge 4: Detect SSH Brute-Force Attackers
* **Log**: `auth.log`
* **Skills**: `grep`, `awk`, conditional alerting
* **Task**: Find IPs with more than 5 failed SSH login attempts:
  ```bash
  grep "Failed password" auth.log | awk '{for(i=1;i<=NF;i++) if($i=="from") print $(i+1)}' | sort | uniq -c | awk '$1 > 5 {print "SUSPICIOUS IP:", $2, "Attempts:", $1}'
  ```

### Challenge 5: Identify Slow Database Queries (>1000ms)
* **Log**: `database.log`
* **Skills**: `awk`, delimiter splitting
* **Command**:
  ```bash
  awk -F'duration: ' '/duration:/ {split($2, a, " "); if (a[1] > 1000) print a[1], "ms ->", $0}' database.log
  ```

### Challenge 6: Parse Structured JSON Logs
* **Log**: `api-service.json.log`
* **Skills**: `grep`, `sed`, `jq` (if installed)
* **Pure Bash / Sed example**:
  ```bash
  grep '"status_code": 500' api-service.json.log | sed -E 's/.*"service": "([^"]+)".*"route": "([^"]+)".*/Service: \1 | Route: \2/'
  ```

### Challenge 7: Build an Automated Log Rotation & Archival Script
* **Directory**: `archive/`
* **Skills**: `find`, `mtime`, `gzip`, `rm`
* **Task**: Write a script to find `.log` files older than 7 days, compress them into `.gz`, and delete files older than 14 days:
  ```bash
  # Find uncompressed logs older than 5 days
  find archive/ -type f -name "*.log" -mtime +5
  ```

### Challenge 8: Real-time Alerting Monitor
* **Log**: `app.log`
* **Skills**: `tail -F`, `grep --line-buffered`
* **Task**: Listen to live entries and print an alert immediately whenever an `ERROR` occurs:
  ```bash
  tail -Fn0 app.log | grep --line-buffered "ERROR" | while read -r line; do
    echo "[ALERT TRIGGERED] $line"
  done
  ```

### Challenge 9: Filter by Specific Time Range
* **Log**: `app.log`
* **Skills**: `awk` range matching `awk '$0 >= "2026-10-22 00:00:00" && $0 <= "2026-10-22 06:00:00"'`

### Challenge 10: Generate an HTML or Markdown Executive Health Report
* **Skills**: Combining multiple scripts to generate a formatted summary file `report.md` with timestamps, error counts, and top offender IPs.
