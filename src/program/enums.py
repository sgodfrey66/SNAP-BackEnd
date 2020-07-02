from enum import Enum


class EnrollmentStatus(Enum):
    AWAITING_ENTRY = 'awaiting entry'
    ENROLLED = 'enrolled'
    EXITED = 'exited'


class ProgramEligibilityStatus(Enum):
    ELIGIBLE = 'eligible'
    NOT_ELIGIBLE = 'not eligible'
