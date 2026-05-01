# DeepBBB

DeepBBB is a deep learning-based framework for blood-brain barrier (BBB) permeability prediction and BBB-oriented molecular library construction. The repository provides training code, pretrained/usage examples, and screening workflows for binary BBB classification and quantitative BBB permeability prediction.

## Overview

This repository contains three major types of resources:

1. **Model training code**
   - Located in the `DeepBBB_training_code/` folder.
   - This folder contains scripts for model training and related data-processing procedures.

2. **Prediction and screening workflows**
   - Located in the following folders:
     - `BBB_binary_pred_usage_database/`
     - `BBB_binary_pred_usage_database_ratio/`
     - `BBB_linear_pred_usage_database/`
   - These folders contain model usage examples, prediction scripts, and screening workflows for identifying potential BBB-permeable compounds.

3. **DeepBBB model variants**
   - `DeepBBB_V1_BC`: binary classification model for BBB permeability prediction.
   - `DeepBBB_V2_BC`: binary classification model with an adjusted data ratio strategy.
   - `DeepBBB_V1_RG`: regression model for quantitative BBB permeability prediction.

The usage and training procedures of `DeepBBB_V1_BC`, `DeepBBB_V2_BC`, and `DeepBBB_V1_RG` can be adapted from the workflows provided in:

```text
BBB_binary_pred_usage_database/
BBB_binary_pred_usage_database_ratio/
BBB_linear_pred_usage_database/
