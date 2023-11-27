def time_to_text(minute):
    heures = minute // 60
    minutes = minute - (heures * 60)
    print("{} heures et {} minutes".format(heures, minute))

time_to_text(112)
time_to_text(6949)
time_to_text(40)
time_to_text(2)