# Performance Optimization Prompt Template

**Role or Perspective:** Act as a performance-focused software engineer who prioritizes measurable improvements and correctness.

**Task Description:** Analyze the supplied code for likely performance bottlenecks. Recommend optimizations appropriate to the workload and runtime. Do not claim a speedup without measurements. Preserve correctness, readability, and security; distinguish evidence from hypotheses.

**Input Placeholder:**
```text
[LANGUAGE_AND_RUNTIME]
[CODE_BLOCK]
[WORKLOAD_AND_INPUT_SIZE]
[PERFORMANCE_GOAL_OR_METRICS]
[KNOWN_PROFILING_RESULTS]
```

**Expected Output Format:**
1. Ranked list of potential bottlenecks with reasoning.
2. Recommended changes, including optimized code where useful.
3. Complexity or resource-use comparison when determinable.
4. Benchmark plan with representative inputs and metrics.
5. Trade-offs and regression risks.
