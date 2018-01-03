"""
Basel IV.py
----------------
This package encapsulates the Basel Committee on Bank Supervision's finalisation of Basel III.
The text is found at https://www.bis.org/bcbs/publ/d424.htm
This will serve as the foundation of any Basel 4 impact analysis.
-----------------
Blake Stratton

A key objective of the revisions in this document is to reduce excessive variability of risk-
weighted assets (RWAs). The revisions (i) enhance the robustness and risk sensitivity of the 
standardised approaches for credit risk and operational risk; (ii) constrain the use of 
internally-modelled approaches (particularly for low default exposures such as FIs and large
corporates); and (iii) complement the risk-weighted capital ratio with a finalised leverage 
ratio and a standardised RWA capital floor.

A comment on nomenclature: BCBS calls this package of reforms Basel III finalisation however
the industry - atleast for the time being - refers to it as Basel IV. We will refer to these
changes as Basel IV until such a time that it no longer suits.

This package is structured as:
- classes for each of the risk categories and their underlying treatments
- treatment setting logic that allocates exposures to treatments
"""

"""
Version 0.1 2017-12-12 Written introduction and start on sacr
Version 0.2 2018-01-01 
"""

"""
Insert dependencies here
"""
import pandas as pd

class sacr(self,dealid,ctptyid,exposureclass,extcrrating,oecdeca):

    """
    
    """

    def __init__(self,dealid):
        self.dealid = dealid
        self.ctptyid = ctptyid
        self.exposureclass = exposureclass

    def RW(exposureclass,extcrrating,oecdeca,ctptyid):

        if exposureclass == "Sovereign":

            """Note for where national regulators set lower RW
            See paragraph BCBS d424 A.8. If national regulator allows lower risk-weight
            for exposures denominated in local currency with corresponding liabilities 
            then a lower risk-weight may apply for sovereigns
            """

            """
            See paragraph A.10. Exposures to counterparties in this list may a 0% risk-weight.
            TO BE UPDATED WITH ACTUAL COUNTERPARTY IDs OR PASSED IN AS LIST
            """
            if ctptyid in [
                "Bank for International Settlments",
                "The International Monetary Fund",
                "The European Union",
                "The European Stability Mechanism"
            ]:
                return 0.00
            elif :
                pass
