############Part one#######################################################
#Annual mortality due to all causes is 18/1,000
#Annual death rate for stroke is 36.2/100,000

# 18 * 100 - 36.2/100,000
# 1,800 - 36.2 = 1,768/100,000 non-stroke associated annual
# mortality
# -ln(1 - 1768/100,000) = 0.01783815812

# 36.2 / 100,000 stroke associated annual mortality
# -ln(1 - 36.2/100,000) = 0.00036206553

############Part two#######################################################
# -ln(1 - 15/1,000) = 0.01511363781

############Part three#####################################################
#Well -> Stroke
#0.01511363781 * .9 = 0.01359

#Well -> Stroke Death
#0.01511363781 * .1 = 0.0015

############Part four######################################################
# -ln(1 - (15/(1-.17))/1000))= 0.0182 / 5 = 0.00364

############Part five######################################################
#Post stroke -> Stroke
#0.1359 / .8 + 0.1359 = 0.305775

#Post stroke -> Stroke Death
#0.0015 / .8 + 0.0015 = 0.003375

############Part six#######################################################
#52