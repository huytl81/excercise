# -*- coding: utf-8 -*-

from . import controllers
from . import models
from . import wizards

def _update_company_email(env):
    company = env.ref('base.main_company')
    if company:
        company.email = 'talehuy81@gmail.com'