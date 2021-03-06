import epics
import time
import numpy as np

# configuration
time_sleep = 2
phase_booster_ring_start = 0
phase_booster_ring_end = 2.1
step_size = 0.01
n_steps = (phase_booster_ring_end - phase_booster_ring_start) / step_size + 1
range_phase_booster_ring = np.linspace(0, 2.1, 211)

print("Phase acceptance scan from %f to %f with step size of %f (%d steps) will approximatly take %.1fs" % (phase_booster_ring_start, phase_booster_ring_end, step_size, n_steps, n_steps * time_sleep + 60))

input("Press any key to set initial phase value: ")

pv_phase_booster_ring_set = epics.PV('PAHB:sDelay')
pv_phase_booster_ring_rdbk = epics.PV('PAHB:pDelay ')

pv_injection_efficeny_1 = epics.PV('TOPUP1T5G:rdEffBoostRraw')
pv_injection_efficeny_2 = epics.PV('TOPUP2T5G:rdEffBoostRraw')

while pv_phase_booster_ring_rdbk < 0.2:
    print("pv_phase_booster_ring_rdbk: %f" % pv_phase_booster_ring_rdbk.get())
    time_sleep(1)

print("Setting Phase to initial value %f" % range_phase_booster_ring[-1])
pv_phase_booster_ring_set.put(range_phase_booster_ring[0])

input("Press Enter to start phase acceptance scan: ")

# for phase_booster_ring in range_phase_booster_ring:
#     print(pv_phase_booster_ring.get())
#     print(pv_injection_efficeny_1.get())
#     print(pv_injection_efficeny_2.get())
#     time.sleep(time_sleep)
