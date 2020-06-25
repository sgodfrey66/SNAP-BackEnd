from .factories import AgencyWithProgramsFactory
from .rules import can_read_program


def test_can_read_program():
    agency = AgencyWithProgramsFactory(users=1, num_programs=1)
    user = agency.user_profiles.first().user

    # user and program are in the same agency - grant access
    assert can_read_program(user, agency.programs.first())


def test_can_read_program_fails():
    agency1 = AgencyWithProgramsFactory(users=1, num_programs=1)
    agency2 = AgencyWithProgramsFactory(num_programs=1)

    user = agency1.user_profiles.first().user

    # user and program are in different agencies - deny access
    assert can_read_program(user, agency2.programs.first()) is False
