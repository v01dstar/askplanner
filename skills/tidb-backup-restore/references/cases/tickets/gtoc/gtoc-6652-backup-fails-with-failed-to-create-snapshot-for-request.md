# GTOC-6652: Backup fails with failed to create snapshot for request {

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-6652
- Status: Canceled
- Resolution: Cancel
- Priority: P2
- Issue type: Incident
- Created: 2024-01-30T06:57:54.000+0800
- Updated: 2024-05-20T13:33:01.000+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: Backup
- Components: BR
- Categories: backup-failure, storage-credential, tikv-data-path, operator-cr, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

Hello, we saw one volumebackup failed due to snapshot creation for one volume 

```
I0112 17:39:23.345398       9 backup.go:302] 
I0112 17:39:23.345414       9 backup.go:312] Error: failed to create snapshot for request {
  CopyTagsFromSource: "volume",
  InstanceSpecification: {
    ExcludeBootVolume: true,
    ExcludeDataVolumeIds: ["vol-02d161948f0154735"],
    InstanceId: "i-07d43e3a1b26547cc"
  }
}: Int
```

we checked tikvs in this region and there’s no restart during that period of time. So wondering do you have insights what’s the root cause?  or more logs about what happened?   
backup log: <custom data-type="smartlink" data-id="id-0">https://gist.github.com/olivia-chen-github/72b7e0c90502a346399d587558b9c99a</custom> 

backup cr: <custom data-type="smartlink" data-id="id-1">https://gist.github.com/olivia-chen-github/461608658bc2fd20cabaaf6794776f55</custom> 

Thanks.

## Recent Comments Excerpt

### 2024-01-30T07:07:08.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 29/Jan/24 11:06 PM

https://jira.tidbcloud.com/projects/GTOC/issues/GTOC-6652

### 2024-01-30T09:46:05.000+0800 [REDACTED_USER]

The failure is from AWS and AirBnB need to open a ticket to AWS to check the reason of snapshot creation request failure. The information clue is "
failed to create snapshot for request { CopyTagsFromSource: "volume", InstanceSpecification: { ExcludeBootVolume: true, ExcludeDataVolumeIds: ["vol-02d161948f0154735"], InstanceId: "i-07d43e3a1b26547cc" } }: InternalError: An internal error has occurred status code: 500, request id: [REDACTED_UUID]
".

### 2024-02-03T05:54:35.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 02/Feb/24 9:54 PM

@[REDACTED_USER] failure is from AWS and you can open a ticket to AWS to check the reason of snapshot creation request failure.
The related information is:
failed to create snapshot for request { CopyTagsFromSource: "volume", InstanceSpecification: { ExcludeBootVolume: true, ExcludeDataVolumeIds: ["vol-02d161948f0154735"], InstanceId: "i-07d43e3a1b26547cc" } }: InternalError: An internal error has occurred status code: 500, request id: [REDACTED_UUID]

### 2024-02-08T22:38:26.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 08/Feb/24 2:38 PM

Hey @[REDACTED_USER] , please let us know if we still have any questions regarding to this ticket. Thanks

### 2024-02-19T12:09:03.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 19/Feb/24 4:08 AM

Since we haven’t received replies for sometime, we would close this ticket for now. Please feel free reopen it if you have further questions.
