# Linux Processes and Permissions

This document outlines key Linux concepts related to processes and file permissions, along with common commands used to manage them.

---

## Processes in Linux

A **process** is an instance of a program running on your system. Every process has:

- A unique **Process ID (PID)**
- A **parent process (PPID)**
- An associated **user**
- A **state** (running, sleeping, stopped, etc.)

---

### List Running Processes

```bash
ps aux
```

- Lists **all** running processes with detailed information.

```bash
top
```

- Real-time view of running processes (press `q` to quit).

---

### List User Processes

```bash
ps -u <username>
```

```bash
ps -u $(whoami)
```

---

### List System Processes

```bash
ps -ef | grep -v $(whoami)
```

---

## What Are Child Processes?

A **child process** is a process created by another (the **parent**). You can view relationships using:

```bash
pstree
```

Or check a process’s parent:

```bash
ps -o ppid= -p <PID>
```

---

## Run a Process in the Background

```bash
command &
```

Check background jobs:

```bash
jobs
```

---

## End a Process

### Kill by PID:

```bash
kill <PID>
```

### Kill by name:

```bash
pkill <process_name>
```

### Stop foreground process:

```bash
Ctrl + C
```

### Kill background job:

```bash
kill %<job_number>
```

---

## Kill Signals

| Signal | Name    | Description                        |
| ------ | ------- | ---------------------------------- |
| 1      | SIGHUP  | Hangup – often causes restart      |
| 15     | SIGTERM | Graceful stop (default for `kill`) |
| 9      | SIGKILL | Force kill – cannot be ignored     |

---

## How Do Linux Permissions Work?

Linux uses a permission model to control access to files and directories. Every file has associated permissions for three categories of users:

| Category | Who it Applies To               |
| -------- | ------------------------------- |
| User     | The file's owner                |
| Group    | Other users in the file’s group |
| Others   | All other users on the system   |

Each category can be assigned three permissions:

- **r** = Read (view contents of a file or list directory)
- **w** = Write (modify file or create/delete inside directory)
- **x** = Execute (run file as a program or access directory)

---

### Long Format Permissions (Symbolic)

Use the `ls -l` command to view detailed file permissions:

```bash
ls -l
```

Example output:

```
-rwxr-xr--
```

This breaks down as:

- `-` : Regular file (`d` would indicate a directory)
- `rwx` : User permissions (read, write, execute)
- `r-x` : Group permissions (read, execute)
- `r--` : Others permissions (read only)

The order is always: **User → Group → Others**

---

### Short Format Permissions (Octal)

Permissions can also be expressed numerically, using the following values:

- `r` = 4
- `w` = 2
- `x` = 1

Add these up for each category:

- `rwx` = 4+2+1 = **7**
- `rw-` = 4+2+0 = **6**
- `r--` = 4+0+0 = **4**

Example:

```bash
chmod 755 script.sh
```

This means:

- User: rwx (7)
- Group: r-x (5)
- Others: r-x (5)

---

### ✏️ Examples of Changing File Permissions

| Command              | Explanation                                 |
| -------------------- | ------------------------------------------- |
| `chmod 744 file.txt` | User: rwx, Group: r--, Others: r--          |
| `chmod +x script.sh` | Add execute permission for all categories   |
| `chmod u+x file`     | Add execute for user only                   |
| `chmod g-w file`     | Remove write from group                     |
| `chmod o=r file`     | Others can only read                        |
| `chmod a-w file`     | Remove write access from everyone           |
| `chmod 000 file.txt` | No one can access the file (no permissions) |

You can always verify permissions using:

```bash
ls -l file.txt
```

---

This concludes the overview of Linux process handling and file permission management.
