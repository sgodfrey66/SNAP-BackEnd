import rules


@rules.predicate
def can_read_program(user, program):
    import logging
    logging.getLogger('app').warning('ccc %s %s' % (user, program))
    return user.profile.agency.agencyprogramconfig_set.filter(program=program).exists()


rules.add_rule('can_read_program', can_read_program)
