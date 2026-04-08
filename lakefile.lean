import Lake
open Lake DSL

package theoremstudio

require mathlib from git
  "https://github.com/leanprover-community/mathlib4"

@[default_target]
lean_lib TheoremStudio
