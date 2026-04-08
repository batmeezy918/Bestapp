# Theorem Studio

A starter scaffold for a clean theorem engineering platform with:
- Lean 4 + mathlib verification workflow
- Coq / Isabelle hooks
- deterministic theorem scaffold generation goals
- crisp multi-pane UI
- backend verifier adapter architecture

## Current scaffold
- `.github/workflows/build.yml`
- `.github/workflows/provers.yml`
- `docs/theorem-studio-spec.md`
- `app/web/` React + Vite starter
- `app/backend/` FastAPI starter
- `formal/lean`, `formal/coq`, `formal/isabelle`

## Local dev

### Web
```bash
cd app/web
npm install
npm run dev
```

### Backend
```bash
cd app/backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn src.main:app --reload
```

## Next build targets
- wire prompt input to backend generation APIs
- add Lean project files (`lean-toolchain`, `lakefile.lean`)
- add verifier adapters and parser/repair engine
