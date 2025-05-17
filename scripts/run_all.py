print("\n>>> STEP 0: Generate Data")
import scripts.generate_dataset

print("\n>>> STEP 1: Verify Data")
import scripts.verify_data

print("\n>>> STEP 2: Balanced Scoring Model")
import scripts.score_balance_weighted

print("\n>>> STEP 3: Expansion Focus")
import scripts.score_expansion_weighted

print("\n>>> STEP 4: Retention Focus")
import scripts.score_retention_weighted

print("\n>>> STEP 5: Revenue Focus")
import scripts.score_revenue_weighted

print("\n>>> STEP 6: Strategy Focus")
import scripts.score_strategy_weighted

print("\n>>> STEP 7: Export Final Comparison")
import scripts.score_summary

print("\n>>> All steps completed.")