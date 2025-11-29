from pybirdai.models.bird_data_model import *
from pybirdai.process_steps.pybird.orchestration import Orchestration
from pybirdai.process_steps.pybird.csv_converter import CSVConverter
from datetime import datetime
from pybirdai.annotations.decorators import lineage, track_table_init

class F_04_01_REF_FINREP_3_0_Base:
	def CRRYNG_AMNT() -> int:
		pass
	def ACCNTNG_CLSSFCTN() -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		pass
	def HLD_SL_INDCTR() -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		pass
	def SBJCT_IMPRMNT_INDCTR() -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		pass
	def INSTTTNL_SCTR() -> str:
		''' return string from INSTTTNL_SCTR enumeration '''
		pass
	def MLTLTRL_DVLPMNT_BNK_INDCTR() -> str:
		''' return string from MLTLTRL_DVLPMNT_BNK_INDCTR enumeration '''
		pass
	def PRTY_RL_TYP() -> str:
		''' return string from ENTTY_RL_TYP enumeration '''
		pass
	def MN_DBTR_INDCTR() -> str:
		''' return string from MN_DBTR_INDCTR enumeration '''
		pass
	def INSTRMNT_TYP_PRDCT() -> str:
		''' return string from INSTRMNT_TYP_PRDCT enumeration '''
		pass
	def NGTBL_SCRTY_INDCTR() -> str:
		''' return string from NGTBL_SCRTY enumeration '''
		pass

class Advances_that_are_not_loans(F_04_01_REF_FINREP_3_0_Base):
	pass
	INSTRMNT = None # INSTRMNT
	@lineage(dependencies={"INSTRMNT.INSTRMNT_TYP_PRDCT"})
	def INSTRMNT_TYP_PRDCT(self):
		return self.INSTRMNT.INSTRMNT_TYP_PRDCT
	INSTRMNT_ENTTY_RL_ASSGNMNT = None # INSTRMNT_ENTTY_RL_ASSGNMNT
	def MN_DBTR_INDCTR(self):
		# return 1 for main debtor
		return '1'
	@lineage(dependencies={"INSTRMNT_ENTTY_RL_ASSGNMNT.PRTY_RL_TYP"})
	def PRTY_RL_TYP(self):
		return self.INSTRMNT_ENTTY_RL_ASSGNMNT.PRTY_RL_TYP
	INSTRMNT_RL = None # INSTRMNT_RL
	@lineage(dependencies={"INSTRMNT_RL.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self):
		return self.INSTRMNT_RL.ACCNTNG_CLSSFCTN
	@lineage(dependencies={"INSTRMNT_RL.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self):
		return self.INSTRMNT_RL.CRRYNG_AMNT
	@lineage(dependencies={"INSTRMNT_RL.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self):
		return self.INSTRMNT_RL.HLD_SL_INDCTR
	@lineage(dependencies={"INSTRMNT_RL.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self):
		return self.INSTRMNT_RL.SBJCT_IMPRMNT_INDCTR
	PRTY = None # PRTY
	@lineage(dependencies={"PRTY.INSTTTNL_SCTR"})
	def INSTTTNL_SCTR(self):
		return self.PRTY.INSTTTNL_SCTR
	@lineage(dependencies={"PRTY.MLTLTRL_DVLPMNT_BNK_INDCTR"})
	def MLTLTRL_DVLPMNT_BNK_INDCTR(self):
		return self.PRTY.MLTLTRL_DVLPMNT_BNK_INDCTR
	def NGTBL_SCRTY_INDCTR(self):
		''' return string from NGTBL_SCRTY enumeration of 2 for non-negotiable '''
		return '2'

class Credit_card_debt(F_04_01_REF_FINREP_3_0_Base):
	pass
	INSTRMNT = None # INSTRMNT
	@lineage(dependencies={"INSTRMNT.INSTRMNT_TYP_PRDCT"})
	def INSTRMNT_TYP_PRDCT(self):
		return self.INSTRMNT.INSTRMNT_TYP_PRDCT
	INSTRMNT_ENTTY_RL_ASSGNMNT = None # INSTRMNT_ENTTY_RL_ASSGNMNT
	@lineage(dependencies={"INSTRMNT_ENTTY_RL_ASSGNMNT.MN_DBTR_INDCTR"})
	def MN_DBTR_INDCTR(self):
		# return 1 for main debtor
		return '1'
	@lineage(dependencies={"INSTRMNT_ENTTY_RL_ASSGNMNT.PRTY_RL_TYP"})
	def PRTY_RL_TYP(self):
		return self.INSTRMNT_ENTTY_RL_ASSGNMNT.PRTY_RL_TYP
	INSTRMNT_RL = None # INSTRMNT_RL
	@lineage(dependencies={"INSTRMNT_RL.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self):
		return self.INSTRMNT_RL.ACCNTNG_CLSSFCTN
	@lineage(dependencies={"INSTRMNT_RL.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self):
		return self.INSTRMNT_RL.CRRYNG_AMNT
	@lineage(dependencies={"INSTRMNT_RL.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self):
		return self.INSTRMNT_RL.HLD_SL_INDCTR
	@lineage(dependencies={"INSTRMNT_RL.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self):
		return self.INSTRMNT_RL.SBJCT_IMPRMNT_INDCTR
	PRTY = None # PRTY
	@lineage(dependencies={"PRTY.INSTTTNL_SCTR"})
	def INSTTTNL_SCTR(self):
		return self.PRTY.INSTTTNL_SCTR
	@lineage(dependencies={"PRTY.MLTLTRL_DVLPMNT_BNK_INDCTR"})
	def MLTLTRL_DVLPMNT_BNK_INDCTR(self):
		return self.PRTY.MLTLTRL_DVLPMNT_BNK_INDCTR
	def NGTBL_SCRTY_INDCTR(self):
		''' return string from NGTBL_SCRTY enumeration of 2 for non-negotiable '''
		return '2'

class Finance_leases(F_04_01_REF_FINREP_3_0_Base):
	pass
	INSTRMNT = None # INSTRMNT
	@lineage(dependencies={"INSTRMNT.INSTRMNT_TYP_PRDCT"})
	def INSTRMNT_TYP_PRDCT(self):
		return self.INSTRMNT.INSTRMNT_TYP_PRDCT
	INSTRMNT_ENTTY_RL_ASSGNMNT = None # INSTRMNT_ENTTY_RL_ASSGNMNT
	@lineage(dependencies={"INSTRMNT_ENTTY_RL_ASSGNMNT.MN_DBTR_INDCTR"})
	def MN_DBTR_INDCTR(self):
		return self.INSTRMNT_ENTTY_RL_ASSGNMNT.MN_DBTR_INDCTR
	@lineage(dependencies={"INSTRMNT_ENTTY_RL_ASSGNMNT.PRTY_RL_TYP"})
	def PRTY_RL_TYP(self):
		return self.INSTRMNT_ENTTY_RL_ASSGNMNT.PRTY_RL_TYP
	INSTRMNT_RL = None # INSTRMNT_RL
	@lineage(dependencies={"INSTRMNT_RL.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self):
		return self.INSTRMNT_RL.ACCNTNG_CLSSFCTN
	@lineage(dependencies={"INSTRMNT_RL.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self):
		return self.INSTRMNT_RL.CRRYNG_AMNT
	@lineage(dependencies={"INSTRMNT_RL.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self):
		return self.INSTRMNT_RL.HLD_SL_INDCTR
	@lineage(dependencies={"INSTRMNT_RL.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self):
		return self.INSTRMNT_RL.SBJCT_IMPRMNT_INDCTR
	PRTY = None # PRTY
	@lineage(dependencies={"PRTY.INSTTTNL_SCTR"})
	def INSTTTNL_SCTR(self):
		return self.PRTY.INSTTTNL_SCTR
	@lineage(dependencies={"PRTY.MLTLTRL_DVLPMNT_BNK_INDCTR"})
	def MLTLTRL_DVLPMNT_BNK_INDCTR(self):
		return self.PRTY.MLTLTRL_DVLPMNT_BNK_INDCTR
	def NGTBL_SCRTY_INDCTR(self):
		''' return string from NGTBL_SCRTY enumeration of 2 for non-negotiable '''
		return '2'

class Other_loans(F_04_01_REF_FINREP_3_0_Base):
	pass
	INSTRMNT = None # INSTRMNT
	@lineage(dependencies={"INSTRMNT.INSTRMNT_TYP_PRDCT"})
	def INSTRMNT_TYP_PRDCT(self):
		return self.INSTRMNT.INSTRMNT_TYP_PRDCT
	INSTRMNT_ENTTY_RL_ASSGNMNT = None # INSTRMNT_ENTTY_RL_ASSGNMNT
	@lineage(dependencies={"INSTRMNT_ENTTY_RL_ASSGNMNT.MN_DBTR_INDCTR"})
	def MN_DBTR_INDCTR(self):
		return self.INSTRMNT_ENTTY_RL_ASSGNMNT.MN_DBTR_INDCTR
	@lineage(dependencies={"INSTRMNT_ENTTY_RL_ASSGNMNT.PRTY_RL_TYP"})
	def PRTY_RL_TYP(self):
		return self.INSTRMNT_ENTTY_RL_ASSGNMNT.PRTY_RL_TYP
	INSTRMNT_RL = None # INSTRMNT_RL
	@lineage(dependencies={"INSTRMNT_RL.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self):
		return self.INSTRMNT_RL.ACCNTNG_CLSSFCTN
	@lineage(dependencies={"INSTRMNT_RL.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self):
		return self.INSTRMNT_RL.CRRYNG_AMNT
	@lineage(dependencies={"INSTRMNT_RL.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self):
		return self.INSTRMNT_RL.HLD_SL_INDCTR
	@lineage(dependencies={"INSTRMNT_RL.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self):
		return self.INSTRMNT_RL.SBJCT_IMPRMNT_INDCTR
	PRTY = None # PRTY
	@lineage(dependencies={"PRTY.INSTTTNL_SCTR"})
	def INSTTTNL_SCTR(self):
		return self.PRTY.INSTTTNL_SCTR
	@lineage(dependencies={"PRTY.MLTLTRL_DVLPMNT_BNK_INDCTR"})
	def MLTLTRL_DVLPMNT_BNK_INDCTR(self):
		return self.PRTY.MLTLTRL_DVLPMNT_BNK_INDCTR
	def NGTBL_SCRTY_INDCTR(self):
		''' return string from NGTBL_SCRTY enumeration of 2 for non-negotiable '''
		return '2'

class Derivatives_ETC(F_04_01_REF_FINREP_3_0_Base):
	EXCHNG_TRDBL_DRVTV_PSTN = None # EXCHNG_TRDBL_DRVTV_PSTN
	@lineage(dependencies={"EXCHNG_TRDBL_DRVTV_PSTN.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self):
		return self.EXCHNG_TRDBL_DRVTV_PSTN.HLD_SL_INDCTR
	EXCHNG_TRDBL_DRVTV_PSTN_RL = None # EXCHNG_TRDBL_DRVTV_PSTN_RL
	@lineage(dependencies={"EXCHNG_TRDBL_DRVTV_PSTN_RL.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self):
		return self.EXCHNG_TRDBL_DRVTV_PSTN_RL.ACCNTNG_CLSSFCTN
	@lineage(dependencies={"EXCHNG_TRDBL_DRVTV_PSTN_RL.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self):
		return self.EXCHNG_TRDBL_DRVTV_PSTN_RL.CRRYNG_AMNT
	PRTY = None # PRTY
	@lineage(dependencies={"PRTY.INSTTTNL_SCTR"})
	def INSTTTNL_SCTR(self):
		return self.PRTY.INSTTTNL_SCTR
	@lineage(dependencies={"PRTY.MLTLTRL_DVLPMNT_BNK_INDCTR"})
	def MLTLTRL_DVLPMNT_BNK_INDCTR(self):
		return self.PRTY.MLTLTRL_DVLPMNT_BNK_INDCTR
	SCRTY_ENTTY_RL_ASSGNMNT = None # SCRTY_ENTTY_RL_ASSGNMNT
	@lineage(dependencies={"SCRTY_ENTTY_RL_ASSGNMNT.PRTY_RL_TYP"})
	def PRTY_RL_TYP(self):
		return self.SCRTY_ENTTY_RL_ASSGNMNT.PRTY_RL_TYP
	SCRTY_EXCHNG_TRDBL_DRVTV = None # SCRTY_EXCHNG_TRDBL_DRVTV
	@lineage(dependencies={"SCRTY_EXCHNG_TRDBL_DRVTV.NGTBL_SCRTY_INDCTR"})
	def NGTBL_SCRTY_INDCTR(self):
		return self.SCRTY_EXCHNG_TRDBL_DRVTV.NGTBL_SCRTY_INDCTR
	def MN_DBTR_INDCTR(self):
		# return 1 for main debtor
		return '1'
	def INSTRMNT_TYP_PRDCT(self):
		''' return string from INSTRMNT_TYP_PRDCT enumeration '''
		return '310'
	def SBJCT_IMPRMNT_INDCTR(self):
		return '2'
	PRTY = None # PRTY

class Equity_instruments_instrument(F_04_01_REF_FINREP_3_0_Base):
	INSTRMNT = None # INSTRMNT
	@lineage(dependencies={"INSTRMNT.INSTRMNT_TYP_PRDCT"})
	def INSTRMNT_TYP_PRDCT(self):
		return self.INSTRMNT.INSTRMNT_TYP_PRDCT
	INSTRMNT_ENTTY_RL_ASSGNMNT = None # INSTRMNT_ENTTY_RL_ASSGNMNT
	@lineage(dependencies={"INSTRMNT_ENTTY_RL_ASSGNMNT.MN_DBTR_INDCTR"})
	def MN_DBTR_INDCTR(self):
		return self.INSTRMNT_ENTTY_RL_ASSGNMNT.MN_DBTR_INDCTR
	INSTRMNT_RL = None # INSTRMNT_RL
	@lineage(dependencies={"INSTRMNT_RL.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self):
		return self.INSTRMNT_RL.CRRYNG_AMNT
	@lineage(dependencies={"INSTRMNT_RL.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self):
		return self.INSTRMNT_RL.SBJCT_IMPRMNT_INDCTR
	PRTY = None # PRTY
	@lineage(dependencies={"PRTY.INSTTNL_SCTR_EBA_ITS"})
	def INSTTTNL_SCTR(self):
		return self.PRTY.INSTTNL_SCTR_EBA_ITS
	@lineage(dependencies={"PRTY.MLTLTRL_DVLPMNT_BNK_INDCTR"})
	def MLTLTRL_DVLPMNT_BNK_INDCTR(self):
		return self.PRTY.MLTLTRL_DVLPMNT_BNK_INDCTR

class On_demand_and_short_notice(F_04_01_REF_FINREP_3_0_Base):
	INSTRMNT = None # INSTRMNT
	@lineage(dependencies={"INSTRMNT.INSTRMNT_TYP_PRDCT"})
	def INSTRMNT_TYP_PRDCT(self):
		return self.INSTRMNT.INSTRMNT_TYP_PRDCT
	INSTRMNT_ENTTY_RL_ASSGNMNT = None # INSTRMNT_ENTTY_RL_ASSGNMNT
	def MN_DBTR_INDCTR(self):
		# return 1 for main debtor
		return '1'
	@lineage(dependencies={"INSTRMNT_ENTTY_RL_ASSGNMNT.PRTY_RL_TYP"})
	def PRTY_RL_TYP(self):
		return self.INSTRMNT_ENTTY_RL_ASSGNMNT.PRTY_RL_TYP
	INSTRMNT_RL = None # INSTRMNT_RL
	@lineage(dependencies={"INSTRMNT_RL.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self):
		return self.INSTRMNT_RL.ACCNTNG_CLSSFCTN
	@lineage(dependencies={"INSTRMNT_RL.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self):
		return self.INSTRMNT_RL.CRRYNG_AMNT
	@lineage(dependencies={"INSTRMNT_RL.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self):
		return self.INSTRMNT_RL.HLD_SL_INDCTR
	@lineage(dependencies={"INSTRMNT_RL.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self):
		return self.INSTRMNT_RL.SBJCT_IMPRMNT_INDCTR
	PRTY = None # PRTY
	@lineage(dependencies={"PRTY.INSTTTNL_SCTR"})
	def INSTTTNL_SCTR(self):
		return self.PRTY.INSTTTNL_SCTR
	@lineage(dependencies={"PRTY.MLTLTRL_DVLPMNT_BNK_INDCTR"})
	def MLTLTRL_DVLPMNT_BNK_INDCTR(self):
		return self.PRTY.MLTLTRL_DVLPMNT_BNK_INDCTR
	def NGTBL_SCRTY_INDCTR(self):
		''' return string from NGTBL_SCRTY enumeration of 2 for non-negotiable '''
		return '2'

class Reverse_repurchase_agreements(F_04_01_REF_FINREP_3_0_Base):
	INSTRMNT = None # INSTRMNT
	@lineage(dependencies={"INSTRMNT.INSTRMNT_TYP_PRDCT"})
	def INSTRMNT_TYP_PRDCT(self):
		return self.INSTRMNT.INSTRMNT_TYP_PRDCT
	INSTRMNT_ENTTY_RL_ASSGNMNT = None # INSTRMNT_ENTTY_RL_ASSGNMNT
	def MN_DBTR_INDCTR(self):
		# return 1 for main debtor
		return '1'
	@lineage(dependencies={"INSTRMNT_ENTTY_RL_ASSGNMNT.PRTY_RL_TYP"})
	def PRTY_RL_TYP(self):
		return self.INSTRMNT_ENTTY_RL_ASSGNMNT.PRTY_RL_TYP
	INSTRMNT_RL = None # INSTRMNT_RL
	@lineage(dependencies={"INSTRMNT_RL.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self):
		return self.INSTRMNT_RL.ACCNTNG_CLSSFCTN
	@lineage(dependencies={"INSTRMNT_RL.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self):
		return self.INSTRMNT_RL.CRRYNG_AMNT
	@lineage(dependencies={"INSTRMNT_RL.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self):
		return self.INSTRMNT_RL.HLD_SL_INDCTR
	@lineage(dependencies={"INSTRMNT_RL.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self):
		return self.INSTRMNT_RL.SBJCT_IMPRMNT_INDCTR
	PRTY = None # PRTY
	@lineage(dependencies={"PRTY.INSTTTNL_SCTR"})
	def INSTTTNL_SCTR(self):
		return self.PRTY.INSTTTNL_SCTR
	@lineage(dependencies={"PRTY.MLTLTRL_DVLPMNT_BNK_INDCTR"})
	def MLTLTRL_DVLPMNT_BNK_INDCTR(self):
		return self.PRTY.MLTLTRL_DVLPMNT_BNK_INDCTR
	def NGTBL_SCRTY_INDCTR(self):
		''' return string from NGTBL_SCRTY enumeration of 2 for non-negotiable '''
		return '2'

class Trade_receivables(F_04_01_REF_FINREP_3_0_Base):
	INSTRMNT = None # INSTRMNT
	@lineage(dependencies={"INSTRMNT.INSTRMNT_TYP_PRDCT"})
	def INSTRMNT_TYP_PRDCT(self):
		return self.INSTRMNT.INSTRMNT_TYP_PRDCT
	INSTRMNT_ENTTY_RL_ASSGNMNT = None # INSTRMNT_ENTTY_RL_ASSGNMNT
	@lineage(dependencies={"INSTRMNT_ENTTY_RL_ASSGNMNT.MN_DBTR_INDCTR"})
	def MN_DBTR_INDCTR(self):
		return self.INSTRMNT_ENTTY_RL_ASSGNMNT.MN_DBTR_INDCTR
	@lineage(dependencies={"INSTRMNT_ENTTY_RL_ASSGNMNT.PRTY_RL_TYP"})
	def PRTY_RL_TYP(self):
		return self.INSTRMNT_ENTTY_RL_ASSGNMNT.PRTY_RL_TYP
	INSTRMNT_RL = None # INSTRMNT_RL
	@lineage(dependencies={"INSTRMNT_RL.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self):
		return self.INSTRMNT_RL.ACCNTNG_CLSSFCTN
	@lineage(dependencies={"INSTRMNT_RL.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self):
		return self.INSTRMNT_RL.CRRYNG_AMNT
	@lineage(dependencies={"INSTRMNT_RL.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self):
		return self.INSTRMNT_RL.HLD_SL_INDCTR
	@lineage(dependencies={"INSTRMNT_RL.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self):
		return self.INSTRMNT_RL.SBJCT_IMPRMNT_INDCTR
	PRTY = None # PRTY
	@lineage(dependencies={"PRTY.INSTTTNL_SCTR"})
	def INSTTTNL_SCTR(self):
		return self.PRTY.INSTTTNL_SCTR
	@lineage(dependencies={"PRTY.MLTLTRL_DVLPMNT_BNK_INDCTR"})
	def MLTLTRL_DVLPMNT_BNK_INDCTR(self):
		return self.PRTY.MLTLTRL_DVLPMNT_BNK_INDCTR
	def NGTBL_SCRTY_INDCTR(self):
		''' return string from NGTBL_SCRTY enumeration of 2 for non-negotiable '''
		return '2'

class Debt_securities(F_04_01_REF_FINREP_3_0_Base):
	LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT = None # LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT
	@lineage(dependencies={"LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.ACCNTNG_CLSSFCTN
	@lineage(dependencies={"LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.CRRYNG_AMNT
	@lineage(dependencies={"LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.HLD_SL_INDCTR
	@lineage(dependencies={"LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.SBJCT_IMPRMNT_INDCTR
	PRTY = None # PRTY
	@lineage(dependencies={"PRTY.INSTTTNL_SCTR"})
	def INSTTTNL_SCTR(self):
		return self.PRTY.INSTTTNL_SCTR
	@lineage(dependencies={"PRTY.MLTLTRL_DVLPMNT_BNK_INDCTR"})
	def MLTLTRL_DVLPMNT_BNK_INDCTR(self):
		return self.PRTY.MLTLTRL_DVLPMNT_BNK_INDCTR
	SCRTY_ENTTY_RL_ASSGNMNT = None # SCRTY_ENTTY_RL_ASSGNMNT
	@lineage(dependencies={"SCRTY_ENTTY_RL_ASSGNMNT.PRTY_RL_TYP"})
	def PRTY_RL_TYP(self):
		return self.SCRTY_ENTTY_RL_ASSGNMNT.PRTY_RL_TYP
	SCRTY_EXCHNG_TRDBL_DRVTV = None # SCRTY_EXCHNG_TRDBL_DRVTV
	@lineage(dependencies={"SCRTY_EXCHNG_TRDBL_DRVTV.NGTBL_SCRTY_INDCTR"})
	def NGTBL_SCRTY_INDCTR(self):
		return self.SCRTY_EXCHNG_TRDBL_DRVTV.NGTBL_SCRTY_INDCTR
	def INSTRMNT_TYP_PRDCT(self):
		''' return string from INSTRMNT_TYP_PRDCT enumeration '''
		return '210'
	def MN_DBTR_INDCTR(self):
		# return 1 for main debtor
		return '1'

class Equity_instruments_security(F_04_01_REF_FINREP_3_0_Base):
	PRTY = None # PRTY
	@lineage(dependencies={"PRTY.INSTTNL_SCTR_EBA_ITS"})
	def INSTTTNL_SCTR(self):
		return self.PRTY.INSTTNL_SCTR_EBA_ITS
	@lineage(dependencies={"PRTY.MLTLTRL_DVLPMNT_BNK_INDCTR"})
	def MLTLTRL_DVLPMNT_BNK_INDCTR(self):
		return self.PRTY.MLTLTRL_DVLPMNT_BNK_INDCTR
	SCRTY_EXCHNG_TRDBL_DRVTV = None # SCRTY_EXCHNG_TRDBL_DRVTV
	@lineage(dependencies={"SCRTY_EXCHNG_TRDBL_DRVTV.NGTBL_SCRTY_INDCTR"})
	def NGTBL_SCRTY_INDCTR(self):
		return self.SCRTY_EXCHNG_TRDBL_DRVTV.NGTBL_SCRTY_INDCTR
	SCRTY_PSTN = None # SCRTY_PSTN
	@lineage(dependencies={"SCRTY_PSTN.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self):
		return self.SCRTY_PSTN.CRRYNG_AMNT

class F_04_01_REF_FINREP_3_0_Other_loans_Table:
	CLLTRL_Table = None # CLLTRL
	INSTRMNT_Table = None # INSTRMNT
	INSTRMNT_ENTTY_RL_ASSGNMNT_Table = None # INSTRMNT_ENTTY_RL_ASSGNMNT
	INSTRMNT_RL_Table = None # INSTRMNT_RL
	PRTY_Table = None # PRTY
	Other_loanss = []# Other_loans[]	
	@lineage(dependencies={"INSTRMNT.INSTRMNT_TYP_PRDCT",
		"INSTRMNT_ENTTY_RL_ASSGNMNT.theINSTRMNT",
		"INSTRMNT_ENTTY_RL_ASSGNMNT.theENTTY_RL",		
		"ENTTY_RL.thePRTY",
		"INSTRMNT.INSTRMNT_uniqueID",
		"INSTRMNT_ENTTY_RL_ASSGNMNT.INSTRMNT_ENTTY_RL_ASSGNMNT_uniqueID",
		"PRTY.PRTY_uniqueID"
		})
	def calc_Other_loanss(self) :
		
		items = [] # Other_loans[
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations
		
		for instrmnt_rl in self.INSTRMNT_RL_Table:
			typeInst = instrmnt_rl.theINSTRMNT.INSTRMNT_TYP_PRDCT
			#if (typeInst == INSTRMNT.INSTRMNT_TYP_PRDCT_INPT_domain['140']) or \
			#		(typeInst == INSTRMNT.INSTRMNT_TYP_PRDCT_INPT_domain['1022'] ) or \
			#	(typeInst == INSTRMNT.INSTRMNT_TYP_PRDCT_INPT_domain['51'] ) or \
			#	(typeInst == INSTRMNT.INSTRMNT_TYP_PRDCT_INPT_domain['80'] ) or \
			#	(typeInst == INSTRMNT.INSTRMNT_TYP_PRDCT_INPT_domain['12'] ) or \
			#	(typeInst == INSTRMNT.INSTRMNT_TYP_PRDCT_INPT_domain['522'] ):
			if (typeInst == '1022' ):
				
				newItem = Other_loans()
				newItem.INSTRMNT_RL = instrmnt_rl
				newItem.INSTRMNT = instrmnt_rl.theINSTRMNT
				
				for era in  self.INSTRMNT_ENTTY_RL_ASSGNMNT_Table:
					inst = era.theINSTRMNT
					if (inst == newItem.INSTRMNT):
						newItem.INSTRMNT_ENTTY_RL_ASSGNMNT = era
						er = era.theENTTY_RL
						newItem.PRTY = er.thePRTY
					
				items.append(newItem)
	
		return items
	@track_table_init
	def init(self):
		Orchestration().init(self)
		self.Other_loanss = []
		self.Other_loanss.extend(self.calc_Other_loanss())
		
		# Explicitly track the created Other_loans objects for lineage
		#from pybirdai.annotations.decorators import _lineage_context
		#orchestration = _lineage_context.get('orchestration')
		#if orchestration and hasattr(orchestration, 'track_data_processing'):
		#	print(f"🔍 Other_loans_Table: Tracking {len(self.Other_loanss)} Other_loans objects")
		#	orchestration.track_data_processing("Other_loans", self.Other_loanss, self.Other_loanss)
		
		CSVConverter.persist_object_as_csv(self,True)
		return None


class F_04_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table:
	INSTRMNT_Table = None # INSTRMNT
	INSTRMNT_ENTTY_RL_ASSGNMNT_Table = None # INSTRMNT_ENTTY_RL_ASSGNMNT
	INSTRMNT_RL_Table = None # INSTRMNT_RL
	PRTY_Table = None # PRTY
	Advances_that_are_not_loanss = []# Advances_that_are_not_loans[]
	@lineage(dependencies={"INSTRMNT.INSTRMNT_TYP_PRDCT",
		"INSTRMNT_ENTTY_RL_ASSGNMNT.theINSTRMNT",
		"INSTRMNT_ENTTY_RL_ASSGNMNT.theENTTY_RL",		
		"ENTTY_RL.thePRTY",
		"INSTRMNT.INSTRMNT_uniqueID",
		"INSTRMNT_ENTTY_RL_ASSGNMNT.INSTRMNT_ENTTY_RL_ASSGNMNT_uniqueID",
		"PRTY.PRTY_uniqueID"
		})
	def calc_Advances_that_are_not_loanss(self) :
		items = [] # 
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations
		
		for instrmnt_rl in self.INSTRMNT_RL_Table:
			typeInst = instrmnt_rl.theINSTRMNT.INSTRMNT_TYP_PRDCT

			if (typeInst == '130') or (typeInst == '120') or (typeInst == '140'):
				
				newItem = Advances_that_are_not_loans()
				newItem.INSTRMNT_RL = instrmnt_rl
				newItem.INSTRMNT = instrmnt_rl.theINSTRMNT
				
				for era in  self.INSTRMNT_ENTTY_RL_ASSGNMNT_Table:
					inst = era.theINSTRMNT
					if (inst == newItem.INSTRMNT):
						newItem.INSTRMNT_ENTTY_RL_ASSGNMNT = era
						er = era.theENTTY_RL
						newItem.PRTY = er.thePRTY
					
				items.append(newItem)
	
		return items
	@track_table_init
	def init(self):
		Orchestration().init(self)
		self.Advances_that_are_not_loanss = []
		self.Advances_that_are_not_loanss.extend(self.calc_Advances_that_are_not_loanss())
		CSVConverter.persist_object_as_csv(self,True)
		return None


class F_04_01_REF_FINREP_3_0_Credit_card_debt_Table:
	CLLTRL_Table = None # CLLTRL
	INSTRMNT_Table = None # INSTRMNT
	INSTRMNT_ENTTY_RL_ASSGNMNT_Table = None # INSTRMNT_ENTTY_RL_ASSGNMNT
	INSTRMNT_RL_Table = None # INSTRMNT_RL
	PRTY_Table = None # PRTY
	Credit_card_debts = []# Credit_card_debt[]

	@lineage(dependencies={"INSTRMNT.INSTRMNT_TYP_PRDCT",
		"INSTRMNT_ENTTY_RL_ASSGNMNT.theINSTRMNT",
		"INSTRMNT_ENTTY_RL_ASSGNMNT.theENTTY_RL",		
		"ENTTY_RL.thePRTY",
		"INSTRMNT.INSTRMNT_uniqueID",
		"INSTRMNT_ENTTY_RL_ASSGNMNT.INSTRMNT_ENTTY_RL_ASSGNMNT_uniqueID",
		"PRTY.PRTY_uniqueID"
		})
	def calc_Credit_card_debts(self) :
		items = [] # 
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations
		
		for instrmnt_rl in self.INSTRMNT_RL_Table:
			typeInst = instrmnt_rl.theINSTRMNT.INSTRMNT_TYP_PRDCT
			#if (typeInst == INSTRMNT.INSTRMNT_TYP_PRDCT_INPT_domain['140']) or \
			#		(typeInst == INSTRMNT.INSTRMNT_TYP_PRDCT_INPT_domain['1022'] ) or \
			#	(typeInst == INSTRMNT.INSTRMNT_TYP_PRDCT_INPT_domain['51'] ) or \
			#	(typeInst == INSTRMNT.INSTRMNT_TYP_PRDCT_INPT_domain['80'] ) or \
			#	(typeInst == INSTRMNT.INSTRMNT_TYP_PRDCT_INPT_domain['12'] ) or \
			#	(typeInst == INSTRMNT.INSTRMNT_TYP_PRDCT_INPT_domain['522'] ):
			if (typeInst == '51' ):
				
				newItem = Credit_card_debt()
				newItem.INSTRMNT_RL = instrmnt_rl
				newItem.INSTRMNT = instrmnt_rl.theINSTRMNT
				
				for era in  self.INSTRMNT_ENTTY_RL_ASSGNMNT_Table:
					inst = era.theINSTRMNT
					if (inst == newItem.INSTRMNT):
						newItem.INSTRMNT_ENTTY_RL_ASSGNMNT = era
						er = era.theENTTY_RL
						newItem.PRTY = er.thePRTY
					
				items.append(newItem)
	
		return items
	def init(self):
		Orchestration().init(self)
		self.Credit_card_debts = []
		self.Credit_card_debts.extend(self.calc_Credit_card_debts())
		CSVConverter.persist_object_as_csv(self,True)
		return None


class F_04_01_REF_FINREP_3_0_Finance_leases_Table:
	CLLTRL_Table = None # CLLTRL
	INSTRMNT_Table = None # INSTRMNT
	INSTRMNT_ENTTY_RL_ASSGNMNT_Table = None # INSTRMNT_ENTTY_RL_ASSGNMNT
	INSTRMNT_RL_Table = None # INSTRMNT_RL
	PRTY_Table = None # PRTY
	Finance_leasess = []# Finance_leases[]
	@lineage(dependencies={"INSTRMNT.INSTRMNT_TYP_PRDCT",
		"INSTRMNT_ENTTY_RL_ASSGNMNT.theINSTRMNT",
		"INSTRMNT_ENTTY_RL_ASSGNMNT.theENTTY_RL",		
		"ENTTY_RL.thePRTY",
		"INSTRMNT.INSTRMNT_uniqueID",
		"INSTRMNT_ENTTY_RL_ASSGNMNT.INSTRMNT_ENTTY_RL_ASSGNMNT_uniqueID",
		"PRTY.PRTY_uniqueID"
		})
	def calc_Finance_leasess(self) :
		items = [] # 
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations
		
		for instrmnt_rl in self.INSTRMNT_RL_Table:
			typeInst = instrmnt_rl.theINSTRMNT.INSTRMNT_TYP_PRDCT
			#if (typeInst == INSTRMNT.INSTRMNT_TYP_PRDCT_INPT_domain['140']) or \
			#		(typeInst == INSTRMNT.INSTRMNT_TYP_PRDCT_INPT_domain['1022'] ) or \
			#	(typeInst == INSTRMNT.INSTRMNT_TYP_PRDCT_INPT_domain['51'] ) or \
			#	(typeInst == INSTRMNT.INSTRMNT_TYP_PRDCT_INPT_domain['80'] ) or \
			#	(typeInst == INSTRMNT.INSTRMNT_TYP_PRDCT_INPT_domain['12'] ) or \
			#	(typeInst == INSTRMNT.INSTRMNT_TYP_PRDCT_INPT_domain['522'] ):
			if (typeInst == '80' ):
				
				newItem = Finance_leases()
				newItem.INSTRMNT_RL = instrmnt_rl
				newItem.INSTRMNT = instrmnt_rl.theINSTRMNT
				
				for era in  self.INSTRMNT_ENTTY_RL_ASSGNMNT_Table:
					inst = era.theINSTRMNT
					if (inst == newItem.INSTRMNT):
						newItem.INSTRMNT_ENTTY_RL_ASSGNMNT = era
						er = era.theENTTY_RL
						newItem.PRTY = er.thePRTY
					
				items.append(newItem)
	
		return items
	def init(self):
		Orchestration().init(self)
		self.Finance_leasess = []
		self.Finance_leasess.extend(self.calc_Finance_leasess())
		CSVConverter.persist_object_as_csv(self,True)
		return None

class F_04_01_REF_FINREP_3_0_Trade_receivables_Table:
	CLLTRL_Table = None # CLLTRL
	INSTRMNT_Table = None # INSTRMNT
	INSTRMNT_ENTTY_RL_ASSGNMNT_Table = None # INSTRMNT_ENTTY_RL_ASSGNMNT
	INSTRMNT_RL_Table = None # INSTRMNT_RL
	PRTY_Table = None # PRTY
	Other_loanss = []# Other_loans[]	
	@lineage(dependencies={"INSTRMNT.INSTRMNT_TYP_PRDCT",
		"INSTRMNT_ENTTY_RL_ASSGNMNT.theINSTRMNT",
		"INSTRMNT_ENTTY_RL_ASSGNMNT.theENTTY_RL",		
		"ENTTY_RL.thePRTY",
		"INSTRMNT.INSTRMNT_uniqueID",
		"INSTRMNT_ENTTY_RL_ASSGNMNT.INSTRMNT_ENTTY_RL_ASSGNMNT_uniqueID",
		"PRTY.PRTY_uniqueID",
		})
	def calc_Trade_receivabless(self) :
		items = [] # Other_loans[
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations
		
		for instrmnt_rl in self.INSTRMNT_RL_Table:
			typeInst = instrmnt_rl.theINSTRMNT.INSTRMNT_TYP_PRDCT
			#if (typeInst == INSTRMNT.INSTRMNT_TYP_PRDCT_INPT_domain['140']) or \
			#		(typeInst == INSTRMNT.INSTRMNT_TYP_PRDCT_INPT_domain['1022'] ) or \
			#	(typeInst == INSTRMNT.INSTRMNT_TYP_PRDCT_INPT_domain['51'] ) or \
			#	(typeInst == INSTRMNT.INSTRMNT_TYP_PRDCT_INPT_domain['80'] ) or \
			#	(typeInst == INSTRMNT.INSTRMNT_TYP_PRDCT_INPT_domain['12'] ) or \
			#	(typeInst == INSTRMNT.INSTRMNT_TYP_PRDCT_INPT_domain['522'] ):
			if (typeInst == '1023' ):
				
				newItem = Trade_receivables()
				newItem.INSTRMNT_RL = instrmnt_rl
				newItem.INSTRMNT = instrmnt_rl.theINSTRMNT
				
				for era in  self.INSTRMNT_ENTTY_RL_ASSGNMNT_Table:
					inst = era.theINSTRMNT
					if (inst == newItem.INSTRMNT):
						newItem.INSTRMNT_ENTTY_RL_ASSGNMNT = era
						er = era.theENTTY_RL
						newItem.PRTY = er.thePRTY
					
				items.append(newItem)
	
		return items
	def init(self):
		Orchestration().init(self)
		self.Trade_receivabless = []
		self.Trade_receivabless.extend(self.calc_Trade_receivabless())
		CSVConverter.persist_object_as_csv(self,True)
		return None

class F_04_01_REF_FINREP_3_0_On_demand_and_short_notice_Table:
	INSTRMNT_Table = None # INSTRMNT
	INSTRMNT_ENTTY_RL_ASSGNMNT_Table = None # INSTRMNT_ENTTY_RL_ASSGNMNT
	INSTRMNT_RL_Table = None # INSTRMNT_RL
	PRTY_Table = None # PRTY
	On_demand_and_short_notices = []# On_demand_and_short_notice[]
	@lineage(dependencies={"INSTRMNT.INSTRMNT_TYP_PRDCT",
		"INSTRMNT_ENTTY_RL_ASSGNMNT.theINSTRMNT",
		"INSTRMNT_ENTTY_RL_ASSGNMNT.theENTTY_RL",		
		"ENTTY_RL.thePRTY",
		"INSTRMNT.INSTRMNT_uniqueID",
		"INSTRMNT_ENTTY_RL_ASSGNMNT.INSTRMNT_ENTTY_RL_ASSGNMNT_uniqueID",
		"PRTY.PRTY_uniqueID"
		})
	def calc_On_demand_and_short_notices(self) :
		items = [] # On_demand_and_short_notice
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations
		
		for instrmnt_rl in self.INSTRMNT_RL_Table:
			typeInst = instrmnt_rl.theINSTRMNT.INSTRMNT_TYP_PRDCT
			if (typeInst == '511' ) or (typeInst == '522' ):
				newItem = On_demand_and_short_notice()
				newItem.INSTRMNT_RL = instrmnt_rl
				newItem.INSTRMNT = instrmnt_rl.theINSTRMNT
				
				for era in  self.INSTRMNT_ENTTY_RL_ASSGNMNT_Table:
					inst = era.theINSTRMNT
					if (inst == newItem.INSTRMNT):
						newItem.INSTRMNT_ENTTY_RL_ASSGNMNT = era
						er = era.theENTTY_RL
						newItem.PRTY = er.thePRTY
					
				items.append(newItem)
	
		return items
	def init(self):
		Orchestration().init(self)
		self.On_demand_and_short_notices = []
		self.On_demand_and_short_notices.extend(self.calc_On_demand_and_short_notices())
		CSVConverter.persist_object_as_csv(self,True)
		return None


class F_04_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table:
	INSTRMNT_Table = None # INSTRMNT
	INSTRMNT_ENTTY_RL_ASSGNMNT_Table = None # INSTRMNT_ENTTY_RL_ASSGNMNT
	INSTRMNT_RL_Table = None # INSTRMNT_RL
	PRTY_Table = None # PRTY
	Reverse_repurchase_agreementss = []# Reverse_repurchase_agreements[]
	@lineage(dependencies={"INSTRMNT.INSTRMNT_TYP_PRDCT",
		"INSTRMNT_ENTTY_RL_ASSGNMNT.theINSTRMNT",
		"INSTRMNT_ENTTY_RL_ASSGNMNT.theENTTY_RL",		
		"ENTTY_RL.thePRTY",
		"INSTRMNT.INSTRMNT_uniqueID",
		"INSTRMNT_ENTTY_RL_ASSGNMNT.INSTRMNT_ENTTY_RL_ASSGNMNT_uniqueID",
		"PRTY.PRTY_uniqueID"
		})
	def calc_Reverse_repurchase_agreementss(self) :
		items = [] # On_demand_and_short_notice
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations
		
		for instrmnt_rl in self.INSTRMNT_RL_Table:
			typeInst = instrmnt_rl.theINSTRMNT.INSTRMNT_TYP_PRDCT
			if (typeInst == '1003' ) :
				newItem = Reverse_repurchase_agreements()
				newItem.INSTRMNT_RL = instrmnt_rl
				newItem.INSTRMNT = instrmnt_rl.theINSTRMNT
				
				for era in  self.INSTRMNT_ENTTY_RL_ASSGNMNT_Table:
					inst = era.theINSTRMNT
					if (inst == newItem.INSTRMNT):
						newItem.INSTRMNT_ENTTY_RL_ASSGNMNT = era
						er = era.theENTTY_RL
						newItem.PRTY = er.thePRTY
					
				items.append(newItem)
	
		return items
	def init(self):
		Orchestration().init(self)
		self.Reverse_repurchase_agreementss = []
		self.Reverse_repurchase_agreementss.extend(self.calc_Reverse_repurchase_agreementss())
		CSVConverter.persist_object_as_csv(self,True)
		return None


class F_04_01_REF_FINREP_3_0_Derivatives_ETC_Table:
	EXCHNG_TRDBL_DRVTV_PSTN_Table = None # EXCHNG_TRDBL_DRVTV_PSTN
	EXCHNG_TRDBL_DRVTV_PSTN_RL_Table = None # EXCHNG_TRDBL_DRVTV_PSTN_RL
	PRTY_Table = None # PRTY
	SCRTY_ENTTY_RL_ASSGNMNT_Table = None # SCRTY_ENTTY_RL_ASSGNMNT
	SCRTY_EXCHNG_TRDBL_DRVTV_Table = None # SCRTY_EXCHNG_TRDBL_DRVTV
	Derivatives_ETCs = []# Derivatives_ETC[]
	def calc_Derivatives_ETCs(self) :
		items = [] # Derivatives_ETC[
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations
		return items
	def init(self):
		Orchestration().init(self)
		self.Derivatives_ETCs = []
		self.Derivatives_ETCs.extend(self.calc_Derivatives_ETCs())
		CSVConverter.persist_object_as_csv(self,True)
		return None


class F_04_01_REF_FINREP_3_0_Equity_instruments_instrument_Table:
	INSTRMNT_Table = None # INSTRMNT
	INSTRMNT_ENTTY_RL_ASSGNMNT_Table = None # INSTRMNT_ENTTY_RL_ASSGNMNT
	INSTRMNT_RL_Table = None # INSTRMNT_RL
	PRTY_Table = None # PRTY
	Equity_instruments_instruments = []# Equity_instruments_instrument[]
	def calc_Equity_instruments_instruments(self) :
		items = [] # Equity_instruments_instrument[
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations
		return items
	def init(self):
		Orchestration().init(self)
		self.Equity_instruments_instruments = []
		self.Equity_instruments_instruments.extend(self.calc_Equity_instruments_instruments())
		CSVConverter.persist_object_as_csv(self,True)
		return None





class F_04_01_REF_FINREP_3_0_Debt_securities_Table:
	LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT_Table = None # LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT
	PRTY_Table = None # PRTY
	SCRTY_ENTTY_RL_ASSGNMNT_Table = None # SCRTY_ENTTY_RL_ASSGNMNT
	SCRTY_EXCHNG_TRDBL_DRVTV_Table = None # SCRTY_EXCHNG_TRDBL_DRVTV
	Debt_securitiess = []# Debt_securities[]
	def calc_Debt_securitiess(self) :
		items = [] # Debt_securities[
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations
		return items
	def init(self):
		Orchestration().init(self)
		self.Debt_securitiess = []
		self.Debt_securitiess.extend(self.calc_Debt_securitiess())
		CSVConverter.persist_object_as_csv(self,True)
		return None


class F_04_01_REF_FINREP_3_0_Equity_instruments_security_Table:
	PRTY_Table = None # PRTY
	SCRTY_EXCHNG_TRDBL_DRVTV_Table = None # SCRTY_EXCHNG_TRDBL_DRVTV
	SCRTY_PSTN_Table = None # SCRTY_PSTN
	Equity_instruments_securitys = []# Equity_instruments_security[]
	def calc_Equity_instruments_securitys(self) :
		items = [] # Equity_instruments_security[
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations
		return items
	def init(self):
		Orchestration().init(self)
		self.Equity_instruments_securitys = []
		self.Equity_instruments_securitys.extend(self.calc_Equity_instruments_securitys())
		CSVConverter.persist_object_as_csv(self,True)
		return None

