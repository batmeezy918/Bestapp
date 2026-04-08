# Theorem Studio Product Spec

## Goal
Build a crisp, clean theorem engineering platform with:
- Lean 4 + mathlib verification
- Coq and Isabelle generation/verification hooks
- deterministic theorem scaffold generation
- verifier-driven repair suggestions
- corpus-aware theorem search
- submission readiness checks
- feature-rich UI with buttons and prompt window

## Core UX

### Layout
- Left sidebar: workspace, theorem history, active definitions, mode toggles
- Center editor: prompt input on top, generated formal code below in tabs (Lean / Coq / Isabelle)
- Right rail: verification results, errors, repair suggestions, library matches
- Bottom panel: decomposition graph, proof roadmap timeline, export tools

### Primary Buttons
- Generate Statement
- Generate Proof Skeleton
- Normalize Deterministically
- Search Libraries
- Verify Lean
- Verify Coq
- Verify Isabelle
- Explain Errors
- Suggest Repairs
- Submission Readiness
- Export Lean
- Export Coq
- Export Isabelle
- Export Patch

## Feature Modules

### 1. Intent-to-Theorem Compiler
Input: informal theorem intent
Output:
- theorem names
- imports
- namespace
- variable block
- exact statement candidates
- proof skeletons

### 2. Deterministic Normal Form
A canonical output mode that fixes:
- theorem naming
- import order
- namespace style
- indentation
- proof skeleton template

### 3. Decomposition Engine
Break theorem requests into:
- required definitions
- lemma candidates
- missing assumptions
- proof obligations

### 4. Multi-Prover Translation
Generate aligned equivalents for Lean, Coq, Isabelle.

### 5. Verifier Adapter Layer
Adapters:
- LeanAdapter
- CoqAdapter
- IsabelleAdapter
Each returns:
- success/failure
- line/column diagnostics
- normalized error classes
- repair suggestions

### 6. Error-to-Repair Engine
Normalized categories:
- MissingImport
- TypeMismatch
- ImplicitArgumentIssue
- UniverseIssue
- MissingInstance
- TacticFailure
- UnknownIdentifier

### 7. Corpus-Aware Search
Search local metadata and external theorem libraries for exact/near matches.

### 8. Submission Readiness
Checks:
- no sorry/admit/oops
- clean build
- minimal imports
- naming conventions
- docstrings/comments where required

## Suggested Repo Structure

```text
app/
  web/
    src/
      components/
      pages/
      hooks/
      styles/
  backend/
    src/
      api/
      services/
      adapters/
      domain/
      utils/
formal/
  lean/
  coq/
  isabelle/
docs/
.github/workflows/
```

## API Routes
- POST /api/generate
- POST /api/normalize
- POST /api/decompose
- POST /api/search
- POST /api/verify/lean
- POST /api/verify/coq
- POST /api/verify/isabelle
- POST /api/repair
- POST /api/readiness

## UI Principles
- high contrast
- minimal chrome
- dense but readable information layout
- monospaced code areas
- one-click actions
- clear pass/fail states
- deterministic outputs surfaced explicitly

## Determinism Contract
Same prompt + same selected mode + same theorem context => same generated scaffold.

## Future Extensions
- HOL Light adapter
- Agda adapter
- AST inspector
- tactic trace explainer
- finite counterexample sanity checks
- PR auto-generation for verified theorems
