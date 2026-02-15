# State Machine Studio

A visual workflow builder for defining complex agent collaboration patterns, task decomposition strategies, and failure recovery paths.

## Features

- **Visual Workflow Designer** - Design complex multi-agent workflows with a visual interface
- **State Management** - Define states with agent assignments, timeouts, and retry logic
- **Transition Control** - Configure success, failure, conditional, and manual transitions
- **Recovery Paths** - Built-in failure recovery with automatic retry and fallback strategies
- **Task Decomposition** - Support for sequential, parallel, hierarchical, fanout-fanin, and pipeline strategies
- **Import/Export** - Save and load workflows as JSON for versioning and sharing

## Installation

```bash
pip install -e .
```

## Quick Start

```python
from state_machine_studio import StateMachineDesigner, WorkflowExecutor

# Create workflow
sm = StateMachineDesigner()
workflow = sm.create_workflow("data_processing", decomposition_strategy="pipeline")

# Add states
ingest = sm.add_state(workflow_id, "Ingest", agent_assignments=["agent-1"])
process = sm.add_state(workflow_id, "Process", agent_assignments=["agent-2"])
analyze = sm.add_state(workflow_id, "Analyze", agent_assignments=["agent-3"])

# Add transitions
sm.add_transition(workflow_id, ingest.state_id, process.state_id)
sm.add_transition(workflow_id, process.state_id, analyze.state_id)

# Execute workflow
executor = WorkflowExecutor(sm)
result = await executor.execute(workflow.workflow_id, agents)
```

## Architecture

```
state-machine-studio/
├── src/
│   ├── __init__.py
│   └── state_machine.py
└── examples/
    └── demo.py
```

## License

MIT
