import numpy as np

SEED = 42
NUM_HIDDEN_UNITS = 128

EPS = np.finfo(np.float32).eps.item()

MAX_EPISODES = 10000
MAX_STEPS_PER_EPISIDES = 1000

REWARD_TRESHOLD = 195
RUNNING_REWARD = 0

GAMMA = 0.99