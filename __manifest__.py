{
	'name'      : 'Number Line Report',
	'version'   : '1.0.0',
	'category'  : 'Report',
	'summary'   : 'Add Number Line in Report',
	'description': """
		This module adds the number line in reports :
		- Sale Order 
		- Purchase Order
		- Picking Type
	""",
	'author'    : 'Panca Putra Pakpahan',
	'website'   :'https://solusiaglis.co.id',
	'license'   : "LGPL-3",
	'depends'   : ['base'],
	'data'      : [
		'reports/purchase_order_templates.xml',  
		'reports/sale_report_templates.xml', 
		'reports/report_deliveryslip.xml', 
		'reports/report_stockpicking_operations.xml', 
		],
	'demo'      : [],
	'test'      : [],
	'installable'   : True,
	'auto_install'  : False,
	'application'   : False,
}
