
POP_SIZE = 2000     # cohort population size
SIM_LENGTH = 50   # length of simulation (years)
ALPHA = 0.05        # significance level for calculating confidence intervals
DELTA_T = 15        # years (length of time step, how frequently you look at the patient)
DISCOUNT = 0.03

# transition matrix
# Without treatment

TRANS_MATRIX = [
    [0.96,  0.0136,     0,          0.00151,     0.0177],   # Well
    [0,     0.0,        52,         0.00056,     0.0177],   # Stroke
    [0,     0.0121,     0.96,       0.00302,     0.0177],   # Post-Stroke
    [0.0,   0.0,        0.0,        1.0,            0.0],   # Dead
    [0.0,   0.0,         0.0,        0.0,           1.0],
    ]

# With treatment
THERAPY_TRANS_MATRIX = [
    [0.96,  0.0136,     0,          0.00151,     0.0177],   # Well
    [0,     0.0,        52,         0.00056,     0.0177],   # Stroke
    [0,     0.0151,     0.961,       0.0052,     0.0187],   # Post-Stroke
    [0.0,   0.0,        0.0,        1.0,            0.0],   # Stroke-Death
    [0.0,   0.0,         0.0,        0.0,           1.0],   # Death
    ]

# anticoagulation relative risk in reducing stroke incidence and stroke death while in “Post-Stroke”
RR_STROKE = 0.65
# anticoagulation relative risk in increasing mortality due to bleeding is 1.05.
RR_BLEEDING = 1.05

HEALTH_UTILITY = [
    1,  # well
    0.2,  # stroke ONLY WHEN THE CYCLE LENGTH IS 1 YEAR
    0.9,  # post-stroke
    0  # dead
]

HEALTH_COST = [
    0,
    5000,  # stroke
    200,  # post-stroke /year
    0
]

Anticoag_COST = 2000

ANNUAL_ALL_CAUSE_MORT = 18 / 1000
ANNUAL_DEATH_RATE_STROKE = 36.2 / 100000
NON_STROKE = 18 * (100 - 36.2) / 100,000