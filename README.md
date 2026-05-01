## Overview

This repository contains two major types of resources:

1. **Model training code**
   - Located in the `DeepBBB_training_code/` folder.
   - This folder contains scripts for model training and related data-processing procedures.

2. **Model usage examples and screening workflows**
   - The repository provides usage examples for three DeepBBB model variants:

     - `DeepBBB_V1_BC`: a binary classification model for BBB permeability prediction.  
       The corresponding usage workflow is provided in:
       ```text
       BBB_binary_pred_usage_database/
       ```

     - `DeepBBB_V2_BC`: a binary classification model with an adjusted data-ratio strategy.  
       The corresponding usage workflow is provided in:
       ```text
       BBB_binary_pred_usage_database_ratio/
       ```

     - `DeepBBB_V1_RG`: a regression model for quantitative BBB permeability prediction.  
       The corresponding usage workflow is provided in:
       ```text
       BBB_linear_pred_usage_database/
       ```

The current examples mainly demonstrate how to construct a potential BBB-permeable molecular library from a compound collection. The same workflows can also be adapted for screening BBB-permeable molecules from user-provided compound libraries or candidate compound sets.
