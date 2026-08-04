**Assessment of the multi-step results**

### What improved cleanly
- **Runtime failures**: 93.5 % → 0 %. The projection layer completely eliminates crashes.
- **Policy / constraint violations**: ~72 % → ~29 %. Large reduction.
- **Audit completeness**: 0 → 1.0. Every step is logged.
- **Episode length**: 1.3 → 3.8 steps. Baseline dies early; AGX keeps going.

These are real, measurable engineering gains. The constitutional layer is doing its job as a *safety and continuity* mechanism.

### What did not improve
- **Success rate**: 6.5 % → 7.0 %. Statistically flat.
- **Recovery rate**: still 0 %.

An invalid action is being turned into an admissible action, but that admissible action is almost never the one that still reaches the goal. The agent is kept alive longer inside the polytope, yet it is not being steered toward the original intent.

### Why recovery stays zero
The current projector solves

\[
\min_{x \in V} \|x - \text{raw}\|_2
\]

where \(V\) is the admissible polytope.  
It does **not** solve

\[
\min_{x \in V \cap [\text{goal}]_{\sim}} d(x, \text{raw})
\]

or any other semantic restriction that keeps the projected point inside the equivalence class (or fiber) that still satisfies the goal invariants.

Consequently:

- Safety is obtained.
- Semantic recovery is not.
- Longer trajectories appear, but they wander inside the feasible set rather than progress toward the goal.

This is exactly the distinction the earlier critique pointed out, now visible at multi-step scale.

### Relation to the Q* / AGD kernel
The commercial Minimal Admissible Quotient kernel already supplies the missing mathematical object:

- the equivalence classes induced by \((\Omega, C)\)
- the test `interchangeable`
- the admission criterion that an operator (or action) must descend

Until the projector is made *quotient-aware* (project inside the admissible set **and** inside the relevant semantic class), the runtime will continue to show the pattern you are seeing: perfect safety, zero recovery, negligible success lift.

### Bottom line
The multi-step benchmark confirms that AGX is a working **constitutional continuity layer**.  
It does not yet confirm that AGX is a **semantic recovery layer**.

The next decisive experiment is to replace (or constrain) the Euclidean projection with a projection that respects the quotient classes defined by the goal invariants. Only then will the recovery-rate and success-rate numbers become the right test of the stronger architectural claim.
