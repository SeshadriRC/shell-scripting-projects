# Shell Scripting for DevOps — Practical Learning Roadmap

A step-by-step, hands-on path to master Shell Scripting (Bash) for DevOps and SRE, starting from the easiest fundamentals up to production-grade automation.

---

## 🗺️ Topic-Wise Roadmap

| # | Topic | Key Skills & Concepts | Status |
|---|---|---|---|
| **1** | **Variables, Arguments & Exit Codes** | User variables, script arguments (`$1`, `$2`), `$#`, `$?`, quoting rules | 🟢 **Active Practice** |
| **2** | **Conditions & Tests** | `if / elif / else`, `[[ ... ]]`, file checks (`-f`, `-d`), string checks (`-z`), numbers (`-eq`, `-gt`) | ⚪ Upcoming |
| **3** | **Loops & Iteration** | `for` loops (lists, ranges), `while read` line-by-line file processing | ⚪ Upcoming |
| **4** | **Functions & Defensive Bash** | Reusable functions, return values, `set -euo pipefail`, signal traps (`trap cleanup EXIT`) | ⚪ Upcoming |
| **5** | **Text Processing & Stream Parsing** | `grep`, `awk`, `sed`, `cut`, `sort`, `uniq -c` for parsing logs and outputs | ⚪ Upcoming |
| **6** | **System & Process Monitoring** | Inspecting disk (`df`), processes (`ps`, `pgrep`), memory, automated triage scripts | ⚪ Upcoming |
| **7** | **API Automation with `curl` & `jq`** | Calling REST APIs (GitHub, GitLab, Vault, Slack), parsing JSON payloads | ⚪ Upcoming |
| **8** | **Production DevOps Projects** | Log rotation & backup daemon, automated health-checker, K8s triage script | ⚪ Upcoming |

---

## 📚 Study Notes
Core concepts, syntax cheat sheets, and defensive best practices are in:
👉 [**`SHELL_NOTES.md`**](file:///mnt/c/Myfolder/MyProjects/shell-scripting-projects/SHELL_NOTES.md)

---

## 🚀 How to Practice Topic 1
Navigate to the Topic 1 folder:
```bash
cd topics/topic_01_variables_and_arguments

# 1. Run the practice demonstration
./practice.sh web-server 3

# 2. Complete your exercise
./exercise.sh
```
