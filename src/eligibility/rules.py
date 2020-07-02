import rules


@rules.predicate
def can_read_eligibility(user, eligibility):
    return user.profile.agency.agencyeligibilityconfig_set.filter(eligibility=eligibility).exists()


rules.add_rule('can_read_eligibility', can_read_eligibility)
