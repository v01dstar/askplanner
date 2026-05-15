# GTOC-8338: Operator PITR CR failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-8338
- Status: UNDER INVESTIGATION
- Resolution: N/A
- Priority: P1
- Issue type: Incident
- Created: 2026-04-02T05:18:13.197+0800
- Updated: 2026-04-15T08:02:05.412+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: TiDB
- Categories: [REDACTED_RESOURCE_NAME], operator-cr, performance-resource, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

> Hi [REDACTED_USER],
>
> Hope you’re doing well.
>
> We would like to check your team’s availability for standby support during our planned DR swingover activity scheduled for this Thursday night (2 April 2026). During this activity, we will be performing a switch from **Production to DR**, and your support would be appreciated in case any TiDB or TiCDC related issues arise.
>
> Details of the activity are as follows:
>
> * **Activity:** DR Swingover (Prod → DR)
> * **Component:** TiDB
> * **Date & Time:** **2/4/2026**, **12:15 AM – 6:00 AM (UTC+8)**
> * **Action Required:** Standby support during swingover activity
> 
> Please confirm your team’s availability for standby support during the mentioned window.
>
> Following is the meeting invite **(Microsoft Teams)** for the activity:
>
> **Join:** [[REDACTED_MEETING_URL])
>
> Meeting ID: 446 070 622 923 4
>
> Passcode: aR6yj3um
>
> Additionally, please let us know if you require any information, grafana snapshots, logs, or any other preparation from our side prior to the activity.
>
> Thank you as always for your continued support.
>
> Best regards,

## Recent Comments Excerpt

### 2026-04-02T09:50:42.169+0800 [REDACTED_USER]

Response(not ack for Critical alert) in lark: om_x100b53ec99215ca0c2eaa4093c9d437

### 2026-04-02T09:50:42.681+0800 [REDACTED_USER]

Response(not ack for Critical alert) in lark: om_x100b53ecf7703ca0c3b5b390dc75499

### 2026-04-02T11:12:51.821+0800 [REDACTED_USER]

Would you try 
br log status
 to check whether here is any task in PD? If there is, try to remove them by 
br log stop
, then clean up objects belong to this backup or just start a log task to a new prefix.
Also, it would be better to specify 
start-ts
 to a existing snapshot backup, because restoring a incremental backup requires a snapshot backup with

### 2026-04-02T13:58:42.167+0800 [REDACTED_USER]

Desmond Foo invited you to a group on Feishu, click 
https://applink.feishu.cn/client/chat/chatter/add_by_link?link_token=[REDACTED_SECRET]
 to join!

### 2026-04-15T08:02:04.961+0800 [REDACTED_USER]

The linked ticket has been resolved.
