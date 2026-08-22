# alokbarsho 🌕

**Smart India Hackathon — Problem Statement 26166**
Multi-modal, Sun-angle and scale-invariant image correspondence using Chandrayaan-2 optical images (OHRC, TMC and IIRS)

> New to Git/GitHub? Don't worry — this README walks you through everything, step by step. Read it top to bottom before touching any code.

---

## 1. What are we actually building?

ISRO takes photos of the Moon using different cameras on Chandrayaan-2 (OHRC, TMC-2, IIRS) and compares them to NASA's LRO camera photos of the same spots. The problem: the same crater looks *different* in each photo because of different sunlight angles, different zoom levels, and different cameras.

**Our job:** build software that automatically figures out "this patch of Photo A is the same place as this patch of Photo B" — even though they look different — and proves it's accurate.

Think of it like: someone shows you two photos of your street, one taken at noon and one at sunset, from different angles — and you have to draw lines connecting the same landmarks in both photos. We're teaching a computer to do that for the Moon, without ever training it on example photos first.

If none of this makes sense yet, that's fine — you don't need to understand the *algorithm* to contribute. Keep reading.

---

## 2. Who's doing what

| Person | Role | What that means day-to-day |
|---|---|---|
| Anik | Architect / Core algorithm | Designs the pipeline, writes the hardest matching code |
| _(fill in)_ | Core algorithm | Helps build the matching logic |
| _(fill in)_ | Data pipeline | Downloads and prepares the Moon images |
| _(fill in)_ | Evaluation | Builds the scoring/metrics code, makes charts |
| _(fill in)_ | UI / Demo | Builds the website people click around during judging |
| _(fill in)_ | Docs / Testing / Integration | Keeps everything glued together, writes tests, tidies docs |

**If you're the newest member:** the UI, docs, testing, and data pipeline roles are the easiest entry points. You don't need to touch the core algorithm code to make a real contribution.

---

## 3. What's in this repo (folder by folder)

```
alokbarsho/
├── dataset/
│   ├── raw/            ← original downloaded Moon images (NOT uploaded to GitHub — too big)
│   └── processed/      ← cleaned-up/resized versions we actually use
├── docs/                ← write-ups and guides (like this file's bigger cousins)
├── papers/               ← reference research papers we're basing our method on
├── images/               ← screenshots/result images for the README and demo
├── notebooks/            ← messy exploration code (Jupyter notebooks) — okay to be messy here
├── src/                  ← the REAL, clean code that makes the project work
│   ├── preprocessing.py      → cleans/resizes images before processing
│   ├── phase_congruency.py   → the "secret sauce" — finds landmarks that don't change with sunlight
│   ├── feature_detection.py  → finds distinctive points in each image
│   ├── feature_matching.py   → matches points between the two images
│   ├── ransac.py              → throws out wrong/bad matches
│   ├── homography.py          → works out how to overlay one image on the other
│   ├── registration.py        → runs the whole pipeline start to finish
│   ├── evaluation.py          → calculates accuracy scores (RMSE, inlier ratio, etc.)
│   └── utils.py                → small helper functions used everywhere
├── tests/                 ← automated checks that make sure code isn't broken
├── app.py                 ← starts the website/demo
├── requirements.txt        ← list of Python packages needed to run this
├── .gitignore              ← tells Git which files to IGNORE (big images, temp files)
└── presentation/           ← slides and demo video for judging day
```

**Rule of thumb:** if you're not sure where your file goes, ask in the group chat before dumping it in the root folder.

---

## 4. Setting up the project on your own laptop (do this once)

### Step 1 — Install Git and Python
- Check if you already have them:
  ```bash
  git --version
  python3 --version
  ```
- If either command fails, install Git from [git-scm.com](https://git-scm.com) and Python from [python.org](https://python.org) (Windows/Mac) or use your package manager on Linux.

### Step 2 — Clone the repo (download it to your computer)
```bash
git clone https://github.com/AnikModak/alokbarsho.git
cd alokbarsho
```

### Step 3 — Set up a virtual environment (keeps packages isolated)
```bash
python3 -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```
You'll know it worked if you see `(venv)` at the start of your terminal prompt.

### Step 4 — Install the required packages
```bash
pip install -r requirements.txt
```

You're set up! You now have a full copy of the project on your machine.

---

## 5. How to actually add or change something (the important part)

**Golden rule: never write code directly on `main`.** `main` is the "official, working" version of the project. You always work on your own *branch* — a safe copy where you can experiment — and only merge it into `main` once it's reviewed.

### Step-by-step, every time you start new work:

**1. Make sure you have the latest version of `main`:**
```bash
git checkout main
git pull origin main
```

**2. Create your own branch** (name it after what you're doing):
```bash
git checkout -b feature/short-description
```
Examples: `feature/upload-ui`, `feature/dataset-download-script`, `feature/fix-readme-typo`

**3. Make your changes** — edit files, add files, whatever your task needs.

**4. Save your changes to Git (this is called "committing"):**
```bash
git add .
git commit -m "Explain what you did in a few words"
```
Example: `git commit -m "Add image upload button to demo page"`

**5. Push your branch to GitHub** (first time on this branch):
```bash
git push --set-upstream origin feature/short-description
```
(After the first time, you can just type `git push`.)

**6. Open a Pull Request (PR) on GitHub:**
- Go to `https://github.com/AnikModak/alokbarsho`
- You'll see a yellow banner: **"Compare & pull request"** — click it
- Make sure Base is `main` and Compare is your branch
- Write a short title/description of what you did
- Click **Create pull request**

**7. Wait for a review.** Someone else on the team checks your code, then merges it in. Don't merge your own PR without at least one teammate looking at it first, if possible.

**8. After it's merged, delete your branch** (GitHub will offer a button to do this) and start fresh from `main` next time.

---

## 6. Common mistakes (and how to avoid them)

| Mistake | Fix |
|---|---|
| "I edited files directly on `main`!" | Don't panic — just don't push yet. Make a new branch from where you are: `git checkout -b feature/oops`, then follow the PR steps normally. |
| "`git push` says no upstream branch" | Use `git push --set-upstream origin your-branch-name` the first time you push a new branch. |
| "My branch is behind `main`, now what?" | ```git checkout main``` → ```git pull origin main``` → ```git checkout your-branch``` → ```git merge main``` |
| "I accidentally added a huge image file" | Check `.gitignore` — raw dataset images should already be excluded. If you're not sure, ask before committing large files. |
| "I don't know what my task even means" | Ask in the group chat. Better to ask than to guess and redo work. |

---

## 7. Cheat sheet (keep this handy)

```bash
git status                 # what's changed?
git checkout main          # switch to main branch
git pull origin main       # get latest updates
git checkout -b NAME       # create + switch to a new branch
git add .                  # stage all changes
git commit -m "message"    # save changes with a note
git push                   # upload to GitHub (after first --set-upstream)
```

---

## 8. Who to ask

Stuck? Ask in the team group chat first. If it's a Git problem specifically, screenshot the **exact error message** — that's the fastest way for someone to help you.

Welcome to the team — let's get this on the Moon. 🚀
