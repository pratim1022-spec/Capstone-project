from datetime import datetime

O2C_FLOW = [
    {"code": "VA11", "name": "Inquiry"},
    {"code": "VA21", "name": "Quotation"},
    {"code": "VA01", "name": "Sales Order"},
    {"code": "VL01N", "name": "Delivery"},
    {"code": "VL02N", "name": "Post Goods Issue"},
    {"code": "VF01", "name": "Billing"},
    {"code": "F-28", "name": "Payment"}
]

STEP_EXPLANATION = {
    "VA11": "Customer inquiry creation",
    "VA21": "Quotation created from inquiry",
    "VA01": "Sales order created",
    "VL01N": "Delivery document created",
    "VL02N": "Goods issued from warehouse",
    "VF01": "Invoice generated",
    "F-28": "Customer payment processed"
}


def get_all_steps():
    return O2C_FLOW


def get_step_details(code):
    return {
        "code": code,
        "description": STEP_EXPLANATION.get(code, "Not found"),
        "timestamp": str(datetime.now())
    }


def simulate_order_flow(customer, material, qty):
    return {
        "customer": customer,
        "material": material,
        "quantity": qty,
        "status": "Order Processed",
        "flow": [step["name"] for step in O2C_FLOW]
    }
