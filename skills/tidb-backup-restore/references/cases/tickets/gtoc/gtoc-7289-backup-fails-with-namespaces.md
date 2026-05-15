# GTOC-7289: Backup fails with namespaces

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7289
- Status: Canceled
- Resolution: Cancel
- Priority: P3
- Issue type: Incident
- Created: 2024-12-04T09:14:28.000+0800
- Updated: 2025-03-06T17:45:45.874+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: Backup
- Components: TiDB Operator
- Categories: backup-failure, storage-credential, operator-cr, performance-resource, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

We were observing logs coming from our tidb-operator controller that looked something like this:

```
E1203 21:21:13.215246       1 backup_controller.go:117] Backup: [REDACTED_ENV_NAME]/[REDACTED_RESOURCE_NAME], sync failed, err: create backup [REDACTED_ENV_NAME]/integ
[REDACTED_RESOURCE_NAME] job [REDACTED_RESOURCE_NAME] failed, err: namespaces "[REDACTED_ENV_NAME]" not found, requeuing
I1203 21:21:13.215308       1 backup_cleaner.go:62] start to ensure that backup [REDACTED_ENV_NAME]/[REDACTED_RESOURCE_NAME] jobs have finished
I1203 21:21:13.215330       1 backup_cleaner.go:73] start to clean backup [REDACTED_ENV_NAME]/[REDACTED_RESOURCE_NAME]
E1203 21:21:13.270067       1 job_control.go:64] failed to create backup job: [[REDACTED_ENV_NAME]/[REDACTED_RESOURCE_NAME], cluster: [REDACTED_CLUSTER], err: namespace
s "[REDACTED_ENV_NAME]" not found
I1203 21:21:13.270192       1 event.go:298] Event(v1.ObjectReference{Kind:"Backup", Namespace:"[REDACTED_ENV_NAME]", Name:"[REDACTED_RESOURCE_NAME]", UID:"[REDACTED_UUID]", APIVersion:"pingcap.com/v1alpha1", ResourceVersion:"166677164", FieldPath:""}): type: 'Warning' reason: 'FailedCreate' create job [REDACTED_ENV_NAME]/[REDACTED_RESOURCE_NAME]-
00 for cluster [REDACTED_CLUSTER] backup failed error: namespaces "[REDACTED_ENV_NAME]" not found                                                                                                       E1203 21:21:13.328274       1 event.go:280] Server rejected event '&v1.Event{TypeMeta:v1.TypeMeta{Kind:"", APIVersion:""}, ObjectMeta:v1.ObjectMeta{Name:"[REDACTED_RESOURCE_NAME].18094db815a4dedc", GenerateName:"", Namespace:"[REDACTED_ENV_NAME]", SelfLink:"", UID:"", ResourceVersion:"", Generation:0, CreationTimestamp:time.Date(1, time.January, 1, 0, 0, 0, 0, time.UTC), DeletionTimestamp:<nil>, DeletionGracePeri
odSeconds:(*int64)(nil), Labels:map[string]string(nil), Annotations:map[string]string(nil), OwnerReferences:[]v1.OwnerReference(nil), Finalizers:[]string(nil), ManagedFields:[]v1.ManagedFieldsEntry(nil)}, InvolvedObject:v1.ObjectR
eference{Kind:"Backup", Namespace:"[REDACTED_ENV_NAME]", Name:"[REDACTED_RESOURCE_NAME]", UID:"[REDACTED_UUID]", APIVersion:"pingcap.com/v1alpha1", ResourceVersion:"
166677164", FieldPath:""}, Reason:"FailedCreate", Message:"create job [REDACTED_ENV_NAME]/[REDACTED_RESOURCE_NAME] for cluster [REDACTED_CLUSTER] backup failed error: na
mespaces \"[REDACTED_ENV_NAME]\" not found", Source:v1.EventSource{Component:"tidb-controller-manager", Host:""}, FirstTimestamp:time.Date(2024, time.November, 19, 7, 23, 4, 733114076, time.Local), LastTimestamp
:time.Date(2024, time.December, 3, 21, 21, 13, 270089996, time.Local), Count:24866, Type:"Warning", EventTime:time.Date(1, time.January, 1, 0, 0, 0, 0, time.UTC), Series:(*v1.EventSeries)(nil), Action:"", Related:(*v1.ObjectRefere
nce)(nil), ReportingController:"tidb-controller-manager", ReportingInstance:""}': 'namespaces "[REDACTED_ENV_NAME]" not found' (will not retry!)
E1203 21:21:13.413263       1 backup_status_updater.go:131] Failed to update backup [[REDACTED_ENV_NAME]/[REDACTED_RESOURCE_NAME], error: namespaces "[REDACTED_ENV_NAME]
kup" not found
```

So I started to look into where this was coming from. The only way I could find the backup(s) in question were by requesting for the resource (backup) across all namespaces with kubectl get backup --all-namespaces and then piping that output into grep [REDACTED_ENV_NAME]. I found a large number (\~50) of backups that way. Some are Completed and others are in a RetryFailed state. They look like this:

```
[REDACTED_ENV_NAME]   [REDACTED_RESOURCE_NAME]         full   snapshot   RetryFailed   s3://[REDACTED_BUCKET]/[REDACTED_OBJECT_PATH]                                                                                                84d
```

I figure due to the age of these they’re likely orphaned from a TiDB cluster that no longer exists in this kubernetes cluster. The odd part is that the namespace they’re reported as being found in ([REDACTED_ENV_NAME]) doesn’t exist at all. So somehow that namespace is deleted, but these backup resources are still there somehow.

## Recent Comments Excerpt

### 2024-12-04T09:14:41.000+0800 [REDACTED_USER]

notified (张学程([REDACTED_EMAIL]), ) by lark

### 2024-12-04T09:15:15.000+0800 [REDACTED_USER]

There is not such a backupSchedule either:
~ kubectl get backupschedule --all-namespaces
NAMESPACE                        NAME                            SCHEDULE    MAXBACKUPS   MAXRESERVEDTIME   AGE
sample-byok                      [REDACTED_RESOURCE_NAME]   0 * * * *                48h               29d
[REDACTED_ENV_NAME]   [REDACTED_RESOURCE_NAME]   0 * * * *                48h               35d
tidb-quarantine                  [REDACTED_RESOURCE_NAME]   0 * * * *                48h               28d
[REDACTED_ENV_NAME]                        [REDACTED_RESOURCE_NAME]   0 * * * *                48h               32d

### 2025-01-03T11:30:00.000+0800 [REDACTED_USER]

@[REDACTED_USER]
 what's the status now?

### 2025-01-07T23:12:44.000+0800 [REDACTED_USER]

@[REDACTED_USER]
 this ticket can be closed now. Thanks.
