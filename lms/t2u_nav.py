import frappe


def update_website_context(context):
	if frappe.session.user == "Guest":
		return

	kyc_status = frappe.db.get_value(
		"T2U KYC Verification",
		{"user": frappe.session.user},
		"kyc_status",
	)

	t2u_nav = []

	if kyc_status != "Verified":
		t2u_nav.append({"label": "KYC", "url": "/kyc"})

	t2u_nav.append({"label": "Earnings", "url": "/earnings"})

	context["t2u_nav"] = t2u_nav
