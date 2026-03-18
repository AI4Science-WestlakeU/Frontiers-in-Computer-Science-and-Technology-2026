# Frontiers in Computer Science and Technology 2026

Course materials for *Frontiers in Computer Science and Technology* (2026).

## Repository Structure

```
slides/      Lecture slides (PDF) covering theory, key concepts, and formulas for each class
notebooks/   Interactive Jupyter Notebooks with runnable code and experiments corresponding to each lecture
```

## How to Use

- **slides/**: PDF slide decks for each lecture. Read these to follow the theoretical content taught in class.
- **notebooks/**: Hands-on notebooks paired with the slides. Each notebook contains code implementations, visualizations, and plain-language Markdown explanations. Open the corresponding notebook after reading the slides to put the concepts into practice. The Lecture 03 notebook additionally includes derivations, a model-relation map, and CPU-friendly runnable examples for major generative models.

## Contents

| Slides | Notebook | Topic |
|---|---|---|
| [01_Course Introduction.pdf](slides/01_Course%20Introduction.pdf) | — | Course Introduction |
| [02_Frontiers in deep learning_1_Maximum likelihood and Information-based objectives.pdf](slides/02_Frontiers%20in%20deep%20learning_1_Maximum%20likelihood%20and%20Information-based%20objectives.pdf) | — | Maximum Likelihood & Information-based Objectives |
| [02_Frontiers in deep learning_2_Optimization.pdf](slides/02_Frontiers%20in%20deep%20learning_2_Optimization.pdf) | [02_optimization_tutorial.ipynb](notebooks/02_optimization_tutorial.ipynb) | Deep Learning Optimization |
| [03_Frontiers in generative modeling.pdf](slides/03_Frontiers%20in%20generative%20modeling.pdf) | [03_generative_modeling_tutorial.ipynb](notebooks/03_generative_modeling_tutorial.ipynb) | Generative Modeling |

## Lecture 03 Supplementary Resources

If you want to go beyond the 2D toy examples in Lecture 03 and see how Flow Matching is used for image generation, the following external resources are especially helpful.

- [MNIST image example from conditional-flow-matching / TorchCFM](https://github.com/atong01/conditional-flow-matching/blob/main/examples/images/mnist_example.ipynb): a runnable MNIST notebook that shows an end-to-end image-generation workflow with Conditional Flow Matching. 
- [Flow Matching Guide and Code](https://arxiv.org/abs/2412.06264): a self-contained guide to the mathematical foundations, design choices, and extensions of Flow Matching. 
- [Official Flow Matching codebase](https://github.com/facebookresearch/flow_matching): the code companion to the guide above. It provides a PyTorch library and example implementations for image and text settings, which makes it a practical starting point for understanding how to use Flow Matching in real experiments.

## Getting Started (No Coding Experience Required)

If you have never written code before, follow the steps below to get everything running.

### Step 1 — Install Python via Anaconda

Anaconda is a beginner-friendly Python distribution that includes everything you need.

1. Go to [https://www.anaconda.com/download](https://www.anaconda.com/download) and download the installer for your operating system (Windows / macOS).
2. Run the installer and follow the on-screen instructions (keep all default settings).

### Step 2 — Install Visual Studio Code

VS Code is the recommended editor for viewing and running the notebooks.

1. Go to [https://code.visualstudio.com](https://code.visualstudio.com) and download the installer for your operating system.
2. Run the installer and follow the on-screen instructions.
3. Open VS Code, click the **Extensions** icon on the left sidebar (or press `Ctrl+Shift+X` / `Cmd+Shift+X`), search for **Python** and **Jupyter**, and install both extensions.

### Step 3 — Install the Required Packages

1. Open **Anaconda Prompt** (Windows) or **Terminal** (macOS).
2. Copy and paste the following command, then press Enter:

```bash
pip install torch numpy matplotlib scikit-learn
```

Wait until the installation finishes (this may take a few minutes).

### Step 4 — Open a Notebook in VS Code

1. In VS Code, go to **File → Open Folder** and select the folder where you downloaded this repository.
2. In the left file explorer, open the `notebooks/` folder and click on any `.ipynb` file.
3. VS Code will ask you to select a Python environment — choose the one provided by Anaconda.
4. To run a code cell, click the **▶ Run** button on the left side of the cell, or press **Shift + Enter**.
5. Run all cells from top to bottom in order.

> **Tip:** You do not need to understand the code to follow along. Focus on the Markdown text and the output figures — they explain what is happening in plain language.

## Reference Resources

The following videos and documentation pages are helpful if you get stuck during setup or want a visual walkthrough.

### Video Tutorials

| Video | What It Covers |
|---|---|
| [VS Code + Jupyter Notebook 安装与使用入门](https://www.youtube.com/watch?v=niWD8kxgpH0) | VS Code environment setup and running Jupyter notebooks step by step |
| [Getting Started with Jupyter Notebooks in VS Code](https://www.youtube.com/watch?v=suAkMeWJ1yE) | Official Microsoft walkthrough: installing extensions, selecting kernels, running cells |
| [Anaconda Installation Guide (Windows & macOS)](https://www.youtube.com/watch?v=MUZtVEDKXsk) | How to install Anaconda and verify your Python environment |

### Official Documentation

| Resource | Link |
|---|---|
| VS Code — Jupyter Notebooks | [https://code.visualstudio.com/docs/datascience/jupyter-notebooks](https://code.visualstudio.com/docs/datascience/jupyter-notebooks) |
| Anaconda Getting Started | [https://docs.anaconda.com/anaconda/getting-started/](https://docs.anaconda.com/anaconda/getting-started/) |
| PyTorch Installation Guide | [https://pytorch.org/get-started/locally/](https://pytorch.org/get-started/locally/) |
