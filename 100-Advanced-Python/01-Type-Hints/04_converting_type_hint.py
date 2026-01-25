from typing import List, Dict, Optional

# --- YOUR TASK ---
# 1. user_data should be a Dictionary
# 2. orders should be a List of strings
# 3. count (optional) should be an Integer or None
# 4. The function should return a List of Dictionaries
from typing import Any
def format_dashboard_results(
        user_data : dict[str , Any],
        orders : list[str],
        count :int | None  = None
    ) -> list[dict[str , Any]]:
    # Imagine some logic here that merges them
    return [{"user": user_data["name"], "order_count": len(orders)}]

