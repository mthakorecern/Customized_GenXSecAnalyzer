# Python Script to calculate Xsec for a dataset(s) using MiniAOD files

This setup uses a configuration file obtained from 

https://github.com/cms-sw/genproductions/blob/master/Utilities/calculateXSectionAndFilterEfficiency/genXsec_cfg.py


##  Usage: 
```
source /cvmfs/cms.cern.ch/cmsset_default.sh
cmsrel CMSSW_15_0_10
cd CMSSW_15_0_10/src/
voms-proxy-init -voms cms -out /tmp/x509up_u10196 -valid 192:00
git clone https://github.com/mthakorecern/Customized_GenXSecAnalyzer.git
cd Customized_GenXSecAnalyzer/
python3 run_genXsec_from_datasets.py -f datasets.txt -n <no-of-events>
```

Populate the datasets.txt file with the list of datasets like
```
/DYto2Mu_Bin-MLL-10to50_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM
/DYto2Mu_Bin-MLL-120to200_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM
```

