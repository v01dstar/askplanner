# GTOC-7013: PITR fails with [BR:Stream:ErrStreamLogTaskExist\]

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7013
- Status: PENDING FOR SUPPORT
- Resolution: N/A
- Priority: P3
- Issue type: Incident
- Created: 2024-07-11T10:50:17.000+0800
- Updated: 2025-03-06T18:08:52.675+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: BR
- Categories: [REDACTED_RESOURCE_NAME], storage-credential, tikv-data-path, operator-cr, performance-resource, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

Customer [REDACTED_CUSTOMER], before change namespace, already deleted all Backup/BackupSchedule CR, and deleted the old namespace [REDACTED_NAMESPACE], but still got this error. The error message:

\[2024/07/09 04:01:54.217 +00:00\] \[ERROR\] \[main.go:38\] \["br failed"\] \[error="It supports single stream log task currently: \[BR:Stream:ErrStreamLogTaskExist\]stream task already exists"\] \[errorVerbose="\[BR:Stream:ErrStreamLogTaskExist\]stream task already exists\\nIt supports single stream log task currently\\ngithub.com/pingcap/tidb/br/pkg/task.RunStreamStart\\n\\t/workspace/source/tidb/br/pkg/task/stream.go:577\\ngithub.com/pingcap/tidb/br/pkg/task.RunStreamCommand\\n\\t/workspace/source/tidb/br/pkg/task/stream.go:530\\nmain.streamCommand\\n\\t/workspace/source/tidb/br/cmd/br/stream.go:232\\nmain.newStreamStartCommand.func1\\n\\t/workspace/source/tidb/br/cmd/br/stream.go:70\\ngithub.com/spf13/cobra.(\*Command).execute\\n\\t/root/go/pkg/mod/github.com/spf13/cobra@v1.8.0/command.go:983\\ngithub.com/spf13/cobra.(\*Command).ExecuteC\\n\\t/root/go/pkg/mod/github.com/spf13/cobra@v1.8.0/command.go:1115\\ngithub.com/spf13/cobra.(\*Command).Execute\\n\\t/root/go/pkg/mod/github.com/spf13/cobra@v1.8.0/command.go:1039\\nmain.main\\n\\t/workspace/source/tidb/br/cmd/br/main.go:36\\nruntime.main\\n\\t/usr/local/go/src/runtime/proc.go:267\\nruntime.goexit\\n\\t/usr/local/go/src/runtime/asm_amd64.s:1650"\] \[stack="main.main\\n\\t/workspace/source/tidb/br/cmd/br/main.go:38\\nruntime.main\\n\\t/usr/local/go/src/runtime/proc.go:267"\]

 

The yaml file:

apiVersion: v1  
kind: Namespace  
[REDACTED_NAMESPACE]:  
name: [REDACTED_RESOURCE_NAME]

---

kind: Role

apiVersion: [rbac.authorization.k8s.io/v1](http://rbac.authorization.k8s.io/v1)  
metadata:  
name: [REDACTED_RESOURCE_NAME]  
namespace: [REDACTED_NAMESPACE]  
labels:  
[app.kubernetes.io/component:](http://app.kubernetes.io/component:) [REDACTED_RESOURCE_NAME]  
rules:

* apiGroups: \[ "" \]  
  resources: \[ "events" \]  
  verbs: \[ "\*" \]

## Recent Comments Excerpt

### 2024-07-11T11:46:45.000+0800 [REDACTED_USER]

I know the customer [REDACTED_CUSTOMER]/BackupSchedule, but for log backup, did the customer "stop" this backup job that is running in TiKV?

### 2024-07-16T08:30:46.000+0800 [REDACTED_USER]

Customer [REDACTED_CUSTOMER], but it still return the same error. Let customer [REDACTED_CUSTOMER], the status has change from Running to Stop or not. The newest yaml file refer to attached file, plz help review the file is right or not.

 
[REDACTED_MEDIA]

### 2024-07-16T08:42:00.000+0800 [REDACTED_USER]

logStop: true is already added
 
% diff [REDACTED_RESOURCE_NAME].yaml [REDACTED_RESOURCE_NAME]normal_new.yaml
4c4
<   name: [REDACTED_RESOURCE_NAME]
---
>   name: [REDACTED_ENV_NAME]
12c12

### 2024-08-28T11:29:31.000+0800 [REDACTED_USER]

notified (张学程([REDACTED_EMAIL]), ) by lark

### 2024-08-28T11:31:31.000+0800 [REDACTED_USER]

@[REDACTED_USER]
 Can we close this now?
