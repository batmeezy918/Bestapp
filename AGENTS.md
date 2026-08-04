# CVR Build Agent Instructions

Do not edit generated files manually.

The only executable entry point is:

```bash
python tools/cvr.py execute-dag
```

Before making changes:

1. Validate Constitution.
2. Validate Kernel.
3. Validate MIR.
4. Validate Build DAG.

After making changes:

1. Run `verify-system`.
2. Execute Build DAG.
3. Validate witnesses.
4. Replay all nodes.
5. Emit repository certificate.

Do not bypass `tools/cvr.py`.

Do not add workflow steps outside the Build DAG.

Every new runtime module must have:

- a MIR node
- a Build DAG node
- tests
- witness support
- replay support
