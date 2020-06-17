from enum import Enum


class EnrollmentStatus(Enum):
    AWAITING_ENTRY = 'awaiting entry'
    ENROLLED = 'enrolled'
    EXITED = 'exited'


class EligibilityStatus(Enum):
    ELIGIBLE = 'eligible'
    NOT_ELIGIBLE = 'not eligible'
