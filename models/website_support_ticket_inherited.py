from openerp import api, fields, models,_
import datetime
from datetime import datetime



class Enquiries_inherited(models.Model):
	_inherit = ["website.support.ticket"]



	name = fields.Char(string="Name",required=True)
	country = fields.Many2one('res.country',string="Country")
	message = fields.Text(string="Message",required=True)
	ticket_no = fields.Char(string="Enquiry No.",required=True, Index= True, default=lambda self:('New'), readonly=True)
	status = fields.Selection([('draft','Draft'),('followup','Followup'),('add-application','Add-Application')],default="draft")
	campus_name = fields.Many2one('school.school',string="Campus-Name")
	address = fields.Char(string="Address")
	enquiry_date = fields.Date(stirng="Enquiry-Date",readonly=True,default=fields.Datetime.now())




	@api.model
	def create(self, vals):
		if vals.get('ticket_no', _('New')) == _('New'):
			vals['ticket_no'] = self.env['ir.sequence'].next_by_code('enquiry.view.id') or _('New')
			result = super(Enquiries_inherited, self).create(vals)

			return result
	

	@api.multi
	def enquiry_status(self):
		self.write({"status":"followup"})
     
	@api.multi
	def application_status(self):
		self.write({"status":"add-application"})


	