# Module 5 Homework — Step-by-step Checklist (2026)

This is the **lead-scoring homework**, separate from the Telco churn example in the lecture notebook. Run commands in WSL Ubuntu. Keep your own repository structure:

`ML-ZoomCamp-Outputs/module5_deployment/homework/`

## 1. Prepare the project and reference files

- [x] Check the existing tools: `python3 --version`, `uv --version`, `docker --version`, `docker info`.
  - We had system Python **3.12.3**, uv **0.12.19**, and Docker **29.5.3**. The homework's uv version is **Q1 (not graded)**.
- [x] Create and enter the folder:

  ```bash
  mkdir -p module5_deployment/homework
  cd module5_deployment/homework
  ```

- [x] Retrieve the official 2026 reference files from DataTalksClub, then copy them into the homework folder. We used a sparse checkout in `/tmp`:

  ```bash
  git clone --depth 1 --filter=blob:none --sparse https://github.com/DataTalksClub/machine-learning-zoomcamp.git /tmp/mlzoomcamp-2026-hw5-source
  git -C /tmp/mlzoomcamp-2026-hw5-source sparse-checkout set cohorts/2026/homework/05-deployment
  cp -a /tmp/mlzoomcamp-2026-hw5-source/cohorts/2026/homework/05-deployment/. .
  ls -la
  ```

  Confirm files such as `pipeline.bin`, `predict.py`, `Dockerfile`, `model_metadata.json`, `pyproject.toml`, `uv.lock`, `smoke_test.py`, and `q6_test.py` exist. The copy command assumes the destination is the intended homework folder and initially empty.

## 2. Set up and verify the frozen environment

- [x] `cat .python-version` → **3.11.15** (managed by uv; no need to replace system Python).
- [x] `uv sync --locked` → install pinned dependencies without changing `uv.lock`.
- [x] `uv run python smoke_test.py` → confirmed deterministic inference; output included `conversion_probability: 0.769799` and `conversion: True`.
- [x] `sha256sum pipeline.bin` → must be:

  ```text
  1646bbdcd38d4f044da6b630c5b332c93a314245a8c21929011c42de51f629f1  pipeline.bin
  ```

The `VIRTUAL_ENV` warning happened because a parent repository environment was active. `uv` correctly used the homework's `.venv`.

## 3. Q2 — Check the locked Scikit-Learn version

- [x] Run:

  ```bash
  grep -A 3 'name = "scikit-learn"' uv.lock
  ```

  **Answer: `1.7.2`**. The question asks about the reference *lockfile*, not the system-wide installation.

## 4. Q3 — Load the pretrained pipeline and predict locally

- [x] Create `q3_predict.py` containing the following core logic:

  ```python
  import pickle

  with open('pipeline.bin', 'rb') as f:
      model = pickle.load(f)

  lead = {
      'lead_source': 'paid_ads',
      'industry': 'technology',
      'employment_status': 'employed',
      'location': 'north_america',
      'number_of_courses_viewed': 2,
      'annual_income': 79276.0,
      'interaction_count': 4,
      'lead_score': 0.41,
  }

  probability = model.predict_proba([lead])[0, 1]
  print(f'Conversion probability: {probability:.3f}')
  ```

- [x] `uv run python q3_predict.py` → **Q3 answer: `0.533`**.

  The saved object is a Scikit-Learn `Pipeline`: no separate `dv.transform()` is needed. Only load trusted pickle files.

## 5. Q4 — Test the local FastAPI application

- [x] In **Terminal 1** (homework directory), start:

  ```bash
  uv run uvicorn predict:app --host 0.0.0.0 --port 9696
  ```

- [x] In **Terminal 2**, check the service:

  ```bash
  curl -s http://localhost:9696/health
  ```

- [x] Send the second lead:

  ```bash
  curl -s http://localhost:9696/predict \
    -H 'Content-Type: application/json' \
    -d '{
      "lead_source": "organic_search",
      "industry": "technology",
      "employment_status": "employed",
      "location": "europe",
      "number_of_courses_viewed": 4,
      "annual_income": 80304.0,
      "interaction_count": 7,
      "lead_score": 0.74
    }'
  ```

  Response: `{"conversion_probability":0.769799,"conversion":true}` → **Q4 answer: `0.770`**.

- [x] Stop local Uvicorn in Terminal 1 with **Ctrl+C** before using Docker's port 9696.

## 6. Container and Q5 — Build, inspect, and run Docker

- [x] In the homework directory:

  ```bash
  docker build -t zoomcamp-model:2026-hw5 .
  docker images zoomcamp-model
  ```

- [x] Check `cat Dockerfile` (or the `FROM` line).
  - **Q5 answer: `python:3.11.15-slim-bookworm`**. The `@sha256:...` portion pins the exact image digest; it is not part of the tag asked for.
- [x] Start the container, leaving the terminal running:

  ```bash
  docker run --rm -p 9696:9696 zoomcamp-model:2026-hw5
  ```

  Docker's image size can vary and is **not graded**.

## 7. Q6 — Verify the Docker API

- [x] In a second terminal, from the homework directory:

  ```bash
  python q6_test.py
  curl -s http://localhost:9696/health
  ```

  The smoke client sends the **same lead as Q4**. It returned `{'conversion_probability': 0.769799, 'conversion': True}` → **Q6 answer: `0.770`**. The `/health` response should show `status: ok` and the model checksum above.
- [ ] Stop the Docker container using **Ctrl+C** when finished.

## 8. Submit and share

- [ ] Keep the committed homework files in your own GitHub repository; exclude `.venv/` and other generated environments from Git.
- [ ] Verify the folder opens publicly:

  [Module 5 homework on GitHub](https://github.com/besteekmen/ML-ZoomCamp-Outputs/tree/master/module5_deployment/homework)

- [ ] Submit the folder link and answers via [Homework 5 submission](https://courses.datatalks.club/ml-zoomcamp-2026/homework/hw05).
- [ ] Optionally add a public learning post and time spent on lectures/homework.

### Answer recap

| Question | Answer |
| --- | --- |
| Q1 (ungraded) | uv `0.12.19` |
| Q2 | scikit-learn `1.7.2` |
| Q3 | `0.533` |
| Q4 | `0.770` |
| Q5 | `python:3.11.15-slim-bookworm` |
| Q6 | `0.770` |
