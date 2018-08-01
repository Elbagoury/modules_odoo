# -*- coding: utf-8 -*-

from openerp import models, fields


class Formation(models.Model):
    _name = "formation.formation"

    name = fields.Char(string="Nom")
    type_formation = fields.Selection([
        ('convention', 'Convention'),
        ('contract', 'Contrat')],
        string='Type de document')
    objet_formation = fields.Char(string="Object Convention / Contrat")
    objectifs_pedagogiques = fields.Html(string="Objectifs pédagogiques")
    contenu = fields.Html(string="Contenu")
    methodes_moyens_pedagogique = fields.Html(string="Méthodes et moyens pédagogiques")
    modalite_validation = fields.Html(string="Modalités de suivi et validation des acquis")
    date_et_duree = fields.Html(string="Date et durée")
    date_debut = fields.Date(string="Date de début")
    date_fin = fields.Date(string="Date de fin")
    lieu = fields.Char(string="Lieu")
    niveau_connaissances = fields.Html(string="Niveau de connaissances préalables nécessaire")
    organisation = fields.Char(string="Organisation de l’action de formation")
    formateurs = fields.Many2many('res.partner', string="formateurs")
    effectifs = fields.Many2many(comodel_name='res.partner',
                                 relation='effectifs',
                                 column1='effectif_formation',
                                 column2='effectif_res_partner')
    modalites_reglement = fields.Html(string="Modalités de règlement")
    date_contrat = fields.Date("Date signature du contrat")
    cotractant = fields.Many2one('res.partner', 'Cotractant')

    urb_logo = fields.Binary("Logo", attachment=True)
    urb_tampon = fields.Binary("Tampon", attachment=True)
