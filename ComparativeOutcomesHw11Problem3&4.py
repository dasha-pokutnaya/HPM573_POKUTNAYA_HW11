import HW10.ParameterClassesHw11 as P
import HW10.MarkovModelHw11 as MarkovCls
import HW10.SupportMarkovModelHw11 as SupportMarkov

# simulate no therapy
# create a cohort
cohort_none = MarkovCls.Cohort(
      id=0,
      therapy=P.Therapies.NONE)

# simulate cohort
simOutputs_none = cohort_none.simulate()

# simulate anticoagulation therapy
cohort_anticoag = MarkovCls.Cohort(id=1, therapy=P.Therapies.ANTICOAG)
simOutputs_anticoag = cohort_anticoag.simulate()

SupportMarkov.draw_survival_curves_and_histograms(simOutputs_none, simOutputs_anticoag)

SupportMarkov.print_outcomes(simOutputs_none, "No therapy")
SupportMarkov.print_outcomes(simOutputs_anticoag, "Anticoagulation therapy")

SupportMarkov.print_comparative_outcomes(simOutputs_none, simOutputs_anticoag)

SupportMarkov.report_CEA_CBA(simOutputs_none, simOutputs_anticoag)

#No therapy
#  Estimate of mean and 95% CI of survival time: 0.15 (0.15, 0.16)
#  Estimate of mean and 95% CI of time to stroke: 1.38 (1.30, 1.45)
#  Estimate of discounted cost and 95% CI: 143.58 (135.78, 151.37)
#  Estimate of discounted utility and 95% CI: 0.14 (0.14, 0.15)

#Anticoagulation theraoy
#  Estimate of mean and 95% CI of survival time: 0.18 (0.17, 0.19)
#  Estimate of mean and 95% CI of time to stroke: 1.29 (1.22, 1.36)
#  Estimate of discounted cost and 95% CI: 495.66 (473.68, 517.64)
#  Estimate of discounted utility and 95% CI: 0.17 (0.16, 0.17)

# Average increase in survival time and 95% CI: 0.02 (0.01, 0.04)
# Average increase in discounted cost and 95% CI: $352 ($311, $394)
# Average increase in discounted utility and 95% CI: 0.02 (0.01, 0.04)