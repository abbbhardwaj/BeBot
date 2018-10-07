
def pto():
    title = "PERSONAL TIME OFF POLICY Standard Operating procedure"
    objective = "the policy is to provide all members with the opportunity to take Personal Time off or PTO from " \
                "the workplace in order to meet their personal needs."
    summary1 = "Number one, All members are entitled for 1.25 day paid PTO and this continues till the 60th month.  "
    summary2 = "Subsequent to the sixtieth  month that is 5 years, the entitlement increases to 1.50 days of paid PTO " \
               "in a month and continues accordingly."
    summary3 = "Number two, there is a loss of pay for 10 or more working days during any " \
               "particular month then the members will not be eligible for PTO entitlement."
    summary4 = "Number three, Member can avail maximum 10 working days leave on reporting supervisor's approval."
    summary5 = "If a member needs to take off for more than 10 working days then the same needs to be approved by Department Head. " \
               "Else, it will be treated as unauthorized absence, liable for disciplinary action."
    summary6 = "More details related to Compensatory offs, gazetted holidays etc. are listed in Policy pdf document"
    summary7 = "We highly recommend you choose email request to get all details."
    list_doc = [title, objective, summary1, summary2, summary3, summary4, summary5, summary6, summary7]
    return list_doc


def answers(question):
    if "how many" in question or "number" in question or "many" in question:
        ans = "Member can avail maximum 10 working days leave on reporting supervisor's approval."
    return ans