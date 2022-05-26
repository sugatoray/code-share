# 🔥 USE tqdm.auto to aumatically switch b/w
#    notebook, asyncio and otherwise.
# 💡 Source: https://tqdm.github.io/docs/shortcuts/
# -------------------------------------------------
# 👉 Method resolution order:
#
#   ✅ tqdm.autonotebook without import warnings
#   ✅ tqdm.asyncio on Python3.6+
#   ✅ tqdm.std base class

import time
from tqdm.auto import tqdm

for _ in tqdm(range(5), desc="Loop..."):
  time.sleep(1)
# Loop...: 100%|█████████████| 5/5 [00:05<00:00,  1.00s/it]
