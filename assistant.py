def get_o2c_steps():
    return [
        "Inquiry (VA11)",
        "Quotation (VA21)",
        "Sales Order (VA01)",
        "Delivery (VL01N)",
        "Post Goods Issue (VL02N)",
        "Billing (VF01)",
        "Payment (F-28)"
    ]


def explain_step(step):
    explanations = {
        "VA01": "Creates Sales Order",
        "VL01N": "Creates Delivery Document",
        "VF01": "Creates Invoice",
        "F-28": "Customer Payment Entry"
    }
    return explanations.get(step, "Step not found")
