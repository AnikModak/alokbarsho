# SIH Lunar Image Registration

**Problem Statement ID:** 26166
**Title:** Multi-modal, Sun angle and scale invariant image correspondence using Chandrayaan-2 optical images (OHRC, TMC and IIRS)
**Organization:** Indian Space Research Organisation (ISRO), Department of Space
**Theme:** Space Technology | **Category:** Software

## Overview

A generic, illumination- and scale-invariant registration pipeline that aligns
Chandrayaan-2 multi-sensor lunar imagery (OHRC, TMC-2, IIRS) to LRO NAC reference
imagery, with sub-pixel accuracy — without requiring labeled training data.

Standard feature matchers (SIFT, ORB) fail on lunar imagery because they key off
intensity gradients, which shift unpredictably with sun angle. This pipeline uses
**phase congruency** based features, which are illumination-invariant by
construction, combined with RANSAC-filtered matching and homography estimation.

## Team

| Name | Role |
|---|---|
| Anik | Project Architect / Phase Congruency & Matching |
| — | Phase Congruency & Matching |
| — | Data Pipeline (OHRC/TMC/IIRS + LRO NAC ingestion) |
| — | Evaluation Harness (RMSE, inlier ratio, visualization) |
| — | UI / Demo |
| — | Documentation, Testing, Integration |

## Repository Structure

```
SIH_Lunar_Image_Registration/
├── dataset/
│   ├── raw/              # original OHRC/TMC/IIRS/LRO tiles (gitignored)
│   └── processed/        # downsampled/normalized versions
├── docs/                 # write-ups, design notes
├── papers/                # RIFT, HOPC, phase congruency references
├── images/                # sample results for README/demo
├── notebooks/             # exploratory Jupyter work
├── src/
│   ├── preprocessing.py
│   ├── phase_congruency.py
│   ├── feature_detection.py
│   ├── feature_matching.py
│   ├── ransac.py
│   ├── homography.py
│   ├── registration.py
│   ├── evaluation.py
│   └── utils.py
├── tests/                 # unit tests
├── app.py                 # entry point / web app
├── requirements.txt
└── presentation/          # slides, demo video
```

## Setup

```bash
git clone https://github.com/YOUR_USERNAME/SIH_Lunar_Image_Registration.git
cd SIH_Lunar_Image_Registration
python3 -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

```bash
python app.py
```

## Method

1. **Preprocessing** — resolution normalization, contrast handling
2. **Phase congruency feature extraction** — illumination-invariant keypoints
3. **Feature matching** — descriptor matching across source/reference
4. **RANSAC + homography** — outlier rejection, geometric transform estimation
5. **Sub-pixel refinement** — cross-correlation refinement around matches
6. **Evaluation** — RMSE, inlier count, inlier ratio

## Datasets

- Chandrayaan-2 OHRC/TMC-2/IIRS: https://chmapbrowse.issdc.gov.in/
- LRO NAC reference imagery: https://lroc.im-ldi.com/

## Team Workflow

See `docs/git-workflow.md` for the branching and PR process.

## License

TBD
