# GTOC-7438: Restore storage credential failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7438
- Status: UNDER INVESTIGATION
- Resolution: N/A
- Priority: P3
- Issue type: Incident
- Created: 2025-02-28T10:04:55.805+0800
- Updated: 2025-03-06T17:36:38.911+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: Restore
- Components: BR
- Categories: storage-credential, performance-resource, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

We’d like to enable br unit tests in our own internal CI to make sure our cherry-picks/internal changes don’t break core BR functionality. However, we are seeing some consistently failing unit tests both on our internal 8.5 release as well as on latest master.

We see test errors when running `make br_unit_test_in_verify_ci` and `make br_unit_test` from latest master. In addition, I’m seeing some failed tests suggest setting the `intest` tag (which appears to be set on other unit test targets as well as when bazel runs the unit tests) – however, when setting it manually I see unit test failures (though there are fewer than without).

Is there any divergence between the base br unit test targets in the Makefile and the bazel versions? I’ve attached logs of the unit test runs w/ and w/out the intest tag that show which cases are failing. Are these flaky tests that we expect to resolve upon subsequent runs, or other test errors based on differences in environment, machine setup, etc.?

## Recent Comments Excerpt

### 2025-02-28T10:05:11.739+0800 [REDACTED_USER]

notified (廖坚钧([REDACTED_EMAIL]), ) by lark

### 2025-02-28T13:37:29.729+0800 [REDACTED_USER]

Most of unit tests in task package are to check the default config, which is skipped in the CI. See 
https://github.com/pingcap/tidb/blob/d39268519f7529261c66a42f70fba310b8e3dddd/Makefile#L634
 
We will fix these unit tests and let CI also run them.

### 2025-03-04T02:04:05.554+0800 [REDACTED_USER]

From customer: [REDACTED_CUSTOMER]
-//br/pkg/task:task_test
 tests are run, which only correspond to
    srcs = [
        "backup_ebs_test.go",
        "backup_test.go",
        "common_test.go",
        "config_test.go",

### 2025-03-04T11:39:45.795+0800 [REDACTED_USER]

We will remove 
-//br/pkg/task:task_test
 in the bazel command and fix the unit tests so that all the unit tests can be run in CI.

### 2025-03-06T09:15:25.218+0800 [REDACTED_USER]

https://github.com/pingcap/tidb/pull/59924
