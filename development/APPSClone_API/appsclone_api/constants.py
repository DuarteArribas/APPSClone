#all the receivers extracted from the receivers file
receiversList = ["ALERTGEO RESOLUTE","AOA BENCHMARK ACT","AOA ICS-4000Z","AOA ICS-4000Z ACT","AOA RASCAL-12","AOA RASCAL-8","AOA SNR-12 ACT","AOA SNR-8000 ACT","AOA SNR-8100 ACT","AOA TTR-12","AOA TTR-4P","ASHTECH","ASHTECH 3DF-XXIV","ASHTECH D-XII","ASHTECH GG24C","ASHTECH G-XII","ASHTECH LCS-XII","ASHTECH LM-XII3","ASHTECH L-XII","ASHTECH MICROZ","ASHTECH MS-XII","ASHTECH M-XII","ASHTECH M-XII0C","ASHTECH P-XII3","ASHTECH RANGER","ASHTECH SUPER-CA","ASHTECH S-XII","ASHTECH UZ-12","ASHTECH Z-12","ASHTECH Z-18","ASHTECH Z18","ASHTECH Z-FX","ASHTECH Z-X","ASHTECH Z-XII","ASHTECH Z-XII3","ASHTECH Z-XII3GETT","ASHTECH Z-XII3T","ASHTECH_Z-XII3","ASHTECH Z-X113","Ashtech Z Series","LM-XII","LM-XII3","M-XII","P-XII3","P-XII","Z-XII3","Z-XII","ZY12","BLACKJACK","JPL BLACKJACK","BLE 4000 SSI","CHAMPION QB1","CMC ALLSTAR 12","CMC ALLSTAR OEM","DNREC","ESA/ISN GNSS","ITT 3750300","Javad Legacy-E","JPS DELTA","JPS EUROCARD","JPS E_GGD","JPS EGGDT","JPS LEGACY","JPS LEGACY GGD","JPS ODYSSEY","JPS ODYSSEY_E","JPS REGENCY","JAVAD DELTA","Javad GGD-160T","JAVAD TRE_G2T DELTA","JAVAD TRE_G2TH SIGMA","JAVAD TRE_3 DELTA","JAVAD TRE_G3TH","JAVAD TR_G3TH","JAVAD TRE_G3TH DELTA","JAVAD TRE_G3T DELTA","JAVAD TRE_G3TH SIGMA","JAVAD TRE_G3T SIGMA","JAVAD TRE_3N DELTA","JAVAD TRE_3","LEICA ATX1230","LEICA CRS1000","LEICA GMX901","LEICA GMX902","LEICA GMX902GG","LEICA GR10","LEICA GR25","LEICA GR30","LEICA GR50","LEICA GX1210","LEICA GX1220","LEICA GX1230","LEICA GX1230GG","LEICA GX1230+GNSS","LEICA GRX1200","LEICA GRX1200+","LEICA GRX1200+GNSS","LEICA GRX1200GGPRO","LEICA GRX1200PRO","LEICA_GRX1200PRO","LEICA GRX1200LITE","LEICA MC1000","LEICA MC500","LEICA RS500","LEICA SR260","LEICA SR261","LEICA SR299","LEICA SR299E","LEICA SR399","LEICA SR399E","LEICA SR510","LEICA SR520","LEICA SR530","LEICA SR9400","LEICA SR9500","LEICA SR9600","MINIMAC 2816","MINIMAC 2816AT","ROCKWELL ZODIAC OEM","NAVCOM NCT-2000D","NAVCOM SF-2000","NAVCOM NCT-2030M","NAVCOM SF-2040G","NAVCOM SF-2050G","NAVCOM SF-2050M","NAVCOM SF-2050R","NAVCOM SF-3050","NAVCOM RT-3010S","NAVCOM RT-3020S","NAVCOM RT-3020M","NOV EURO4-1.00-222","NOVATEL GSV4004","NOV MILLEN-RT2","NOV MILLEN-RT2OS","NOV MILLEN-STD","NOV MILLEN-STDW","NOVATEL MILLENIUM","NOV OEMV3","NOV OEMV3-RT2","NOV OEM4-G2","NOV OEM6","NOV WAAS","NOV WAASGII","NOVATEL OEM4","NovWaas","PANDA PD51A","POLARX2","DSN ROGUE","MINI-ROGUE SNR-8C","ROGUE","ROGUE SNR-","ROGUE SNR-12","ROGUE SNR-12 RM","ROGUE SNR-8","ROGUE SNR-800","ROGUE SNR-8000","ROGUE SNR-8100","ROGUE SNR-8A","ROGUE SNR-8C","ROGUE 8C","SNR-8C MINI-ROGUE","TURBOROGUE","SEPT POLARX2","SEPT POLARX2E","SEPT POLARX3ETR","SEPT POLARX4","SEPT POLARX4TR","SEPT POLARX4TR PRO","SEPT POLARXS","SEPT ASTERX-M2 OEM","SEPT ASTERX3","SEPT ASTERX4","SEPT ASTERX SB","SEPT POLARX5","SEPT POLARX5S","SEPT POLARX5TR","SEPT POLARX5E","SEPT SSRC3","SIMULA","SOK RADIAN","SOK RADIAN_IS","SOK GSR2600","SOK GSR2700 RS","SPECTRA SP90M","SPP GEODIMETER-L1","SPP GEOTRACER100","SPP GEOTRACER3220","SPP GEOTRACER3320","STONEX SC2200","TI4100","TOPCON JPS_LEGACY","TOPCON GP-DX1","TOPCON GP-R1","TOPCON GP-R1D","TOPCON GP-R1DP","TOPCON GP-R1DY","TOPCON GP-R1SD","TOPCON GP-S1","TOPCON GP-SX1","TOPCON TT4000SSI","TOPCON TURBO-SII","TPS DELTA","TPS E_GGD","TPS EUROCARD","TPS LEGACY","TPS HIPER_GD","TPS HIPER_GGD","TPS HIPER_LITE","TPS HIPER_PLUS","TPS NETG3","TPS NET-G3A","TPS NETG5","TPS NET-G5","TPS ODDYSSEY_1","TPS ODYSSEY_E","TPS GB-1000","TPS MAXOR","TRIMBLE","TRIMBLE 4000 SSI","TRIMBLE 4000 SST","TRIMBLE 4000S","TRIMBLE 4000SE","TRIMBLE 4000SL","TRIMBLE 4000SLD","TRIMBLE 4000SSE","TRIMBLE 4000 SSE","TRIMBLE 4000SSI","TRIMBLE 4000SSI-SS","TRIMBLE 4000SST","TRIMBLE 4000ST","TRIMBLE 4000ST S","TRIMBLE 4000SX","TRIMBLE 4400","TRIMBLE 4600","TRIMBLE 4700","TRIMBLE 4800","TRIMBLE 5700","TRIM5700","TRIMBLE 5800","TRIMBLE 7400MSI","TRIMBLE GEODESIST P","TRIMBLE MS750","TRIMBLE R7","TRIMBLE R7 GNSS","TRIMBLE R8","TRIMBLE NETRC","TRIMBLE NETRS","TRIMBLE_NETRS","TRIMBLE NETR3","TRIMBLE NETR5","TRIMBLE NETR8","TRIMBLE NETR9","TRIMBLE ALLOY","TRIMBLE SPS855","HEMISPHERE ECLIPSE","TRSR","4000SSI","5700","GP-R1DY","GENERIC_P1","GENERIC_C1","GENERIC_UNK","SEPT POLARX5E","ASHTECH PF800","TRIMBLE R9S","TRIMBLE R5","TRIMBLE R6","NOV GSV4004A","SOK GSR2700 RSX","RAYMAND IRNET-G3B","CNT M300PRO","CNT M300PLUS","TPS GR3"]
receivers     = set(receiversList)
#all the antennas extracted from the antennas file
antennasList  = ["BLOCK IIA","BLOCK IIA","BLOCK IIR-M","BLOCK IIA","BLOCK IIF","BLOCK II","BLOCK IIR-B","BLOCK I","BLOCK IIA","BLOCK IIA","BLOCK IIF","BLOCK I","BLOCK IIA","BLOCK IIR-M","BLOCK IIA","BLOCK IIA","BLOCK IIR-M","BLOCK IIA","BLOCK IIA","BLOCK IIR-M","BLOCK IIA","BLOCK IIIA","BLOCK IIA","BLOCK IIIA","BLOCK I","BLOCK IIA","BLOCK IIR-M","BLOCK I","BLOCK IIA","BLOCK IIR-M","BLOCK IIF","BLOCK I","BLOCK IIA","BLOCK IIR-M","BLOCK I","BLOCK IIA","BLOCK IIR-M","BLOCK IIF","BLOCK I","BLOCK IIA","BLOCK IIF","BLOCK IIA","BLOCK IIA","BLOCK IIF","BLOCK I","BLOCK IIR-A","BLOCK IIIA","BLOCK I","BLOCK IIR-M","BLOCK I","BLOCK IIR-A","BLOCK II","BLOCK IIR-A","BLOCK IIIA","BLOCK II","BLOCK IIR-M","BLOCK II","BLOCK IIR-A","BLOCK II","BLOCK IIR-M","BLOCK II","BLOCK IIR-A","BLOCK IIA","BLOCK IIIA","BLOCK II","BLOCK IIR-B","BLOCK II","BLOCK IIR-A","BLOCK II","BLOCK IIR-A","BLOCK IIA","BLOCK IIR-B","BLOCK IIR-A","BLOCK IIA","BLOCK IIR-B","BLOCK IIIA","BLOCK IIA","BLOCK IIR-M","BLOCK IIA","BLOCK IIA","BLOCK IIR-M","BLOCK IIF","BLOCK IIA","BLOCK IIA","BLOCK IIF","BLOCK IIA","BLOCK IIA","BLOCK IIA","BLOCK IIF","BLOCK IIA","BLOCK IIR-M","BLOCK IIF","BLOCK IIA","BLOCK IIR-A","BLOCK IIA","BLOCK IIR-M","BLOCK IIA","BLOCK IIA","BLOCK IIR-M","BLOCK IIA","BLOCK IIA","BLOCK IIA","BLOCK IIR-M","BLOCK IIF","BLOCK IIA","BLOCK IIR-M","BLOCK IIA","BLOCK IIF","GLONASS","GLONASS","GLONASS-M","GLONASS","GLONASS-M","GLONASS-M","GLONASS","GLONASS","GLONASS-M","GLONASS-M","GLONASS-M","GLONASS-M","GLONASS-K1","GLONASS-M","GLONASS","GLONASS","GLONASS-M","GLONASS-M","GLONASS-K1","GLONASS-M","GLONASS-M","GLONASS","GLONASS-M","GLONASS-M","GLONASS","GLONASS","GLONASS-M","GLONASS-M","GLONASS-M","GLONASS","GLONASS-M","GLONASS-M","GLONASS","GLONASS","GLONASS-M","GLONASS-M","GLONASS-M","GLONASS-M","GLONASS-K1","GLONASS-M","GLONASS","GLONASS-M","GLONASS-M","GLONASS-K1","GLONASS","GLONASS-M","GLONASS-M","GLONASS","GLONASS-M","GLONASS-M","GLONASS-K1","GLONASS","GLONASS-M","GLONASS-M","GLONASS-M","GLONASS","GLONASS-M","GLONASS","GLONASS-M","GLONASS-M","GLONASS-M","GLONASS-K1","GLONASS-M","GLONASS","GLONASS","GLONASS-M","GLONASS-M","GLONASS","GLONASS-M","GLONASS-M","GLONASS-M","GLONASS","GLONASS","GLONASS-M","GLONASS-M","GLONASS-M","GLONASS-M","GLONASS-K1","GLONASS-M","GLONASS-M","GLONASS","GLONASS","GLONASS-M","GLONASS-M","GLONASS-M","GLONASS","GLONASS","GLONASS-M","GLONASS","GLONASS","GLONASS-M","GLONASS","GLONASS-M","GLONASS-M","GLONASS","GLONASS","GLONASS","GLONASS-M","GLONASS-M","GLONASS-M","GLONASS","GLONASS","GLONASS-M","GLONASS-M","GLONASS","GLONASS-M","GLONASS-M","GLONASS-M","GLONASS-K1","GLONASS-K1","GLONASS-K1","GLONASS-K1","GLONASS-K1","GLONASS-M","GALILEO-2","GALILEO-2","GALILEO-2","GALILEO-2","GALILEO-2","GALILEO-2","GALILEO-2","GALILEO-2","GALILEO-2","GALILEO-1","GALILEO-1","GALILEO-2","GALILEO-2","GALILEO-2","GALILEO-2","GALILEO-1","GALILEO-1","GALILEO-2","GALILEO-2","GALILEO-2","GALILEO-2","GALILEO-2","GALILEO-2","GALILEO-2","GALILEO-2","GALILEO-2","GALILEO-2","GALILEO-2","GALILEO-0A","GALILEO-0B","BEIDOU-2G","BEIDOU-2G","BEIDOU-2G","BEIDOU-2G","BEIDOU-2G","BEIDOU-2G","BEIDOU-2G","BEIDOU-2I","BEIDOU-2I","BEIDOU-2I","BEIDOU-2I","BEIDOU-2I","BEIDOU-2M","BEIDOU-2M","BEIDOU-2M","BEIDOU-2I","BEIDOU-2M","BEIDOU-2I","BEIDOU-3SI-SECM","BEIDOU-2I","BEIDOU-2G","BEIDOU-3SI-CAST","BEIDOU-2G","BEIDOU-3M-CAST","BEIDOU-3SM-CAST","BEIDOU-3M-CAST","BEIDOU-3M-CAST","BEIDOU-3M-CAST","BEIDOU-3M-CAST","BEIDOU-3M-CAST","BEIDOU-3M-CAST","BEIDOU-3M-SECM","BEIDOU-3M-SECM","BEIDOU-3M-SECM","BEIDOU-3M-SECM","BEIDOU-3SM-CAST","BEIDOU-3M-SECM","BEIDOU-3M-SECM","BEIDOU-2M","BEIDOU-3M-SECM","BEIDOU-3SI-SECM","BEIDOU-3SI-SECM","BEIDOU-3SI-CAST","BEIDOU-3M-CAST","BEIDOU-3SM-CAST","BEIDOU-3M-CAST","BEIDOU-3SM-CAST","BEIDOU-3M-SECM","BEIDOU-3M-SECM","BEIDOU-3M-CAST","BEIDOU-3M-CAST","BEIDOU-3I","BEIDOU-3I","BEIDOU-3I","BEIDOU-3M-CAST","BEIDOU-3M-CAST","BEIDOU-3M-SECM","BEIDOU-3M-SECM","BEIDOU-3M-CAST","BEIDOU-3M-CAST","BEIDOU-3M-CAST","BEIDOU-3M-SECM","BEIDOU-3SI-CAST","BEIDOU-3SM-CAST","BEIDOU-3SM-CAST","BEIDOU-3G-CAST","BEIDOU-3G-CAST","BEIDOU-3G-CAST","QZSS","QZSS-2I","QZSS-2I","QZSS-2A","QZSS-2G","IRNSS-1IGSO","IRNSS-1IGSO","IRNSS-1GEO","IRNSS-1IGSO","IRNSS-1IGSO","IRNSS-1GEO","IRNSS-1GEO","3S-02-TSADM     NONE","3S-02-TSATE     NONE","AERAT1675_120   SPKE","AERAT1675_542E  NEVE","AERAT2775_43    NONE","AERAT2775_43    SPKE","AOAD/M_B        NONE","AOAD/M_T        NONE","AOAD/M_T        DUTD","AOAD/M_T_RFI_T  NONE","AOAD/M_T_RFI_T  SCIS","AOAD/M_TA_NGS   NONE","APSAPS-3        NONE","ARFAS13DFS      ARFS","ARFAS1FS        ARFC","ASH700228A      NONE","ASH700228B      NONE","ASH700228C      NONE","ASH700228D      NONE","ASH700228E      NONE","ASH700699.L1    NONE","ASH700700.A     NONE","ASH700700.B     NONE","ASH700700.C     NONE","ASH700718A      NONE","ASH700718B      NONE","ASH700829.2     SNOW","ASH700829.3     SNOW","ASH700829.A     SNOW","ASH700829.A1    SNOW","ASH700936A_M    NONE","ASH700936A_M    SNOW","ASH700936B_M    NONE","ASH700936B_M    SNOW","ASH700936C_M    NONE","ASH700936C_M    SNOW","ASH700936D_M    NONE","ASH700936D_M    SCIS","ASH700936D_M    SNOW","ASH700936E      NONE","ASH700936E      SCIS","ASH700936E      SNOW","ASH700936E_C    NONE","ASH700936E_C    SNOW","ASH700936F_C    NONE","ASH700936F_C    SNOW","ASH701008.01B   NONE","ASH701023.A     NONE","ASH701073.1     NONE","ASH701073.1     SCIS","ASH701073.1     SNOW","ASH701073.3     NONE","ASH701933A_M    NONE","ASH701933A_M    SNOW","ASH701933B_M    NONE","ASH701933B_M    SNOW","ASH701933C_M    NONE","ASH701933C_M    SCIS","ASH701933C_M    SCIT","ASH701933C_M    SNOW","ASH701941.1     NONE","ASH701941.2     NONE","ASH701941.A     NONE","ASH701941.B     NONE","ASH701941.B     SCIS","ASH701945B.99   NONE","ASH701945B.99   SCIS","ASH701945B.99   SCIT","ASH701945B_M    NONE","ASH701945B_M    SCIS","ASH701945B_M    SCIT","ASH701945B_M    SNOW","ASH701945C_M    NONE","ASH701945C_M    OLGA","ASH701945C_M    PFAN","ASH701945C_M    SCIS","ASH701945C_M    SCIT","ASH701945C_M    SNOW","ASH701945D_M    NONE","ASH701945D_M    SCIS","ASH701945D_M    SCIT","ASH701945D_M    SNOW","ASH701945E_M    NONE","ASH701945E_M    SCIS","ASH701945E_M    SCIT","ASH701945E_M    SNOW","ASH701945G_M    NONE","ASH701945G_M    SCIS","ASH701945G_M    SCIT","ASH701945G_M    SNOW","ASH701946.2     NONE","ASH701946.2     SNOW","ASH701946.3     NONE","ASH701946.3     SNOW","ASH701975.01A   NONE","ASH701975.01AGP NONE","CHAPS9017       NONE","CHCC220GR       CHCD","CHCC220GR2      CHCD","CHCI80          NONE","CHCX91+S        NONE","CNTAT340        NONE","CNTAT350        CNTS","CNTAT500        CNTS","CNTAT600        CNTS","CNTT30          NONE","CNTT300         NONE","CNTT300PLUS     NONE","EML_REACH_RS2   NONE","FOIA90          NONE","GINCYF90        NONE","GMXZENITH10     NONE","GMXZENITH15     NONE","GMXZENITH16     NONE","GMXZENITH20     NONE","GMXZENITH25     NONE","GMXZENITH25PRO  NONE","GMXZENITH35     NONE","GMXZENITH40     NONE","GMXZENITH60     NONE","HEMS631         NONE","HGGCYH8372      HGGS","HITAT45101CP    HITZ","HXCCGX601A      HXCS","HXCCGX611A      HXCM","IGAIG8          NONE","ITT3750323      SCIS","JAV_GRANT-G3T   NONE","JAV_GRANT-G3T+G JVSD","JAV_RINGANT_G3T NONE","JAV_RINGANT_G3T JAVC","JAV_RINGANT_G3T JAVD","JAVGRANT_G5T+GP JVSD","JAVRINGANT_DM   NONE","JAVRINGANT_DM   JVDM","JAVRINGANT_DM   SCIS","JAVRINGANT_G5T  NONE","JAVRINGANT_G5T  JAVC","JAVRINGANT_G5T  JAVD","JAVTRIUMPH_1M   NONE","JAVTRIUMPH_1MR  NONE","JAVTRIUMPH_2A   NONE","JAVTRIUMPH_2A+G JVGR","JAVTRIUMPH_2A+P JVGR","JAVTRIUMPH_2A+P JVSD","JAVTRIUMPH_3A   NONE","JAVTRIUMPH_LSA  NONE","JNSCR_C146-22-1 NONE","JNSMARANT_GGD   NONE","JPLD/M_R        NONE","JPLD/M_RA_SOP   NONE","JPSLEGANT_E     NONE","JPSODYSSEY_I    NONE","JPSREGANT_DD_E  NONE","JPSREGANT_DD_E1 NONE","JPSREGANT_DD_E2 NONE","JPSREGANT_SD_E  NONE","JPSREGANT_SD_E1 NONE","JPSREGANT_SD_E2 NONE","LEIAR10         NONE","LEIAR20         NONE","LEIAR20         LEIM","LEIAR25         NONE","LEIAR25         LEIT","LEIAR25.R3      NONE","LEIAR25.R3      LEIT","LEIAR25.R4      NONE","LEIAR25.R4      LEIT","LEIAR25.R4      SCIT","LEIAS05         NONE","LEIAS10         NONE","LEIAS11         NONE","LEIAT202+GP     NONE","LEIAT202-GP     NONE","LEIAT302+GP     NONE","LEIAT302-GP     NONE","LEIAT303        NONE","LEIAT303        LEIC","LEIAT502        NONE","LEIAT503        NONE","LEIAT503        LEIC","LEIAT504        NONE","LEIAT504        LEIS","LEIAT504        OLGA","LEIAT504        SCIS","LEIAT504GG      NONE","LEIAT504GG      LEIS","LEIAT504GG      SCIS","LEIAT504GG      SCIT","LEIATX1230      NONE","LEIATX1230+GNSS NONE","LEIATX1230GG    NONE","LEIAX1202       NONE","LEIAX1202GG     NONE","LEIAX1203+GNSS  NONE","LEICGA60        NONE","LEICGA100       NONE","LEIFLX100       NONE","LEIGG02PLUS     NONE","LEIGG03         NONE","LEIGG04         NONE","LEIGG04PLUS     NONE","LEIGS08         NONE","LEIGS08PLUS     NONE","LEIGS09         NONE","LEIGS12         NONE","LEIGS14         NONE","LEIGS15         NONE","LEIGS15.R2      NONE","LEIGS16         NONE","LEIGS18         NONE","LEIICG60        NONE","LEIICG70        NONE","LEIMNA950GG     NONE","LEISR299_INT    NONE","LEISR399_INT    NONE","LEISR399_INTA   NONE","MAC4647942      NONE","MAC4647942      MMAC","MPL_WAAS_2224NW NONE","MPL_WAAS_2225NW NONE","MPLL1/L2_SURV   NONE","MVECR152GNSSA   NONE","MVEGA152GNSSA   NONE","NAVAN2004T      NONE","NAVAN2008T      NONE","NAX3G+C         NONE","NOV_WAAS_600    NONE","NOV501          NONE","NOV501+CR       NONE","NOV502          NONE","NOV502+CR       NONE","NOV503+CR       NONE","NOV503+CR       SPKE","NOV531          NONE","NOV531+CR       NONE","NOV533+CR       NOVC","NOV600          NONE","NOV702          NONE","NOV702GG        NONE","NOV703GGG.R2    NONE","NOV750.R4       NONE","NOV750.R4       NOVS","NOV750.R5       NOVS","NOV850          NONE","RNG80971.00     NONE","SEN67157596+CR  NONE","SEPALTUS_NR3    NONE","SEPCHOKE_B3E6   NONE","SEPCHOKE_B3E6   SPKE","SEPCHOKE_MC     NONE","SEPCHOKE_MC     SPKE","SEPPOLANT_X_MF  NONE","SEPVC6150L      NONE","SEPVC6150L      SCIS","SJTTL111        NONE","SLGAT45101CP    SLGZ","SOK_RADIAN_IS   NONE","SOK502          NONE","SOK600          NONE","SOK702          NONE","SOKGCX3         NONE","SOKGRX3         NONE","SOKSA500        NONE","SPP135000.00    NONE","SPP571212238+GP NONE","SPPSP85         NONE","SPPSP85UHF      NONE","STHCR3-G3       STHC","STXS10SX017A    NONE","STXS700A        NONE","STXS8PX003A     NONE","STXS800         NONE","STXS800A        NONE","STXS900A        NONE","STXS990A        NONE","STXS9I          NONE","STXS9PX001A     NONE","STXS9SA7224V3.0 NONE","STXS900         NONE","STXSA1000       NONE","STXSA1200       STXR","STXSA1500       STXG","STXSA1800       STXS","TIAPENG2100B    NONE","TIAPENG2100R    NONE","TIAPENG3100R1   NONE","TIAPENG3100R2   NONE","TIAPENG6J2      NONE","TIAPENG7N       NONE","TOP700779A      NONE","TOP72110        NONE","TPSCR.G3        NONE","TPSCR.G3        SCIS","TPSCR.G3        TPSH","TPSCR.G5        NONE","TPSCR.G5        TPSH","TPSCR.G5C       NONE","TPSCR.G5C       TPSH","TPSCR3_GGD      NONE","TPSCR3_GGD      CONE","TPSCR3_GGD      OLGA","TPSCR3_GGD      PFAN","TPSCR4          NONE","TPSCR4          CONE","TPSG3_A1        NONE","TPSG3_A1        TPSD","TPSG5_A1        NONE","TPSHIPER_GD     NONE","TPSHIPER_GGD    NONE","TPSHIPER_HR     NONE","TPSHIPER_HR+PS  NONE","TPSHIPER_LITE   NONE","TPSHIPER_PLUS   NONE","TPSHIPER_VR     NONE","TPSLEGANT_G     NONE","TPSLEGANT2      NONE","TPSLEGANT3_UHF  NONE","TPSODYSSEY_I    NONE","TPSPG_A1        NONE","TPSPG_A1+GP     NONE","TPSPN.A5        NONE","TRM105000.10    NONE","TRM115000.00    NONE","TRM115000.00    TZGD","TRM115000.00+S  SCIT","TRM115000.10    NONE","TRM14177.00     NONE","TRM14532.00     NONE","TRM14532.10     NONE","TRM159800.00    NONE","TRM159800.00    SCIS","TRM159800.00    SCIT","TRM159900.00    NONE","TRM159900.00    SCIS","TRM22020.00+GP  NONE","TRM22020.00-GP  NONE","TRM23903.00     NONE","TRM27947.00+GP  NONE","TRM27947.00-GP  NONE","TRM29659.00     NONE","TRM29659.00     OLGA","TRM29659.00     SCIS","TRM29659.00     SCIT","TRM29659.00     SNOW","TRM29659.00     TCWD","TRM29659.00     UNAV","TRM33429.00+GP  NONE","TRM33429.00-GP  NONE","TRM33429.20+GP  NONE","TRM33429.20+GP  TCWD","TRM33429.20+GP  UNAV","TRM39105.00     NONE","TRM41249.00     NONE","TRM41249.00     SCIT","TRM41249.00     TZGD","TRM41249USCG    SCIT","TRM4800         NONE","TRM55970.00     NONE","TRM55971.00     NONE","TRM55971.00     SCIT","TRM55971.00     TZGD","TRM57970.00     NONE","TRM57971.00     NONE","TRM57971.00     SCIT","TRM57971.00     TZGD","TRM5800         NONE","TRM59800.00     NONE","TRM59800.00C    NONE","TRM59800.00     SCIS","TRM59800.00     SCIT","TRM59800.80     NONE","TRM59800.80     SCIS","TRM59800.80     SCIT","TRM59800.99     NONE","TRM59800.99     SCIT","TRM59900.00     NONE","TRM59900.00     SCIS","TRMR10          NONE","TRMR10-2        NONE","TRMR12          NONE","TRMR12I         NONE","TRMR2           NONE","TRMR4-3         NONE","TRMR6-4         NONE","TRMR8-4         NONE","TRMR8_GNSS      NONE","TRMR8_GNSS3     NONE","TRMR8S          NONE","TRMSPS985       NONE","TRMSPS986       NONE","TRSAX4E02       NONE","TWIVC6050       NONE","TWIVC6050       SCIS","TWIVC6050       SCIT","TWIVC6150       NONE","TWIVC6150       SCIS","TWIVP6000       NONE","TWIVP6050_CONE  NONE","TWIVSP6037L     NONE"]
antennas      = set(antennasList)


# == CONNECTION ==
# = Routines =
rinexUpload   = "Upload on file '{file}'"
# = Other =
uploadSuccess = "Successfully uploaded file '{file}' to APPS"


connectionSuccessLog       = "An attempt to test the connection with APPS was made and the connection was successful."
connectionFailedLog        = "An attempt to test the connection with APPS was made and the connection was failed."
uploadStartLog             = "=== UPLOAD START on file {file} ==="
uploadEndLog               = "=== UPLOAD END on file {file} ==="
fileDoesNotExistLog        = "The {file} does not exist or has been removed."
fileValidatedLog           = "The file {file} was validated and is being considered a valid file for uploading."
fileNotValidatedLog        = "The file {file} is invalid - {validity}"
compressedLog              = "File {file} was compressed. Decompressing it, so its header can be read."
addedToQueueSuccessLog     = "Successfully added file {file} to the uploaded queue."
removedFromQueueSuccessLog = "Successfully removed file {file} from the uploaded queue."
uuidNotInQueueLog          = "The file {file} was not in the uploaded queue, so cannot be removed from it."
invalidArgLog              = "The value `{arg}` is invalid for argument {argName}. Using default value `{defaultValue}`."
checkStateStartLog         = "=== STATE CHECK START ==="
checkStateStartFileLog     = "Checking file {file}."
checkStateEndLog           = "=== STATE CHECK END ==="
checkStateEndFileLog       = "=== STATE CHECK END on file {file} ==="
stateLog                   = "The file {file} is in the `{state}` state."
approvedSuccessfullLog     = "The file {file} has been verified by APPS and is now approved for processing."
approvedUnsuccessfullLog   = "The file {file} could not be approved for processing."
downloadSuccessfullLog     = "The file {file}'s processed files have been successfully downloaded."
downloadUnsuccessfullLog   = "The file {file}'s processed files could not be downloaded."
dataDeletedSuccessfulLog   = "The file {file} has been deleted from APPS."
dataDeletedUnsuccessfulLog = "Could not delete {file} from APPS."
dataNotFoundLog            = "The file {file} was not found on APPS."
InvalidIdentifierLog       = "The uuid {uuid} is not valid."
criticalExceptionLog       = "Something that wasn't accounted for happened. It's recommended to check what happened to file {file}."
errorFromAPPSLog           = "There was an error with the file {file} in APPS."
fileDataStartLog           = "== GATHERING DATA START on uuid {uuid} =="
fileDataEndLog             = "== GATHERING DATA END on uuid {uuid} =="
approveStartLog            = "== APPROVAL START on file {file} =="
approveEndLog              = "== APPROVAL END on file {file} =="
removeDataStartLog         = "== REMOVE DATA START on file {file} =="
removeDataEndLog           = "== REMOVE DATA END on file {file} =="
retrieveDataStartLog       = "== RETRIEVE DATA START on file {file}"
retrieveDataEndLog         = "== RETRIEVE DATA END on file {file}"

#routines
downloadRinexFilesRoutineStartLog   = "=== RINEX FILES DOWNLOAD ROUTINE (START) ==="
downloadRinexFilesRoutineEndLog     = "=== RINEX FILES DOWNLOAD ROUTINE (END) ==="
downloadRinexFileSubroutineStartLog = "== RINEX FILE '{file}' DOWNLOAD SUBROUTINE (START) =="
downloadRinexFileSubroutineEndLog   = "== RINEX FILE '{file}' DOWNLOAD SUBROUTINE (END) =="
#other
uploadFilesCheckingLog              = "Checking for upload files."
invalidUploadFileLog                = "The upload file '{file}' is invalid. Reason: '{reason}'."
validUploadFileLog                  = "The upload file '{file}' was validated."
uploadFilesExistLog                 = "{numOfUploadFiles} upload files were found. Attempting to download corresponding rinex files."
noUploadFilesLog                    = "No upload files were found."
sshConnectAttemptLog                = "Attempting to connect to '{ip}:{port}', with user '{username}'."
connectAttemptSuccessfulLog         = "Successfully established a connection to the server."
connectAttemptUnsuccessfulLog       = "Could not establish a connection to the server. Reason: '{reason}'."
scpSuccessful                       = "Successfully copied file '{file}' to '{downloadFolder}'."
scpUnsuccessful                     = "Could not copy file '{file}' to '{downloadFolder}'."
unexpectedErrorLog                  = "An unexpected error ocurred. Files were not downloaded."
fileAddedToQueueLog                 = "The file {file} was added upload files queue file."