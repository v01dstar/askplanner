# Issue 64969: Log backup checkpoint lag

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/64969
- State: CLOSED
- Author: [REDACTED_USER]
- Created: 2025-12-11T02:53:26Z
- Updated: 2025-12-11T09:33:15Z
- Closed: 2025-12-11T09:28:47Z
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Classic
- Operation: Restore
- Components: TiDB, TiKV, BR
- Categories: restore-failure, schema-metadata, observability-diagnosis
- Labels: component/br, contribution, severity/major, type/bug, wontfix
- Affected versions: N/A

## Quick Match

- Title/error signature: `Log backup checkpoint lag`
- Search terms: BR; Restore; TiDB; TiKV; observability-diagnosis; restore-failure; schema-metadata

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]

<!-- a step by step guide for reproducing the bug. -->
full restore tables which have foreign key.  some backupmeta message:
```
{"id":69,"name":{"O":"t_child","L":"t_child"},"charset":"utf8mb4","collate":"utf8mb4_bin","cols":[{"id":1,"name":{"O":"id","L":"id"},"offset":0,"origin_default":null,"origin_default_bit":null,"default":null,"default_bit":null,"default_is_expr":false,"generated_expr_string":"","generated_stored":false,"dependences":null,"type":{"Tp":3,"Flag":4099,"Flen":11,"Decimal":0,"Charset":"binary","Collate":"binary","Elems":null},"state":5,"comment":"","hidden":false,"change_state_info":null,"version":2},{"id":2,"name":{"O":"pid","L":"pid"},"offset":1,"origin_default":null,"origin_default_bit":null,"default":null,"default_bit":null,"default_is_expr":false,"generated_expr_string":"","generated_stored":false,"dependences":null,"type":{"Tp":3,"Flag":0,"Flen":11,"Decimal":0,"Charset":"binary","Collate":"binary","Elems":null},"state":5,"comment":"","hidden":false,"change_state_info":null,"version":2}],"index_info":null,"constraint_info":null,"fk_info":[{"id":0,"fk_name":{"O":"fk_pid","L":"fk_pid"},"ref_table":{"O":"t_parent","L":"t_parent"},"ref_cols":[{"O":"id","L":"id"}],"cols":[{"O":"pid","L":"pid"}],"on_delete":2,"on_update":2,"state":5}],"state":5,"pk_is_handle":true,"is_common_handle":false,"common_handle_version":0,"comment":"","auto_inc_id":0,"auto_id_cache":0,"auto_rand_id":0,"max_col_id":2,"max_idx_id":0,"max_cst_id":0,"update_timestamp":[REDACTED_LONG_ID],"ShardRowIDBits":0,"max_shard_row_id_bits":0,"auto_random_bits":0,"pre_split_regions":0,"partition":null,"compression":"","view":null,"sequence":null,"Lock":null,"version":4,"tiflash_replica":null,"is_columnar":false,"temp_table_type":0,"cache_table_status":0,"policy_ref_info":null,"stats_options":null}ﺐ�����] (t:�

|{"id":65,"db_name":{"O":"fktest","L":"fktest"},"charset":"utf8mb4","collate":"utf8mb4_bin","state":5,"policy_ref_info":null}�
                                                                                                                              {"id":67,"name":{"O":"t_parent","L":"t_parent"},"charset":"utf8mb4","collate":"utf8mb4_bin","cols":[{"id":1,"name":{"O":"id","L":"id"},"offset":0,"origin_default":null,"origin_default_bit":null,"default":null,"default_bit":null,"default_is_expr":false,"generated_expr_string":"","generated_stored":false,"dependences":null,"type":{"Tp":3,"Flag":4099,"Flen":11,"Decimal":0,"Charset":"binary","Collate":"binary","Elems":null},"state":5,"comment":"","hidden":false,"change_state_info":null,"version":2},{"id":2,"name":{"O":"a","L":"a"},"offset":1,"origin_default":null,"origin_default_bit":null,"default":null,"default_bit":null,"default_is_expr":false,"generated_expr_string":"","generated_stored":false,"dependences":null,"type":{"Tp":3,"Flag":0,"Flen":11,"Decimal":0,"Charset":"binary","Collate":"binary","Elems":null},"state":5,"comment":"","hidden":false,"change_state_info":null,"version":2}],"index_info":null,"constraint_info":null,"fk_info":null,"state":5,"pk_is_handle":true,"is_common_handle":false,"common_handle_version":0,"comment":"","auto_inc_id":0,"auto_id_cache":0,"auto_rand_id":0,"max_col_id":2,"max_idx_id":0,"max_cst_id":0,"update_timestamp":[REDACTED_LONG_ID],"ShardRowIDBits":0,"max_shard_row_id_bits":0,"auto_random_bits":0,"pre_split_regions":0,"partition":null,"compression":"","view":null,"sequence":null,"Lock":null,"version":4,"tiflash_replica":null,"is_columnar":false,"temp_table_type":0,"cache_table_status":0,"policy_ref_info":null,"stats_options":null}ﺐ�����] (tR[]Z�BR
Release Version: v6.0.0
Git Commit Hash: 36a9810441ca0e496cbd22064af274b3be771081
Git Branch: HEAD
Go Version: go1.19.3
UTC Build Time: 2023-01-05 02:49:58
```


### 2. [REDACTED_USER]
full restore can succeed

### 3. [REDACTED_USER]
`[2025/12/04 04:52:38.253 +00:00] [INFO] [collector.go:77] [\"Full Restore failed summary\"] [total-ranges=0] [ranges-succeed=0] [ranges-failed=0]\n", "stderr": "Detail BR log in /tmp/br.log.2025-12-04T04.52.35Z \nError: DDL job operating on schema or table, must have non-empty name set in InvolvingSchemaInfo\n"`

### 4. [REDACTED_USER]

<!-- Paste the output of SELECT tidb_version() -->
TIDB_VERSION(): Release Version: v9.0.0-beta.2.pre-871-g704d4c8
Edition: Community
Git Commit Hash: 704d4c88f0dac3b7ffd28863ad0c741033b66fce
Git Branch: HEAD
UTC Build Time: 2025-12-10 04:17:28
GoVersion: go1.23.12
Race Enabled: false
Check Table Before Drop: false
Store: tikv
Kernel Type: Classic
1 row in set (0.03 sec)
