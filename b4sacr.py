"""
Basel IV Standardised Approach to Credit Risk.py (b4sacr.py)
----------------
This package encapsulates the Basel Committee on Bank Supervision's finalisation of Basel III 
for standardised credit risk.
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
- classes for each of the exposure classes

See Basel4.py script for overarching logic for Basel 4 packages. 
"""

"""
Version 0.1 2017-12-12 Written introduction and start on sacr
Version 0.2 2018-01-01 
"""

"""
Insert dependencies here
"""
import pandas as pd

class sacr():

    """
    
    """

    def __init__(self,bookingentity,dealid,ctptyid,exposureclass,extcrrating,oecdeca):
        self.bookingentity = bookingentity
        self.dealid = dealid
        self.ctptyid = ctptyid
        self.exposureclass = exposureclass
        self.extcrrating = extcrrating
        self.oecdeca = oecdeca

    "TO INSERT LOOKUPS BASED ON BOOKING ENTITY AND CTPYID ONCE BASEL4.PY BUILT TO GET VALUES LIKE SUPERVISOR____"

    def RW(self,exposureclass,extcrrating,oecdeca,ctptyid):

        if exposureclass == "Sovereign":

            """Note for where national regulators set lower RW
            See paragraph BCBS d424 A.8. If national regulator allows lower risk-weight
            for exposures denominated in local currency with corresponding liabilities 
            then a lower risk-weight may apply for sovereigns.
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
                self.rwtreatment == "SACR-Sovereign-0%Multinationals"
                return 0.00

            elif supervisoroecdused is True:
                
                """For national regulators who recognise ECA scores.
                See paragraph A.9.
                """
                self.rwtreatment == "SACR-Sovereign-OECD{oecdeca}"
                if oecdeca in [0,1]:
                    return 0.00
                elif oecdeca == 2:
                    return 0.20
                elif oecdeca == 3:
                    return 0.50
                elif oecdeca in [4,5,6]:
                    return 1.00
                elif oecdeca == 7:
                    return 1.50
                else:
                    return None
            
            else:
                """The standard risk-weight table 
                See paragraph A.7. Exposures to sovereigns and their central banks will be risk-weighted as follows,
                after taking into account the preceding logic.
                Below logic is based on S&P credit rating mapping. Input will need to be mapped to S&P equivalent.
                Unchanged since Basel II framework (June 2006).
                """
                self.rwtreatment == "SACR-Sovereign-ExtCR{extcrrating}"
                if extcrrating in ["AAA","AA+","AA","AA-"]:
                    return 0.00
                elif extcrrating in ["A+","A","A-"]:
                    return 0.20
                elif extcrrating in ["BBB+","BBB","BBB-"]:
                    return 0.50
                elif extcrrating in ["BB+","BB","BB-","B+","B","B-"]:
                    return 1.00
                elif extcrrating in ["CCC","CC","C"]:
                    return 1.50
                elif extcrrating == "D":
                    return 0.00
                elif extcrrating == "NR"#Not rated
                    return 1.00
                else:
                    return None
        
        if exposureclass == "Public Sector":

            """Exposures to domestic public sector entities 
            Risk weighted according to either of the following two options dictated by the national supervisor
            """

            if supervisorsacrpseoption == 1:
                """Based on external credit rating of 
                
                """
                if extcrrating in ["AAA","AA+","AA","AA-"]:
                    return 0.00
                elif extcrrating in ["A+","A","A-"]:
                    return 0.20
                elif extcrrating in ["BBB+","BBB","BBB-"]:
                    return 0.50
                elif extcrrating in ["BB+","BB","BB-","B+","B","B-"]:
                    return 1.00
                elif extcrrating in ["CCC","CC","C"]:
                    return 1.50
                elif extcrrating == "D":
                    return 0.00
                elif extcrrating == "NR"#Not rated
                    return 1.00
                else:
                    return None