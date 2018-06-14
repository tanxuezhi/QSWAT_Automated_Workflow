import cj_function_lib as cj
import init_file as variables

till = """   1    Fallplow           0.950         150.000          75.000
   2    Sprgplow           0.500         125.000          50.000
   3    Constill           0.250         100.000          40.000
   4    Zerotill           0.050          25.000          10.000
   5    Duckftc            0.550         100.000          15.000
   6    Fldcge15           0.300         100.000          20.000
   7    Fldclt15           0.300         100.000          20.000
   8    Furowout           0.750          25.000          15.000
   9    Marker             0.450         100.000          15.000
  10    Rollge15           0.500          25.000          15.000
  11    Rolllt15           0.500          25.000          15.000
  12    Rowcge15           0.250          25.000          15.000
  13    Rowclt15           0.250          25.000          15.000
  14    Discovat           0.500          25.000          15.000
  15    Leveler            0.500          25.000          15.000
  16    Hrw10bar           0.200          25.000          10.000
  17    Cmulge18           0.250          25.000           5.000
  18    Cmullt18           0.250          25.000           5.000
  19    Culpkpul           0.350          40.000           5.000
  20    Landlevl           0.500          75.000          15.000
  21    Landall            0.300         150.000          15.000
  22    Lasrplan           0.300         150.000          15.000
  23    Levpldis           0.750          25.000          50.000
  24    Float              0.100          60.000          10.000
  25    Fldcdscr           0.100          60.000          20.000
  26    Listrmid           0.150          40.000          25.000
  27    Rollgrov           0.250          60.000           0.000
  28    Rolpkrat           0.050          40.000           0.000
  29    Rolpkrft           0.350          40.000           0.000
  30    Sandfigt           0.700         100.000          10.000
  31    Seedroll           0.700         100.000           0.000
  32    Crustbst           0.100          60.000          10.000
  33    Rollhrrw           0.400          60.000           5.000
  34    Triple K           0.400         100.000          25.000
  35    Cult1row           0.250          25.000          15.000
  36    Finhge15           0.550         100.000           5.000
  37    Finhlt15           0.550         100.000           5.000
  38    Flexge20           0.200          25.000          13.000
  39    Flexlt20           0.200          25.000          13.000
  40    Spiketth           0.400          75.000          10.000
  41    Spikgt25           0.250          25.000          13.000
  42    Spikle25           0.250          25.000          13.000
  43    Spthge15           0.350          25.000          13.000
  44    Spthlt15           0.350          25.000          13.000
  45    Soilfins           0.550          75.000           5.000
  46    Rothoe             0.100           5.000          13.000
  47    Roterra            0.800           5.000          10.000
  48    Rototill           0.800           5.000          13.000
  49    Rotbeddr           0.800         100.000          40.000
  50    Rowbuck            0.700         100.000          35.000
  51    Ripper10           0.250         350.000          15.000
  52    Midbst1r           0.700         100.000          35.000
  53    Rodweedr           0.300          25.000          10.000
  54    Rubwhwpl           0.350           5.000           5.000
  55    Multiwdr           0.300          25.000          10.000
  56    Mldbge10           0.950         150.000          30.000
  57    Chplgt21           0.300         150.000          20.000
  58    Chplgt15           0.300         150.000          20.000
  59    Chplle15           0.300         150.000          20.000
  60    Cchplow            0.500         150.000          20.000
  61    Dkplge23           0.850         100.000          50.000
  62    Dkpllt23           0.850         100.000          50.000
  63    Mlbdr4-6           0.950         150.000          30.000
  64    Mlbdrge7           0.950         150.000          30.000
  65    Mlbdrle3           0.950         150.000          30.000
  66    Mlbd24-6           0.950         150.000          30.000
  67    Mldb2ge7           0.950         150.000          30.000
  68    Mldb2le3           0.950         150.000          30.000
  69    Smchgt15           0.150          75.000          20.000
  70    Smchle15           0.150          75.000          20.000
  71    Subchplw           0.450         350.000          15.000
  72    Rowcond1           0.500          25.000          10.000
  73    Hipper1r           0.500         100.000          30.000
  74    Riceroll           0.100          50.000           0.000
  75    Paraplow           0.150         350.000          25.000
  76    Sbedhipr           0.700         350.000          40.000
  77    Riprsubs           0.250         350.000          15.000
  78    Vripper            0.250         350.000          25.000
  79    Bedrol4r           0.250          50.000           5.000
  80    Bedder D           0.550         150.000          35.000
  81    Beddhipr           0.650         150.000          35.000
  82    Beddkrow           0.850         100.000          40.000
  83    Bedder S           0.550         150.000          30.000
  84    Dskbrmkr           0.550         150.000          20.000
  85    Dkchmtil           0.550         150.000          25.000
  86    Offdge19           0.700         100.000          50.000
  87    Offhle13           0.700         100.000          50.000
  88    Offh1418           0.600         100.000          50.000
  89    Offlge19           0.550         100.000          40.000
  90    Offlle13           0.550         100.000          40.000
  91    Offl1418           0.550         100.000          40.000
  92    One-wayt           0.600         100.000          50.000
  93    Tanpge19           0.700          75.000          18.000
  94    Tanple13           0.400          75.000          18.000
  95    Tanp1418           0.550          75.000          30.000
  96    Tanrge19           0.750         100.000          50.000
  97    Tanrle13           0.600          75.000          20.000
  98    Tanr1418           0.400          75.000          18.000
  99    Singldis           0.450         100.000          30.000
 100    Pwrmulch           0.700          50.000          15.000
 101    Blade 10           0.250          75.000          13.000
 102    Furwdike           0.700         100.000          13.000
 103    Beetcult           0.250          25.000          15.000
 104    Dskplw36           0.700         100.000          50.000
 105    Cltiwd36           0.300         100.000          15.000
 106    Packer40           0.350          40.000           0.000
 107    Rodwdr36           0.300         100.000          20.000
"""

fileName = "till.dat"
cj.write_to(variables.DefaultSimDir + "TxtInOut\\" + fileName, till)
#print fileName