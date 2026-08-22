# Git Workflow Cheat Sheet

## One-time setup
```bash
git clone https://github.com/YOUR_USERNAME/SIH_Lunar_Image_Registration.git
cd SIH_Lunar_Image_Registration
```

## Starting new work
Never commit directly to `main`. Always branch:
```bash
git checkout main
git pull origin main
git checkout -b feature/your-feature-name
```

## Saving work
```bash
git add .
git commit -m "Short description of what you did"
```

## Pushing a new branch (first time)
```bash
git push --set-upstream origin feature/your-feature-name
```
After the first push, plain `git push` works.

## Opening a Pull Request
1. Go to the repo on GitHub
2. Click "Compare & pull request" (or Pull requests → New pull request)
3. Base: `main`  ←  Compare: `feature/your-feature-name`
4. Add a title + short description, then "Create pull request"
5. Get one teammate to review before merging

## Keeping your branch up to date
```bash
git checkout main
git pull origin main
git checkout feature/your-feature-name
git merge main
```

## Placeholders to fill in
- Replace `YOUR_USERNAME` above with the actual GitHub org/user.
