from odoo import fields, models, api
from odoo.exceptions import ValidationError


class Lead(models.Model):
    _inherit = "crm.lead"
    _description = 'Sales Team'

    info_1 = fields.Char(string = "Info 1:")
    info_2 = fields.Char(string = "Info 2:")
    info_3 = fields.Float(string = "Info 3:")

    def _handle_partner_assignment(self, force_partner_id=False, create_missing=True):

        for lead in self:
            if force_partner_id:
                lead.partner_id = force_partner_id
                print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,",force_partner_id)
                get_partner_id = self.env['res.partner'].search([('id','=',force_partner_id)])
                get_partner_id.write({
                    'info_1':self.info_1,
                    'info_2':self.info_2,
                    'info_3':self.info_3,
                })
            if not lead.partner_id and create_missing:
                print("...............................",lead)
                partner = lead._create_customer()
                lead.partner_id = partner.id

    def _prepare_customer_values(self, partner_name, is_company=False, parent_id=False):
        partner_data = super(Lead, self)._prepare_customer_values(partner_name, is_company=False, parent_id=False)
        partner_data['info_1'] = self.info_1
        partner_data['info_2'] = self.info_2
        partner_data['info_3'] = self.info_3
        return partner_data

    @api.onchange('stage_id')
    def validate_stage(self):
        for rec in self:
            if rec.stage_id == self.env.ref("crm_task.stage_lead5"):
                raise ValidationError("You cannot modify lost from Status Bar")

    def action_set_lost(self, **additional_values):
        res = super(Lead, self).action_set_lost()
        # print("----------------------------------",self.stage_id)
        self.stage_id = self.env.ref("crm_task.stage_lead5")
        self.action_unarchive()
        return res