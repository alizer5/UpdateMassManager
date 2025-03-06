from odoo import models, fields


class MassManagerWizard(models.TransientModel):
    _name = 'mass.manager.wizard'
    _description = 'Mass Manager Wizard'

    new_manager_id = fields.Many2one('hr.employee', string='Manager')
    new_job_id = fields.Many2one('hr.job', string='Job')
    is_manager = fields.Boolean(string='Update Manager')
    is_job = fields.Boolean(string='Update Job', default=False)

    def action_update_manager_job(self):
        employees = self.env['hr.employee'].browse(self._context.get('active_ids', []))
        updates = {}

        if self.is_manager and self.new_manager_id:
            updates['parent_id'] = self.new_manager_id.id

        if self.is_job and self.new_job_id:
            updates['job_id'] = self.new_job_id.id

        if updates:
            employees.write(updates)
