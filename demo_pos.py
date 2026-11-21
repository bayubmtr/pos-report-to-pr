"""Small POS application fixture for the closeout receipt bug."""

import json
from typing import Optional


def close_register(shift: dict, templates: dict[str, str]) -> dict:
    """Close a shift and return the receipt payload for the print queue."""
    shift["status"] = "closed"
    receipt: Optional[str] = None
    template = templates.get("CASHIER_CLOSE")
    if template:
        receipt = template.format(shift_id=shift["id"], sales=shift["sales"])

    return {"status": shift["status"], "receipt": receipt}


if __name__ == "__main__":
    shift = {"id": "DEMO-104", "status": "open", "sales": 3}
    templates = {"SALE": "Sale receipt"}
    print(json.dumps(close_register(shift, templates)))
