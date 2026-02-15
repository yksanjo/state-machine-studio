#!/usr/bin/env python3
"""Demo script for State Machine Studio."""

import asyncio
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src import (
    StateMachineDesigner, WorkflowExecutor, TransitionType, 
    DecompositionStrategy, Agent, AgentType
)

async def main():
    print("=" * 50)
    print("State Machine Studio Demo")
    print("=" * 50)
    
    # Create workflow
    sm = StateMachineDesigner()
    workflow = sm.create_workflow("Data Pipeline", decomposition_strategy=DecompositionStrategy.PIPELINE)
    
    # Add states
    ingest = sm.add_state(workflow.workflow_id, "Ingest", agent_assignments=["agent-1"])
    process = sm.add_state(workflow.workflow_id, "Process", agent_assignments=["agent-2"])
    analyze = sm.add_state(workflow.workflow_id, "Analyze", agent_assignments=["agent-3"])
    
    # Add transitions
    sm.add_transition(workflow.workflow_id, ingest.state_id, process.state_id)
    sm.add_transition(workflow.workflow_id, process.state_id, analyze.state_id)
    sm.set_final_state(workflow.workflow_id, analyze.state_id)
    
    # Get diagram
    diagram = sm.get_state_diagram(workflow.workflow_id)
    print(f"\nWorkflow: {workflow.name}")
    print(f"States: {len(diagram['nodes'])}")
    print(f"Transitions: {len(diagram['edges'])}")
    
    print("\n✓ Demo completed successfully!")

if __name__ == "__main__":
    asyncio.run(main())
